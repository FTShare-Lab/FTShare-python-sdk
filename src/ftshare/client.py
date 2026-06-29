"""Public synchronous FTShare client assembled from ftshare-doc topic mixins."""

from __future__ import annotations

from collections.abc import Mapping

from .apis import (
    BondApiMixin,
    EconomicApiMixin,
    EtfApiMixin,
    ForexApiMixin,
    FundApiMixin,
    FuturesApiMixin,
    HkApiMixin,
    IndexApiMixin,
    LlmCorpusApiMixin,
    SpotApiMixin,
    StockApiMixin,
    UnpublishedApiMixin,
    UsApiMixin,
)
from .base import DEFAULT_BASE_URL, BaseClient, get_base_url, set_base_url


class FtshareClient(
    StockApiMixin,
    HkApiMixin,
    UsApiMixin,
    IndexApiMixin,
    EtfApiMixin,
    FundApiMixin,
    FuturesApiMixin,
    BondApiMixin,
    EconomicApiMixin,
    LlmCorpusApiMixin,
    SpotApiMixin,
    ForexApiMixin,
    UnpublishedApiMixin,
    BaseClient,
):
    """Synchronous client for all documented FTShare data endpoints.

    The class combines ftshare-doc topic mixins while keeping one public
    client surface. Users should continue to construct it via ``ftshare.market_api``.
    """


def market_api(
    base_url: str | None = None,
    timeout: float = 10,
    headers: Mapping[str, str] | None = None,
) -> FtshareClient:
    """Create a synchronous FTShare market data API client.

    Args:
        base_url: Optional client-specific base URL. Defaults to the module
            base URL.
        timeout: Request timeout in seconds.
        headers: Optional headers sent with every request.

    Returns:
        A configured ``FtshareClient`` instance.
    """
    return FtshareClient(base_url=base_url, timeout=timeout, headers=headers)


__all__ = [
    "DEFAULT_BASE_URL",
    "FtshareClient",
    "get_base_url",
    "market_api",
    "set_base_url",
]
