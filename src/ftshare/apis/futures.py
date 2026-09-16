"""Futures API methods grouped by ftshare-doc."""

from __future__ import annotations

from collections.abc import Sequence
from typing import Any

from ..endpoints import ENDPOINTS


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
            symbol: 合约全码如 A2605.DCE；大小写不敏感；不传或空表示该日全部 (type: string; required: N).
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

    def futures_minutes(
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
        """期货历史分钟行情.

        Endpoint: ``api/v2/market/data/futures_minutes``.
        Method: ``GET``.
        Documented endpoint: ``futures_minutes``.

        Args:
            symbol: 期货合约代码，带交易所短后缀 (type: string; required: Y).
            interval: 分钟周期，默认 ``1min`` (type: string; required: N).
            start: 起始时间戳，单位毫秒 (type: integer; required: N).
            end: 结束时间戳，单位毫秒，不能单独传 (type: integer; required: N).
            limit: 返回条数上限，范围 1～1000 (type: integer; required: N).
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
            'futures_minutes',
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
        """期货行情.

        Endpoint: ``api/v1/market/data/futures/kline``.
        Method: ``GET``.
        Documented endpoint: ``futures_contract_kline``.

        Args:
            symbol: 期货合约代码 (type: string; required: Y).
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
            'futures_contract_kline',
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
            symbols: 期货合约代码列表，1～20 个 (type: array; required: Y).
            raw: Return the decoded JSON payload without tabular extraction.
            fields: Optional field list or comma-separated field string applied after extraction.
            as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
            **kwargs: Extra request parameters forwarded unchanged.

        Returns:
            A pandas ``DataFrame`` by default, Python rows when
            ``as_dataframe=False``, or raw JSON when ``raw=True``.
        """
        request_params = {'symbols': symbols}
        request_params.update(kwargs)
        return self._call_endpoint(
            'futures_minutes_realtime',
            raw=raw,
            fields=fields,
            as_dataframe=as_dataframe,
            **request_params,
        )
    def fut_wsr(self, trade_date: Any | None = None, start_date: Any | None = None, end_date: Any | None = None, symbol: Any | None = None, exchange: Any | None = None, page: int | None = None, page_size: int | None = None, *, raw: bool = False, fields: Sequence[str] | str | None = None, as_dataframe: bool = True, **kwargs: Any) -> Any:
        """期货仓单日报."""
        params = {'trade_date': trade_date, 'start_date': start_date, 'end_date': end_date, 'symbol': symbol, 'exchange': exchange, 'page': page, 'page_size': page_size}
        params.update(kwargs)
        return self._call_endpoint('fut_wsr', raw=raw, fields=fields, as_dataframe=as_dataframe, **params)


    def fut_weekly_detail(self, week: Any | None = None, prd: Any | None = None, start_week: Any | None = None, end_week: Any | None = None, exchange: Any | None = None, page: int | None = None, page_size: int | None = None, *, raw: bool = False, fields: Sequence[str] | str | None = None, as_dataframe: bool = True, **kwargs: Any) -> Any:
        """期货主要品种交易周报."""
        params = {'week': week, 'prd': prd, 'start_week': start_week, 'end_week': end_week, 'exchange': exchange, 'page': page, 'page_size': page_size}
        params.update(kwargs)
        return self._call_endpoint('fut_weekly_detail', raw=raw, fields=fields, as_dataframe=as_dataframe, **params)


    def fut_settle(self, ts_code: Any | None = None, trade_date: Any | None = None, start_date: Any | None = None, end_date: Any | None = None, exchange: Any | None = None, page: int | None = None, page_size: int | None = None, *, raw: bool = False, fields: Sequence[str] | str | None = None, as_dataframe: bool = True, **kwargs: Any) -> Any:
        """期货每日结算参数."""
        params = {'ts_code': ts_code, 'trade_date': trade_date, 'start_date': start_date, 'end_date': end_date, 'exchange': exchange, 'page': page, 'page_size': page_size}
        params.update(kwargs)
        return self._call_endpoint('fut_settle', raw=raw, fields=fields, as_dataframe=as_dataframe, **params)


    def ft_limit(self, ts_code: Any | None = None, trade_date: Any | None = None, start_date: Any | None = None, end_date: Any | None = None, cont: Any | None = None, exchange: Any | None = None, page: int | None = None, page_size: int | None = None, *, raw: bool = False, fields: Sequence[str] | str | None = None, as_dataframe: bool = True, **kwargs: Any) -> Any:
        """期货合约涨跌停价."""
        params = {'ts_code': ts_code, 'trade_date': trade_date, 'start_date': start_date, 'end_date': end_date, 'cont': cont, 'exchange': exchange, 'page': page, 'page_size': page_size}
        params.update(kwargs)
        return self._call_endpoint('ft_limit', raw=raw, fields=fields, as_dataframe=as_dataframe, **params)


    def futures_nanhua_index_kline(self, code: Any | None = None, trade_date: Any | None = None, start_date: Any | None = None, end_date: Any | None = None, page: int | None = None, page_size: int | None = None, *, raw: bool = False, fields: Sequence[str] | str | None = None, as_dataframe: bool = True, **kwargs: Any) -> Any:
        """南华期货指数日K线."""
        params = {'code': code, 'trade_date': trade_date, 'start_date': start_date, 'end_date': end_date, 'page': page, 'page_size': page_size}
        params.update(kwargs)
        return self._call_endpoint('futures_nanhua_index_kline', raw=raw, fields=fields, as_dataframe=as_dataframe, **params)

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

    def futures_minutes_batch(self, symbols: Any | None = None, interval: Any | None = None, start: Any | None = None, end: Any | None = None, limit: Any | None = None, *, raw: bool = False, fields: Sequence[str] | str | None = None, as_dataframe: bool = True, **kwargs: Any) -> Any:
        """批量期货历史分钟行情."""
        params = {'symbols': symbols, 'interval': interval, 'start': start, 'end': end, 'limit': limit}
        params.update(kwargs)
        return self._call_endpoint('futures_minutes_batch', raw=raw, fields=fields, as_dataframe=as_dataframe, **params)
