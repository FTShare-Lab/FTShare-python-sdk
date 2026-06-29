"""Hong Kong market API methods grouped by ftshare-doc."""

from __future__ import annotations

from collections.abc import Sequence
from typing import Any

from ..endpoints import ENDPOINTS


class HkApiMixin:
    """Endpoint methods for the hk ftshare-doc topic."""

    def company_hk(
        self,
        trade_code: Any | None = None,
        *,
        raw: bool = False,
        fields: Sequence[str] | str | None = None,
        as_dataframe: bool = True,
        **kwargs: Any,
    ) -> Any:
        """港股公司信息.

        Endpoint: ``api/v1/market/data/hk/company-hk``.
        Method: ``GET``.
        Documented endpoint: ``get_company_hk``.

        Args:
            trade_code: 港股交易代码 (type: string; required: Y).
            raw: Return the decoded JSON payload without tabular extraction.
            fields: Optional field list or comma-separated field string applied after extraction.
            as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
            **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

        Returns:
            A pandas ``DataFrame`` by default, Python rows when
            ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
            payloads when multi-page fetching is used with ``raw=True``.
        """
        request_params = {'trade_code': trade_code}
        request_params.update(kwargs)
        return self._call_endpoint(
            'company_hk',
            raw=raw,
            fields=fields,
            as_dataframe=as_dataframe,
            **request_params,
        )

    def hk_balance_bank(
        self,
        trade_code: Any | None = None,
        year: Any | None = None,
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
        """港股资产负债表.

        Endpoint: ``api/v1/market/data/hk/hk-balance-bank``.
        Method: ``GET``.
        Documented endpoint: ``hk_balance_bank``.

        Args:
            trade_code: 港股代码（支持 `700` / `00700.HK`） (type: string; required: N).
            year: 报告期年份（如 2024），按 `end_date` 日历年过滤，需配 `report_type` (type: int32; required: N).
            report_type: 报告类型：annual（年报）/ semi（半年报），需配 `year` (type: string; required: N).
            start_date: 起始截止日期 YYYYMMDD，筛选 `end_date >= 此值` (type: int32; required: N).
            end_date: 结束截止日期 YYYYMMDD，筛选 `end_date <= 此值` (type: int32; required: N).
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
        request_params = {'trade_code': trade_code, 'year': year, 'report_type': report_type, 'start_date': start_date, 'end_date': end_date}
        request_params.update(kwargs)
        path = ENDPOINTS['hk_balance_bank'].path
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

    def hk_balance_gene(
        self,
        trade_code: Any | None = None,
        year: Any | None = None,
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
        """港股资产负债表.

        Endpoint: ``api/v1/market/data/hk/hk-balance-gene``.
        Method: ``GET``.
        Documented endpoint: ``hk_balance_gene``.

        Args:
            trade_code: 港股代码（支持 `700` / `00700.HK`） (type: string; required: N).
            year: 报告期年份（如 2024），按 `end_date` 日历年过滤，需配 `report_type` (type: int32; required: N).
            report_type: 报告类型：annual（年报）/ semi（半年报），需配 `year` (type: string; required: N).
            start_date: 起始截止日期 YYYYMMDD，筛选 `end_date >= 此值` (type: int32; required: N).
            end_date: 结束截止日期 YYYYMMDD，筛选 `end_date <= 此值` (type: int32; required: N).
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
        request_params = {'trade_code': trade_code, 'year': year, 'report_type': report_type, 'start_date': start_date, 'end_date': end_date}
        request_params.update(kwargs)
        path = ENDPOINTS['hk_balance_gene'].path
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

    def hk_balance_insur(
        self,
        trade_code: Any | None = None,
        year: Any | None = None,
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
        """港股资产负债表.

        Endpoint: ``api/v1/market/data/hk/hk-balance-insur``.
        Method: ``GET``.
        Documented endpoint: ``hk_balance_insur``.

        Args:
            trade_code: 港股代码（支持 `700` / `00700.HK`） (type: string; required: N).
            year: 报告期年份（如 2024），按 `end_date` 日历年过滤，需配 `report_type` (type: int32; required: N).
            report_type: 报告类型：annual（年报）/ semi（半年报），需配 `year` (type: string; required: N).
            start_date: 起始截止日期 YYYYMMDD，筛选 `end_date >= 此值` (type: int32; required: N).
            end_date: 结束截止日期 YYYYMMDD，筛选 `end_date <= 此值` (type: int32; required: N).
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
        request_params = {'trade_code': trade_code, 'year': year, 'report_type': report_type, 'start_date': start_date, 'end_date': end_date}
        request_params.update(kwargs)
        path = ENDPOINTS['hk_balance_insur'].path
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

    def hk_basinfo_get(
        self,
        hk_code: Any | None = None,
        *,
        raw: bool = False,
        fields: Sequence[str] | str | None = None,
        as_dataframe: bool = True,
        **kwargs: Any,
    ) -> Any:
        """港股个股信息.

        Endpoint: ``api/v1/market/data/hk/hk-view``.
        Method: ``GET``.
        Documented endpoint: ``get_hk_basinfo_get``.

        Args:
            hk_code: 港股代码，如 `00700.HK` (type: string; required: Y).
            raw: Return the decoded JSON payload without tabular extraction.
            fields: Optional field list or comma-separated field string applied after extraction.
            as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
            **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

        Returns:
            A pandas ``DataFrame`` by default, Python rows when
            ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
            payloads when multi-page fetching is used with ``raw=True``.
        """
        request_params = {'hk_code': hk_code}
        request_params.update(kwargs)
        return self._call_endpoint(
            'hk_basinfo_get',
            raw=raw,
            fields=fields,
            as_dataframe=as_dataframe,
            **request_params,
        )

    def hk_basinfo_post(
        self,
        hk_code: Any | None = None,
        *,
        raw: bool = False,
        fields: Sequence[str] | str | None = None,
        as_dataframe: bool = True,
        **kwargs: Any,
    ) -> Any:
        """港股个股信息.

        Endpoint: ``api/v1/market/data/hk/hk-view``.
        Method: ``GET``.
        Documented endpoint: ``get_hk_basinfo_post``.

        Args:
            hk_code: 港股代码，如 `00700.HK` (type: string; required: Y).
            raw: Return the decoded JSON payload without tabular extraction.
            fields: Optional field list or comma-separated field string applied after extraction.
            as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
            **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

        Returns:
            A pandas ``DataFrame`` by default, Python rows when
            ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
            payloads when multi-page fetching is used with ``raw=True``.
        """
        request_params = {'hk_code': hk_code}
        request_params.update(kwargs)
        return self._call_endpoint(
            'hk_basinfo_post',
            raw=raw,
            fields=fields,
            as_dataframe=as_dataframe,
            **request_params,
        )

    def hk_candlesticks(
        self,
        trade_code: Any | None = None,
        interval_unit: Any | None = None,
        until_date: Any | None = None,
        since_date: Any | None = None,
        interval_value: Any | None = None,
        limit: Any | None = None,
        adjust_kind: Any | None = None,
        *,
        raw: bool = False,
        fields: Sequence[str] | str | None = None,
        as_dataframe: bool = True,
        **kwargs: Any,
    ) -> Any:
        """港股K线.

        Endpoint: ``api/v1/market/data/hk/hk-candlesticks``.
        Method: ``GET``.
        Documented endpoint: ``get_hk_candlesticks``.

        Args:
            trade_code: 港股代码，如 `00700.HK` 或 `700` (type: string; required: Y).
            interval_unit: 间隔单位：day / month / quarter / year (type: string; required: Y).
            until_date: 结束日期（YYYY-MM-DD） (type: date; required: Y).
            since_date: 开始日期（YYYY-MM-DD） (type: date; required: N).
            interval_value: 间隔数值（当前仅支持 1） (type: int; required: N).
            limit: 数量限制（保留最近 N 根） (type: int; required: N).
            adjust_kind: 复权类型：forward(默认/前复权) / none(不复权) (type: string; required: N).
            raw: Return the decoded JSON payload without tabular extraction.
            fields: Optional field list or comma-separated field string applied after extraction.
            as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
            **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

        Returns:
            A pandas ``DataFrame`` by default, Python rows when
            ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
            payloads when multi-page fetching is used with ``raw=True``.
        """
        request_params = {'trade_code': trade_code, 'interval_unit': interval_unit, 'until_date': until_date, 'since_date': since_date, 'interval_value': interval_value, 'limit': limit, 'adjust_kind': adjust_kind}
        request_params.update(kwargs)
        return self._call_endpoint(
            'hk_candlesticks',
            raw=raw,
            fields=fields,
            as_dataframe=as_dataframe,
            **request_params,
        )

    def hk_cashflow(
        self,
        stock_code: Any | None = None,
        year: Any | None = None,
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
        """港股现金流量表.

        Endpoint: ``api/v1/market/data/hk/hk-cashflow``.
        Method: ``GET``.
        Documented endpoint: ``hk_cashflow``.

        Args:
            stock_code: 港股代码（如 `00700.HK`） (type: string; required: N).
            year: 报告期年份（如 2024），按 `end_date` 日历年过滤，需配 `report_type` (type: int32; required: N).
            report_type: 报告类型：annual（年报）/ semi（半年报），需配 `year` (type: string; required: N).
            start_date: 报告期范围下界 YYYYMMDD（含），过滤 `end_date >= 此值` (type: int32; required: N).
            end_date: 报告期范围上界 YYYYMMDD（含），过滤 `end_date <= 此值` (type: int32; required: N).
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
        request_params = {'stock_code': stock_code, 'year': year, 'report_type': report_type, 'start_date': start_date, 'end_date': end_date}
        request_params.update(kwargs)
        path = ENDPOINTS['hk_cashflow'].path
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

    def hk_income_bank(
        self,
        trade_code: Any | None = None,
        year: Any | None = None,
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
        """港股利润表.

        Endpoint: ``api/v1/market/data/hk/hk-income-bank``.
        Method: ``GET``.
        Documented endpoint: ``hk_income_bank``.

        Args:
            trade_code: 港股代码（支持 `700` / `00700.HK`） (type: string; required: N).
            year: 报告期年份（如 2024），按 `end_date` 日历年过滤，需配 `report_type` (type: int32; required: N).
            report_type: 报告类型：annual（年报）/ semi（半年报），需配 `year` (type: string; required: N).
            start_date: 起始截止日期 YYYYMMDD，筛选 `end_date >= 此值` (type: int32; required: N).
            end_date: 结束截止日期 YYYYMMDD，筛选 `end_date <= 此值` (type: int32; required: N).
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
        request_params = {'trade_code': trade_code, 'year': year, 'report_type': report_type, 'start_date': start_date, 'end_date': end_date}
        request_params.update(kwargs)
        path = ENDPOINTS['hk_income_bank'].path
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

    def hk_income_gene(
        self,
        trade_code: Any | None = None,
        year: Any | None = None,
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
        """港股利润表.

        Endpoint: ``api/v1/market/data/hk/hk-income-gene``.
        Method: ``GET``.
        Documented endpoint: ``hk_income_gene``.

        Args:
            trade_code: 港股代码（支持 `700` / `00700.HK`） (type: string; required: N).
            year: 报告期年份（如 2024），按 `end_date` 日历年过滤，需配 `report_type` (type: int32; required: N).
            report_type: 报告类型：annual（年报）/ semi（半年报），需配 `year` (type: string; required: N).
            start_date: 起始截止日期 YYYYMMDD，筛选 `end_date >= 此值` (type: int32; required: N).
            end_date: 结束截止日期 YYYYMMDD，筛选 `end_date <= 此值` (type: int32; required: N).
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
        request_params = {'trade_code': trade_code, 'year': year, 'report_type': report_type, 'start_date': start_date, 'end_date': end_date}
        request_params.update(kwargs)
        path = ENDPOINTS['hk_income_gene'].path
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

    def hk_income_insur(
        self,
        trade_code: Any | None = None,
        year: Any | None = None,
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
        """港股利润表.

        Endpoint: ``api/v1/market/data/hk/hk-income-insur``.
        Method: ``GET``.
        Documented endpoint: ``hk_income_insur``.

        Args:
            trade_code: 港股代码（支持 `700` / `00700.HK`） (type: string; required: N).
            year: 报告期年份（如 2024），按 `end_date` 日历年过滤，需配 `report_type` (type: int32; required: N).
            report_type: 报告类型：annual（年报）/ semi（半年报），需配 `year` (type: string; required: N).
            start_date: 起始截止日期 YYYYMMDD，筛选 `end_date >= 此值` (type: int32; required: N).
            end_date: 结束截止日期 YYYYMMDD，筛选 `end_date <= 此值` (type: int32; required: N).
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
        request_params = {'trade_code': trade_code, 'year': year, 'report_type': report_type, 'start_date': start_date, 'end_date': end_date}
        request_params.update(kwargs)
        path = ENDPOINTS['hk_income_insur'].path
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

    def hk_valuatnanalyd(
        self,
        trade_code: Any | None = None,
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
        """港股估值分析.

        Endpoint: ``api/v1/market/data/hk/hk-valuatnanalyd``.
        Method: ``GET``.
        Documented endpoint: ``get_hk_valuatnanalyd``.

        Args:
            trade_code: 港股代码（支持 `700` / `00700.HK`）；留空查全市场 (type: string; required: N).
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
        request_params = {'trade_code': trade_code}
        request_params.update(kwargs)
        path = ENDPOINTS['hk_valuatnanalyd'].path
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

    def market_cap_hk(
        self,
        trade_code: Any | None = None,
        *,
        raw: bool = False,
        fields: Sequence[str] | str | None = None,
        as_dataframe: bool = True,
        **kwargs: Any,
    ) -> Any:
        """港股市值.

        Endpoint: ``api/v1/market/data/hk/market-cap-hk``.
        Method: ``GET``.
        Documented endpoint: ``get_market_cap_hk``.

        Args:
            trade_code: 港股交易代码 (type: string; required: Y).
            raw: Return the decoded JSON payload without tabular extraction.
            fields: Optional field list or comma-separated field string applied after extraction.
            as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
            **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

        Returns:
            A pandas ``DataFrame`` by default, Python rows when
            ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
            payloads when multi-page fetching is used with ``raw=True``.
        """
        request_params = {'trade_code': trade_code}
        request_params.update(kwargs)
        return self._call_endpoint(
            'market_cap_hk',
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
