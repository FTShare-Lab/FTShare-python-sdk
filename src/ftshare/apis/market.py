"""FTShare market endpoint methods generated from ``ftshare-doc/api-doc``."""

from __future__ import annotations

from collections.abc import Sequence
from typing import Any

from ..endpoints import ENDPOINTS


class MarketApiMixin:
    """Endpoint methods for the market API group."""

    def auction_results(
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
        """集合竞价结果.

        Endpoint: ``api/v1/market/data/auction-results``.
        Method: ``GET``.
        Source document: ``ftshare-doc/api-doc/集合竞价结果.md``.
        Documented endpoint: ``auction_results``.

        Args:
            ts_code: 股票代码，如 000001.XSHE (type: string; required: N).
            trade_date: 交易日，格式 YYYYMMDD (type: string; required: N).
            start_date: 起始日期，格式 YYYYMMDD (type: string; required: N).
            end_date: 结束日期，格式 YYYYMMDD (type: string; required: N).
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
        path = ENDPOINTS['auction_results'].path
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

    def bse_mapping(
        self,
        o_code: Any | None = None,
        n_code: Any | None = None,
        *,
        raw: bool = False,
        fields: Sequence[str] | str | None = None,
        as_dataframe: bool = True,
        **kwargs: Any,
    ) -> Any:
        """北交所映射.

        Endpoint: ``api/v1/market/data/bse-mapping``.
        Method: ``GET``.
        Source document: ``ftshare-doc/api-doc/北交所映射.md``.
        Documented endpoint: ``get_bse_mapping``.

        Args:
            o_code: 旧代码（如 `838163.BJ`） (type: string; required: N).
            n_code: 新代码（如 `920163.BJ`） (type: string; required: N).
            raw: Return the decoded JSON payload without tabular extraction.
            fields: Optional field list or comma-separated field string applied after extraction.
            as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
            **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

        Returns:
            A pandas ``DataFrame`` by default, Python rows when
            ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
            payloads when multi-page fetching is used with ``raw=True``.
        """
        request_params = {'o_code': o_code, 'n_code': n_code}
        request_params.update(kwargs)
        return self._call_endpoint(
            'bse_mapping',
            raw=raw,
            fields=fields,
            as_dataframe=as_dataframe,
            **request_params,
        )

    def bullion_price(
        self,
        symbol: Any | None = None,
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
        """贵金属价格.

        Endpoint: ``api/v1/market/data/bullion/price``.
        Method: ``GET``.
        Source document: ``ftshare-doc/api-doc/贵金属价格.md``.
        Documented endpoint: ``get_bullion_price``.

        Args:
            symbol: 标的代码，如 XAUUSD、AU9999 (type: string; required: Y).
            start_date: 查询起始日期 YYYYMMDD (type: int; required: Y).
            end_date: 查询结束日期 YYYYMMDD；与 start_date 跨度 ≤3 天 (type: int; required: Y).
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
        request_params = {'symbol': symbol, 'start_date': start_date, 'end_date': end_date}
        request_params.update(kwargs)
        path = ENDPOINTS['bullion_price'].path
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

    def bullion_support_symbol(
        self,
        *,
        raw: bool = False,
        fields: Sequence[str] | str | None = None,
        as_dataframe: bool = True,
        **kwargs: Any,
    ) -> Any:
        """贵金属支持标的.

        Endpoint: ``api/v1/market/data/bullion/support-symbol``.
        Method: ``GET``.
        Source document: ``ftshare-doc/api-doc/贵金属支持标的.md``.
        Documented endpoint: ``get_bullion_support_symbol``.

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
            'bullion_support_symbol',
            raw=raw,
            fields=fields,
            as_dataframe=as_dataframe,
            **request_params,
        )

    def cb_base_data(
        self,
        symbol_code: Any | None = None,
        *,
        raw: bool = False,
        fields: Sequence[str] | str | None = None,
        as_dataframe: bool = True,
        **kwargs: Any,
    ) -> Any:
        """可转债基础数据.

        Endpoint: ``api/v1/market/data/cb/cb-base-data``.
        Method: ``GET``.
        Source document: ``ftshare-doc/api-doc/可转债基础数据.md``.
        Documented endpoint: ``get_cb_base_data_handler``.

        Args:
            symbol_code: 转债代码 (type: string; required: Y).
            raw: Return the decoded JSON payload without tabular extraction.
            fields: Optional field list or comma-separated field string applied after extraction.
            as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
            **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

        Returns:
            A pandas ``DataFrame`` by default, Python rows when
            ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
            payloads when multi-page fetching is used with ``raw=True``.
        """
        request_params = {'symbol_code': symbol_code}
        request_params.update(kwargs)
        return self._call_endpoint(
            'cb_base_data',
            raw=raw,
            fields=fields,
            as_dataframe=as_dataframe,
            **request_params,
        )

    def cb_lists(
        self,
        *,
        raw: bool = False,
        fields: Sequence[str] | str | None = None,
        as_dataframe: bool = True,
        **kwargs: Any,
    ) -> Any:
        """可转债列表.

        Endpoint: ``api/v1/market/data/cb/cb-lists``.
        Method: ``GET``.
        Source document: ``ftshare-doc/api-doc/可转债列表.md``.
        Documented endpoint: ``get_cb_lists_handler``.

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
            'cb_lists',
            raw=raw,
            fields=fields,
            as_dataframe=as_dataframe,
            **request_params,
        )

    def company_list(
        self,
        stock_name: Any | None = None,
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
        """公司列表.

        Endpoint: ``api/v1/market/data/company-list``.
        Method: ``GET``.
        Source document: ``ftshare-doc/api-doc/公司列表.md``.
        Documented endpoint: ``get_company_list``.

        Args:
            stock_name: 股票名称，精确匹配 (type: string; required: N).
            stock_code: 股票代码，精确匹配 (type: string; required: N).
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
        request_params = {'stock_name': stock_name, 'stock_code': stock_code}
        request_params.update(kwargs)
        path = ENDPOINTS['company_list'].path
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

    def eastmoney_board_constituents(
        self,
        board_code: Any | None = None,
        *,
        raw: bool = False,
        fields: Sequence[str] | str | None = None,
        as_dataframe: bool = True,
        **kwargs: Any,
    ) -> Any:
        """东方财富板块成份股.

        Endpoint: ``api/v1/market/data/eastmoney-board-constituents``.
        Method: ``GET``.
        Source document: ``ftshare-doc/api-doc/东方财富板块成份股.md``.
        Documented endpoint: ``eastmoney_board_constituents``.

        Args:
            board_code: 板块代码，如 BK1024 (type: string; required: Y).
            raw: Return the decoded JSON payload without tabular extraction.
            fields: Optional field list or comma-separated field string applied after extraction.
            as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
            **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

        Returns:
            A pandas ``DataFrame`` by default, Python rows when
            ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
            payloads when multi-page fetching is used with ``raw=True``.
        """
        request_params = {'board_code': board_code}
        request_params.update(kwargs)
        return self._call_endpoint(
            'eastmoney_board_constituents',
            raw=raw,
            fields=fields,
            as_dataframe=as_dataframe,
            **request_params,
        )

    def eastmoney_board_daily_kline(
        self,
        board_code: Any | None = None,
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
        """东方财富板块日线OHLC.

        Endpoint: ``api/v1/market/data/eastmoney-board-daily-ohlc``.
        Method: ``GET``.
        Source document: ``ftshare-doc/api-doc/东方财富板块日线OHLC.md``.
        Documented endpoint: ``eastmoney_board_daily_kline``.

        Args:
            board_code: 板块代码，如 BK1024 (type: string; required: Y).
            start_date: 起始日期（含），YYYY-MM-DD 或 YYYYMMDD (type: string; required: N).
            end_date: 截止日期（含），YYYY-MM-DD 或 YYYYMMDD (type: string; required: N).
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
        request_params = {'board_code': board_code, 'start_date': start_date, 'end_date': end_date}
        request_params.update(kwargs)
        path = ENDPOINTS['eastmoney_board_daily_kline'].path
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

    def eastmoney_board_latest_kline(
        self,
        board_code: Any | None = None,
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
        """东方财富板块最新OHLC.

        Endpoint: ``api/v1/market/data/eastmoney-board-latest-ohlc``.
        Method: ``GET``.
        Source document: ``ftshare-doc/api-doc/东方财富板块最新OHLC.md``.
        Documented endpoint: ``eastmoney_board_latest_kline``.

        Args:
            board_code: 板块代码，如 BK1024；不传则返回全部板块最新K线 (type: string; required: N).
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
        request_params = {'board_code': board_code}
        request_params.update(kwargs)
        path = ENDPOINTS['eastmoney_board_latest_kline'].path
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

    def eastmoney_concept_boards(
        self,
        *,
        raw: bool = False,
        fields: Sequence[str] | str | None = None,
        as_dataframe: bool = True,
        **kwargs: Any,
    ) -> Any:
        """东方财富概念板块.

        Endpoint: ``api/v1/market/data/eastmoney-concept-boards``.
        Method: ``GET``.
        Source document: ``ftshare-doc/api-doc/东方财富概念板块.md``.
        Documented endpoint: ``eastmoney_concept_boards``.

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
            'eastmoney_concept_boards',
            raw=raw,
            fields=fields,
            as_dataframe=as_dataframe,
            **request_params,
        )

    def eastmoney_dapan_flow(
        self,
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
        """东方财富大盘资金流.

        Endpoint: ``api/v1/market/data/eastmoney-dapan-flow``.
        Method: ``GET``.
        Source document: ``ftshare-doc/api-doc/东方财富大盘资金流.md``.
        Documented endpoint: ``get_eastmoney_dapan_flow``.

        Args:
            trade_date: 交易日 YYYYMMDD；与 start_date/end_date 互斥 (type: string; required: N).
            start_date: 区间起始日 YYYYMMDD；需与 end_date 同时提供 (type: string; required: N).
            end_date: 区间结束日 YYYYMMDD；需与 start_date 同时提供 (type: string; required: N).
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
        request_params = {'trade_date': trade_date, 'start_date': start_date, 'end_date': end_date}
        request_params.update(kwargs)
        path = ENDPOINTS['eastmoney_dapan_flow'].path
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

    def eastmoney_hk_index_daily_kline(
        self,
        index_code: Any | None = None,
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
        """东方财富港股指数日K.

        Endpoint: ``api/v1/market/data/eastmoney-hk-index-daily-kline``.
        Method: ``GET``.
        Source document: ``ftshare-doc/api-doc/东方财富港股指数日K.md``.
        Documented endpoint: ``get_eastmoney_hk_index_daily_kline``.

        Args:
            index_code: 指数代码，如 HSI / HSCEI / HSTECH；不传返回全部指数 (type: string; required: N).
            trade_date: 交易日 YYYY-MM-DD；与 start_date/end_date 互斥 (type: string; required: N).
            start_date: 区间起始日 YYYY-MM-DD；需与 end_date 同时提供 (type: string; required: N).
            end_date: 区间结束日 YYYY-MM-DD；需与 start_date 同时提供 (type: string; required: N).
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
        request_params = {'index_code': index_code, 'trade_date': trade_date, 'start_date': start_date, 'end_date': end_date}
        request_params.update(kwargs)
        path = ENDPOINTS['eastmoney_hk_index_daily_kline'].path
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

    def eastmoney_market_valuation(
        self,
        market_code: Any | None = None,
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
        """东方财富市场估值.

        Endpoint: ``api/v1/market/data/eastmoney-market-valuation``.
        Method: ``GET``.
        Source document: ``ftshare-doc/api-doc/东方财富市场估值.md``.
        Documented endpoint: ``get_eastmoney_market_valuation``.

        Args:
            market_code: 市场代码，如 000001=上证指数、000300=沪深300；不传返回全部 (type: string; required: N).
            trade_date: 交易日 YYYYMMDD；与 start_date/end_date 互斥 (type: string; required: N).
            start_date: 区间起始日 YYYYMMDD；需与 end_date 同时提供 (type: string; required: N).
            end_date: 区间结束日 YYYYMMDD；需与 start_date 同时提供 (type: string; required: N).
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
        request_params = {'market_code': market_code, 'trade_date': trade_date, 'start_date': start_date, 'end_date': end_date}
        request_params.update(kwargs)
        path = ENDPOINTS['eastmoney_market_valuation'].path
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

    def eastmoney_rank(
        self,
        rank_group: Any | None = None,
        market: Any | None = None,
        trade_date: Any | None = None,
        *,
        raw: bool = False,
        fields: Sequence[str] | str | None = None,
        as_dataframe: bool = True,
        **kwargs: Any,
    ) -> Any:
        """东方财富股票排名.

        Endpoint: ``api/v1/market/data/eastmoney-rank``.
        Method: ``GET``.
        Source document: ``ftshare-doc/api-doc/东方财富股票排名.md``.
        Documented endpoint: ``eastmoney_rank``.

        Args:
            rank_group: 榜单组：`hot`（人气榜）/ `up`（飙升榜） (type: string; required: N).
            market: 市场：`A`（A股）/ `HK`（港股）/ `US`（美股） (type: string; required: N).
            trade_date: 交易日期，格式 `YYYY-MM-DD`，不传默认取最新 (type: string; required: N).
            raw: Return the decoded JSON payload without tabular extraction.
            fields: Optional field list or comma-separated field string applied after extraction.
            as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
            **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

        Returns:
            A pandas ``DataFrame`` by default, Python rows when
            ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
            payloads when multi-page fetching is used with ``raw=True``.
        """
        request_params = {'rank_group': rank_group, 'market': market, 'trade_date': trade_date}
        request_params.update(kwargs)
        return self._call_endpoint(
            'eastmoney_rank',
            raw=raw,
            fields=fields,
            as_dataframe=as_dataframe,
            **request_params,
        )

    def eastmoney_sector_flow(
        self,
        sector_code: Any | None = None,
        sector_type: Any | None = None,
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
        """东方财富板块资金流.

        Endpoint: ``api/v1/market/data/eastmoney-sector-flow``.
        Method: ``GET``.
        Source document: ``ftshare-doc/api-doc/东方财富板块资金流.md``.
        Documented endpoint: ``get_eastmoney_sector_flow``.

        Args:
            sector_code: 板块代码，如 BK0488 (type: string; required: N).
            sector_type: 板块类型：industry / concept / regional (type: string; required: N).
            trade_date: 交易日 YYYYMMDD；与 start_date/end_date 互斥 (type: string; required: N).
            start_date: 区间起始日 YYYYMMDD；需与 end_date 同时提供 (type: string; required: N).
            end_date: 区间结束日 YYYYMMDD；需与 start_date 同时提供 (type: string; required: N).
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
        request_params = {'sector_code': sector_code, 'sector_type': sector_type, 'trade_date': trade_date, 'start_date': start_date, 'end_date': end_date}
        request_params.update(kwargs)
        path = ENDPOINTS['eastmoney_sector_flow'].path
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

    def eastmoney_stock_flow(
        self,
        symbol: Any | None = None,
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
        """东方财富个股资金流.

        Endpoint: ``api/v1/market/data/eastmoney-stock-flow``.
        Method: ``GET``.
        Source document: ``ftshare-doc/api-doc/东方财富个股资金流.md``.
        Documented endpoint: ``get_eastmoney_stock_flow``.

        Args:
            symbol: 股票代码，如 600522 (type: string; required: N).
            trade_date: 交易日 YYYYMMDD；与 start_date/end_date 互斥 (type: string; required: N).
            start_date: 区间起始日 YYYYMMDD；需与 end_date 同时提供 (type: string; required: N).
            end_date: 区间结束日 YYYYMMDD；需与 start_date 同时提供 (type: string; required: N).
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
        request_params = {'symbol': symbol, 'trade_date': trade_date, 'start_date': start_date, 'end_date': end_date}
        request_params.update(kwargs)
        path = ENDPOINTS['eastmoney_stock_flow'].path
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

    def eastmoney_stock_valuation(
        self,
        symbol: Any | None = None,
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
        """东方财富个股估值.

        Endpoint: ``api/v1/market/data/eastmoney-stock-valuation``.
        Method: ``GET``.
        Source document: ``ftshare-doc/api-doc/东方财富个股估值.md``.
        Documented endpoint: ``get_eastmoney_stock_valuation``.

        Args:
            symbol: 股票代码，如 000001；不传返回全部 (type: string; required: N).
            trade_date: 交易日 YYYYMMDD；与 start_date/end_date 互斥 (type: string; required: N).
            start_date: 区间起始日 YYYYMMDD；需与 end_date 同时提供 (type: string; required: N).
            end_date: 区间结束日 YYYYMMDD；需与 start_date 同时提供 (type: string; required: N).
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
        request_params = {'symbol': symbol, 'trade_date': trade_date, 'start_date': start_date, 'end_date': end_date}
        request_params.update(kwargs)
        path = ENDPOINTS['eastmoney_stock_valuation'].path
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

    def eastmoney_us_stock_daily_kline(
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
        Source document: ``ftshare-doc/api-doc/东方财富美股日OHLC.md``.
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
        path = ENDPOINTS['eastmoney_us_stock_daily_kline'].path
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
        Source document: ``ftshare-doc/api-doc/东方财富美股日OHLC.md``.
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

    def eastmoney_us_stock_latest_kline(
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
        """东方财富美股最新OHLC.

        Endpoint: ``api/v1/market/data/eastmoney-us-stock-latest-ohlc``.
        Method: ``GET``.
        Source document: ``ftshare-doc/api-doc/东方财富美股最新OHLC.md``.
        Documented endpoint: ``eastmoney_us_stock_latest_kline``.

        Args:
            stock_code: 股票代码，如 ADV；不传返回全部美股最新 K 线 (type: string; required: N).
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
        path = ENDPOINTS['eastmoney_us_stock_latest_kline'].path
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

    def eastmoney_us_stock_latest_ohlc(
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
        """东方财富美股最新OHLC.

        Endpoint: ``api/v1/market/data/eastmoney-us-stock-latest-ohlc``.
        Method: ``GET``.
        Source document: ``ftshare-doc/api-doc/东方财富美股最新OHLC.md``.
        Documented endpoint: ``eastmoney_us_stock_latest_kline``.

        Args:
            stock_code: 股票代码，如 ADV；不传返回全部美股最新 K 线 (type: string; required: N).
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
        path = ENDPOINTS['eastmoney_us_stock_latest_ohlc'].path
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
        Source document: ``ftshare-doc/api-doc/东方财富美股列表.md``.
        Documented endpoint: ``eastmoney_us_stock_list``.

        Args:
            refresh: 为 true 时强制从 CSV 重新加载列表缓存 (type: bool; required: N).
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

    def hk_sh_stock_connect_members(
        self,
        *,
        raw: bool = False,
        fields: Sequence[str] | str | None = None,
        as_dataframe: bool = True,
        **kwargs: Any,
    ) -> Any:
        """沪港通成份.

        Endpoint: ``api/v1/market/data/hk-sh-stock-connect-members``.
        Method: ``GET``.
        Source document: ``ftshare-doc/api-doc/沪港通成份.md``.
        Documented endpoint: ``hk_sh_stock_connect_members``.

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
            'hk_sh_stock_connect_members',
            raw=raw,
            fields=fields,
            as_dataframe=as_dataframe,
            **request_params,
        )

    def hk_sz_stock_connect_members(
        self,
        *,
        raw: bool = False,
        fields: Sequence[str] | str | None = None,
        as_dataframe: bool = True,
        **kwargs: Any,
    ) -> Any:
        """深港通成份.

        Endpoint: ``api/v1/market/data/hk-sz-stock-connect-members``.
        Method: ``GET``.
        Source document: ``ftshare-doc/api-doc/深港通成份.md``.
        Documented endpoint: ``hk_sz_stock_connect_members``.

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
            'hk_sz_stock_connect_members',
            raw=raw,
            fields=fields,
            as_dataframe=as_dataframe,
            **request_params,
        )

    def index_description_all(
        self,
        *,
        raw: bool = False,
        fields: Sequence[str] | str | None = None,
        as_dataframe: bool = True,
        **kwargs: Any,
    ) -> Any:
        """指数基础信息.

        Endpoint: ``api/v1/market/data/index-description-all``.
        Method: ``GET``.
        Source document: ``ftshare-doc/api-doc/指数基础信息.md``.
        Documented endpoint: ``index_description_all``.

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
            'index_description_all',
            raw=raw,
            fields=fields,
            as_dataframe=as_dataframe,
            **request_params,
        )

    def northbound(
        self,
        date: Any | None = None,
        *,
        raw: bool = False,
        fields: Sequence[str] | str | None = None,
        as_dataframe: bool = True,
        **kwargs: Any,
    ) -> Any:
        """北向资金交易.

        Endpoint: ``api/v1/market/data/northbound``.
        Method: ``GET``.
        Source document: ``ftshare-doc/api-doc/北向资金交易.md``.
        Documented endpoint: ``northbound``.

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
            'northbound',
            raw=raw,
            fields=fields,
            as_dataframe=as_dataframe,
            **request_params,
        )

    def nth_trade_date(
        self,
        n: Any | None = None,
        *,
        raw: bool = False,
        fields: Sequence[str] | str | None = None,
        as_dataframe: bool = True,
        **kwargs: Any,
    ) -> Any:
        """第N个交易日.

        Endpoint: ``api/v1/market/data/time/get-nth-trade-date``.
        Method: ``GET``.
        Source document: ``ftshare-doc/api-doc/第N个交易日.md``.
        Documented endpoint: ``get_nth_trade_date``.

        Args:
            n: 需要获取的前 N 个交易日，N >= 1 (type: uint32; required: Y).
            raw: Return the decoded JSON payload without tabular extraction.
            fields: Optional field list or comma-separated field string applied after extraction.
            as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
            **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

        Returns:
            A pandas ``DataFrame`` by default, Python rows when
            ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
            payloads when multi-page fetching is used with ``raw=True``.
        """
        request_params = {'n': n}
        request_params.update(kwargs)
        return self._call_endpoint(
            'nth_trade_date',
            raw=raw,
            fields=fields,
            as_dataframe=as_dataframe,
            **request_params,
        )

    def price_change(
        self,
        stock_code: Any | None = None,
        base_date: Any | None = None,
        n: Any | None = None,
        direction: Any | None = None,
        *,
        raw: bool = False,
        fields: Sequence[str] | str | None = None,
        as_dataframe: bool = True,
        **kwargs: Any,
    ) -> Any:
        """价格变动.

        Endpoint: ``api/v1/market/data/price/get-price-change``.
        Method: ``GET``.
        Source document: ``ftshare-doc/api-doc/价格变动.md``.
        Documented endpoint: ``get_price_change``.

        Args:
            stock_code: 目标股票 6 位纯数字代码，兼容沪市/深市/创业板/科创板 (type: string; required: Y).
            base_date: 涨跌幅计算基准日，格式 YYYYMMDD (type: string; required: Y).
            n: 需计算的有效交易日数量，建议不超过 365 (type: uint32; required: Y).
            direction: 计算方向：forward（基准日为结束日）/ backward（基准日为开始日） (type: string; required: Y).
            raw: Return the decoded JSON payload without tabular extraction.
            fields: Optional field list or comma-separated field string applied after extraction.
            as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
            **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

        Returns:
            A pandas ``DataFrame`` by default, Python rows when
            ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
            payloads when multi-page fetching is used with ``raw=True``.
        """
        request_params = {'stock_code': stock_code, 'base_date': base_date, 'n': n, 'direction': direction}
        request_params.update(kwargs)
        return self._call_endpoint(
            'price_change',
            raw=raw,
            fields=fields,
            as_dataframe=as_dataframe,
            **request_params,
        )

    def search(
        self,
        query: Any | None = None,
        limit: Any | None = None,
        *,
        raw: bool = False,
        fields: Sequence[str] | str | None = None,
        as_dataframe: bool = True,
        **kwargs: Any,
    ) -> Any:
        """标的搜索.

        Endpoint: ``api/v1/market/security/search``.
        Method: ``GET``.
        Source document: ``ftshare-doc/api-doc/标的搜索.md``.
        Documented endpoint: ``search``.

        Args:
            query: 搜索关键词；支持名称、标的代码、拼音全拼/首字母；大小写不敏感，自动 trim (type: string; required: Y).
            limit: 返回最大条数，默认 1 (type: int; required: N).
            raw: Return the decoded JSON payload without tabular extraction.
            fields: Optional field list or comma-separated field string applied after extraction.
            as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
            **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

        Returns:
            A pandas ``DataFrame`` by default, Python rows when
            ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
            payloads when multi-page fetching is used with ``raw=True``.
        """
        request_params = {'q': query, 'limit': limit}
        request_params.update(kwargs)
        return self._call_endpoint(
            'search',
            raw=raw,
            fields=fields,
            as_dataframe=as_dataframe,
            **request_params,
        )

    def semantic_search_news(
        self,
        query: Any | None = None,
        limit: Any | None = None,
        year: Any | None = None,
        start_time: Any | None = None,
        end_time: Any | None = None,
        *,
        raw: bool = False,
        fields: Sequence[str] | str | None = None,
        as_dataframe: bool = True,
        **kwargs: Any,
    ) -> Any:
        """新闻语义搜索.

        Endpoint: ``api/v1/market/data/semantic-search-news``.
        Method: ``GET``.
        Source document: ``ftshare-doc/api-doc/新闻语义搜索.md``.
        Documented endpoint: ``semantic_search_news_handler``.

        Args:
            query: 搜索文字 (type: string; required: Y).
            limit: 返回条数，默认由服务端决定 (type: int; required: N).
            year: 年份，限定搜索范围 (type: int; required: N).
            start_time: 起始时间（带时区），与 end_time 同传时区间不超过 3 天 (type: datetime; required: N).
            end_time: 结束时间（带时区），与 start_time 同传时区间不超过 3 天 (type: datetime; required: N).
            raw: Return the decoded JSON payload without tabular extraction.
            fields: Optional field list or comma-separated field string applied after extraction.
            as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
            **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

        Returns:
            A pandas ``DataFrame`` by default, Python rows when
            ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
            payloads when multi-page fetching is used with ``raw=True``.
        """
        request_params = {'query': query, 'limit': limit, 'year': year, 'start_time': start_time, 'end_time': end_time}
        request_params.update(kwargs)
        return self._call_endpoint(
            'semantic_search_news',
            raw=raw,
            fields=fields,
            as_dataframe=as_dataframe,
            **request_params,
        )

    def sh_hk_stock_connect_members(
        self,
        *,
        raw: bool = False,
        fields: Sequence[str] | str | None = None,
        as_dataframe: bool = True,
        **kwargs: Any,
    ) -> Any:
        """沪股通成份.

        Endpoint: ``api/v1/market/data/sh-hk-stock-connect-members``.
        Method: ``GET``.
        Source document: ``ftshare-doc/api-doc/沪股通成份.md``.
        Documented endpoint: ``sh_hk_stock_connect_members``.

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
            'sh_hk_stock_connect_members',
            raw=raw,
            fields=fields,
            as_dataframe=as_dataframe,
            **request_params,
        )

    def southbound(
        self,
        date: Any | None = None,
        *,
        raw: bool = False,
        fields: Sequence[str] | str | None = None,
        as_dataframe: bool = True,
        **kwargs: Any,
    ) -> Any:
        """南向资金交易.

        Endpoint: ``api/v1/market/data/southbound``.
        Method: ``GET``.
        Source document: ``ftshare-doc/api-doc/南向资金交易.md``.
        Documented endpoint: ``southbound``.

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
            'southbound',
            raw=raw,
            fields=fields,
            as_dataframe=as_dataframe,
            **request_params,
        )

    def suspension_list(
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
        """停牌列表.

        Endpoint: ``api/v1/market/data/suspension-list``.
        Method: ``GET``.
        Source document: ``ftshare-doc/api-doc/停牌列表.md``.
        Documented endpoint: ``suspension_list``.

        Args:
            trade_date: 交易日，格式 YYYYMMDD，默认当天 (type: string; required: N).
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
        path = ENDPOINTS['suspension_list'].path
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

    def sw_industry_constituent_history(
        self,
        industry_code: Any | None = None,
        *,
        raw: bool = False,
        fields: Sequence[str] | str | None = None,
        as_dataframe: bool = True,
        **kwargs: Any,
    ) -> Any:
        """申万行业成份股历史.

        Endpoint: ``api/v1/market/data/sw-industry/constituent-history``.
        Method: ``GET``.
        Source document: ``ftshare-doc/api-doc/申万行业成份股历史.md``.
        Documented endpoint: ``sw_industry_constituent_history``.

        Args:
            industry_code: 行业代码，带 .SI 后缀，如 801010.SI (type: string; required: Y).
            raw: Return the decoded JSON payload without tabular extraction.
            fields: Optional field list or comma-separated field string applied after extraction.
            as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
            **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

        Returns:
            A pandas ``DataFrame`` by default, Python rows when
            ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
            payloads when multi-page fetching is used with ``raw=True``.
        """
        request_params = {'industry_code': industry_code}
        request_params.update(kwargs)
        return self._call_endpoint(
            'sw_industry_constituent_history',
            raw=raw,
            fields=fields,
            as_dataframe=as_dataframe,
            **request_params,
        )

    def sw_industry_daily_metrics(
        self,
        level: Any | None = None,
        start_date: Any | None = None,
        end_date: Any | None = None,
        industry_code: Any | None = None,
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
        """申万行业日度指标.

        Endpoint: ``api/v1/market/data/sw-industry/daily-metrics``.
        Method: ``GET``.
        Source document: ``ftshare-doc/api-doc/申万行业日度指标.md``.
        Documented endpoint: ``sw_industry_daily_metrics``.

        Args:
            level: 行业层级：1/2/3 (type: int; required: Y).
            start_date: 起始日期，YYYYMMDD (type: string; required: Y).
            end_date: 截止日期，YYYYMMDD (type: string; required: Y).
            industry_code: 行业代码，带 .SI 后缀，如 801010.SI (type: string; required: Y).
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
        request_params = {'level': level, 'start_date': start_date, 'end_date': end_date, 'industry_code': industry_code}
        request_params.update(kwargs)
        path = ENDPOINTS['sw_industry_daily_metrics'].path
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

    def sw_industry_overview(
        self,
        date: Any | None = None,
        level: Any | None = None,
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
        """申万行业总览.

        Endpoint: ``api/v1/market/data/sw-industry/overview``.
        Method: ``GET``.
        Source document: ``ftshare-doc/api-doc/申万行业总览.md``.
        Documented endpoint: ``sw_industry_overview``.

        Args:
            date: 交易日，格式 YYYYMMDD (type: string; required: Y).
            level: 行业层级：1/2/3，不传返回全部 (type: int; required: N).
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
        request_params = {'date': date, 'level': level}
        request_params.update(kwargs)
        path = ENDPOINTS['sw_industry_overview'].path
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

    def sz_hk_stock_connect_members(
        self,
        *,
        raw: bool = False,
        fields: Sequence[str] | str | None = None,
        as_dataframe: bool = True,
        **kwargs: Any,
    ) -> Any:
        """深股通成份.

        Endpoint: ``api/v1/market/data/sz-hk-stock-connect-members``.
        Method: ``GET``.
        Source document: ``ftshare-doc/api-doc/深股通成份.md``.
        Documented endpoint: ``sz_hk_stock_connect_members``.

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
            'sz_hk_stock_connect_members',
            raw=raw,
            fields=fields,
            as_dataframe=as_dataframe,
            **request_params,
        )

    def ths_all_board_kline(
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
        """同花顺全板块K线.

        Endpoint: ``api/v1/market/data/ths-all-board-kline``.
        Method: ``GET``.
        Source document: ``ftshare-doc/api-doc/同花顺全板块K线.md``.
        Documented endpoint: ``ths_all_board_kline``.

        Args:
            start_date: 起始日期（含），YYYY-MM-DD 或 YYYYMMDD (type: string; required: N).
            end_date: 截止日期（含），YYYY-MM-DD 或 YYYYMMDD (type: string; required: N).
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
        path = ENDPOINTS['ths_all_board_kline'].path
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

    def ths_board_kline(
        self,
        board_code: Any | None = None,
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
        """同花顺板块K线.

        Endpoint: ``api/v1/market/data/ths-board-kline``.
        Method: ``GET``.
        Source document: ``ftshare-doc/api-doc/同花顺板块K线.md``.
        Documented endpoint: ``ths_board_kline``.

        Args:
            board_code: 板块代码，如 886056 (type: string; required: Y).
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
        request_params = {'board_code': board_code}
        request_params.update(kwargs)
        path = ENDPOINTS['ths_board_kline'].path
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

    def ths_board_list(
        self,
        *,
        raw: bool = False,
        fields: Sequence[str] | str | None = None,
        as_dataframe: bool = True,
        **kwargs: Any,
    ) -> Any:
        """同花顺板块列表.

        Endpoint: ``api/v1/market/data/ths-board-list``.
        Method: ``GET``.
        Source document: ``ftshare-doc/api-doc/同花顺板块列表.md``.
        Documented endpoint: ``ths_board_list``.

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
            'ths_board_list',
            raw=raw,
            fields=fields,
            as_dataframe=as_dataframe,
            **request_params,
        )

    def type_reports(
        self,
        rept_type: Any | None = None,
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
        """研报分类.

        Endpoint: ``api/v1/market/data/report/type-reports``.
        Method: ``GET``.
        Source document: ``ftshare-doc/api-doc/研报分类.md``.
        Documented endpoint: ``type_reports``.

        Args:
            rept_type: 研报类型：MacroReport / IndustryReport / BrokerMorningReport / StrategyReport / NewStockReport (type: string; required: Y).
            start_date: 开始日期 YYYYMMDD (type: string; required: Y).
            end_date: 结束日期 YYYYMMDD，不填默认与 `start_date` 相同 (type: string; required: N).
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
        request_params = {'rept_type': rept_type, 'start_date': start_date, 'end_date': end_date}
        request_params.update(kwargs)
        path = ENDPOINTS['type_reports'].path
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

    def us_balance(
        self,
        stock_code: Any | None = None,
        period: Any | None = None,
        report_type: Any | None = None,
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
        """美股资产负债表.

        Endpoint: ``api/v1/market/data/us/us-balance``.
        Method: ``GET``.
        Source document: ``ftshare-doc/api-doc/美股资产负债表.md``.
        Documented endpoint: ``us_balance``.

        Args:
            stock_code: 美股代码，纯代码不带后缀，如 NVDA (type: string; required: Y).
            period: 财年（如 2024），匹配 stmt_year，非自然年 (type: int; required: N).
            report_type: 报告期类型：Q1 / Q2 / Q3 / Q4 / H1 (type: string; required: N).
            start_date: 报告期下界 YYYYMMDD（含），过滤 end_date (type: int; required: N).
            end_date: 报告期上界 YYYYMMDD（含），过滤 end_date (type: int; required: N).
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
        request_params = {'stock_code': stock_code, 'period': period, 'report_type': report_type, 'start_date': start_date, 'end_date': end_date}
        request_params.update(kwargs)
        path = ENDPOINTS['us_balance'].path
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

    def us_basic(
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
        """美股基础信息.

        Endpoint: ``api/v1/market/data/us/us-basic``.
        Method: ``GET``.
        Source document: ``ftshare-doc/api-doc/美股基础信息.md``.
        Documented endpoint: ``us_basic``.

        Args:
            stock_code: 美股代码（可选），纯代码如 NVDA；不传则分页返回全部 (type: string; required: N).
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
        path = ENDPOINTS['us_basic'].path
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

    def us_cashflow(
        self,
        stock_code: Any | None = None,
        period: Any | None = None,
        report_type: Any | None = None,
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
        """美股现金流.

        Endpoint: ``api/v1/market/data/us/us-cashflow``.
        Method: ``GET``.
        Source document: ``ftshare-doc/api-doc/美股现金流.md``.
        Documented endpoint: ``us_cashflow``.

        Args:
            stock_code: 美股代码，纯代码不带后缀，如 NVDA (type: string; required: Y).
            period: 财年（如 2024），匹配 stmt_year，非自然年 (type: int; required: N).
            report_type: 报告期类型：Q1 / Q2 / Q3 / Q4 / H1 (type: string; required: N).
            start_date: 报告期下界 YYYYMMDD（含），过滤 end_date (type: int; required: N).
            end_date: 报告期上界 YYYYMMDD（含），过滤 end_date (type: int; required: N).
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
        request_params = {'stock_code': stock_code, 'period': period, 'report_type': report_type, 'start_date': start_date, 'end_date': end_date}
        request_params.update(kwargs)
        path = ENDPOINTS['us_cashflow'].path
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

    def us_income(
        self,
        stock_code: Any | None = None,
        period: Any | None = None,
        report_type: Any | None = None,
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
        """美股利润表.

        Endpoint: ``api/v1/market/data/us/us-income``.
        Method: ``GET``.
        Source document: ``ftshare-doc/api-doc/美股利润表.md``.
        Documented endpoint: ``us_income``.

        Args:
            stock_code: 美股代码，纯代码不带后缀，如 NVDA (type: string; required: Y).
            period: 财年（如 2024），匹配 stmt_year，非自然年 (type: int; required: N).
            report_type: 报告期类型：Q1 / Q2 / Q3 / Q4 / H1 (type: string; required: N).
            start_date: 报告期下界 YYYYMMDD（含），过滤 end_date (type: int; required: N).
            end_date: 报告期上界 YYYYMMDD（含），过滤 end_date (type: int; required: N).
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
        request_params = {'stock_code': stock_code, 'period': period, 'report_type': report_type, 'start_date': start_date, 'end_date': end_date}
        request_params.update(kwargs)
        path = ENDPOINTS['us_income'].path
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

    def xueqiu_rank(
        self,
        rank_group: Any | None = None,
        period: Any | None = None,
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
        """雪球股票排名.

        Endpoint: ``api/v1/market/data/xueqiu-rank``.
        Method: ``GET``.
        Source document: ``ftshare-doc/api-doc/雪球股票排名.md``.
        Documented endpoint: ``xueqiu_rank``.

        Args:
            rank_group: 榜单组：`follow`（关注）/ `tweet`（讨论）/ `deal`（交易） (type: string; required: N).
            period: 周期：`7d`（本周新增）/ `total`（最热门） (type: string; required: N).
            trade_date: 交易日期，格式 `YYYY-MM-DD`，不传默认取最新 (type: string; required: N).
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
        request_params = {'rank_group': rank_group, 'period': period, 'trade_date': trade_date}
        request_params.update(kwargs)
        path = ENDPOINTS['xueqiu_rank'].path
        return self.get_paginated(
            path,
            page=page,
            page_size=page_size,
            limit=limit,
            all_pages=all_pages,
            max_pages=max_pages,
            max_page_size=100,
            raw=raw,
            fields=fields,
            as_dataframe=as_dataframe,
            **request_params,
        )

    def yzxdr_detail(
        self,
        year: Any | None = None,
        quarter: Any | None = None,
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
        """除权除息明细.

        Endpoint: ``api/v1/market/data/yzxdr-detail``.
        Method: ``GET``.
        Source document: ``ftshare-doc/api-doc/除权除息明细.md``.
        Documented endpoint: ``get_yzxdr_detail``.

        Args:
            year: 年份（如 2026） (type: uint32; required: Y).
            quarter: 季度，1-4 (type: uint32; required: Y).
            stock_code: 股票代码，6 位数字 (type: string; required: N).
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
        request_params = {'year': year, 'quarter': quarter, 'stock_code': stock_code}
        request_params.update(kwargs)
        path = ENDPOINTS['yzxdr_detail'].path
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

