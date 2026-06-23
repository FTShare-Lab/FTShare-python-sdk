"""FTShare stock endpoint methods generated from ``ftshare-doc/api-doc``."""

from __future__ import annotations

from collections.abc import Sequence
from typing import Any

from ..endpoints import ENDPOINTS


class StockApiMixin:
    """Endpoint methods for the stock API group."""

    def abnormal_trading_details(
        self,
        date: Any | None = None,
        *,
        raw: bool = False,
        fields: Sequence[str] | str | None = None,
        as_dataframe: bool = True,
        **kwargs: Any,
    ) -> Any:
        """龙虎榜明细.

        Endpoint: ``api/v1/market/data/abnormal-trading-details``.
        Method: ``GET``.
        Source document: ``ftshare-doc/api-doc/龙虎榜明细.md``.
        Documented endpoint: ``abnormal_trading_details``.

        Args:
            date: 查询日期 YYYYMMDD；不传则使用当前内存快照 (type: string; required: N).
            raw: Return the decoded JSON payload without tabular extraction.
            fields: Optional field list or comma-separated field string applied after extraction.
            as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
            **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

        Returns:
            A pandas ``DataFrame`` by default, Python rows when
            ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
            payloads when multi-page fetching is used with ``raw=True``.
        """
        request_params = {'date': date}
        request_params.update(kwargs)
        return self._call_endpoint(
            'abnormal_trading_details',
            raw=raw,
            fields=fields,
            as_dataframe=as_dataframe,
            **request_params,
        )

    def abnormal_trading_overview(
        self,
        date: Any | None = None,
        *,
        raw: bool = False,
        fields: Sequence[str] | str | None = None,
        as_dataframe: bool = True,
        **kwargs: Any,
    ) -> Any:
        """龙虎榜总览.

        Endpoint: ``api/v1/market/data/abnormal-trading-overview``.
        Method: ``GET``.
        Source document: ``ftshare-doc/api-doc/龙虎榜总览.md``.
        Documented endpoint: ``abnormal_trading_overview``.

        Args:
            date: 查询日期 YYYYMMDD；不传则使用当前内存快照 (type: string; required: N).
            raw: Return the decoded JSON payload without tabular extraction.
            fields: Optional field list or comma-separated field string applied after extraction.
            as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
            **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

        Returns:
            A pandas ``DataFrame`` by default, Python rows when
            ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
            payloads when multi-page fetching is used with ``raw=True``.
        """
        request_params = {'date': date}
        request_params.update(kwargs)
        return self._call_endpoint(
            'abnormal_trading_overview',
            raw=raw,
            fields=fields,
            as_dataframe=as_dataframe,
            **request_params,
        )

    def block_trades(
        self,
        date: Any | None = None,
        *,
        raw: bool = False,
        fields: Sequence[str] | str | None = None,
        as_dataframe: bool = True,
        **kwargs: Any,
    ) -> Any:
        """大宗交易.

        Endpoint: ``api/v1/market/data/block-trades``.
        Method: ``GET``.
        Source document: ``ftshare-doc/api-doc/大宗交易.md``.
        Documented endpoint: ``block_trades``.

        Args:
            date: 查询日期 YYYYMMDD；不传则使用当前内存快照 (type: string; required: N).
            raw: Return the decoded JSON payload without tabular extraction.
            fields: Optional field list or comma-separated field string applied after extraction.
            as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
            **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

        Returns:
            A pandas ``DataFrame`` by default, Python rows when
            ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
            payloads when multi-page fetching is used with ``raw=True``.
        """
        request_params = {'date': date}
        request_params.update(kwargs)
        return self._call_endpoint(
            'block_trades',
            raw=raw,
            fields=fields,
            as_dataframe=as_dataframe,
            **request_params,
        )

    def limit_down_pool(
        self,
        *,
        raw: bool = False,
        fields: Sequence[str] | str | None = None,
        as_dataframe: bool = True,
        **kwargs: Any,
    ) -> Any:
        """跌停池.

        Endpoint: ``api/v1/market/data/limit-down-pool``.
        Method: ``GET``.
        Source document: ``ftshare-doc/api-doc/跌停池.md``.
        Documented endpoint: ``limit_down_pool``.

        Args:
            raw: Return the decoded JSON payload without tabular extraction.
            fields: Optional field list or comma-separated field string applied after extraction.
            as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
            **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

        Returns:
            A pandas ``DataFrame`` by default, Python rows when
            ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
            payloads when multi-page fetching is used with ``raw=True``.
        """
        request_params = {}
        request_params.update(kwargs)
        return self._call_endpoint(
            'limit_down_pool',
            raw=raw,
            fields=fields,
            as_dataframe=as_dataframe,
            **request_params,
        )

    def limit_event_timeline_3s(
        self,
        symbol: Any | None = None,
        *,
        raw: bool = False,
        fields: Sequence[str] | str | None = None,
        as_dataframe: bool = True,
        **kwargs: Any,
    ) -> Any:
        """涨跌停事件时间线.

        Endpoint: ``api/v1/market/data/limit-event-timeline-3s``.
        Method: ``GET``.
        Source document: ``ftshare-doc/api-doc/涨跌停事件时间线.md``.
        Documented endpoint: ``limit_event_timeline_3s``.

        Args:
            symbol: 标的代码，如 000001.XSHE；不传返回全市场 (type: string; required: N).
            raw: Return the decoded JSON payload without tabular extraction.
            fields: Optional field list or comma-separated field string applied after extraction.
            as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
            **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

        Returns:
            A pandas ``DataFrame`` by default, Python rows when
            ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
            payloads when multi-page fetching is used with ``raw=True``.
        """
        request_params = {'symbol': symbol}
        request_params.update(kwargs)
        return self._call_endpoint(
            'limit_event_timeline_3s',
            raw=raw,
            fields=fields,
            as_dataframe=as_dataframe,
            **request_params,
        )

    def limit_up_break_pool(
        self,
        *,
        raw: bool = False,
        fields: Sequence[str] | str | None = None,
        as_dataframe: bool = True,
        **kwargs: Any,
    ) -> Any:
        """炸板池.

        Endpoint: ``api/v1/market/data/limit-up-break-pool``.
        Method: ``GET``.
        Source document: ``ftshare-doc/api-doc/炸板池.md``.
        Documented endpoint: ``limit_up_break_pool``.

        Args:
            raw: Return the decoded JSON payload without tabular extraction.
            fields: Optional field list or comma-separated field string applied after extraction.
            as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
            **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

        Returns:
            A pandas ``DataFrame`` by default, Python rows when
            ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
            payloads when multi-page fetching is used with ``raw=True``.
        """
        request_params = {}
        request_params.update(kwargs)
        return self._call_endpoint(
            'limit_up_break_pool',
            raw=raw,
            fields=fields,
            as_dataframe=as_dataframe,
            **request_params,
        )

    def limit_up_pool(
        self,
        *,
        raw: bool = False,
        fields: Sequence[str] | str | None = None,
        as_dataframe: bool = True,
        **kwargs: Any,
    ) -> Any:
        """涨停池.

        Endpoint: ``api/v1/market/data/limit-up-pool``.
        Method: ``GET``.
        Source document: ``ftshare-doc/api-doc/涨停池.md``.
        Documented endpoint: ``limit_up_pool``.

        Args:
            raw: Return the decoded JSON payload without tabular extraction.
            fields: Optional field list or comma-separated field string applied after extraction.
            as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
            **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

        Returns:
            A pandas ``DataFrame`` by default, Python rows when
            ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
            payloads when multi-page fetching is used with ``raw=True``.
        """
        request_params = {}
        request_params.update(kwargs)
        return self._call_endpoint(
            'limit_up_pool',
            raw=raw,
            fields=fields,
            as_dataframe=as_dataframe,
            **request_params,
        )

    def limit_up_pool_yesterday(
        self,
        *,
        raw: bool = False,
        fields: Sequence[str] | str | None = None,
        as_dataframe: bool = True,
        **kwargs: Any,
    ) -> Any:
        """昨日涨停池.

        Endpoint: ``api/v1/market/data/limit-up-pool-yesterday``.
        Method: ``GET``.
        Source document: ``ftshare-doc/api-doc/昨日涨停池.md``.
        Documented endpoint: ``limit_up_pool_yesterday``.

        Args:
            raw: Return the decoded JSON payload without tabular extraction.
            fields: Optional field list or comma-separated field string applied after extraction.
            as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
            **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

        Returns:
            A pandas ``DataFrame`` by default, Python rows when
            ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
            payloads when multi-page fetching is used with ``raw=True``.
        """
        request_params = {}
        request_params.update(kwargs)
        return self._call_endpoint(
            'limit_up_pool_yesterday',
            raw=raw,
            fields=fields,
            as_dataframe=as_dataframe,
            **request_params,
        )

    def margin_trading_details(
        self,
        date: Any | None = None,
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
        """融资融券明细.

        Endpoint: ``api/v1/market/data/margin-trading-details``.
        Method: ``GET``.
        Source document: ``ftshare-doc/api-doc/融资融券明细.md``.
        Documented endpoint: ``margin_trading_details``.

        Args:
            date: 查询日期 YYYYMMDD；不传则使用当前内存快照 (type: string; required: N).
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
        request_params = {'date': date}
        request_params.update(kwargs)
        path = ENDPOINTS['margin_trading_details'].path
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

    def margin_trading_details_paginated(
        self,
        date: Any | None = None,
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
        """融资融券明细分页.

        Endpoint: ``api/v1/market/data/margin-trading-details``.
        Method: ``GET``.
        Source document: ``ftshare-doc/api-doc/融资融券明细分页.md``.
        Documented endpoint: ``margin_trading_details_paginated``.

        Args:
            date: 查询日期 YYYYMMDD；不传则使用当前内存快照 (type: string; required: N).
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
        request_params = {'date': date}
        request_params.update(kwargs)
        path = ENDPOINTS['margin_trading_details_paginated'].path
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

    def risk_warning_stock_quotes(
        self,
        date: Any | None = None,
        *,
        raw: bool = False,
        fields: Sequence[str] | str | None = None,
        as_dataframe: bool = True,
        **kwargs: Any,
    ) -> Any:
        """风险警示股行情.

        Endpoint: ``api/v1/market/data/risk-warning-stocks/quotes``.
        Method: ``GET``.
        Source document: ``ftshare-doc/api-doc/风险警示股行情.md``.
        Documented endpoint: ``risk_warning_stock_quotes``.

        Args:
            date: 交易日，格式 YYYYMMDD (type: string; required: Y).
            raw: Return the decoded JSON payload without tabular extraction.
            fields: Optional field list or comma-separated field string applied after extraction.
            as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
            **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

        Returns:
            A pandas ``DataFrame`` by default, Python rows when
            ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
            payloads when multi-page fetching is used with ``raw=True``.
        """
        request_params = {'date': date}
        request_params.update(kwargs)
        return self._call_endpoint(
            'risk_warning_stock_quotes',
            raw=raw,
            fields=fields,
            as_dataframe=as_dataframe,
            **request_params,
        )

    def risk_warning_stocks(
        self,
        date: Any | None = None,
        *,
        raw: bool = False,
        fields: Sequence[str] | str | None = None,
        as_dataframe: bool = True,
        **kwargs: Any,
    ) -> Any:
        """风险警示股.

        Endpoint: ``api/v1/market/data/risk-warning-stocks``.
        Method: ``GET``.
        Source document: ``ftshare-doc/api-doc/风险警示股.md``.
        Documented endpoint: ``risk_warning_stocks``.

        Args:
            date: 交易日，格式 YYYYMMDD (type: string; required: Y).
            raw: Return the decoded JSON payload without tabular extraction.
            fields: Optional field list or comma-separated field string applied after extraction.
            as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
            **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

        Returns:
            A pandas ``DataFrame`` by default, Python rows when
            ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
            payloads when multi-page fetching is used with ``raw=True``.
        """
        request_params = {'date': date}
        request_params.update(kwargs)
        return self._call_endpoint(
            'risk_warning_stocks',
            raw=raw,
            fields=fields,
            as_dataframe=as_dataframe,
            **request_params,
        )

    def stk_limit(
        self,
        instrument_type: Any | None = None,
        symbol: Any | None = None,
        symbol_id: Any | None = None,
        market_id: Any | None = None,
        trade_date: Any | None = None,
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
        """涨跌停价.

        Endpoint: ``api/v1/market/data/stk-limit``.
        Method: ``GET``.
        Source document: ``ftshare-doc/api-doc/涨跌停价.md``.
        Documented endpoint: ``stk_limit``.

        Args:
            instrument_type: 标的类型：stock / etf / cb；不传返回三类（排除指数） (type: string; required: N).
            symbol: 标的代码，支持 000001.SZ / 000001.XSHE / 600519.SH 等；存在时忽略 symbol_id+market_id (type: string; required: N).
            symbol_id: 标的 ID，与 market_id 配合使用 (type: int32; required: N).
            market_id: 市场 ID，与 symbol_id 配合使用 (type: int16; required: N).
            trade_date: 交易日 YYYYMMDD，查单日全市场时使用 (type: int32; required: N).
            start_date: 单票历史区间起始日 YYYYMMDD（需配 symbol 或 symbol_id+market_id） (type: int32; required: N).
            end_date: 单票历史区间结束日 YYYYMMDD (type: int32; required: N).
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
        request_params = {'instrument_type': instrument_type, 'symbol': symbol, 'symbol_id': symbol_id, 'market_id': market_id, 'trade_date': trade_date, 'start_date': start_date, 'end_date': end_date}
        request_params.update(kwargs)
        path = ENDPOINTS['stk_limit'].path
        return self.get_paginated(
            path,
            page=page,
            page_size=page_size,
            limit=limit,
            all_pages=all_pages,
            max_pages=max_pages,
            max_page_size=500,
            raw=raw,
            fields=fields,
            as_dataframe=as_dataframe,
            **request_params,
        )

    def stk_premarket(
        self,
        ts_code: Any | None = None,
        trade_date: Any | None = None,
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
        """盘前数据.

        Endpoint: ``api/v1/market/data/stk-premarket``.
        Method: ``GET``.
        Source document: ``ftshare-doc/api-doc/盘前数据.md``.
        Documented endpoint: ``stk_premarket``.

        Args:
            ts_code: 股票代码，如 000001.SZ / 600519.SH (type: string; required: N).
            trade_date: 交易日 YYYYMMDD，查单日全市场时使用 (type: int32; required: N).
            start_date: 单票历史区间起始日 YYYYMMDD（需配 ts_code） (type: int32; required: N).
            end_date: 单票历史区间结束日 YYYYMMDD (type: int32; required: N).
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
        request_params = {'ts_code': ts_code, 'trade_date': trade_date, 'start_date': start_date, 'end_date': end_date}
        request_params.update(kwargs)
        path = ENDPOINTS['stk_premarket'].path
        return self.get_paginated(
            path,
            page=page,
            page_size=page_size,
            limit=limit,
            all_pages=all_pages,
            max_pages=max_pages,
            max_page_size=500,
            raw=raw,
            fields=fields,
            as_dataframe=as_dataframe,
            **request_params,
        )

    def stock_adjust_factor(
        self,
        symbol: Any | None = None,
        trade_date: Any | None = None,
        start_date: Any | None = None,
        end_date: Any | None = None,
        offset: Any | None = None,
        limit: Any | None = None,
        *,
        raw: bool = False,
        fields: Sequence[str] | str | None = None,
        as_dataframe: bool = True,
        **kwargs: Any,
    ) -> Any:
        """股票复权因子.

        Endpoint: ``api/v1/market/data/stock-adjust-factor``.
        Method: ``GET``.
        Source document: ``ftshare-doc/api-doc/股票复权因子.md``.
        Documented endpoint: ``stock_adjust_factor``.

        Args:
            symbol: 股票代码，支持纯数字或带后缀格式；区间扫描必填 (type: string; required: N).
            trade_date: 交易日期 YYYYMMDD；空则默认当天，非交易日回退前一交易日 (type: string; required: N).
            start_date: 区间起始日期 YYYYMMDD；区间扫描必填且需配 symbol (type: string; required: N).
            end_date: 区间结束日期 YYYYMMDD；区间扫描必填且需配 symbol (type: string; required: N).
            offset: 返回结果起始偏移 (type: int; required: N).
            limit: 返回结果最大条数 (type: int; required: N).
            raw: Return the decoded JSON payload without tabular extraction.
            fields: Optional field list or comma-separated field string applied after extraction.
            as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
            **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

        Returns:
            A pandas ``DataFrame`` by default, Python rows when
            ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
            payloads when multi-page fetching is used with ``raw=True``.
        """
        request_params = {'symbol': symbol, 'trade_date': trade_date, 'start_date': start_date, 'end_date': end_date, 'offset': offset, 'limit': limit}
        request_params.update(kwargs)
        return self._call_endpoint(
            'stock_adjust_factor',
            raw=raw,
            fields=fields,
            as_dataframe=as_dataframe,
            **request_params,
        )

    def stock_announcements(
        self,
        stock_code: Any | None = None,
        start_date: Any | None = None,
        end_date: Any | None = None,
        type: Any | None = None,
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
        """公告列表.

        Endpoint: ``api/v1/market/data/announcements/stock-announcements``.
        Method: ``GET``.
        Source document: ``ftshare-doc/api-doc/公告列表.md``.
        Documented endpoint: ``stock_announcements``.

        Args:
            stock_code: 证券代码（按标的查询时必填） (type: string; required: N).
            start_date: 开始日期 YYYYMMDD（按日期范围查询时必填） (type: string; required: N).
            end_date: 结束日期 YYYYMMDD，不填默认当前时间 (type: string; required: N).
            type: 查询类型，当前只支持 `stock` (type: string; required: Y).
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
        request_params = {'stock_code': stock_code, 'start_date': start_date, 'end_date': end_date, 'type': type}
        request_params.update(kwargs)
        path = ENDPOINTS['stock_announcements'].path
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

    def stock_candlesticks(
        self,
        symbol: Any | None = None,
        interval_unit: Any | None = None,
        interval_value: Any | None = None,
        adjust_kind: Any | None = None,
        since_ts_millis: Any | None = None,
        until_ts_millis: Any | None = None,
        limit: Any | None = None,
        *,
        raw: bool = False,
        fields: Sequence[str] | str | None = None,
        as_dataframe: bool = True,
        **kwargs: Any,
    ) -> Any:
        """股票K线.

        Endpoint: ``api/v1/market/data/stock-candlesticks``.
        Method: ``POST``.
        Source document: ``ftshare-doc/api-doc/股票K线.md``.
        Documented endpoint: ``stock_candlesticks``.

        Args:
            symbol: 标的代码，如 000001.SZ (type: SymbolKey; required: Y).
            interval_unit: 周期单位：Minute/Day/Week/Month/Year (type: enum; required: Y).
            interval_value: 间隔数值（默认1，如 Day+1=日K，Minute+5=5分钟） (type: int; required: N).
            adjust_kind: 复权：None(默认,除权)/Forward(前复权)/Backward(后复权) (type: enum; required: N).
            since_ts_millis: 开始时间戳（毫秒）；与 until 跨度 ≤3 天 (type: DateTime(ms); required: N).
            until_ts_millis: 结束时间戳（毫秒） (type: DateTime(ms); required: Y).
            limit: 返回条数上限 (type: int; required: N).
            raw: Return the decoded JSON payload without tabular extraction.
            fields: Optional field list or comma-separated field string applied after extraction.
            as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
            **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

        Returns:
            A pandas ``DataFrame`` by default, Python rows when
            ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
            payloads when multi-page fetching is used with ``raw=True``.
        """
        request_params = {'symbol': symbol, 'interval_unit': interval_unit, 'interval_value': interval_value, 'adjust_kind': adjust_kind, 'since_ts_millis': since_ts_millis, 'until_ts_millis': until_ts_millis, 'limit': limit}
        request_params.update(kwargs)
        return self._call_endpoint(
            'stock_candlesticks',
            raw=raw,
            fields=fields,
            as_dataframe=as_dataframe,
            **request_params,
        )

    def stock_candlesticks_batch(
        self,
        symbols: Any | None = None,
        interval_unit: Any | None = None,
        interval_value: Any | None = None,
        adjust_kind: Any | None = None,
        since_ts_millis: Any | None = None,
        until_ts_millis: Any | None = None,
        limit: Any | None = None,
        *,
        raw: bool = False,
        fields: Sequence[str] | str | None = None,
        as_dataframe: bool = True,
        **kwargs: Any,
    ) -> Any:
        """批量股票K线.

        Endpoint: ``api/v1/market/data/stock-candlesticks/batch``.
        Method: ``POST``.
        Source document: ``ftshare-doc/api-doc/批量股票K线.md``.
        Documented endpoint: ``stock_candlesticks_batch``.

        Args:
            symbols: 标的代码列表，如 ["000001.SZ","600000.SH"] (type: array[SymbolKey]; required: Y).
            interval_unit: 周期单位：Minute/Day/Week/Month/Year (type: enum; required: Y).
            interval_value: 间隔数值（默认1） (type: int; required: N).
            adjust_kind: 复权：None(默认)/Forward(前复权)/Backward(后复权) (type: enum; required: N).
            since_ts_millis: 开始时间戳（毫秒）；与 until 跨度 ≤3 天 (type: DateTime(ms); required: N).
            until_ts_millis: 结束时间戳（毫秒） (type: DateTime(ms); required: Y).
            limit: 每标的返回条数上限 (type: int; required: N).
            raw: Return the decoded JSON payload without tabular extraction.
            fields: Optional field list or comma-separated field string applied after extraction.
            as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
            **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

        Returns:
            A pandas ``DataFrame`` by default, Python rows when
            ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
            payloads when multi-page fetching is used with ``raw=True``.
        """
        request_params = {'symbols': symbols, 'interval_unit': interval_unit, 'interval_value': interval_value, 'adjust_kind': adjust_kind, 'since_ts_millis': since_ts_millis, 'until_ts_millis': until_ts_millis, 'limit': limit}
        request_params.update(kwargs)
        return self._call_endpoint(
            'stock_candlesticks_batch',
            raw=raw,
            fields=fields,
            as_dataframe=as_dataframe,
            **request_params,
        )

    def stock_capital_flows(
        self,
        date: Any | None = None,
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
        """股票资金流向.

        Endpoint: ``api/v1/market/data/stock-capital-flows``.
        Method: ``GET``.
        Source document: ``ftshare-doc/api-doc/股票资金流向.md``.
        Documented endpoint: ``stock_capital_flows_paginated``.

        Args:
            date: 查询日期 YYYYMMDD；传入时查询该日 15:30 快照 (type: string; required: N).
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
        request_params = {'date': date}
        request_params.update(kwargs)
        path = ENDPOINTS['stock_capital_flows'].path
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

    def stock_capital_flows_paginated(
        self,
        date: Any | None = None,
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
        """股票资金流向.

        Endpoint: ``api/v1/market/data/stock-capital-flows``.
        Method: ``GET``.
        Source document: ``ftshare-doc/api-doc/股票资金流向.md``.
        Documented endpoint: ``stock_capital_flows_paginated``.

        Args:
            date: 查询日期 YYYYMMDD；传入时查询该日 15:30 快照 (type: string; required: N).
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
        request_params = {'date': date}
        request_params.update(kwargs)
        path = ENDPOINTS['stock_capital_flows_paginated'].path
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

    def stock_comment_desire_em(
        self,
        symbol: Any | None = None,
        *,
        raw: bool = False,
        fields: Sequence[str] | str | None = None,
        as_dataframe: bool = True,
        **kwargs: Any,
    ) -> Any:
        """千股千评意愿度.

        Endpoint: ``api/v1/market/data/stock-comment/desire``.
        Method: ``GET``.
        Source document: ``ftshare-doc/api-doc/千股千评意愿度.md``.
        Documented endpoint: ``stock_comment_desire_em``.

        Args:
            symbol: 证券代码（纯数字，如 600000） (type: string; required: Y).
            raw: Return the decoded JSON payload without tabular extraction.
            fields: Optional field list or comma-separated field string applied after extraction.
            as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
            **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

        Returns:
            A pandas ``DataFrame`` by default, Python rows when
            ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
            payloads when multi-page fetching is used with ``raw=True``.
        """
        request_params = {'symbol': symbol}
        request_params.update(kwargs)
        return self._call_endpoint(
            'stock_comment_desire_em',
            raw=raw,
            fields=fields,
            as_dataframe=as_dataframe,
            **request_params,
        )

    def stock_comment_em(
        self,
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
        """千股千评.

        Endpoint: ``api/v1/market/data/stock-comment/index``.
        Method: ``GET``.
        Source document: ``ftshare-doc/api-doc/千股千评.md``.
        Documented endpoint: ``stock_comment_em``.

        Args:
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
        request_params = {}
        request_params.update(kwargs)
        path = ENDPOINTS['stock_comment_em'].path
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

    def stock_comment_focus_em(
        self,
        symbol: Any | None = None,
        *,
        raw: bool = False,
        fields: Sequence[str] | str | None = None,
        as_dataframe: bool = True,
        **kwargs: Any,
    ) -> Any:
        """千股千评关注度.

        Endpoint: ``api/v1/market/data/stock-comment/focus``.
        Method: ``GET``.
        Source document: ``ftshare-doc/api-doc/千股千评关注度.md``.
        Documented endpoint: ``stock_comment_focus_em``.

        Args:
            symbol: 证券代码（纯数字，如 600000） (type: string; required: Y).
            raw: Return the decoded JSON payload without tabular extraction.
            fields: Optional field list or comma-separated field string applied after extraction.
            as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
            **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

        Returns:
            A pandas ``DataFrame`` by default, Python rows when
            ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
            payloads when multi-page fetching is used with ``raw=True``.
        """
        request_params = {'symbol': symbol}
        request_params.update(kwargs)
        return self._call_endpoint(
            'stock_comment_focus_em',
            raw=raw,
            fields=fields,
            as_dataframe=as_dataframe,
            **request_params,
        )

    def stock_comment_org_participate_em(
        self,
        symbol: Any | None = None,
        *,
        raw: bool = False,
        fields: Sequence[str] | str | None = None,
        as_dataframe: bool = True,
        **kwargs: Any,
    ) -> Any:
        """机构参与度.

        Endpoint: ``api/v1/market/data/stock-comment/org-participate``.
        Method: ``GET``.
        Source document: ``ftshare-doc/api-doc/机构参与度.md``.
        Documented endpoint: ``stock_comment_org_participate_em``.

        Args:
            symbol: 证券代码（纯数字，如 600000） (type: string; required: Y).
            raw: Return the decoded JSON payload without tabular extraction.
            fields: Optional field list or comma-separated field string applied after extraction.
            as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
            **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

        Returns:
            A pandas ``DataFrame`` by default, Python rows when
            ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
            payloads when multi-page fetching is used with ``raw=True``.
        """
        request_params = {'symbol': symbol}
        request_params.update(kwargs)
        return self._call_endpoint(
            'stock_comment_org_participate_em',
            raw=raw,
            fields=fields,
            as_dataframe=as_dataframe,
            **request_params,
        )

    def stock_comment_score_em(
        self,
        symbol: Any | None = None,
        *,
        raw: bool = False,
        fields: Sequence[str] | str | None = None,
        as_dataframe: bool = True,
        **kwargs: Any,
    ) -> Any:
        """千股千评评分.

        Endpoint: ``api/v1/market/data/stock-comment/score``.
        Method: ``GET``.
        Source document: ``ftshare-doc/api-doc/千股千评评分.md``.
        Documented endpoint: ``stock_comment_score_em``.

        Args:
            symbol: 证券代码（纯数字，如 600000） (type: string; required: Y).
            raw: Return the decoded JSON payload without tabular extraction.
            fields: Optional field list or comma-separated field string applied after extraction.
            as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
            **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

        Returns:
            A pandas ``DataFrame`` by default, Python rows when
            ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
            payloads when multi-page fetching is used with ``raw=True``.
        """
        request_params = {'symbol': symbol}
        request_params.update(kwargs)
        return self._call_endpoint(
            'stock_comment_score_em',
            raw=raw,
            fields=fields,
            as_dataframe=as_dataframe,
            **request_params,
        )

    def stock_dividends_paginated(
        self,
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
        """股票分红记录分页.

        Endpoint: ``api/v1/market/data/dividends``.
        Method: ``GET``.
        Source document: ``ftshare-doc/api-doc/股票分红记录分页.md``.
        Documented endpoint: ``stock_dividends_paginated``.

        Args:
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
        request_params = {}
        request_params.update(kwargs)
        path = ENDPOINTS['stock_dividends_paginated'].path
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

    def stock_filter(
        self,
        board: Any | None = None,
        listing_date_since: Any | None = None,
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
        """股票筛选.

        Endpoint: ``api/v1/market/data/stock-list/filter``.
        Method: ``GET``.
        Source document: ``ftshare-doc/api-doc/股票筛选.md``.
        Documented endpoint: ``stock_filter``.

        Args:
            board: 板块/交易所筛选：`star` / `chi_next` / `bjse` / `xshg` / `xshe` / `main` (type: string; required: N).
            listing_date_since: 上市日期起点 YYYYMMDD，筛选此后上市的股票 (type: string; required: N).
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
        request_params = {'board': board, 'listing_date_since': listing_date_since}
        request_params.update(kwargs)
        path = ENDPOINTS['stock_filter'].path
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

    def stock_institution_holdings(
        self,
        year: Any | None = None,
        report_type: Any | None = None,
        inst_type: Any | None = None,
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
        """机构持股.

        Endpoint: ``api/v1/market/data/share/stock-institution-holdings``.
        Method: ``GET``.
        Source document: ``ftshare-doc/api-doc/机构持股.md``.
        Documented endpoint: ``get_stock_institution_holdings``.

        Args:
            year: 年份 (type: int; required: Y).
            report_type: 报告类型：q1 / q2 / q3 / annual / announcement (type: ReportType; required: Y).
            inst_type: 机构类型：all_inst / fund / qfii / insurance / social_security / securities / trust / other (type: InstitutionType; required: Y).
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
        request_params = {'year': year, 'report_type': report_type, 'inst_type': inst_type}
        request_params.update(kwargs)
        path = ENDPOINTS['stock_institution_holdings'].path
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

    def stock_institution_holdings_detail(
        self,
        stock_code: Any | None = None,
        year: Any | None = None,
        report_type: Any | None = None,
        inst_type: Any | None = None,
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
        """机构持股明细.

        Endpoint: ``api/v1/market/data/share/stock-institution-holdings-detail``.
        Method: ``GET``.
        Source document: ``ftshare-doc/api-doc/机构持股明细.md``.
        Documented endpoint: ``get_stock_institution_holdings_detail``.

        Args:
            stock_code: 股票代码 (type: string; required: Y).
            year: 年份 (type: int; required: Y).
            report_type: 报告类型：q1 / q2 / q3 / annual / announcement (type: ReportType; required: Y).
            inst_type: 机构类型：all_inst / fund / qfii / insurance / social_security / securities / trust / other (type: InstitutionType; required: Y).
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
        request_params = {'stock_code': stock_code, 'year': year, 'report_type': report_type, 'inst_type': inst_type}
        request_params.update(kwargs)
        path = ENDPOINTS['stock_institution_holdings_detail'].path
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

    def stock_institution_share_holdings(
        self,
        institution_id: Any | None = None,
        year: Any | None = None,
        report_type: Any | None = None,
        invest_type: Any | None = None,
        *,
        raw: bool = False,
        fields: Sequence[str] | str | None = None,
        as_dataframe: bool = True,
        **kwargs: Any,
    ) -> Any:
        """机构股本持股.

        Endpoint: ``api/v1/market/data/institution/institution-share-holdings``.
        Method: ``GET``.
        Source document: ``ftshare-doc/api-doc/机构股本持股.md``.
        Documented endpoint: ``get_stock_institution_share_holdings``.

        Args:
            institution_id: 机构 ID (type: string; required: Y).
            year: 年份 (type: int; required: Y).
            report_type: 报告类型：q1 / q2 / q3 / annual / announcement (type: ReportType; required: Y).
            invest_type: 持仓类型：all / stock / fund / bond / other (type: InvestType; required: Y).
            raw: Return the decoded JSON payload without tabular extraction.
            fields: Optional field list or comma-separated field string applied after extraction.
            as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
            **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

        Returns:
            A pandas ``DataFrame`` by default, Python rows when
            ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
            payloads when multi-page fetching is used with ``raw=True``.
        """
        request_params = {'institution_id': institution_id, 'year': year, 'report_type': report_type, 'invest_type': invest_type}
        request_params.update(kwargs)
        return self._call_endpoint(
            'stock_institution_share_holdings',
            raw=raw,
            fields=fields,
            as_dataframe=as_dataframe,
            **request_params,
        )

    def stock_intraday(
        self,
        symbol: Any | None = None,
        *,
        raw: bool = False,
        fields: Sequence[str] | str | None = None,
        as_dataframe: bool = True,
        **kwargs: Any,
    ) -> Any:
        """股票日内分时.

        Endpoint: ``api/v1/market/security/{symbol}/intraday``.
        Method: ``GET``.
        Source document: ``ftshare-doc/api-doc/股票日内分时.md``.
        Documented endpoint: ``stock_intraday``.

        Args:
            symbol: 标的代码 (type: SymbolKey; required: Y).
            raw: Return the decoded JSON payload without tabular extraction.
            fields: Optional field list or comma-separated field string applied after extraction.
            as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
            **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

        Returns:
            A pandas ``DataFrame`` by default, Python rows when
            ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
            payloads when multi-page fetching is used with ``raw=True``.
        """
        request_params = {}
        request_params.update(kwargs)
        return self._call_endpoint(
            'stock_intraday',
            path_params={'symbol': symbol},
            raw=raw,
            fields=fields,
            as_dataframe=as_dataframe,
            **request_params,
        )

    def stock_intraday_auction_volume(
        self,
        trade_date: Any | None = None,
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
        """集合竞价成交量.

        Endpoint: ``api/v1/market/data/intraday-auction-volume``.
        Method: ``GET``.
        Source document: ``ftshare-doc/api-doc/集合竞价成交量.md``.
        Documented endpoint: ``stock_intraday_auction_volume``.

        Args:
            trade_date: 交易日期 YYYYMMDD；不传返回当日实时数据 (type: string; required: N).
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
        request_params = {'trade_date': trade_date}
        request_params.update(kwargs)
        path = ENDPOINTS['stock_intraday_auction_volume'].path
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

    def stock_intraday_auction_volume_symbol(
        self,
        symbol: Any | None = None,
        trade_date: Any | None = None,
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
        """单标的集合竞价成交量.

        Endpoint: ``api/v1/market/data/intraday-auction-volume/symbol``.
        Method: ``GET``.
        Source document: ``ftshare-doc/api-doc/单标的集合竞价成交量.md``.
        Documented endpoint: ``stock_intraday_auction_volume_symbol``.

        Args:
            symbol: 标的代码，格式 code.suffix（XSHG/SH、XSHE/SZ、BJSE/BJ） (type: string; required: Y).
            trade_date: 交易日期 YYYYMMDD；不传返回当日实时数据 (type: string; required: N).
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
        request_params = {'symbol': symbol, 'trade_date': trade_date}
        request_params.update(kwargs)
        path = ENDPOINTS['stock_intraday_auction_volume_symbol'].path
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

    def stock_ipos(
        self,
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
        """股票IPO.

        Endpoint: ``api/v1/market/data/stock-ipos``.
        Method: ``GET``.
        Source document: ``ftshare-doc/api-doc/股票IPO.md``.
        Documented endpoint: ``stock_ipos``.

        Args:
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
        request_params = {}
        request_params.update(kwargs)
        path = ENDPOINTS['stock_ipos'].path
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

    def stock_ipos_paginated(
        self,
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
        """股票IPO分页.

        Endpoint: ``api/v1/market/data/stock-ipos``.
        Method: ``GET``.
        Source document: ``ftshare-doc/api-doc/股票IPO分页.md``.
        Documented endpoint: ``stock_ipos_paginated``.

        Args:
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
        request_params = {}
        request_params.update(kwargs)
        path = ENDPOINTS['stock_ipos_paginated'].path
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

    def stock_list(
        self,
        *,
        raw: bool = False,
        fields: Sequence[str] | str | None = None,
        as_dataframe: bool = True,
        **kwargs: Any,
    ) -> Any:
        """股票列表.

        Endpoint: ``api/v1/market/data/stock-list``.
        Method: ``GET``.
        Source document: ``ftshare-doc/api-doc/股票列表.md``.
        Documented endpoint: ``get_stock_list``.

        Args:
            raw: Return the decoded JSON payload without tabular extraction.
            fields: Optional field list or comma-separated field string applied after extraction.
            as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
            **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

        Returns:
            A pandas ``DataFrame`` by default, Python rows when
            ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
            payloads when multi-page fetching is used with ``raw=True``.
        """
        request_params = {}
        request_params.update(kwargs)
        return self._call_endpoint(
            'stock_list',
            raw=raw,
            fields=fields,
            as_dataframe=as_dataframe,
            **request_params,
        )

    def stock_market(
        self,
        scope: Any | None = None,
        *,
        raw: bool = False,
        fields: Sequence[str] | str | None = None,
        as_dataframe: bool = True,
        **kwargs: Any,
    ) -> Any:
        """股票市场行情.

        Endpoint: ``api/v1/market/data/daec/market/snapshot``.
        Method: ``GET``.
        Source document: ``ftshare-doc/api-doc/股票市场行情.md``.
        Documented endpoint: ``stock_market``.

        Args:
            scope: 市场范围：ChinaStock(默认) / Xshg / Xshe / Bjse (type: string; required: N).
            raw: Return the decoded JSON payload without tabular extraction.
            fields: Optional field list or comma-separated field string applied after extraction.
            as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
            **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

        Returns:
            A pandas ``DataFrame`` by default, Python rows when
            ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
            payloads when multi-page fetching is used with ``raw=True``.
        """
        request_params = {'scope': scope}
        request_params.update(kwargs)
        return self._call_endpoint(
            'stock_market',
            raw=raw,
            fields=fields,
            as_dataframe=as_dataframe,
            **request_params,
        )

    def stock_market_distribution_intraday(
        self,
        scope: Any | None = None,
        *,
        raw: bool = False,
        fields: Sequence[str] | str | None = None,
        as_dataframe: bool = True,
        **kwargs: Any,
    ) -> Any:
        """市场涨跌分布分时.

        Endpoint: ``api/v1/market/data/daec/market/distribution-history``.
        Method: ``GET``.
        Source document: ``ftshare-doc/api-doc/市场涨跌分布分时.md``.
        Documented endpoint: ``stock_market_distribution_intraday``.

        Args:
            scope: 市场范围：ChinaStock(默认) / Xshg / Xshe / Bjse (type: string; required: N).
            raw: Return the decoded JSON payload without tabular extraction.
            fields: Optional field list or comma-separated field string applied after extraction.
            as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
            **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

        Returns:
            A pandas ``DataFrame`` by default, Python rows when
            ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
            payloads when multi-page fetching is used with ``raw=True``.
        """
        request_params = {'scope': scope}
        request_params.update(kwargs)
        return self._call_endpoint(
            'stock_market_distribution_intraday',
            raw=raw,
            fields=fields,
            as_dataframe=as_dataframe,
            **request_params,
        )

    def stock_prev_close(
        self,
        symbol: Any | None = None,
        since: Any | None = None,
        until: Any | None = None,
        *,
        raw: bool = False,
        fields: Sequence[str] | str | None = None,
        as_dataframe: bool = True,
        **kwargs: Any,
    ) -> Any:
        """股票前收盘价.

        Endpoint: ``api/v1/market/data/daec/history/prev-closes``.
        Method: ``GET``.
        Source document: ``ftshare-doc/api-doc/股票前收盘价.md``.
        Documented endpoint: ``stock_prev_close``.

        Args:
            symbol: 标的代码 (type: SymbolKey; required: Y).
            since: 开始日期，格式 YYYYMMDD (type: date; required: Y).
            until: 结束日期，格式 YYYYMMDD (type: date; required: Y).
            raw: Return the decoded JSON payload without tabular extraction.
            fields: Optional field list or comma-separated field string applied after extraction.
            as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
            **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

        Returns:
            A pandas ``DataFrame`` by default, Python rows when
            ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
            payloads when multi-page fetching is used with ``raw=True``.
        """
        request_params = {'symbol': symbol, 'since': since, 'until': until}
        request_params.update(kwargs)
        return self._call_endpoint(
            'stock_prev_close',
            raw=raw,
            fields=fields,
            as_dataframe=as_dataframe,
            **request_params,
        )

    def stock_rating_top5(
        self,
        date: Any | None = None,
        variant: Any | None = None,
        type: Any | None = None,
        *,
        raw: bool = False,
        fields: Sequence[str] | str | None = None,
        as_dataframe: bool = True,
        **kwargs: Any,
    ) -> Any:
        """飞兔股票评级Top5.

        Endpoint: ``api/v1/market/data/feitu/stock-rating-top5``.
        Method: ``GET``.
        Source document: ``ftshare-doc/api-doc/飞兔股票评级Top5.md``.
        Documented endpoint: ``stock_rating_top5``.

        Args:
            date: 日期 YYYYMMDD (type: string; required: Y).
            variant: 档位，如 300001（30w01）、300000（30w），默认 300001 (type: string; required: N).
            type: 市场：all / xshg / xshe / bjse，默认 all (type: StockRatingMarketFilter; required: N).
            raw: Return the decoded JSON payload without tabular extraction.
            fields: Optional field list or comma-separated field string applied after extraction.
            as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
            **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

        Returns:
            A pandas ``DataFrame`` by default, Python rows when
            ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
            payloads when multi-page fetching is used with ``raw=True``.
        """
        request_params = {'date': date, 'variant': variant, 'type': type}
        request_params.update(kwargs)
        return self._call_endpoint(
            'stock_rating_top5',
            raw=raw,
            fields=fields,
            as_dataframe=as_dataframe,
            **request_params,
        )

    def stock_related(
        self,
        symbol: Any | None = None,
        limit: Any | None = None,
        *,
        raw: bool = False,
        fields: Sequence[str] | str | None = None,
        as_dataframe: bool = True,
        **kwargs: Any,
    ) -> Any:
        """相关股票.

        Endpoint: ``api/v1/market/security/{symbol}/related``.
        Method: ``GET``.
        Source document: ``ftshare-doc/api-doc/相关股票.md``.
        Documented endpoint: ``stock_related``.

        Args:
            symbol: 标的代码 (type: SymbolKey; required: Y).
            limit: 返回数量上限，服务端默认 3 (type: int; required: N).
            raw: Return the decoded JSON payload without tabular extraction.
            fields: Optional field list or comma-separated field string applied after extraction.
            as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
            **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

        Returns:
            A pandas ``DataFrame`` by default, Python rows when
            ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
            payloads when multi-page fetching is used with ``raw=True``.
        """
        request_params = {'limit': limit}
        request_params.update(kwargs)
        return self._call_endpoint(
            'stock_related',
            path_params={'symbol': symbol},
            raw=raw,
            fields=fields,
            as_dataframe=as_dataframe,
            **request_params,
        )

    def stock_reports(
        self,
        stock_code: Any | None = None,
        start_date: Any | None = None,
        end_date: Any | None = None,
        type: Any | None = None,
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
        """研报列表.

        Endpoint: ``api/v1/market/data/report/stock-reports``.
        Method: ``GET``.
        Source document: ``ftshare-doc/api-doc/研报列表.md``.
        Documented endpoint: ``stock_reports``.

        Args:
            stock_code: 证券代码（按标的查询时必填） (type: string; required: N).
            start_date: 开始日期 YYYYMMDD（按日期范围查询时必填） (type: string; required: N).
            end_date: 结束日期 YYYYMMDD，不填默认当前时间 (type: string; required: N).
            type: 查询类型，当前只支持 `stock` (type: string; required: Y).
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
        request_params = {'stock_code': stock_code, 'start_date': start_date, 'end_date': end_date, 'type': type}
        request_params.update(kwargs)
        path = ENDPOINTS['stock_reports'].path
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

    def stock_share(
        self,
        stock_code: Any | None = None,
        date: Any | None = None,
        *,
        raw: bool = False,
        fields: Sequence[str] | str | None = None,
        as_dataframe: bool = True,
        **kwargs: Any,
    ) -> Any:
        """股本.

        Endpoint: ``api/v1/market/data/share/get-stock-share``.
        Method: ``GET``.
        Source document: ``ftshare-doc/api-doc/股本.md``.
        Documented endpoint: ``get_stock_share_handler``.

        Args:
            stock_code: 股票代码 (type: string; required: Y).
            date: 日期 YYYYMMDD (type: string; required: Y).
            raw: Return the decoded JSON payload without tabular extraction.
            fields: Optional field list or comma-separated field string applied after extraction.
            as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
            **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

        Returns:
            A pandas ``DataFrame`` by default, Python rows when
            ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
            payloads when multi-page fetching is used with ``raw=True``.
        """
        request_params = {'stock_code': stock_code, 'date': date}
        request_params.update(kwargs)
        return self._call_endpoint(
            'stock_share',
            raw=raw,
            fields=fields,
            as_dataframe=as_dataframe,
            **request_params,
        )

    def stock_signal_latest_snapshot(
        self,
        signal_type: Any | None = None,
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
        """信号最新快照.

        Endpoint: ``api/v1/market/data/stock-signal-latest-snapshot``.
        Method: ``GET``.
        Source document: ``ftshare-doc/api-doc/信号最新快照.md``.
        Documented endpoint: ``stock_signal_latest_snapshot``.

        Args:
            signal_type: 信号类型过滤，不传返回全部。可选值：`new_high_month`、`new_high_60d`、`new_high_120d`、`new_high_250d`、`new_low_month`、`new_low_60d`、`new_low_120d`、`new_low_250d`、`consecutive_up`、`consecutive_down`、`consecutive_vol_up`、`consecutive_vol_down`、`break_up_ma5`、`break_up_ma10`、`break_up_ma20`、`break_down_ma5`、`break_down_ma10`、`break_down_ma20`、`vol_price_rise`、`vol_price_fall` (type: string; required: N).
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
        request_params = {'signal_type': signal_type}
        request_params.update(kwargs)
        path = ENDPOINTS['stock_signal_latest_snapshot'].path
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

    def stock_trade(
        self,
        symbol: Any | None = None,
        *,
        raw: bool = False,
        fields: Sequence[str] | str | None = None,
        as_dataframe: bool = True,
        **kwargs: Any,
    ) -> Any:
        """股票分时成交.

        Endpoint: ``api/v1/market/data/daec/history/trades``.
        Method: ``GET``.
        Source document: ``ftshare-doc/api-doc/股票分时成交.md``.
        Documented endpoint: ``stock_trade``.

        Args:
            symbol: 标的代码 (type: SymbolKey; required: Y).
            raw: Return the decoded JSON payload without tabular extraction.
            fields: Optional field list or comma-separated field string applied after extraction.
            as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
            **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

        Returns:
            A pandas ``DataFrame`` by default, Python rows when
            ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
            payloads when multi-page fetching is used with ``raw=True``.
        """
        request_params = {'symbol': symbol}
        request_params.update(kwargs)
        return self._call_endpoint(
            'stock_trade',
            raw=raw,
            fields=fields,
            as_dataframe=as_dataframe,
            **request_params,
        )

    def stock_unlock(
        self,
        stock_code: Any | None = None,
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
        """限售解禁.

        Endpoint: ``api/v1/market/data/unlock/stock-unlock``.
        Method: ``GET``.
        Source document: ``ftshare-doc/api-doc/限售解禁.md``.
        Documented endpoint: ``stock_unlock_handler``.

        Args:
            stock_code: 证券代码 (type: string; required: Y).
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
        request_params = {'stock_code': stock_code}
        request_params.update(kwargs)
        path = ENDPOINTS['stock_unlock'].path
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

    def stock_unlock_by_date(
        self,
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
        """限售解禁按日期.

        Endpoint: ``api/v1/market/data/unlock/stock-unlock-by-date``.
        Method: ``GET``.
        Source document: ``ftshare-doc/api-doc/限售解禁按日期.md``.
        Documented endpoint: ``stock_unlock_by_date_handler``.

        Args:
            start_date: 起始日期（YYYY-MM-DD） (type: string; required: Y).
            end_date: 结束日期（YYYY-MM-DD） (type: string; required: Y).
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
        request_params = {'start_date': start_date, 'end_date': end_date}
        request_params.update(kwargs)
        path = ENDPOINTS['stock_unlock_by_date'].path
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

