"""Bond API methods grouped by ftshare-doc."""

from __future__ import annotations

from collections.abc import Sequence
from typing import Any

from ..endpoints import ENDPOINTS
from ..params import symbols_to_json_string


class BondApiMixin:
    """Endpoint methods for the bond ftshare-doc topic."""

    def convertible_bond_candlesticks(
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
        """可转债历史K线.

        Endpoint: ``api/v1/market/data/convertible-bond-candlesticks``.
        Method: ``GET``.
        Documented endpoint: ``convertible_bond_candlesticks``.

        Args:
            symbol: 单只可转债代码，如 113042.SH；也接受 .XSHG、.XSHE 后缀 (type: string; required: Y).
            interval_unit: 周期单位：Day/Week/Month/Year，大小写不敏感 (type: enum; required: Y).
            interval_value: 可省略；周期查询无需设置 (type: int; required: N).
            adjust_kind: 复权：None（默认，不复权）/Forward（前复权）/Backward（后复权） (type: enum; required: N).
            since_ts_millis: 起始时间戳，单位毫秒；不得晚于 until，且与 until 相差不超过 12 个自然月 (type: int(ms); required: Y).
            until_ts_millis: 结束时间戳，单位毫秒 (type: int(ms); required: Y).
            limit: 保留最新 K 线条数上限；省略返回窗口内全部记录 (type: int; required: N).
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
            'convertible_bond_candlesticks',
            raw=raw,
            fields=fields,
            as_dataframe=as_dataframe,
            **request_params,
        )

    def convertible_bond_candlesticks_batch(
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
        """批量可转债历史K线.

        Endpoint: ``api/v2/market/data/convertible-bond-candlesticks/batch``.
        Method: ``GET``.
        Documented endpoint: ``convertible_bond_candlesticks_batch``.

        Args:
            symbols: 可转债代码列表，1～20 个；支持重复参数、逗号分隔或 JSON 字符串数组 (type: string[]; required: Y).
            interval_unit: 周期单位：Day/Week/Month/Year，大小写不敏感 (type: enum; required: Y).
            interval_value: 可省略；周期查询无需设置 (type: int; required: N).
            adjust_kind: 复权：None（默认，不复权）/Forward（前复权）/Backward（后复权） (type: enum; required: N).
            since_ts_millis: 起始时间戳，单位毫秒；不得晚于 until，且与 until 相差不超过 12 个自然月 (type: int(ms); required: Y).
            until_ts_millis: 结束时间戳，单位毫秒 (type: int(ms); required: Y).
            limit: 每个标的最新 K 线条数上限；省略返回窗口内全部记录 (type: int; required: N).
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
            'convertible_bond_candlesticks_batch',
            raw=raw,
            fields=fields,
            as_dataframe=as_dataframe,
            **request_params,
        )

    def convertible_bond_minute_candlesticks(
        self,
        symbol: Any | None = None,
        symbols: Any | None = None,
        interval_value: Any | None = None,
        since_ts_millis: Any | None = None,
        until_ts_millis: Any | None = None,
        limit: Any | None = None,
        *,
        raw: bool = False,
        fields: Sequence[str] | str | None = None,
        as_dataframe: bool = True,
        **kwargs: Any,
    ) -> Any:
        """可转债历史分钟K线.

        Endpoint: ``api/v2/market/data/convertible-bond-minute-candlesticks``.
        Method: ``GET``.
        Documented endpoint: ``convertible_bond_minute_candlesticks``.

        Args:
            symbol: 单只可转债代码（与 symbols 二选一，不能同时传） (type: string; required: N).
            symbols: 1～20 个可转债代码；支持重复参数、逗号分隔或 JSON 字符串数组（与 symbol 二选一） (type: string[]; required: N).
            interval_value: 分钟周期：仅支持 1、5、15，默认 1 (type: enum; required: N).
            since_ts_millis: 起始时间戳，单位毫秒；单只、批量都必须提供 (type: int(ms); required: Y).
            until_ts_millis: 结束时间戳，单位毫秒；不得早于 since，且单次跨度不超过 3 个自然日 (type: int(ms); required: Y).
            limit: 每只标的聚合后最多返回条数，范围 1～1000；省略返回窗口内全部记录 (type: int; required: N).
            raw: Return the decoded JSON payload without tabular extraction.
            fields: Optional field list or comma-separated field string applied after extraction.
            as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
            **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

        Returns:
            A pandas ``DataFrame`` by default, Python rows when
            ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
            payloads when multi-page fetching is used with ``raw=True``.
        """
        request_params = {'symbol': symbol, 'symbols': symbols, 'interval_value': interval_value, 'since_ts_millis': since_ts_millis, 'until_ts_millis': until_ts_millis, 'limit': limit}
        request_params.update(kwargs)
        return self._call_endpoint(
            'convertible_bond_minute_candlesticks',
            raw=raw,
            fields=fields,
            as_dataframe=as_dataframe,
            **request_params,
        )

    def convertible_bond_realtime_day_kline(self, symbols: Any | None = None, *, raw: bool = False, fields: Sequence[str] | str | None = None, as_dataframe: bool = True, **kwargs: Any) -> Any:
        """可转债实时日K线.

        Endpoint: ``api/v4/market/data/convertible-bond-realtime-day-kline``.
        Method: ``GET``.
        Documented endpoint: ``convertible_bond_realtime_day_kline``.

        Args:
            symbols: 1～20 个可转债代码的 JSON 字符串数组，如 ``["113042.SH","123107.SZ"]``；单只也必须传单元素数组 (type: string; required: Y).
            raw: Return the decoded JSON payload without tabular extraction.
            fields: Optional field list or comma-separated field string applied after extraction.
            as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
            **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

        Returns:
            A pandas ``DataFrame`` by default, Python rows when
            ``as_dataframe=False``, or raw JSON when ``raw=True``.
        """
        params = {'symbols': symbols_to_json_string(symbols)}
        params.update(kwargs)
        return self._call_endpoint('convertible_bond_realtime_day_kline', raw=raw, fields=fields, as_dataframe=as_dataframe, **params)

    def convertible_bond_realtime_minute_kline(self, symbols: Any | None = None, *, raw: bool = False, fields: Sequence[str] | str | None = None, as_dataframe: bool = True, **kwargs: Any) -> Any:
        """可转债实时分钟K线.

        Endpoint: ``api/v4/market/data/convertible-bond-realtime-minute-kline``.
        Method: ``GET``.
        Documented endpoint: ``convertible_bond_realtime_minute_kline``.

        Args:
            symbols: 1～20 个可转债代码的 JSON 字符串数组，如 ``["113042.SH","123107.SZ"]``；单只也必须传单元素数组 (type: string; required: Y).
            raw: Return the decoded JSON payload without tabular extraction.
            fields: Optional field list or comma-separated field string applied after extraction.
            as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
            **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

        Returns:
            A pandas ``DataFrame`` by default, Python rows when
            ``as_dataframe=False``, or raw JSON when ``raw=True``.
        """
        params = {'symbols': symbols_to_json_string(symbols)}
        params.update(kwargs)
        return self._call_endpoint('convertible_bond_realtime_minute_kline', raw=raw, fields=fields, as_dataframe=as_dataframe, **params)

    def szse_convertible_bond_matching_trades(
        self,
        security_code: Any | None = None,
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
        """深交所可转债匹配成交.

        Endpoint: ``api/v1/market/data/convertible-bond/szse/matching-trades``.
        Method: ``GET``.
        Documented endpoint: ``szse_convertible_bond_matching_trades``.

        Args:
            security_code: 六位可转债证券代码，例如 `123001`。 (type: string; required: N).
            trade_date: 单个交易日，格式 `YYYYMMDD`；不能与 `start_date`、`end_date` 同时使用。 (type: integer; required: N).
            start_date: 查询开始日期，格式 `YYYYMMDD`。 (type: integer; required: N).
            end_date: 查询结束日期，格式 `YYYYMMDD`。 (type: integer; required: N).
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
        request_params = {'security_code': security_code, 'trade_date': trade_date, 'start_date': start_date, 'end_date': end_date}
        request_params.update(kwargs)
        path = ENDPOINTS['szse_convertible_bond_matching_trades'].path
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


    def szse_convertible_bond_negotiated_trades(
        self,
        security_code: Any | None = None,
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
        """深交所可转债协议成交.

        Endpoint: ``api/v1/market/data/convertible-bond/szse/negotiated-trades``.
        Method: ``GET``.
        Documented endpoint: ``szse_convertible_bond_negotiated_trades``.

        Args:
            security_code: 六位可转债证券代码，例如 `123001`。 (type: string; required: N).
            trade_date: 单个交易日，格式 `YYYYMMDD`；不能与 `start_date`、`end_date` 同时使用。 (type: integer; required: N).
            start_date: 查询开始日期，格式 `YYYYMMDD`。 (type: integer; required: N).
            end_date: 查询结束日期，格式 `YYYYMMDD`。 (type: integer; required: N).
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
        request_params = {'security_code': security_code, 'trade_date': trade_date, 'start_date': start_date, 'end_date': end_date}
        request_params.update(kwargs)
        path = ENDPOINTS['szse_convertible_bond_negotiated_trades'].path
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


    def szse_convertible_bond_directed_trades(
        self,
        security_code: Any | None = None,
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
        """深交所可转债定向成交.

        Endpoint: ``api/v1/market/data/convertible-bond/szse/directed-trades``.
        Method: ``GET``.
        Documented endpoint: ``szse_convertible_bond_directed_trades``.

        Args:
            security_code: 六位可转债证券代码，例如 `123001`。 (type: string; required: N).
            trade_date: 单个交易日，格式 `YYYYMMDD`；不能与 `start_date`、`end_date` 同时使用。 (type: integer; required: N).
            start_date: 查询开始日期，格式 `YYYYMMDD`。 (type: integer; required: N).
            end_date: 查询结束日期，格式 `YYYYMMDD`。 (type: integer; required: N).
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
        request_params = {'security_code': security_code, 'trade_date': trade_date, 'start_date': start_date, 'end_date': end_date}
        request_params.update(kwargs)
        path = ENDPOINTS['szse_convertible_bond_directed_trades'].path
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


    def cb_lists(self, *, raw: bool = False, fields: Sequence[str] | str | None = None, as_dataframe: bool = True, **kwargs: Any) -> Any:
        """可转债列表."""
        params = {}
        params.update(kwargs)
        return self._call_endpoint('cb_lists', raw=raw, fields=fields, as_dataframe=as_dataframe, **params)

    def szse_convertible_bond_declaration_snapshots(
        self,
        security_code: Any | None = None,
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
        """深交所可转债申报快照.

        Endpoint: ``api/v1/market/data/convertible-bond/szse/declaration-snapshots``.
        Method: ``GET``.
        Documented endpoint: ``szse_convertible_bond_declaration_snapshots``.

        Args:
            security_code: 六位可转债证券代码，例如 `123001`。 (type: string; required: N).
            trade_date: 单个交易日，格式 `YYYYMMDD`；不能与 `start_date`、`end_date` 同时使用。 (type: integer; required: N).
            start_date: 查询开始日期，格式 `YYYYMMDD`。 (type: integer; required: N).
            end_date: 查询结束日期，格式 `YYYYMMDD`。 (type: integer; required: N).
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
        request_params = {'security_code': security_code, 'trade_date': trade_date, 'start_date': start_date, 'end_date': end_date}
        request_params.update(kwargs)
        path = ENDPOINTS['szse_convertible_bond_declaration_snapshots'].path
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
