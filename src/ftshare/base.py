"""Shared synchronous transport for the ftshare SDK."""

from __future__ import annotations

import hashlib
import json
import os
import re
from collections.abc import Mapping, Sequence
from pathlib import Path
from typing import Any
from urllib.parse import quote

import requests

from .config import DEFAULT_BASE_URL, DEFAULT_MAX_PAGE_SIZE, get_base_url, normalize_base_url, set_base_url
from .dataframe import to_dataframe
from .endpoints import ENDPOINTS
from .exceptions import FtshareDecodeError, FtshareDownloadError, FtshareHTTPError
from .fields import normalize_fields, select_fields
from .pagination import validate_pagination
from .response import extract_tabular, raise_for_api_error, total_pages as extract_total_pages


class BaseClient:
    """Base synchronous client with shared HTTP behavior.

    Args:
        base_url: API base URL. Defaults to ``DEFAULT_BASE_URL``.
        timeout: Request timeout in seconds.
        headers: Optional headers sent with every request.
        api_key: Optional FTShare API key. Defaults to the ``FTSHARE_API_KEY``
            environment variable.
        session: Optional ``requests.Session``. Primarily useful for tests or
            for callers that need custom adapters.
    """

    def __init__(
        self,
        base_url: str | None = None,
        timeout: float = 10,
        headers: Mapping[str, str] | None = None,
        api_key: str | None = None,
        session: requests.Session | None = None,
    ) -> None:
        self.base_url = normalize_base_url(base_url or get_base_url())
        self.timeout = timeout
        self.session = session or requests.Session()
        self.headers = dict(headers or {})
        if api_key is None:
            api_key = os.environ.get("FTSHARE_API_KEY")
        if api_key is not None:
            self.headers["FTSHARE_API_KEY"] = api_key

    def close(self) -> None:
        """Close the underlying HTTP session."""
        self.session.close()

    def __enter__(self) -> "BaseClient":
        """Return the client when used as a context manager."""
        return self

    def __exit__(self, exc_type: Any, exc: Any, traceback: Any) -> None:
        """Close the HTTP session when leaving a context manager block."""
        self.close()

    def get(
        self,
        path: str,
        *,
        raw: bool = False,
        fields: Sequence[str] | str | None = None,
        as_dataframe: bool = True,
        unwrap_bare_data: bool = False,
        **params: Any,
    ) -> Any:
        """Send a GET request and normalize the response.

        Args:
            path: Endpoint path relative to ``base_url``. Absolute URLs are
                also accepted.
            raw: When ``True``, return the decoded JSON payload. When
                ``False`` by default, extract ``data.records`` or ``items``
                when possible.
            fields: Optional field list or comma-separated field string. Field
                selection is applied after tabular extraction.
            as_dataframe: Return a pandas ``DataFrame`` by default. Set to
                ``False`` to return Python rows such as ``list[dict]``.
            unwrap_bare_data: When ``True``, an object-shaped ``data`` field
                is returned directly instead of the full envelope. Intended
                for single-item query endpoints documented to answer with a
                bare object.
            **params: Query parameters. Values set to ``None`` are omitted.

        Returns:
            A pandas ``DataFrame`` by default, Python rows when
            ``as_dataframe=False``, or raw JSON when ``raw=True``.

        Raises:
            FtshareHTTPError: If the server returns a non-2xx HTTP status.
            FtshareDecodeError: If the response body is not JSON.
            FtshareAPIError: If the JSON response includes ``code != 0``.
        """
        return self._request(
            "GET",
            path,
            raw=raw,
            fields=fields,
            as_dataframe=as_dataframe,
            unwrap_bare_data=unwrap_bare_data,
            **params,
        )

    def post(
        self,
        path: str,
        *,
        raw: bool = False,
        fields: Sequence[str] | str | None = None,
        as_dataframe: bool = True,
        **params: Any,
    ) -> Any:
        """Send a compatibility request using GET and normalize the response."""
        return self.get(
            path,
            raw=raw,
            fields=fields,
            as_dataframe=as_dataframe,
            **params,
        )

    def _request(
        self,
        method: str,
        path: str,
        *,
        raw: bool = False,
        fields: Sequence[str] | str | None = None,
        as_dataframe: bool = True,
        unwrap_bare_data: bool = False,
        **params: Any,
    ) -> Any:
        """Send an HTTP request and normalize the response."""
        url = self._url_for(path)
        clean_params = {key: value for key, value in params.items() if value is not None}
        request_method = method.upper()
        if request_method != "GET":
            raise ValueError(f"Unsupported HTTP method: {method}")
        query_params = {
            key: str(value).lower() if isinstance(value, bool) else value
            for key, value in clean_params.items()
        }
        response = self.session.get(
            url,
            params=query_params,
            timeout=self.timeout,
            headers=self.headers or None,
        )
        if not 200 <= response.status_code < 300:
            raise FtshareHTTPError(response.status_code, url, response.text)

        try:
            payload = response.json()
        except ValueError as exc:
            raise FtshareDecodeError(url, response.text) from exc

        raise_for_api_error(payload)

        if raw:
            return payload

        result = self._extract_tabular(payload, unwrap_bare_data=unwrap_bare_data)
        result = self._select_fields(result, fields)
        if as_dataframe:
            return self._to_dataframe(result)
        return result

    def _call_endpoint(
        self,
        endpoint_name: str,
        *,
        path_params: Mapping[str, Any] | None = None,
        raw: bool = False,
        fields: Sequence[str] | str | None = None,
        as_dataframe: bool = True,
        **params: Any,
    ) -> Any:
        """Call an endpoint by registry name using its documented HTTP method."""
        endpoint = ENDPOINTS[endpoint_name]
        path = self._format_path(endpoint.path, path_params or {})
        if endpoint.method != "GET":
            raise ValueError(f"Unsupported HTTP method for endpoint: {endpoint.method}")
        return self.get(path, raw=raw, fields=fields, as_dataframe=as_dataframe, **params)

    def download(
        self,
        path: str,
        *,
        save_dir: str | os.PathLike[str] = ".",
        filename: str | None = None,
    ) -> str:
        """Download a binary attachment and write it to ``save_dir``.

        Args:
            path: Endpoint path relative to ``base_url``. Absolute URLs are
                also accepted. Path parameters must already be substituted.
            save_dir: Destination directory. Created when missing.
            filename: Destination file name. Defaults to the last path segment.

        Returns:
            The path of the written file, or an empty string when the server
            answers 2xx with an empty body.

        Raises:
            FtshareHTTPError: If the server returns a non-2xx HTTP status.
        """
        url = self._url_for(path)
        response = self.session.get(url, timeout=self.timeout, headers=self.headers or None)
        if not 200 <= response.status_code < 300:
            raise FtshareHTTPError(response.status_code, url, response.text)

        content = response.content
        if not content:
            return ""

        target = Path(save_dir) / (filename or Path(path).name)
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(content)
        return str(target)

    def download_resumable(
        self,
        path: str,
        *,
        expected_size: int | None = None,
        expected_sha256: str | None = None,
        save_dir: str | os.PathLike[str] = ".",
        filename: str | None = None,
        retries: int = 3,
        chunk_size: int = 1024 * 1024,
    ) -> str:
        """Download a large file with range resume, retries, and digest verification.

        The body streams into ``<target>.part`` and only becomes ``<target>``
        after size and sha256 verification, so a failed or interrupted
        transfer never leaves a file that looks complete. A small
        ``<target>.part.meta`` sidecar records the source URL and ``ETag`` so a
        later call can safely resume: when the server's ``ETag`` changed, the
        stale partial file is discarded and the transfer restarts.

        Args:
            path: Endpoint path relative to ``base_url``. Path parameters must
                already be substituted.
            expected_size: Expected final size in bytes, usually from the
                listing endpoint.
            expected_sha256: Expected lowercase hex sha256 of the final file.
            save_dir: Destination directory. Created when missing.
            filename: Destination file name. Defaults to the last path segment.
            retries: Additional attempts after the first one, so at most
                ``retries + 1`` transfers run. Network failures, 429, 5xx and
                416 responses are retried; other HTTP failures are not.
            chunk_size: Streaming read size in bytes.

        Returns:
            The path of the completed file.

        Raises:
            FtshareHTTPError: If the server returns a non-retryable HTTP status.
            FtshareDownloadError: If the transfer completes but fails size or
                sha256 verification.
            requests.RequestException: If every attempt fails with a network
                error.
        """
        url = self._url_for(path)
        target = Path(save_dir) / (filename or Path(path).name)
        part = target.with_name(target.name + ".part")
        meta_path = part.with_name(part.name + ".meta")
        target.parent.mkdir(parents=True, exist_ok=True)

        if target.exists() and expected_sha256 and self._file_sha256(target, chunk_size) == expected_sha256:
            return str(target)

        last_error: Exception | None = None
        for _ in range(retries + 1):
            offset = 0
            etag = ""
            if part.exists():
                sidecar = self._read_download_meta(meta_path)
                if sidecar and sidecar.get("url") == url and sidecar.get("etag"):
                    etag = str(sidecar["etag"])
                    offset = part.stat().st_size
                else:
                    # Never resume from a prefix we cannot attribute to this URL.
                    part.unlink(missing_ok=True)
                    meta_path.unlink(missing_ok=True)

            headers = dict(self.headers)
            if offset > 0:
                headers["Range"] = f"bytes={offset}-"
                headers["If-Range"] = etag

            try:
                with self.session.get(url, headers=headers or None, timeout=self.timeout, stream=True) as response:
                    status = response.status_code
                    if status in (400, 404):
                        raise FtshareHTTPError(status, url, response.text)
                    if status == 416:
                        # Server reports the resume offset is past EOF: restart.
                        part.unlink(missing_ok=True)
                        meta_path.unlink(missing_ok=True)
                        last_error = FtshareHTTPError(status, url, response.text)
                        continue
                    if status not in (200, 206):
                        if status == 429 or status >= 500:
                            last_error = FtshareHTTPError(status, url, response.text)
                            continue
                        raise FtshareHTTPError(status, url, response.text)

                    if status == 200:
                        # Whole file: the server ignored the Range (fresh
                        # download, or If-Range reported a newer version), so
                        # truncate instead of appending to a stale prefix.
                        offset = 0
                        mode = "wb"
                    else:
                        start = self._content_range_start(response.headers.get("Content-Range"))
                        if start != offset:
                            part.unlink(missing_ok=True)
                            meta_path.unlink(missing_ok=True)
                            last_error = FtshareDownloadError(
                                url,
                                f"resumed at {start} while the partial file holds {offset} bytes",
                            )
                            continue
                        mode = "ab"

                    response_etag = response.headers.get("ETag") or ""
                    if response_etag:
                        etag = response_etag
                        self._write_download_meta(meta_path, url, etag, offset)

                    written = offset
                    with part.open(mode) as handle:
                        for chunk in response.iter_content(chunk_size=chunk_size):
                            if not chunk:
                                continue
                            handle.write(chunk)
                            written += len(chunk)
                            if expected_size is not None and written > expected_size:
                                raise FtshareDownloadError(
                                    url,
                                    "response exceeded the expected file size",
                                    expected=expected_size,
                                    actual=written,
                                )
            except requests.RequestException as error:
                last_error = error
                continue

            size = part.stat().st_size
            if expected_size is not None and size != expected_size:
                part.unlink(missing_ok=True)
                meta_path.unlink(missing_ok=True)
                raise FtshareDownloadError(url, "size mismatch", expected=expected_size, actual=size)
            if expected_sha256:
                digest = self._file_sha256(part, chunk_size)
                if digest != expected_sha256:
                    # Drop the corrupt file: resuming from a known-bad prefix
                    # would fail verification again on every later call.
                    part.unlink(missing_ok=True)
                    meta_path.unlink(missing_ok=True)
                    raise FtshareDownloadError(url, "sha256 mismatch", expected=expected_sha256, actual=digest)

            os.replace(part, target)
            meta_path.unlink(missing_ok=True)
            return str(target)

        if last_error is not None:
            raise last_error
        raise FtshareDownloadError(url, f"download failed after {retries + 1} attempts")

    @staticmethod
    def _file_sha256(path: Path, chunk_size: int) -> str:
        """Return the lowercase hex sha256 of an existing file."""
        digest = hashlib.sha256()
        with path.open("rb") as handle:
            for block in iter(lambda: handle.read(chunk_size), b""):
                digest.update(block)
        return digest.hexdigest()

    @staticmethod
    def _content_range_start(value: str | None) -> int | None:
        """Return the first byte offset of a ``Content-Range`` header value."""
        if not value:
            return None
        match = re.match(r"bytes\s+(\d+)-", value.strip())
        return int(match.group(1)) if match else None

    @staticmethod
    def _read_download_meta(path: Path) -> dict[str, Any] | None:
        """Read a partial-download sidecar, tolerating missing or corrupt files."""
        try:
            payload = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, ValueError):
            return None
        return payload if isinstance(payload, dict) else None

    @staticmethod
    def _write_download_meta(path: Path, url: str, etag: str, size: int) -> None:
        """Record the ETag a partial file was downloaded from, atomically."""
        temporary = path.with_name(path.name + ".tmp")
        temporary.write_text(json.dumps({"url": url, "etag": etag, "size": size}), encoding="utf-8")
        os.replace(temporary, path)

    def get_paginated(
        self,
        path: str,
        *,
        page: int | None = None,
        page_size: int | None = None,
        limit: int | None = None,
        all_pages: bool = False,
        max_pages: int | None = None,
        max_page_size: int = DEFAULT_MAX_PAGE_SIZE,
        raw: bool = False,
        fields: Sequence[str] | str | None = None,
        as_dataframe: bool = True,
        unwrap_bare_data: bool = False,
        **params: Any,
    ) -> Any:
        """Send a request to an endpoint that supports page/page_size.

        Args:
            path: Endpoint path relative to ``base_url``.
            page: Page number, starting from 1. Advanced use.
            page_size: Number of rows per request. Advanced use.
            limit: Maximum number of rows to return. The SDK automatically
                fetches multiple pages when ``limit`` is larger than one page.
            all_pages: Fetch and combine pages until the server reports the
                last page. If ``limit`` is also provided, stop after collecting
                at most that many rows.
            max_pages: Optional safety cap used with ``all_pages``.
            max_page_size: Maximum allowed page size for this endpoint.
            raw: Return raw JSON. When multiple pages are fetched, returns a
                list of raw page payloads.
            fields: Optional field list or comma-separated field string.
            as_dataframe: Return a pandas ``DataFrame`` by default.
            unwrap_bare_data: When ``True``, an object-shaped ``data`` field
                is returned directly instead of the full envelope. Only used
                on the single-request path (no ``limit``/``all_pages``).
            **params: Query parameters. Values set to ``None`` are omitted.

        Returns:
            A pandas ``DataFrame`` by default, Python rows when
            ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
            payloads when multiple pages are fetched with ``raw=True``.
        """
        effective_page = 1 if page is None else page
        self._validate_pagination(effective_page, page_size, max_pages, max_page_size, limit=limit)

        if not all_pages and limit is None:
            return self.get(
                path,
                page=effective_page if page is not None else None,
                page_size=page_size,
                raw=raw,
                fields=fields,
                as_dataframe=as_dataframe,
                unwrap_bare_data=unwrap_bare_data,
                **params,
            )

        rows: list[Any] = []
        payloads: list[Any] = []
        fetched_pages = 0
        remaining = limit
        if page_size is not None:
            request_page_size = page_size
        elif limit is not None:
            request_page_size = min(limit, max_page_size)
        else:
            request_page_size = max_page_size

        while True:
            current_page_size = request_page_size
            if remaining is not None:
                current_page_size = min(current_page_size, remaining)

            payload = self.get(
                path,
                page=effective_page,
                page_size=current_page_size,
                raw=True,
                **params,
            )
            payloads.append(payload)
            page_rows = extract_tabular(payload)
            if not isinstance(page_rows, list):
                break

            rows.extend(page_rows)
            fetched_pages += 1
            if remaining is not None:
                remaining -= len(page_rows)
                if remaining <= 0:
                    break

            page_count = extract_total_pages(payload)
            if max_pages is not None and fetched_pages >= max_pages:
                break
            if page_count is not None and effective_page >= page_count:
                break
            if page_count is None and len(page_rows) < current_page_size:
                break
            if not page_rows:
                break
            effective_page += 1

        if raw:
            return payloads[0] if len(payloads) == 1 and not all_pages else payloads

        result = self._select_fields(rows, fields)
        if as_dataframe:
            return self._to_dataframe(result)
        return result

    def fetch_all(
        self,
        method_name: str,
        *,
        page_size: int = 200,
        max_pages: int | None = None,
        fields: Sequence[str] | str | None = None,
        as_dataframe: bool = True,
        **params: Any,
    ) -> Any:
        """Fetch all pages from a paginated endpoint method.

        The target method must accept ``page`` and ``page_size`` parameters.
        Pagination stops when the response reports the last page, returns fewer
        rows than requested, returns no rows, or reaches ``max_pages``.

        Args:
            method_name: Name of a public ``FtshareClient`` endpoint method.
            page_size: Page size to request on each call.
            max_pages: Optional hard limit for the number of pages fetched.
            fields: Optional field list or comma-separated field string.
            as_dataframe: Return a pandas ``DataFrame`` by default. Set to
                ``False`` to return a row list.
            **params: Parameters forwarded to the endpoint method.

        Returns:
            A combined pandas ``DataFrame`` by default, or a row list when
            ``as_dataframe=False``.

        Raises:
            AttributeError: If ``method_name`` does not exist on the client.
        """
        method = getattr(self, method_name, None)
        if method is None or not callable(method):
            raise AttributeError(f"Unknown ftshare API method: {method_name}")

        page = int(params.pop("page", 1) or 1)
        rows: list[Any] = []
        fetched_pages = 0

        while True:
            payload = method(raw=True, page=page, page_size=page_size, **params)
            page_rows = extract_tabular(payload)
            if not isinstance(page_rows, list):
                break

            rows.extend(page_rows)
            fetched_pages += 1

            page_count = extract_total_pages(payload)
            if max_pages is not None and fetched_pages >= max_pages:
                break
            if page_count is not None and page >= page_count:
                break
            if page_count is None and len(page_rows) < page_size:
                break
            if not page_rows:
                break
            page += 1

        result = self._select_fields(rows, fields)
        if as_dataframe:
            return self._to_dataframe(result)
        return result

    def _url_for(self, path: str) -> str:
        """Build the final URL for an endpoint path without duplicating gateway prefixes."""
        clean_path = path.strip()
        if clean_path.startswith("http://") or clean_path.startswith("https://"):
            return clean_path
        clean_path = clean_path.lstrip("/")
        for prefix in ("gateway/", "data/"):
            if clean_path.startswith(prefix):
                clean_path = clean_path[len(prefix) :]
                break
        return self.base_url + clean_path

    @staticmethod
    def _format_path(path: str, path_params: Mapping[str, Any] | None = None) -> str:
        """Substitute dynamic ``{name}`` or ``:name`` path parameters.

        Values are URL-encoded before substitution. Query/body parameters
        should be passed separately to ``get`` or ``post``.
        """
        formatted = path
        for name, value in (path_params or {}).items():
            if value is None:
                raise ValueError(f"{name} is required in endpoint path")
            encoded = quote(str(value), safe="")
            formatted = formatted.replace(f"{{{name}}}", encoded)
            formatted = formatted.replace(f":{name}", encoded)
        unresolved = re.search(r"\{([A-Za-z_][A-Za-z0-9_]*)\}|:([A-Za-z_][A-Za-z0-9_]*)", formatted)
        if unresolved is not None:
            name = unresolved.group(1) or unresolved.group(2)
            raise ValueError(f"{name} is required in endpoint path")
        return formatted

    @staticmethod
    def _validate_pagination(
        page: int,
        page_size: int | None,
        max_pages: int | None,
        max_page_size: int,
        *,
        limit: int | None = None,
    ) -> None:
        """Validate client-side pagination controls before sending a request."""
        validate_pagination(page, page_size, max_pages, max_page_size, limit=limit)

    @staticmethod
    def _raise_for_api_error(payload: Any) -> None:
        """Raise ``FtshareAPIError`` when a business response reports failure."""
        raise_for_api_error(payload)

    @classmethod
    def _extract_tabular(cls, payload: Any, unwrap_bare_data: bool = False) -> Any:
        """Extract common row containers from FTShare response shapes."""
        return extract_tabular(payload, unwrap_bare_data=unwrap_bare_data)

    @staticmethod
    def _total_pages(payload: Any) -> int | None:
        """Return total page count from supported pagination envelopes."""
        return extract_total_pages(payload)

    @staticmethod
    def _normalize_fields(fields: Sequence[str] | str | None) -> list[str] | None:
        """Normalize ``fields`` from sequence or comma-separated string."""
        return normalize_fields(fields)

    @classmethod
    def _select_fields(cls, result: Any, fields: Sequence[str] | str | None) -> Any:
        """Select requested fields from mapping rows while preserving row order."""
        return select_fields(result, fields)

    @staticmethod
    def _to_dataframe(result: Any) -> Any:
        """Convert a row-like result into a pandas ``DataFrame``."""
        return to_dataframe(result)
