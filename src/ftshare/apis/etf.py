"""ETF API methods grouped by ftshare-doc."""

from __future__ import annotations

from collections.abc import Sequence
from typing import Any

from ..endpoints import ENDPOINTS
from ..params import symbols_to_json_string


class EtfApiMixin:
    """Endpoint methods for the etf ftshare-doc topic."""

    def etf_adjust_factor(
        self,
        symbol: Any | None = None,
        trade_date: Any | None = None,
        start_date: Any | None = None,
        end_date: Any | None = None,
        page: int | None = None,
        page_size: int | None = None,
        *,
        raw: bool = False,
        fields: Sequence[str] | str | None = None,
        as_dataframe: bool = True,
        **kwargs: Any,
    ) -> Any:
        """ETF复权因子.

        Endpoint: ``api/v1/market/data/etf-adjust-factor``.
        Method: ``GET``.
        Documented endpoint: ``etf_adjust_factor``.

        Args:
            symbol: ETF 代码，支持纯数字或带后缀格式；区间扫描必填 (type: string; required: N).
            trade_date: 交易日期 YYYYMMDD；空则默认当天，非交易日回退前一交易日 (type: string; required: N).
            start_date: 区间起始日期 YYYYMMDD；区间扫描必填且需配 symbol (type: string; required: N).
            end_date: 区间结束日期 YYYYMMDD；区间扫描必填且需配 symbol (type: string; required: N).
            page: 页码，从 1 开始。
            page_size: 每页条数，最大 2000。
            raw: Return the decoded JSON payload without tabular extraction.
            fields: Optional field list or comma-separated field string applied after extraction.
            as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
            **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

        Returns:
            A pandas ``DataFrame`` by default, Python rows when
            ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
            payloads when multi-page fetching is used with ``raw=True``.
        """
        request_params = {'symbol': symbol, 'trade_date': trade_date, 'start_date': start_date, 'end_date': end_date, 'page': page, 'page_size': page_size}
        request_params.update(kwargs)
        return self._call_endpoint(
            'etf_adjust_factor',
            raw=raw,
            fields=fields,
            as_dataframe=as_dataframe,
            **request_params,
        )

    def etf_candlesticks(
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
        """ETFK线.

        Endpoint: ``api/v1/market/data/etf-candlesticks``.
        Method: ``GET``.
        Documented endpoint: ``etf_candlesticks``.

        Args:
            symbol: ETF 代码，如 510300.XSHG、159915.XSHE；也接受 .SH、.SZ 短后缀 (type: string; required: Y).
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
            'etf_candlesticks',
            raw=raw,
            fields=fields,
            as_dataframe=as_dataframe,
            **request_params,
        )

    def etf_components_all(
        self,
        symbol: Any | None = None,
        *,
        raw: bool = False,
        fields: Sequence[str] | str | None = None,
        as_dataframe: bool = True,
        **kwargs: Any,
    ) -> Any:
        """ETF成份列表.

        Endpoint: ``api/v2/market/data/etf-components-all``.
        Method: ``GET``.
        Documented endpoint: ``etf_components_all``.

        Args:
            symbol: ETF 标的代码；不传返回全部 ETF (type: string; required: N).
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
            'etf_components_all',
            raw=raw,
            fields=fields,
            as_dataframe=as_dataframe,
            **request_params,
        )

    def etf_description_all(
        self,
        *,
        raw: bool = False,
        fields: Sequence[str] | str | None = None,
        as_dataframe: bool = True,
        **kwargs: Any,
    ) -> Any:
        """ETF基础信息.

        Endpoint: ``api/v1/market/data/etf-description-all``.
        Method: ``GET``.
        Documented endpoint: ``etf_description_all``.

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
            'etf_description_all',
            raw=raw,
            fields=fields,
            as_dataframe=as_dataframe,
            **request_params,
        )

    def etf_pcf_list(
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
        """ETF-PCF清单列表.

        Endpoint: ``api/v1/market/data/etf-pcf/etf-pcfs``.
        Method: ``GET``.
        Documented endpoint: ``etf_pcf_list_handler``.

        Args:
            date: 日期 YYYYMMDD，必填 (type: int; required: Y).
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
        path = ENDPOINTS['etf_pcf_list'].path
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

    def etf_pre(
        self,
        date: Any | None = None,
        *,
        raw: bool = False,
        fields: Sequence[str] | str | None = None,
        as_dataframe: bool = True,
        **kwargs: Any,
    ) -> Any:
        """ETF盘前数据.

        Endpoint: ``api/v1/market/data/etf-pre-data``.
        Method: ``GET``.
        Documented endpoint: ``get_etf_pre``.

        Args:
            date: 交易日 YYYYMMDD；不传则使用当日（CST） (type: int; required: N).
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
            'etf_pre',
            raw=raw,
            fields=fields,
            as_dataframe=as_dataframe,
            **request_params,
        )

    def etf_pre_single(
        self,
        symbol: Any | None = None,
        date: Any | None = None,
        *,
        raw: bool = False,
        fields: Sequence[str] | str | None = None,
        as_dataframe: bool = True,
        **kwargs: Any,
    ) -> Any:
        """单只ETF盘前数据.

        Endpoint: ``api/v1/market/data/etf-pre-single``.
        Method: ``GET``.
        Documented endpoint: ``get_etf_pre_single_handler``.

        Args:
            symbol: ETF 标的代码，带交易所后缀，如 510300.XSHG、159915.XSHE (type: string; required: Y).
            date: 交易日 YYYYMMDD；不传则使用当日（CST） (type: int; required: N).
            raw: Return the decoded JSON payload without tabular extraction.
            fields: Optional field list or comma-separated field string applied after extraction.
            as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
            **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

        Returns:
            A pandas ``DataFrame`` by default, Python rows when
            ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
            payloads when multi-page fetching is used with ``raw=True``.
        """
        request_params = {'symbol': symbol, 'date': date}
        request_params.update(kwargs)
        return self._call_endpoint(
            'etf_pre_single',
            raw=raw,
            fields=fields,
            as_dataframe=as_dataframe,
            **request_params,
        )
    def etf_minutes(self, symbol: Any | None = None, interval_value: Any | None = None, adjust_kind: Any | None = None, since_ts_millis: Any | None = None, until_ts_millis: Any | None = None, limit: Any | None = None, *, raw: bool = False, fields: Sequence[str] | str | None = None, as_dataframe: bool = True, **kwargs: Any) -> Any:
        """ETF历史分钟行情."""
        params = {'symbol': symbol, 'interval_value': interval_value, 'adjust_kind': adjust_kind, 'since_ts_millis': since_ts_millis, 'until_ts_millis': until_ts_millis, 'limit': limit}
        params.update(kwargs)
        return self._call_endpoint('etf_minutes', raw=raw, fields=fields, as_dataframe=as_dataframe, **params)


    def etf_realtime_minute_kline(self, symbols: Any | None = None, *, raw: bool = False, fields: Sequence[str] | str | None = None, as_dataframe: bool = True, **kwargs: Any) -> Any:
        """ETF实时分钟K线."""
        params = {'symbols': symbols_to_json_string(symbols)}
        params.update(kwargs)
        return self._call_endpoint('etf_realtime_minute_kline', raw=raw, fields=fields, as_dataframe=as_dataframe, **params)


    def etf_realtime_day_kline(self, symbols: Any | None = None, *, raw: bool = False, fields: Sequence[str] | str | None = None, as_dataframe: bool = True, **kwargs: Any) -> Any:
        """ETF实时日K线."""
        params = {'symbols': symbols_to_json_string(symbols)}
        params.update(kwargs)
        return self._call_endpoint('etf_realtime_day_kline', raw=raw, fields=fields, as_dataframe=as_dataframe, **params)

    def etf_minutes_batch(self, symbols: Any | None = None, interval_value: Any | None = None, adjust_kind: Any | None = None, since_ts_millis: Any | None = None, until_ts_millis: Any | None = None, limit: Any | None = None, *, raw: bool = False, fields: Sequence[str] | str | None = None, as_dataframe: bool = True, **kwargs: Any) -> Any:
        """批量ETF历史分钟行情."""
        params = {'symbols': symbols, 'interval_value': interval_value, 'adjust_kind': adjust_kind, 'since_ts_millis': since_ts_millis, 'until_ts_millis': until_ts_millis, 'limit': limit}
        params.update(kwargs)
        return self._call_endpoint('etf_minutes_batch', raw=raw, fields=fields, as_dataframe=as_dataframe, **params)

    def etf_announcements(
        self,
        etf_code: Any | None = None,
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
        """ETF公告列表.

        Endpoint: ``api/v2/market/data/announcements/etf-announcements``.
        Method: ``GET``.
        Documented endpoint: ``etf_announcements``.

        Args:
            etf_code: ETF 代码（按标的查询时必填），支持裸代码/短后缀/长后缀 (type: string; required: N).
            start_date: 日期 YYYYMMDD（按日期查询时必填，单日）；与 etf_code 二选一 (type: string; required: N).
            end_date: 日期 YYYYMMDD，不填默认等于 start_date（必须等于 start_date） (type: string; required: N).
            page: 页码。
            page_size: 每页条数。
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
        request_params = {'etf_code': etf_code, 'start_date': start_date, 'end_date': end_date}
        request_params.update(kwargs)
        path = ENDPOINTS['etf_announcements'].path
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

    def etf_candlesticks_batch(self, symbols: Any | None = None, interval_unit: Any | None = None, adjust_kind: Any | None = None, since_ts_millis: Any | None = None, until_ts_millis: Any | None = None, limit: Any | None = None, *, raw: bool = False, fields: Sequence[str] | str | None = None, as_dataframe: bool = True, **kwargs: Any) -> Any:
        """批量ETFK线."""
        params = {'symbols': symbols, 'interval_unit': interval_unit, 'adjust_kind': adjust_kind, 'since_ts_millis': since_ts_millis, 'until_ts_millis': until_ts_millis, 'limit': limit}
        params.update(kwargs)
        return self._call_endpoint('etf_candlesticks_batch', raw=raw, fields=fields, as_dataframe=as_dataframe, **params)

    def etf_component_details(self, symbol: Any | None = None, trade_date: Any | None = None, *, raw: bool = False, fields: Sequence[str] | str | None = None, as_dataframe: bool = True, **kwargs: Any) -> Any:
        """ETF成分证券明细."""
        params = {'symbol': symbol, 'trade_date': trade_date}
        params.update(kwargs)
        return self._call_endpoint('etf_component_details', raw=raw, fields=fields, as_dataframe=as_dataframe, **params)

    def etf_net_value(
        self,
        etf_code: Any | None = None,
        nav_date: Any | None = None,
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
        """ETF净值.

        Endpoint: ``api/v2/market/data/etf-net-value``.
        Method: ``GET``.
        Documented endpoint: ``etf_net_value``.

        Args:
            etf_code: ETF 代码，如 510300；兼容参数名 fund_code (type: string; required: Y).
            nav_date: 净值日期 YYYYMMDD；与日期区间参数互斥 (type: integer; required: N).
            start_date: 净值开始日期 YYYYMMDD；须与 end_date 同时提供 (type: integer; required: N).
            end_date: 净值结束日期 YYYYMMDD；须与 start_date 同时提供 (type: integer; required: N).
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
        request_params = {'etf_code': etf_code, 'nav_date': nav_date, 'start_date': start_date, 'end_date': end_date}
        request_params.update(kwargs)
        path = ENDPOINTS['etf_net_value'].path
        return self.get_paginated(
            path,
            page=page,
            page_size=page_size,
            limit=limit,
            all_pages=all_pages,
            max_pages=max_pages,
            max_page_size=ENDPOINTS['etf_net_value'].max_page_size,
            raw=raw,
            fields=fields,
            as_dataframe=as_dataframe,
            **request_params,
        )

    def etf_pcf_infos(
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
        """ETF申赎清单.

        Endpoint: ``api/v2/market/data/etf-pcf/etf-pcf-infos``.
        Method: ``GET``.
        Documented endpoint: ``etf_pcf_infos``.

        Args:
            symbol: ETF 代码；单标的单日或区间查询时必填，如 510300.SH (type: string; required: N).
            trade_date: 交易日 YYYYMMDD；单日查询时必填，不能与 start_date/end_date 同时使用 (type: integer; required: N).
            start_date: 区间开始日期 YYYYMMDD；须与 end_date、symbol 同时提供 (type: integer; required: N).
            end_date: 区间结束日期 YYYYMMDD；须与 start_date、symbol 同时提供 (type: integer; required: N).
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
            单标的单日查询时服务端返回裸对象，SDK 直接返回该 ``data`` 对象
            （``as_dataframe=True`` 时为单行 DataFrame）。
        """
        request_params = {'symbol': symbol, 'trade_date': trade_date, 'start_date': start_date, 'end_date': end_date}
        request_params.update(kwargs)
        path = ENDPOINTS['etf_pcf_infos'].path
        return self.get_paginated(
            path,
            page=page,
            page_size=page_size,
            limit=limit,
            all_pages=all_pages,
            max_pages=max_pages,
            max_page_size=ENDPOINTS['etf_pcf_infos'].max_page_size,
            raw=raw,
            fields=fields,
            as_dataframe=as_dataframe,
            unwrap_bare_data=True,
            **request_params,
        )

    def etf_share(
        self,
        etf_code: Any | None = None,
        stati_perd: Any | None = None,
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
        """ETF份额.

        Endpoint: ``api/v2/market/data/etf-share``.
        Method: ``GET``.
        Documented endpoint: ``etf_share``.

        Args:
            etf_code: ETF 代码，如 510300；兼容参数名 fund_code (type: string; required: Y).
            stati_perd: 统计周期：日/季度/年度/截止时点/半年/全部，默认全部 (type: string; required: N).
            start_date: 开始日期 YYYYMMDD，按 trade_date 过滤 (type: integer; required: N).
            end_date: 结束日期 YYYYMMDD，按 trade_date 过滤 (type: integer; required: N).
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
        request_params = {'etf_code': etf_code, 'stati_perd': stati_perd, 'start_date': start_date, 'end_date': end_date}
        request_params.update(kwargs)
        path = ENDPOINTS['etf_share'].path
        return self.get_paginated(
            path,
            page=page,
            page_size=page_size,
            limit=limit,
            all_pages=all_pages,
            max_pages=max_pages,
            max_page_size=ENDPOINTS['etf_share'].max_page_size,
            raw=raw,
            fields=fields,
            as_dataframe=as_dataframe,
            **request_params,
        )
