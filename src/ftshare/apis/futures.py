"""Futures API methods grouped by ftshare-doc."""

from __future__ import annotations

from collections.abc import Sequence
from typing import Any

from ..endpoints import ENDPOINTS
from ..params import symbols_to_csv_string


class FuturesApiMixin:
    """Endpoint methods for the futures ftshare-doc topic."""

    def major_contract(
        self,
        start_date: Any | None = None,
        end_date: Any | None = None,
        *,
        raw: bool = False,
        fields: Sequence[str] | str | None = None,
        as_dataframe: bool = True,
        **kwargs: Any,
    ) -> Any:
        """重大合同.

        Endpoint: ``api/v1/market/data/corporate/contract``.
        Method: ``GET``.
        Documented endpoint: ``major_contract``.

        Args:
            start_date: 起始日期（YYYYMMDD），区间跨度 ≤ 3 天 (type: string; required: Y).
            end_date: 结束日期（YYYYMMDD），区间跨度 ≤ 3 天 (type: string; required: Y).
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
        return self._call_endpoint(
            'major_contract',
            raw=raw,
            fields=fields,
            as_dataframe=as_dataframe,
            **request_params,
        )

    def major_contract_by_symbol(
        self,
        symbol: Any | None = None,
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
        """重大合同按标的.

        Endpoint: ``api/v1/market/data/corporate/contract/by-symbol``.
        Method: ``GET``.
        Documented endpoint: ``major_contract_by_symbol``.

        Args:
            symbol: 证券代码（标的） (type: string; required: Y).
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
        request_params = {'symbol': symbol}
        request_params.update(kwargs)
        path = ENDPOINTS['major_contract_by_symbol'].path
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

    def major_contract_summary(
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
        """重大合同汇总.

        Endpoint: ``api/v1/market/data/corporate/contract/summary``.
        Method: ``GET``.
        Documented endpoint: ``major_contract_summary``.

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
        path = ENDPOINTS['major_contract_summary'].path
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

    def china_futures_base_data(
        self,
        trade_date: Any | None = None,
        symbol: Any | None = None,
        *,
        raw: bool = False,
        fields: Sequence[str] | str | None = None,
        as_dataframe: bool = True,
        **kwargs: Any,
    ) -> Any:
        """中国期货基础数据.

        Endpoint: ``api/v1/market/data/futures/futures-base-data``.
        Method: ``GET``.
        Documented endpoint: ``get_china_futures_base_data_handler``.

        Args:
            trade_date: 交易日 YYYYMMDD；不传则使用前一交易日（CST） (type: int; required: N).
            symbol: 不带交易所后缀的合约代码，如 ``CU2609``；请求不区分大小写；CZCE 真实合约必须使用四位年份代码（如 ``AP2612``）；不传或空表示该日全部 (type: string; required: N).
            raw: Return the decoded JSON payload without tabular extraction.
            fields: Optional field list or comma-separated field string applied after extraction.
            as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
            **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

        Returns:
            A pandas ``DataFrame`` by default, Python rows when
            ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
            payloads when multi-page fetching is used with ``raw=True``.
        """
        request_params = {'trade_date': trade_date, 'symbol': symbol}
        request_params.update(kwargs)
        return self._call_endpoint(
            'china_futures_base_data',
            raw=raw,
            fields=fields,
            as_dataframe=as_dataframe,
            **request_params,
        )

    def china_futures_lists(
        self,
        trade_date: Any | None = None,
        *,
        raw: bool = False,
        fields: Sequence[str] | str | None = None,
        as_dataframe: bool = True,
        **kwargs: Any,
    ) -> Any:
        """中国期货列表.

        Endpoint: ``api/v1/market/data/futures/futures-lists``.
        Method: ``GET``.
        Documented endpoint: ``get_china_futures_lists_handler``.

        Args:
            trade_date: 交易日 YYYYMMDD；不传则使用前一交易日（CST） (type: int; required: N).
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
        return self._call_endpoint(
            'china_futures_lists',
            raw=raw,
            fields=fields,
            as_dataframe=as_dataframe,
            **request_params,
        )

    def eastmoney_futures_position(
        self,
        exchange: Any | None = None,
        variety_code: Any | None = None,
        contract_code: Any | None = None,
        trade_date: Any | None = None,
        start_date: Any | None = None,
        end_date: Any | None = None,
        member_name_abbr: Any | None = None,
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
        """东方财富期货持仓.

        Endpoint: ``api/v1/market/data/eastmoney-futures-position``.
        Method: ``GET``.
        Documented endpoint: ``get_eastmoney_futures_position``.

        Args:
            exchange: 交易所代码：shfe / dce / czce / cffex / ine / gfe (type: string; required: N).
            variety_code: 品种代码，如 cu / au / al / IF (type: string; required: N).
            contract_code: 合约代码，如 CU2607 / AU2608；请求不区分大小写，CZCE 真实合约使用四位年份代码 (type: string; required: N).
            trade_date: 交易日 YYYYMMDD；与 start_date/end_date 互斥 (type: string; required: N).
            start_date: 区间起始日 YYYYMMDD；需与 end_date 同时提供 (type: string; required: N).
            end_date: 区间结束日 YYYYMMDD；需与 start_date 同时提供 (type: string; required: N).
            member_name_abbr: 会员简称 (type: string; required: N).
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
        request_params = {'exchange': exchange, 'variety_code': variety_code, 'contract_code': contract_code, 'trade_date': trade_date, 'start_date': start_date, 'end_date': end_date, 'member_name_abbr': member_name_abbr}
        request_params.update(kwargs)
        path = ENDPOINTS['eastmoney_futures_position'].path
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

    def futures_minutes(
        self,
        symbol: Any | None = None,
        symbols: Any | None = None,
        interval: Any | None = None,
        start: Any | None = None,
        end: Any | None = None,
        limit: Any | None = None,
        *,
        raw: bool = False,
        fields: Sequence[str] | str | None = None,
        as_dataframe: bool = True,
        **kwargs: Any,
    ) -> Any:
        """期货历史分钟K线.

        Endpoint: ``api/v2/market/data/futures_minutes``.
        Method: ``GET``.
        Documented endpoint: ``futures_minutes``.

        Args:
            symbol: 单个期货合约代码，不带交易所后缀，如 ``A2611``；请求不区分大小写，CZCE 真实合约必须使用四位年份代码；与 ``symbols`` 二选一 (type: string; required: N).
            symbols: 1～20 个不带交易所后缀的期货合约代码；使用逗号分隔，兼容重复参数；CZCE 真实合约必须使用四位年份代码；与 ``symbol`` 二选一 (type: string; required: N).
            interval: 分钟周期，默认 ``1min`` (type: string; required: N).
            start: 起始时间戳，单位毫秒；必填 (type: integer; required: Y).
            end: 结束时间戳，单位毫秒；必填，不能单独传 (type: integer; required: Y).
            limit: 返回条数上限，范围 1～10000，批量时按每个合约分别限制 (type: integer; required: N).
            raw: Return the decoded JSON payload without tabular extraction.
            fields: Optional field list or comma-separated field string applied after extraction.
            as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
            **kwargs: Extra request parameters forwarded unchanged.

        Returns:
            A pandas ``DataFrame`` by default, Python rows when
            ``as_dataframe=False``, or raw JSON when ``raw=True``.
        """
        request_params = {
            'symbol': symbol,
            'symbols': symbols_to_csv_string(symbols),
            'interval': interval,
            'start': start,
            'end': end,
            'limit': limit,
        }
        request_params.update(kwargs)
        return self._call_endpoint(
            'futures_minutes',
            raw=raw,
            fields=fields,
            as_dataframe=as_dataframe,
            **request_params,
        )

    def futures_minutes_single(
        self,
        symbol: Any | None = None,
        interval: Any | None = None,
        start: Any | None = None,
        end: Any | None = None,
        limit: Any | None = None,
        *,
        raw: bool = False,
        fields: Sequence[str] | str | None = None,
        as_dataframe: bool = True,
        **kwargs: Any,
    ) -> Any:
        """期货历史分钟K线单合约.

        Endpoint: ``api/v2/market/data/futures_minutes/single``.
        Method: ``GET``.
        Documented endpoint: ``futures_minutes_single``.

        Args:
            symbol: 单个期货合约代码，使用不带交易所后缀的裸代码，如 ``A2611``，不区分大小写；只接受 ``symbol``，传 ``symbols`` 会返回 HTTP 400 (type: string; required: Y).
            interval: 分钟周期，默认 ``1min``；可选 ``1min`` / ``5min`` / ``15min`` / ``30min`` / ``60min`` (type: string; required: N).
            start: 起始时间戳，单位毫秒，闭区间，按北京时间解释；必须与 ``end`` 同时传入 (type: integer; required: Y).
            end: 结束时间戳，单位毫秒，闭区间；与 ``start`` 的时间跨度不得超过 3 个自然日（含首尾） (type: integer; required: Y).
            limit: 返回的最新 K 线条数，默认 500，范围 1～10000 (type: integer; required: N).
            raw: Return the decoded JSON payload without tabular extraction.
            fields: Optional field list or comma-separated field string applied after extraction.
            as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
            **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

        Returns:
            A pandas ``DataFrame`` by default, Python rows when
            ``as_dataframe=False``, or raw JSON when ``raw=True``。``data.total``
            为查询范围内聚合后的总记录数，不受 ``limit`` 截断。
        """
        request_params = {
            'symbol': symbol,
            'interval': interval,
            'start': start,
            'end': end,
            'limit': limit,
        }
        request_params.update(kwargs)
        return self._call_endpoint(
            'futures_minutes_single',
            raw=raw,
            fields=fields,
            as_dataframe=as_dataframe,
            **request_params,
        )

    def futures_daily_kline(
        self,
        symbol: Any | None = None,
        trade_date: Any | None = None,
        start_date: Any | None = None,
        end_date: Any | None = None,
        rule_version: Any | None = None,
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
        """期货官方日K与9999主连.

        Endpoint: ``api/v1/market/data/futures/daily-kline``.
        Method: ``GET``.
        Documented endpoint: ``futures_daily_kline``.

        Args:
            symbol: 期货合约或 9999 主连代码，交易所后缀可带可不带，如 ``A2405``、``A2405.DCE``、``A9999``、``A9999.DCE``；不带后缀时由服务端推断交易所。CZCE 真实合约必须使用四位年份代码（如 ``AP2612.CZCE``），三位代码返回成功空结果 (type: string; required: Y).
            trade_date: 单个交易日 ``YYYYMMDD``；与 ``start_date``、``end_date`` 二选一 (type: string; required: N).
            start_date: 范围查询起始交易日 ``YYYYMMDD``；必须与 ``end_date`` 成对传入，不能与 ``trade_date`` 同时传入 (type: string; required: N).
            end_date: 范围查询结束交易日 ``YYYYMMDD``；必须与 ``start_date`` 成对传入，且不能早于 ``start_date`` (type: string; required: N).
            rule_version: 9999 主连映射规则版本，默认 ``v1``；查询真实合约时无需传入 (type: string; required: N).
            page: Page number, starting from 1. If omitted, the server default is used unless ``limit`` or ``all_pages`` is set.
            page_size: Rows per page, default 50. The SDK validates this against the endpoint-specific maximum of 500.
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
        request_params = {
            'symbol': symbol,
            'trade_date': trade_date,
            'start_date': start_date,
            'end_date': end_date,
            'rule_version': rule_version,
        }
        request_params.update(kwargs)
        endpoint = ENDPOINTS['futures_daily_kline']
        return self.get_paginated(
            endpoint.path,
            page=page,
            page_size=page_size,
            limit=limit,
            all_pages=all_pages,
            max_pages=max_pages,
            max_page_size=endpoint.max_page_size,
            raw=raw,
            fields=fields,
            as_dataframe=as_dataframe,
            **request_params,
        )

    def futures_kline(
        self,
        symbol: Any | None = None,
        interval: Any | None = None,
        start: Any | None = None,
        end: Any | None = None,
        limit: Any | None = None,
        *,
        raw: bool = False,
        fields: Sequence[str] | str | None = None,
        as_dataframe: bool = True,
        **kwargs: Any,
    ) -> Any:
        """期货合约历史K线.

        Endpoint: ``api/v1/market/data/futures/kline``.
        Method: ``GET``.
        Documented endpoint: ``futures_kline``.

        Args:
            symbol: 不带交易所后缀的期货合约代码，如 ``A2611``；请求不区分大小写，CZCE 真实合约必须使用四位年份代码 (type: string; required: Y).
            interval: K线周期，默认 ``daily`` (type: string; required: N).
            start: 起始时间戳，单位毫秒 (type: integer; required: N).
            end: 结束时间戳，单位毫秒，不能单独传 (type: integer; required: N).
            limit: 返回条数上限，0 按 1 处理 (type: integer; required: N).
            raw: Return the decoded JSON payload without tabular extraction.
            fields: Optional field list or comma-separated field string applied after extraction.
            as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
            **kwargs: Extra request parameters forwarded unchanged.

        Returns:
            A pandas ``DataFrame`` by default, Python rows when
            ``as_dataframe=False``, or raw JSON when ``raw=True``.
        """
        request_params = {
            'symbol': symbol,
            'interval': interval,
            'start': start,
            'end': end,
            'limit': limit,
        }
        request_params.update(kwargs)
        return self._call_endpoint(
            'futures_kline',
            raw=raw,
            fields=fields,
            as_dataframe=as_dataframe,
            **request_params,
        )

    def futures_kline_batch(
        self,
        symbols: Any | None = None,
        interval: Any | None = None,
        start: Any | None = None,
        end: Any | None = None,
        limit: Any | None = None,
        *,
        raw: bool = False,
        fields: Sequence[str] | str | None = None,
        as_dataframe: bool = True,
        **kwargs: Any,
    ) -> Any:
        """批量期货合约历史K线.

        Endpoint: ``api/v2/market/data/futures/kline/batch``.
        Method: ``GET``.
        Documented endpoint: ``futures_kline_batch``.

        Args:
            symbols: 1～20 个不带交易所后缀的期货合约代码；使用逗号分隔，兼容重复参数；CZCE 真实合约必须使用四位年份代码 (type: string; required: Y).
            interval: K 线周期，默认 ``daily`` (type: string; required: N).
            start: 起始时间戳，单位毫秒 (type: integer; required: N).
            end: 结束时间戳，单位毫秒，不能单独传 (type: integer; required: N).
            limit: 每个合约返回条数上限，默认 500 (type: integer; required: N).
            raw: Return the decoded JSON payload without tabular extraction.
            fields: Optional field list or comma-separated field string applied after extraction.
            as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
            **kwargs: Extra request parameters forwarded unchanged.

        Returns:
            A pandas ``DataFrame`` by default, Python rows when
            ``as_dataframe=False``, or raw JSON when ``raw=True``.
        """
        request_params = {
            'symbols': symbols_to_csv_string(symbols),
            'interval': interval,
            'start': start,
            'end': end,
            'limit': limit,
        }
        request_params.update(kwargs)
        return self._call_endpoint(
            'futures_kline_batch',
            raw=raw,
            fields=fields,
            as_dataframe=as_dataframe,
            **request_params,
        )

    def futures_minutes_realtime(
        self,
        symbols: Sequence[str] | str | None = None,
        *,
        raw: bool = False,
        fields: Sequence[str] | str | None = None,
        as_dataframe: bool = True,
        **kwargs: Any,
    ) -> Any:
        """期货实时分钟K线.

        Endpoint: ``api/v4/market/data/futures_minutes/realtime``.
        Method: ``GET``.
        Documented endpoint: ``futures_minutes_realtime``.

        Args:
            symbols: 逗号分隔的不带交易所后缀的期货合约代码列表，1～20 个；CZCE 真实合约必须使用四位年份代码 (type: string; required: Y).
            raw: Return the decoded JSON payload without tabular extraction.
            fields: Optional field list or comma-separated field string applied after extraction.
            as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
            **kwargs: Extra request parameters forwarded unchanged.

        Returns:
            A pandas ``DataFrame`` by default, Python rows when
            ``as_dataframe=False``, or raw JSON when ``raw=True``.
        """
        request_params = {'symbols': symbols_to_csv_string(symbols)}
        request_params.update(kwargs)
        return self._call_endpoint(
            'futures_minutes_realtime',
            raw=raw,
            fields=fields,
            as_dataframe=as_dataframe,
            **request_params,
        )

    def futures_realtime_day_kline(
        self,
        symbols: Any | None = None,
        *,
        raw: bool = False,
        fields: Sequence[str] | str | None = None,
        as_dataframe: bool = True,
        **kwargs: Any,
    ) -> Any:
        """期货实时日K线.

        Endpoint: ``api/v4/market/data/futures-realtime-day-kline``.
        Method: ``GET``.
        Documented endpoint: ``futures_realtime_day_kline``.

        Args:
            symbols: 1～20 个不带交易所后缀的期货合约代码；使用逗号分隔，兼容重复参数；CZCE 真实合约必须使用四位年份代码 (type: string; required: Y).
            raw: Return the decoded JSON payload without tabular extraction.
            fields: Optional field list or comma-separated field string applied after extraction.
            as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
            **kwargs: Extra request parameters forwarded unchanged.

        Returns:
            A pandas ``DataFrame`` by default, Python rows when
            ``as_dataframe=False``, or raw JSON when ``raw=True``.
        """
        request_params = {'symbols': symbols_to_csv_string(symbols)}
        request_params.update(kwargs)
        return self._call_endpoint(
            'futures_realtime_day_kline',
            raw=raw,
            fields=fields,
            as_dataframe=as_dataframe,
            **request_params,
        )

    def fut_wsr(
        self,
        trade_date: Any | None = None,
        start_date: Any | None = None,
        end_date: Any | None = None,
        symbol: Any | None = None,
        exchange: Any | None = None,
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
        """期货仓单日报.

        Endpoint: ``api/v1/market/data/futures/fut-wsr``.
        Method: ``GET``.
        Documented endpoint: ``fut_wsr``.

        Args:
            trade_date: 单个交易日，格式 `YYYYMMDD`；不能与日期区间同时使用。 (type: integer; required: N).
            start_date: 开始交易日，格式 `YYYYMMDD`。 (type: integer; required: N).
            end_date: 结束交易日，格式 `YYYYMMDD`。 (type: integer; required: N).
            symbol: 品种代码，例如 `CU`、`A`、`SR`。 (type: string; required: N).
            exchange: 交易所代码：`SHFE`、`INE`、`CZCE`、`DCE`、`GFEX`。 (type: string; required: N).
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
        request_params = {'trade_date': trade_date, 'start_date': start_date, 'end_date': end_date, 'symbol': symbol, 'exchange': exchange}
        request_params.update(kwargs)
        path = ENDPOINTS['fut_wsr'].path
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


    def fut_weekly_detail(
        self,
        week: Any | None = None,
        prd: Any | None = None,
        start_week: Any | None = None,
        end_week: Any | None = None,
        exchange: Any | None = None,
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
        """期货主要品种交易周报.

        Endpoint: ``api/v1/market/data/futures/fut-weekly-detail``.
        Method: ``GET``.
        Documented endpoint: ``fut_weekly_detail``.

        Args:
            week: 单个统计周期，格式 `YYYYWW`，例如 `202601`。 (type: string; required: N).
            prd: 期货品种代码；支持逗号分隔，例如 `CU,AL`。 (type: string; required: N).
            start_week: 开始统计周期，格式 `YYYYWW`。 (type: string; required: N).
            end_week: 结束统计周期，格式 `YYYYWW`。 (type: string; required: N).
            exchange: 交易所代码：`SHFE`、`INE`、`CZCE`、`CFFEX`、`DCE`、`GFEX`。 (type: string; required: N).
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
        request_params = {'week': week, 'prd': prd, 'start_week': start_week, 'end_week': end_week, 'exchange': exchange}
        request_params.update(kwargs)
        path = ENDPOINTS['fut_weekly_detail'].path
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


    def fut_settle(
        self,
        ts_code: Any | None = None,
        trade_date: Any | None = None,
        start_date: Any | None = None,
        end_date: Any | None = None,
        exchange: Any | None = None,
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
        """期货每日结算参数.

        Endpoint: ``api/v1/market/data/futures/fut-settle``.
        Method: ``GET``.
        Documented endpoint: ``fut_settle``.

        Args:
            ts_code: 不带交易所后缀的合约代码，如 ``A2609``；请求不区分大小写，CZCE 真实合约必须使用四位年份代码（如 ``AP2612``） (type: string; required: N).
            trade_date: 单个交易日，格式 `YYYYMMDD`；不能与日期区间同时使用。 (type: integer; required: N).
            start_date: 开始交易日，格式 `YYYYMMDD`；必须与 `end_date` 同时传入，且日期区间跨度不超过 31 天。 (type: integer; required: N).
            end_date: 结束交易日，格式 `YYYYMMDD`；必须与 `start_date` 同时传入。 (type: integer; required: N).
            exchange: 交易所代码：`SHFE`、`INE`、`CZCE`、`CFFEX`、`DCE`、`GFEX`。 (type: string; required: Y).
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
        request_params = {'ts_code': ts_code, 'trade_date': trade_date, 'start_date': start_date, 'end_date': end_date, 'exchange': exchange}
        request_params.update(kwargs)
        path = ENDPOINTS['fut_settle'].path
        return self.get_paginated(
            path,
            page=page,
            page_size=page_size,
            limit=limit,
            all_pages=all_pages,
            max_pages=max_pages,
            max_page_size=ENDPOINTS['fut_settle'].max_page_size,
            raw=raw,
            fields=fields,
            as_dataframe=as_dataframe,
            **request_params,
        )


    def ft_limit(
        self,
        ts_code: Any | None = None,
        trade_date: Any | None = None,
        start_date: Any | None = None,
        end_date: Any | None = None,
        cont: Any | None = None,
        exchange: Any | None = None,
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
        """期货合约涨跌停价.

        Endpoint: ``api/v1/market/data/futures/ft-limit``.
        Method: ``GET``.
        Documented endpoint: ``ft_limit``.

        Args:
            ts_code: 不带交易所后缀的合约代码，如 ``A2609``、``CU2608``；请求不区分大小写并兼容 Tushare 短后缀，响应统一返回完整交易所后缀 (type: string; required: N).
            trade_date: 单个交易日，格式 `YYYYMMDD`；不能与日期区间同时使用。`trade_date` 与 `start_date`+`end_date` 至少提供一组。 (type: integer; required: N).
            start_date: 开始交易日，格式 `YYYYMMDD`；须与 `end_date` 同时提供。 (type: integer; required: N).
            end_date: 结束交易日，格式 `YYYYMMDD`；须与 `start_date` 同时提供。 (type: integer; required: N).
            cont: 品种代码，例如 `CU`、`A`。 (type: string; required: N).
            exchange: 交易所代码：`SHFE`、`INE`、`CZCE`、`CFFEX`、`DCE`、`GFEX`。 (type: string; required: Y).
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
        request_params = {'ts_code': ts_code, 'trade_date': trade_date, 'start_date': start_date, 'end_date': end_date, 'cont': cont, 'exchange': exchange}
        request_params.update(kwargs)
        path = ENDPOINTS['ft_limit'].path
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


    def futures_nanhua_index_kline(
        self,
        code: Any | None = None,
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
        """南华期货指数日K线.

        Endpoint: ``api/v1/market/data/futures/nanhua-index-kline``.
        Method: ``GET``.
        Documented endpoint: ``futures_nanhua_index_kline``.

        Args:
            code: 指数代码，如 AD_NH、AG_NH；与 trade_date 至少传一个 (type: string; required: N).
            trade_date: 交易日期（YYYYMMDD）；传入时为单日截面模式，忽略 start_date/end_date (type: string; required: N).
            start_date: 起始日期（YYYYMMDD），区间模式下界 (type: string; required: N).
            end_date: 结束日期（YYYYMMDD），区间模式上界；不得早于 start_date (type: string; required: N).
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
        request_params = {'code': code, 'trade_date': trade_date, 'start_date': start_date, 'end_date': end_date}
        request_params.update(kwargs)
        path = ENDPOINTS['futures_nanhua_index_kline'].path
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

    def index_fut_depth(
        self,
        trade_date: Any | None = None,
        start_date: Any | None = None,
        end_date: Any | None = None,
        code_prefix: Any | None = None,
        *,
        raw: bool = False,
        fields: Sequence[str] | str | None = None,
        as_dataframe: bool = True,
        **kwargs: Any,
    ) -> Any:
        """股指期货与指数深度行情.

        Endpoint: ``api/v1/market/data/index-fut/depth``.
        Method: ``GET``.
        Documented endpoint: ``index_fut_depth``.

        Args:
            trade_date: 单日查询日期 YYYYMMDD；不传日期参数时查询最新交易日，与 start_date、end_date 互斥 (type: string; required: N).
            start_date: 历史区间起始交易日 YYYYMMDD；必须与 end_date 同时传入 (type: string; required: N).
            end_date: 历史区间结束交易日 YYYYMMDD；必须与 start_date 同时传入，区间不能超过 3 年 (type: string; required: N).
            code_prefix: 品种筛选，支持 ``IF`` / ``IC`` / ``IM`` / ``IH``，不区分大小写；不传返回全部品种 (type: string; required: N).
            raw: Return the decoded JSON payload without tabular extraction.
            fields: Optional field list or comma-separated field string applied after extraction.
            as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
            **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

        Returns:
            A pandas ``DataFrame`` by default, Python rows when
            ``as_dataframe=False``, or raw JSON when ``raw=True``。服务端返回
            ``data`` 对象（``count`` / ``futures`` / ``index`` / ``instrument_map``），
            SDK 直接返回该对象（``as_dataframe=True`` 时为单行 DataFrame，
            嵌套数组保留原样）。
        """
        request_params = {
            'trade_date': trade_date,
            'start_date': start_date,
            'end_date': end_date,
            'code_prefix': code_prefix,
        }
        request_params.update(kwargs)
        path = ENDPOINTS['index_fut_depth'].path
        return self.get(
            path,
            raw=raw,
            fields=fields,
            as_dataframe=as_dataframe,
            unwrap_bare_data=True,
            **request_params,
        )

    def eastmoney_futures_strange(self, exchange: Any | None = None, variety: Any | None = None, contract: Any | None = None, trade_date: Any | None = None, *, raw: bool = False, fields: Sequence[str] | str | None = None, as_dataframe: bool = True, **kwargs: Any) -> Any:
        """东方财富期货龙虎榜."""
        params = {'exchange': exchange, 'variety': variety, 'contract': contract, 'trade_date': trade_date}
        params.update(kwargs)
        return self._call_endpoint('eastmoney_futures_strange', raw=raw, fields=fields, as_dataframe=as_dataframe, **params)

    def member_build_process(self, exchange: Any | None = None, member_name: Any | None = None, instrument_id: Any | None = None, start_date: Any | None = None, end_date: Any | None = None, contract_multiplier: Any | None = None, page: int | None = None, page_size: int | None = None, limit: int | None = None, all_pages: bool = False, max_pages: int | None = None, *, raw: bool = False, fields: Sequence[str] | str | None = None, as_dataframe: bool = True, **kwargs: Any) -> Any:
        """会员建仓过程."""
        params = {'exchange': exchange, 'member_name': member_name, 'instrument_id': instrument_id, 'start_date': start_date, 'end_date': end_date, 'contract_multiplier': contract_multiplier}
        params.update(kwargs)
        return self.get_paginated(ENDPOINTS['member_build_process'].path, page=page, page_size=page_size, limit=limit, all_pages=all_pages, max_pages=max_pages, raw=raw, fields=fields, as_dataframe=as_dataframe, **params)

    def member_position_ranking(self, exchange: Any | None = None, instrument_id: Any | None = None, trade_date: Any | None = None, direction: Any | None = None, page: int | None = None, page_size: int | None = None, limit: int | None = None, all_pages: bool = False, max_pages: int | None = None, *, raw: bool = False, fields: Sequence[str] | str | None = None, as_dataframe: bool = True, **kwargs: Any) -> Any:
        """会员持仓排名."""
        params = {'exchange': exchange, 'instrument_id': instrument_id, 'trade_date': trade_date, 'direction': direction}
        params.update(kwargs)
        return self.get_paginated(ENDPOINTS['member_position_ranking'].path, page=page, page_size=page_size, limit=limit, all_pages=all_pages, max_pages=max_pages, raw=raw, fields=fields, as_dataframe=as_dataframe, **params)
