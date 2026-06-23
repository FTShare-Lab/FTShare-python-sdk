"""FTShare futures endpoint methods for FTShare market data."""

from __future__ import annotations

from collections.abc import Sequence
from typing import Any

from ..endpoints import ENDPOINTS


class FuturesApiMixin:
    """Endpoint methods for the futures API group."""

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
            symbol: WIND 合约全码如 A2605.DCE；大小写不敏感；不传或空表示该日全部 (type: string; required: N).
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
            contract_code: 合约代码，如 CU2607 / AU2608 (type: string; required: N).
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

    def eastmoney_futures_strange(
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
            contract_code: 合约代码，如 CU2607 / AU2608 (type: string; required: N).
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
        path = ENDPOINTS['eastmoney_futures_strange'].path
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

    def futures_contract_kline(
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
        """期货合约K线.

        Endpoint: ``api/v1/market/data/futures/kline``.
        Method: ``GET``.
        Documented endpoint: ``futures_contract_kline``.

        Args:
            symbol: WIND 合约全码，如 A2605.DCE (type: string; required: Y).
            interval: 周期，默认 1min；可选 1min/5min/15min/30min/60min/daily/weekly/monthly/quarterly/yearly (type: string; required: N).
            start: 开始时间戳（毫秒）；与 end 跨度 ≤3 天；仅 start 表示 [start,+∞) (type: int64; required: N).
            end: 结束时间戳（毫秒，闭区间）；须与 start 同时传入，禁止只传 end (type: int64; required: N).
            limit: 最大返回条数，默认 500 (type: int; required: N).
            raw: Return the decoded JSON payload without tabular extraction.
            fields: Optional field list or comma-separated field string applied after extraction.
            as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
            **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

        Returns:
            A pandas ``DataFrame`` by default, Python rows when
            ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
            payloads when multi-page fetching is used with ``raw=True``.
        """
        request_params = {'symbol': symbol, 'interval': interval, 'start': start, 'end': end, 'limit': limit}
        request_params.update(kwargs)
        return self._call_endpoint(
            'futures_contract_kline',
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
        """期货合约K线.

        Endpoint: ``api/v1/market/data/futures/kline``.
        Method: ``GET``.
        Documented endpoint: ``futures_contract_kline``.

        Args:
            symbol: WIND 合约全码，如 A2605.DCE (type: string; required: Y).
            interval: 周期，默认 1min；可选 1min/5min/15min/30min/60min/daily/weekly/monthly/quarterly/yearly (type: string; required: N).
            start: 开始时间戳（毫秒）；与 end 跨度 ≤3 天；仅 start 表示 [start,+∞) (type: int64; required: N).
            end: 结束时间戳（毫秒，闭区间）；须与 start 同时传入，禁止只传 end (type: int64; required: N).
            limit: 最大返回条数，默认 500 (type: int; required: N).
            raw: Return the decoded JSON payload without tabular extraction.
            fields: Optional field list or comma-separated field string applied after extraction.
            as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
            **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

        Returns:
            A pandas ``DataFrame`` by default, Python rows when
            ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
            payloads when multi-page fetching is used with ``raw=True``.
        """
        request_params = {'symbol': symbol, 'interval': interval, 'start': start, 'end': end, 'limit': limit}
        request_params.update(kwargs)
        return self._call_endpoint(
            'futures_kline',
            raw=raw,
            fields=fields,
            as_dataframe=as_dataframe,
            **request_params,
        )

