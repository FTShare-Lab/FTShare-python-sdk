"""US market API methods grouped by ftshare-doc."""

from __future__ import annotations

from collections.abc import Sequence
from typing import Any

from ..endpoints import ENDPOINTS


class UsApiMixin:
    """Endpoint methods for the us ftshare-doc topic."""

    def eastmoney_us_stock_list(
        self,
        refresh: Any | None = None,
        page: int | None = None,
        page_size: int | None = None,
        limit: int | None = None,
        all_pages: bool = False,
        max_pages: int | None = None,
        *,
        raw: bool = False,
        fields: Sequence[str] | str | None = None,
        as_dataframe: bool = True,
        **kwargs: Any,
    ) -> Any:
        """东方财富美股列表.

        Endpoint: ``api/v1/market/data/eastmoney-us-stock-list``.
        Method: ``GET``.
        Documented endpoint: ``eastmoney_us_stock_list``.

        Args:
            refresh: 为 true 时刷新列表数据 (type: bool; required: N).
            page: Page number, starting from 1. If omitted, the server default is used unless ``limit`` or ``all_pages`` is set.
            page_size: Rows per page. The SDK validates this against the endpoint-specific maximum.
            limit: Maximum number of rows to return. The SDK may fetch multiple pages to satisfy this limit.
            all_pages: Fetch and combine pages until the server reports the last page.
            max_pages: Optional safety cap for ``all_pages``.
            raw: Return the decoded JSON payload without tabular extraction.
            fields: Optional field list or comma-separated field string applied after extraction.
            as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
            **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.
        """
        request_params = {'refresh': refresh}
        request_params.update(kwargs)
        path = ENDPOINTS['eastmoney_us_stock_list'].path
        return self.get_paginated(
            path,
            page=page,
            page_size=page_size,
            limit=limit,
            all_pages=all_pages,
            max_pages=max_pages,
            raw=raw,
            fields=fields,
            as_dataframe=as_dataframe,
            **request_params,
        )

    def eastmoney_us_stock_daily_ohlc(
        self,
        stock_code: Any | None = None,
        start_date: Any | None = None,
        end_date: Any | None = None,
        page: int | None = None,
        page_size: int | None = None,
        limit: int | None = None,
        all_pages: bool = False,
        max_pages: int | None = None,
        *,
        raw: bool = False,
        fields: Sequence[str] | str | None = None,
        as_dataframe: bool = True,
        **kwargs: Any,
    ) -> Any:
        """东方财富美股日OHLC.

        Endpoint: ``api/v1/market/data/eastmoney-us-stock-daily-ohlc``.
        Method: ``GET``.
        Documented endpoint: ``eastmoney_us_stock_daily_kline``.

        Args:
            stock_code: 股票代码，如 AAPL (type: string; required: Y).
            start_date: 起始日期（含），YYYY-MM-DD 或 YYYYMMDD；不传从最早开始 (type: string; required: N).
            end_date: 截止日期（含），YYYY-MM-DD 或 YYYYMMDD；不传到最晚 (type: string; required: N).
            page: Page number, starting from 1. If omitted, the server default is used unless ``limit`` or ``all_pages`` is set.
            page_size: Rows per page. The SDK validates this against the endpoint-specific maximum.
            limit: Maximum number of rows to return. The SDK may fetch multiple pages to satisfy this limit.
            all_pages: Fetch and combine pages until the server reports the last page.
            max_pages: Optional safety cap for ``all_pages``.
            raw: Return the decoded JSON payload without tabular extraction.
            fields: Optional field list or comma-separated field string applied after extraction.
            as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
            **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

        Returns:
            A pandas ``DataFrame`` by default, Python rows when
            ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
            payloads when multi-page fetching is used with ``raw=True``.
        """
        request_params = {'stock_code': stock_code, 'start_date': start_date, 'end_date': end_date}
        request_params.update(kwargs)
        path = ENDPOINTS['eastmoney_us_stock_daily_ohlc'].path
        return self.get_paginated(
            path,
            page=page,
            page_size=page_size,
            limit=limit,
            all_pages=all_pages,
            max_pages=max_pages,
            raw=raw,
            fields=fields,
            as_dataframe=as_dataframe,
            **request_params,
        )
