"""Public synchronous FTShare client assembled from domain API mixins."""

from __future__ import annotations

from collections.abc import Mapping

from .apis import (
    CorporateApiMixin,
    EconomicApiMixin,
    EtfApiMixin,
    FinanceApiMixin,
    FundApiMixin,
    FuturesApiMixin,
    GlobalIndexApiMixin,
    GoodwillApiMixin,
    HkApiMixin,
    HolderApiMixin,
    IndexApiMixin,
    MarketApiMixin,
    PledgeApiMixin,
    StockApiMixin,
)
from .base import DEFAULT_BASE_URL, BaseClient, get_base_url, set_base_url


class FtshareClient(
    CorporateApiMixin,
    EconomicApiMixin,
    EtfApiMixin,
    FinanceApiMixin,
    FundApiMixin,
    FuturesApiMixin,
    GlobalIndexApiMixin,
    GoodwillApiMixin,
    HkApiMixin,
    HolderApiMixin,
    IndexApiMixin,
    MarketApiMixin,
    PledgeApiMixin,
    StockApiMixin,
    BaseClient,
):
    """Synchronous client for all documented FTShare data endpoints.

    The class combines small business-domain mixins while keeping one public
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
