"""FTShare etf endpoint methods generated from ``ftshare-doc/api-doc``."""

from __future__ import annotations

from collections.abc import Sequence
from typing import Any

from ..endpoints import ENDPOINTS


class EtfApiMixin:
    """Endpoint methods for the etf API group."""

    def etf_adjust_factor(
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
        """ETF复权因子.

        Endpoint: ``api/v1/market/data/etf-adjust-factor``.
        Method: ``GET``.
        Source document: ``ftshare-doc/api-doc/ETF复权因子.md``.
        Documented endpoint: ``etf_adjust_factor``.

        Args:
            symbol: ETF 代码，支持纯数字或带后缀格式；区间扫描必填 (type: string; required: N).
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
            'etf_adjust_factor',
            raw=raw,
            fields=fields,
            as_dataframe=as_dataframe,
            **request_params,
        )

    def etf_components(
        self,
        symbol: Any | None = None,
        *,
        raw: bool = False,
        fields: Sequence[str] | str | None = None,
        as_dataframe: bool = True,
        **kwargs: Any,
    ) -> Any:
        """ETF成份股.

        Endpoint: ``api/v1/market/data/etf-component``.
        Method: ``GET``.
        Source document: ``ftshare-doc/api-doc/ETF成份股.md``.
        Documented endpoint: ``get_etf_components_handler``.

        Args:
            symbol: ETF 标的代码，带交易所后缀，如 510300.XSHG、159915.XSHE (type: string; required: Y).
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
            'etf_components',
            raw=raw,
            fields=fields,
            as_dataframe=as_dataframe,
            **request_params,
        )

    def etf_components_all(
        self,
        *,
        raw: bool = False,
        fields: Sequence[str] | str | None = None,
        as_dataframe: bool = True,
        **kwargs: Any,
    ) -> Any:
        """ETF成份列表.

        Endpoint: ``api/v1/market/data/etf-components-all``.
        Method: ``GET``.
        Source document: ``ftshare-doc/api-doc/ETF成份列表.md``.
        Documented endpoint: ``etf_components_all``.

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
        Source document: ``ftshare-doc/api-doc/ETF基础信息.md``.
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

    def etf_fund_export(
        self,
        request_id: Any | None = None,
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
        """指数ETF基金导出.

        Endpoint: ``api/v1/market/data/etf/zhitou-etf``.
        Method: ``GET``.
        Source document: ``ftshare-doc/api-doc/指数ETF基金导出.md``.
        Documented endpoint: ``etf_fund_export``.

        Args:
            request_id: 请求唯一标识，由调用方生成，原样写入响应 (type: string; required: Y).
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
        request_params = {'request_id': request_id}
        request_params.update(kwargs)
        path = ENDPOINTS['etf_fund_export'].path
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
        Source document: ``ftshare-doc/api-doc/ETF-PCF清单列表.md``.
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
        Source document: ``ftshare-doc/api-doc/ETF盘前数据.md``.
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
        Source document: ``ftshare-doc/api-doc/单只ETF盘前数据.md``.
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

