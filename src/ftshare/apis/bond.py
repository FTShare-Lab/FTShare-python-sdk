"""Bond API methods grouped by ftshare-doc."""

from __future__ import annotations

from collections.abc import Sequence
from typing import Any

from ..endpoints import ENDPOINTS


class BondApiMixin:
    """Endpoint methods for the bond ftshare-doc topic."""

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
        """可转债K线.

        Endpoint: ``api/v1/market/data/convertible-bond-candlesticks``.
        Method: ``POST``.
        Documented endpoint: ``convertible_bond_candlesticks``.

        Args:
            symbol: 可转债代码，如 113027.XSHG、128048.XSHE；也接受 .SH、.SZ 短后缀 (type: string; required: Y).
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
        """批量可转债K线.

        Endpoint: ``api/v1/market/data/convertible-bond-candlesticks/batch``.
        Method: ``POST``.
        Documented endpoint: ``convertible_bond_candlesticks_batch``.

        Args:
            symbols: 可转债代码列表，如 ["113027.XSHG","128048.XSHE"]；也接受 .SH、.SZ 短后缀 (type: string[]; required: Y).
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
            'convertible_bond_candlesticks_batch',
            raw=raw,
            fields=fields,
            as_dataframe=as_dataframe,
            **request_params,
        )
