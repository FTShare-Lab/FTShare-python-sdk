"""Shared synchronous transport for the ftshare SDK."""

from __future__ import annotations

import re
from collections.abc import Mapping, Sequence
from typing import Any
from urllib.parse import quote

import requests

from .config import DEFAULT_BASE_URL, DEFAULT_MAX_PAGE_SIZE, get_base_url, normalize_base_url, set_base_url
from .dataframe import to_dataframe
from .endpoints import ENDPOINTS
from .exceptions import FtshareDecodeError, FtshareHTTPError
from .fields import normalize_fields, select_fields
from .pagination import validate_pagination
from .response import extract_tabular, raise_for_api_error, total_pages as extract_total_pages


class BaseClient:
    """Base synchronous client with shared HTTP behavior.

    Args:
        base_url: API base URL. Defaults to ``DEFAULT_BASE_URL``.
        timeout: Request timeout in seconds.
        headers: Optional headers sent with every request.
        session: Optional ``requests.Session``. Primarily useful for tests or
            for callers that need custom adapters.
    """

    def __init__(
        self,
        base_url: str | None = None,
        timeout: float = 10,
        headers: Mapping[str, str] | None = None,
        session: requests.Session | None = None,
    ) -> None:
        self.base_url = normalize_base_url(base_url or get_base_url())
        self.timeout = timeout
        self.session = session or requests.Session()
        self.headers = dict(headers or {})

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
        """Send a POST request with a JSON body and normalize the response.

        Args:
            path: Endpoint path relative to ``base_url``.
            raw: When ``True``, return the decoded JSON payload.
            fields: Optional field list or comma-separated field string.
            as_dataframe: Return a pandas ``DataFrame`` by default.
            **params: JSON body parameters. Values set to ``None`` are omitted.

        Returns:
            A pandas ``DataFrame`` by default, Python rows when
            ``as_dataframe=False``, or raw JSON when ``raw=True``.
        """
        return self._request(
            "POST",
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
        **params: Any,
    ) -> Any:
        """Send an HTTP request and normalize the response."""
        url = self._url_for(path)
        clean_params = {key: value for key, value in params.items() if value is not None}
        request_method = method.upper()
        if request_method == "POST":
            response = self.session.post(
                url,
                json=clean_params,
                timeout=self.timeout,
                headers=self.headers or None,
            )
        else:
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

        result = self._extract_tabular(payload)
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
        if endpoint.method == "POST":
            return self.post(path, raw=raw, fields=fields, as_dataframe=as_dataframe, **params)
        return self.get(path, raw=raw, fields=fields, as_dataframe=as_dataframe, **params)

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
    def _extract_tabular(cls, payload: Any) -> Any:
        """Extract common row containers from FTShare response shapes."""
        return extract_tabular(payload)

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
