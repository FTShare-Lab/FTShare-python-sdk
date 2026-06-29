"""Public entrypoint for the ftshare Python SDK.

Typical usage:

    import ftshare as ft

    market = ft.market_api()
    payload = market.baidu_financial_calendar(
        start_date="2026-05-26",
        end_date="2026-05-27",
    )

The package-level ``BASE_URL`` is intentionally mutable so deployments can
switch environments without changing every client construction site.
"""

from __future__ import annotations

from collections.abc import Mapping

from . import client as _client
from .client import DEFAULT_BASE_URL, FtshareClient
from .exceptions import (
    FtshareAPIError,
    FtshareDecodeError,
    FtshareError,
    FtshareHTTPError,
)

BASE_URL = _client.get_base_url()


def get_base_url() -> str:
    """Return the package-level base URL used by ``market_api()``.

    Returns:
        The normalized base URL, always ending with ``/``.
    """
    return BASE_URL


def set_base_url(url: str) -> str:
    """Set the package-level base URL used by new clients.

    Args:
        url: API base URL. Both ``https://host/gateway`` and
            ``https://host/gateway/`` are accepted.

    Returns:
        The normalized base URL.

    Raises:
        ValueError: If ``url`` is empty after stripping whitespace.
    """
    global BASE_URL
    BASE_URL = _client.set_base_url(url)
    return BASE_URL


def market_api(
    base_url: str | None = None,
    timeout: float = 10,
    headers: Mapping[str, str] | None = None,
) -> FtshareClient:
    """Create a synchronous FTShare market data API client.

    Args:
        base_url: Optional client-specific base URL. If omitted, the current
            package-level ``BASE_URL`` is used.
        timeout: Request timeout in seconds.
        headers: Optional headers applied to every request from this client.

    Returns:
        A configured ``FtshareClient`` instance.
    """
    return _client.market_api(base_url=base_url or BASE_URL, timeout=timeout, headers=headers)


__all__ = [
    "BASE_URL",
    "DEFAULT_BASE_URL",
    "FtshareAPIError",
    "FtshareClient",
    "FtshareDecodeError",
    "FtshareError",
    "FtshareHTTPError",
    "get_base_url",
    "market_api",
    "set_base_url",
]
