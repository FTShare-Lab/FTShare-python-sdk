"""FTShare finance endpoint methods generated from ``ftshare-doc/api-doc``."""

from __future__ import annotations

from collections.abc import Sequence
from typing import Any

from ..endpoints import ENDPOINTS


class FinanceApiMixin:
    """Endpoint methods for the finance API group."""

    def baidu_financial_calendar(
        self,
        start_date: Any | None = None,
        end_date: Any | None = None,
        category: Any | None = None,
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
        """百度财经日历.

        Endpoint: ``api/v1/market/data/finance/financial-calendar/baidu``.
        Method: ``GET``.
        Source document: ``ftshare-doc/api-doc/百度财经日历.md``.
        Documented endpoint: ``baidu_financial_calendar``.

        Args:
            start_date: 起始日期 (type: string; required: Y).
            end_date: 结束日期（与 start_date 间隔 ≤ 3 天） (type: string; required: Y).
            category: 筛选大类：`economic` / `ipo` / `report_time` / `trade_reminder`；不传返回全部 (type: string; required: N).
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
        request_params = {'start_date': start_date, 'end_date': end_date, 'category': category}
        request_params.update(kwargs)
        path = ENDPOINTS['baidu_financial_calendar'].path
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

    def balance(
        self,
        stock_code: Any | None = None,
        year: Any | None = None,
        report_type: Any | None = None,
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
        """A股资产负债表.

        Endpoint: ``api/v1/market/data/finance/balance``.
        Method: ``GET``.
        Source document: ``ftshare-doc/api-doc/A股资产负债表.md``.
        Documented endpoint: ``balance``.

        Args:
            stock_code: A 股代码，6 位数字 + 后缀（如 600519.SH）；存在则进入模式A 单票查询 (type: string; required: N).
            year: 年份（模式B 必填），如 2024 (type: int; required: N).
            report_type: 报告期类型（模式B 必填）：q1 / q2 / q3 / annual（兼容 h1） (type: string; required: N).
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
        request_params = {'stock_code': stock_code, 'year': year, 'report_type': report_type}
        request_params.update(kwargs)
        path = ENDPOINTS['balance'].path
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

    def cashflow(
        self,
        stock_code: Any | None = None,
        year: Any | None = None,
        report_type: Any | None = None,
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
        """A股现金流量表.

        Endpoint: ``api/v1/market/data/finance/cashflow``.
        Method: ``GET``.
        Source document: ``ftshare-doc/api-doc/A股现金流量表.md``.
        Documented endpoint: ``cashflow``.

        Args:
            stock_code: A 股代码，6 位数字 + 后缀（如 000001.SZ）；存在则进入模式A 单票查询 (type: string; required: N).
            year: 年份（模式B 必填），如 2024 (type: int; required: N).
            report_type: 报告期类型（模式B 必填）：q1 / q2 / q3 / annual (type: string; required: N).
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
        request_params = {'stock_code': stock_code, 'year': year, 'report_type': report_type}
        request_params.update(kwargs)
        path = ENDPOINTS['cashflow'].path
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

    def cashflow_stock_code(
        self,
        *,
        raw: bool = False,
        fields: Sequence[str] | str | None = None,
        as_dataframe: bool = True,
        **kwargs: Any,
    ) -> Any:
        """现金流支持股票代码.

        Endpoint: ``api/v1/market/data/finance/cashflow-stock-code``.
        Method: ``GET``.
        Source document: ``ftshare-doc/api-doc/现金流支持股票代码.md``.
        Documented endpoint: ``get_cashflow_stock_code``.

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
            'cashflow_stock_code',
            raw=raw,
            fields=fields,
            as_dataframe=as_dataframe,
            **request_params,
        )

    def earnings_reports_paginated(
        self,
        stock_code: Any | None = None,
        year: Any | None = None,
        report_type: Any | None = None,
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
        """业绩快报.

        Endpoint: ``api/v1/market/data/finance/stock-performance-express``.
        Method: ``GET``.
        Source document: ``ftshare-doc/api-doc/业绩快报.md``.
        Documented endpoint: ``earnings_reports_paginated``.

        Args:
            stock_code: A 股代码（如 000001.SZ）；传则查单票全部业绩快报 (type: string; required: N).
            year: 年份（按报告期查询时必填），如 2024 (type: int; required: N).
            report_type: 报告类型枚举（按报告期查询时必填）：q1 / q2 / q3 / annual / announcement (type: string; required: N).
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
        request_params = {'stock_code': stock_code, 'year': year, 'report_type': report_type}
        request_params.update(kwargs)
        path = ENDPOINTS['earnings_reports_paginated'].path
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

    def income(
        self,
        stock_code: Any | None = None,
        year: Any | None = None,
        report_type: Any | None = None,
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
        """A股利润表.

        Endpoint: ``api/v1/market/data/finance/income``.
        Method: ``GET``.
        Source document: ``ftshare-doc/api-doc/A股利润表.md``.
        Documented endpoint: ``income``.

        Args:
            stock_code: A 股代码，6 位数字 + 后缀（如 000001.SZ）；存在则进入模式A 单票查询 (type: string; required: N).
            year: 年份（模式B 必填），如 2024 (type: int; required: N).
            report_type: 报告期类型（模式B 必填）：q1 / q2 / q3 / annual（兼容 h1） (type: string; required: N).
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
        request_params = {'stock_code': stock_code, 'year': year, 'report_type': report_type}
        request_params.update(kwargs)
        path = ENDPOINTS['income'].path
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

    def performance_forecasts_paginated(
        self,
        stock_code: Any | None = None,
        year: Any | None = None,
        report_type: Any | None = None,
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
        """业绩预告.

        Endpoint: ``api/v1/market/data/finance/stock-performance-forecast``.
        Method: ``GET``.
        Source document: ``ftshare-doc/api-doc/业绩预告.md``.
        Documented endpoint: ``performance_forecasts_paginated``.

        Args:
            stock_code: A 股代码，6 位数字 + 后缀（如 000001.SZ）；存在则进入模式A 单票查询 (type: string; required: N).
            year: 年份（模式B 必填），如 2024 (type: int; required: N).
            report_type: 报告期类型（模式B 必填）：q1 / q2 / q3 / annual (type: string; required: N).
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
        request_params = {'stock_code': stock_code, 'year': year, 'report_type': report_type}
        request_params.update(kwargs)
        path = ENDPOINTS['performance_forecasts_paginated'].path
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

    def wallstreetcn_financial_calendar(
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
        """华尔街见闻财经日历.

        Endpoint: ``api/v1/market/data/finance/financial-calendar/wallstreetcn``.
        Method: ``GET``.
        Source document: ``ftshare-doc/api-doc/华尔街见闻财经日历.md``.
        Documented endpoint: ``wallstreetcn_financial_calendar``.

        Args:
            start_date: 起始日期 (type: string; required: Y).
            end_date: 结束日期（与 start_date 间隔 ≤ 3 天） (type: string; required: Y).
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
        path = ENDPOINTS['wallstreetcn_financial_calendar'].path
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

