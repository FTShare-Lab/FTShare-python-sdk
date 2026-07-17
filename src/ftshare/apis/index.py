"""Index API methods grouped by ftshare-doc."""

from __future__ import annotations

from collections.abc import Sequence
from typing import Any

from ..endpoints import ENDPOINTS


class IndexApiMixin:
    """Endpoint methods for the index ftshare-doc topic."""

    def global_index_daily_kline(
        self,
        secid: Any | None = None,
        start_date: Any | None = None,
        end_date: Any | None = None,
        *,
        raw: bool = False,
        fields: Sequence[str] | str | None = None,
        as_dataframe: bool = True,
        **kwargs: Any,
    ) -> Any:
        """全球指数日K线.

        Endpoint: ``api/v1/market/data/global-index/daily-kline``.
        Method: ``GET``.
        Documented endpoint: ``global_index_daily_kline``.

        Args:
            secid: 东方财富全球指数编码，如 100.NDX、100.DJIA、100.SPX、100.HSI、100.N225 (type: string; required: Y).
            start_date: 开始日期 YYYY-MM-DD（含） (type: string; required: N).
            end_date: 结束日期 YYYY-MM-DD（含） (type: string; required: N).
            raw: Return the decoded JSON payload without tabular extraction.
            fields: Optional field list or comma-separated field string applied after extraction.
            as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
            **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

        Returns:
            A pandas ``DataFrame`` by default, Python rows when
            ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
            payloads when multi-page fetching is used with ``raw=True``.
        """
        request_params = {'secid': secid, 'start_date': start_date, 'end_date': end_date}
        request_params.update(kwargs)
        return self._call_endpoint(
            'global_index_daily_kline',
            raw=raw,
            fields=fields,
            as_dataframe=as_dataframe,
            **request_params,
        )

    def index_candlesticks(
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
        """指数K线.

        Endpoint: ``api/v1/market/data/index-candlesticks``.
        Method: ``POST``.
        Documented endpoint: ``index_candlesticks``.

        Args:
            symbol: 指数代码，如 000300.XSHG、399001.XSHE；也接受 .SH、.SZ 短后缀 (type: string; required: Y).
            interval_unit: 周期单位：Minute/Day/Week/Month/Year (type: enum; required: Y).
            interval_value: 间隔数值，默认 1；例如 Minute+5 表示 5 分钟 K 线 (type: int; required: N).
            adjust_kind: 复权：None（默认，不复权）/Forward（前复权）/Backward（后复权） (type: enum; required: N).
            since_ts_millis: 开始时间戳，单位毫秒；分钟 K 线与 until 的跨度 ≤3 天 (type: int(ms); required: N).
            until_ts_millis: 结束时间戳，单位毫秒 (type: int(ms); required: Y).
            limit: 返回条数上限；未传 since 和 limit 时默认最多返回 50 根 K 线 (type: int; required: N).
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
            'index_candlesticks',
            raw=raw,
            fields=fields,
            as_dataframe=as_dataframe,
            **request_params,
        )

    def index_candlesticks_batch(
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
        """批量指数K线.

        Endpoint: ``api/v1/market/data/index-candlesticks/batch``.
        Method: ``POST``.
        Documented endpoint: ``index_candlesticks_batch``.

        Args:
            symbols: 指数代码列表，如 ["000300.XSHG","399001.XSHE"]；也接受 .SH、.SZ 短后缀 (type: string[]; required: Y).
            interval_unit: 周期单位：Minute/Day/Week/Month/Year (type: enum; required: Y).
            interval_value: 间隔数值，默认 1；例如 Minute+5 表示 5 分钟 K 线 (type: int; required: N).
            adjust_kind: 复权：None（默认，不复权）/Forward（前复权）/Backward（后复权） (type: enum; required: N).
            since_ts_millis: 开始时间戳，单位毫秒；分钟 K 线与 until 的跨度 ≤3 天 (type: int(ms); required: N).
            until_ts_millis: 结束时间戳，单位毫秒 (type: int(ms); required: Y).
            limit: 每个标的的返回条数上限；未传 since 和 limit 时默认最多返回 50 根 K 线 (type: int; required: N).
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
            'index_candlesticks_batch',
            raw=raw,
            fields=fields,
            as_dataframe=as_dataframe,
            **request_params,
        )

    def index_description_list(
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
        """中证指数描述列表.

        Endpoint: ``api/v1/market/data/index/index_description``.
        Method: ``GET``.
        Documented endpoint: ``index_description_list_handler``.

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
        path = ENDPOINTS['index_description_list'].path
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

    def index_weight_list(
        self,
        index_code: Any | None = None,
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
        """指数权重列表.

        Endpoint: ``api/v1/market/data/index/index_weight``.
        Method: ``GET``.
        Documented endpoint: ``index_weight_list_handler``.

        Args:
            index_code: 指数代码，如 000300（沪深300），为空会被拒 (type: string; required: Y).
            date: 权重采集日期 YYYYMMDD（如 20260529），不传取最新期 (type: string; required: N).
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
        request_params = {'index_code': index_code, 'date': date}
        request_params.update(kwargs)
        path = ENDPOINTS['index_weight_list'].path
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

    def index_weight_summary(
        self,
        index_code: Any | None = None,
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
        """指数权重汇总.

        Endpoint: ``api/v1/market/data/index/index_weight_summary``.
        Method: ``GET``.
        Documented endpoint: ``index_weight_summary_handler``.

        Args:
            index_code: 指数代码，如 `000300` (type: string; required: Y).
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
        request_params = {'index_code': index_code}
        request_params.update(kwargs)
        path = ENDPOINTS['index_weight_summary'].path
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
