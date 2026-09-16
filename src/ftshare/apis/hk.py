"""Hong Kong market API methods grouped by ftshare-doc."""

from __future__ import annotations

from collections.abc import Sequence
from typing import Any

from ..endpoints import ENDPOINTS


class HkApiMixin:
    """Endpoint methods for the hk ftshare-doc topic."""

    def hk_candlesticks(
        self,
        trade_code: Any | None = None,
        interval_unit: Any | None = None,
        until_date: Any | None = None,
        since_date: Any | None = None,
        interval_value: Any | None = None,
        limit: Any | None = None,
        adjust_kind: Any | None = None,
        *,
        raw: bool = False,
        fields: Sequence[str] | str | None = None,
        as_dataframe: bool = True,
        **kwargs: Any,
    ) -> Any:
        """港股K线."""
        params = {'trade_code': trade_code, 'interval_unit': interval_unit, 'until_date': until_date, 'since_date': since_date, 'interval_value': interval_value, 'limit': limit, 'adjust_kind': adjust_kind}
        params.update(kwargs)
        return self._call_endpoint('hk_candlesticks', raw=raw, fields=fields, as_dataframe=as_dataframe, **params)

    def stk_ah_comparison(self, hk_code: Any | None = None, ts_code: Any | None = None, trade_date: Any | None = None, start_date: Any | None = None, end_date: Any | None = None, page: int | None = None, page_size: int | None = None, limit: int | None = None, all_pages: bool = False, max_pages: int | None = None, *, raw: bool = False, fields: Sequence[str] | str | None = None, as_dataframe: bool = True, **kwargs: Any) -> Any:
        """AH股对比."""
        params = {'hk_code': hk_code, 'ts_code': ts_code, 'trade_date': trade_date, 'start_date': start_date, 'end_date': end_date}
        params.update(kwargs)
        return self.get_paginated(ENDPOINTS['stk_ah_comparison'].path, page=page, page_size=page_size, limit=limit, all_pages=all_pages, max_pages=max_pages, max_page_size=1000, raw=raw, fields=fields, as_dataframe=as_dataframe, **params)

    def hsi_daily_weight(self, trade_date: Any | None = None, start_date: Any | None = None, end_date: Any | None = None, index_slug: Any | None = None, stock_code: Any | None = None, page: int | None = None, page_size: int | None = None, limit: int | None = None, all_pages: bool = False, max_pages: int | None = None, *, raw: bool = False, fields: Sequence[str] | str | None = None, as_dataframe: bool = True, **kwargs: Any) -> Any:
        """恒生指数每日权重."""
        params = {'trade_date': trade_date, 'start_date': start_date, 'end_date': end_date, 'index_slug': index_slug, 'stock_code': stock_code}
        params.update(kwargs)
        return self.get_paginated(ENDPOINTS['hsi_daily_weight'].path, page=page, page_size=page_size, limit=limit, all_pages=all_pages, max_pages=max_pages, raw=raw, fields=fields, as_dataframe=as_dataframe, **params)
