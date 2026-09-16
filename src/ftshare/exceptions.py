"""Exception types raised by the ftshare Python SDK."""

from __future__ import annotations

from typing import Any


class FtshareError(Exception):
    """Base exception for ftshare SDK errors."""


class FtshareHTTPError(FtshareError):
    """Raised when the FTShare API returns a non-2xx HTTP status."""

    def __init__(self, status_code: int, url: str, response_text: str) -> None:
        """Initialize an HTTP transport error.

        Args:
            status_code: HTTP status code returned by the server.
            url: Final request URL.
            response_text: Raw response body.
        """
        self.status_code = status_code
        self.url = url
        self.response_text = response_text
        super().__init__(f"HTTP {status_code} for {url}: {response_text[:200]}")


class FtshareDecodeError(FtshareError):
    """Raised when the response body cannot be decoded as JSON."""

    def __init__(self, url: str, response_text: str) -> None:
        """Initialize a JSON decoding error.

        Args:
            url: Final request URL.
            response_text: Raw response body.
        """
        self.url = url
        self.response_text = response_text
        super().__init__(f"Failed to decode JSON response from {url}: {response_text[:200]}")


class FtshareAPIError(FtshareError):
    """Raised when a JSON response contains a non-zero business code."""

    def __init__(self, code: Any, message: str | None, payload: Any) -> None:
        """Initialize a business-level API error.

        Args:
            code: Business error code from the response.
            message: Business error message from the response, if present.
            payload: Full decoded JSON payload.
        """
        self.code = code
        self.message = message
        self.payload = payload
        detail = message or "API returned a non-zero business code"
        super().__init__(f"FTShare API error {code}: {detail}")
