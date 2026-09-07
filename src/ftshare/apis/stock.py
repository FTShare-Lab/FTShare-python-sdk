"""Stock data API methods grouped by ftshare-doc."""

from __future__ import annotations

from collections.abc import Sequence
from typing import Any

from ..endpoints import ENDPOINTS


def _present_params(params: dict[str, Any]) -> list[str]:
    return [name for name, value in params.items() if value is not None]


class StockApiMixin:
    """Endpoint methods for the stock ftshare-doc topic."""

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

    def goodwill_industry(
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
        """商誉行业.

        Endpoint: ``api/v1/market/data/goodwill/industry``.
        Method: ``GET``.
        Documented endpoint: ``goodwill_industry``.

        Args:
            date: 报告期，如 20250331 (type: string; required: Y).
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
        path = ENDPOINTS['goodwill_industry'].path
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

    def goodwill_market_overview(
        self,
        *,
        raw: bool = False,
        fields: Sequence[str] | str | None = None,
        as_dataframe: bool = True,
        **kwargs: Any,
    ) -> Any:
        """商誉市场总览.

        Endpoint: ``api/v1/market/data/goodwill/market-overview``.
        Method: ``GET``.
        Documented endpoint: ``goodwill_market_overview``.

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
            'goodwill_market_overview',
            raw=raw,
            fields=fields,
            as_dataframe=as_dataframe,
            **request_params,
        )

    def goodwill_predict(
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
        """商誉预测.

        Endpoint: ``api/v1/market/data/goodwill/predict``.
        Method: ``GET``.
        Documented endpoint: ``goodwill_predict``.

        Args:
            date: 报告期，如 20250331 (type: string; required: Y).
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
        path = ENDPOINTS['goodwill_predict'].path
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

    def goodwill_stock_detail(
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
        """商誉个股明细.

        Endpoint: ``api/v1/market/data/goodwill/stock-detail``.
        Method: ``GET``.
        Documented endpoint: ``goodwill_stock_detail``.

        Args:
            date: 报告期，如 20250331 (type: string; required: Y).
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
        path = ENDPOINTS['goodwill_stock_detail'].path
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

    def goodwill_stock_impairment(
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
        """商誉减值.

        Endpoint: ``api/v1/market/data/goodwill/stock-impairment``.
        Method: ``GET``.
        Documented endpoint: ``goodwill_stock_impairment``.

        Args:
            date: 报告期，如 20250331 (type: string; required: Y).
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
        path = ENDPOINTS['goodwill_stock_impairment'].path
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

    def stock_float_holders(
        self,
        stock_code: Any | None = None,
        is_last: Any | None = None,
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
        """十大流通股东.

        Endpoint: ``api/v1/market/data/holder/stock-holder-ften``.
        Method: ``GET``.
        Documented endpoint: ``get_stock_holder_float_top10``.

        Args:
            stock_code: 标的代码，指定时返回该标的全部历史数据 (type: string; required: N).
            is_last: 是否取所有标的最新一期，true 时按 page/page_size 分页 (type: bool; required: N).
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
        request_params = {'stock_code': stock_code, 'is_last': is_last}
        request_params.update(kwargs)
        path = ENDPOINTS['stock_float_holders'].path
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

    def stock_ggmx_buy_ranking(
        self,
        time_range: Any | None = None,
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
        """董监高增持排名.

        Endpoint: ``api/v2/market/data/holder/stock-ggmx-buy-ranking``.
        Method: ``GET``.
        Documented endpoint: ``stock_ggmx_buy_ranking_handler``.

        Args:
            time_range: 时间范围：1m / 3m / 6m / 1y / 2y，默认 1m，别名 timeRange (type: string; required: N).
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
        request_params = {'time_range': time_range}
        request_params.update(kwargs)
        path = ENDPOINTS['stock_ggmx_buy_ranking'].path
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

    def stock_ggmx_sell_ranking(
        self,
        time_range: Any | None = None,
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
        """董监高减持排名.

        Endpoint: ``api/v2/market/data/holder/stock-ggmx-sell-ranking``.
        Method: ``GET``.
        Documented endpoint: ``stock_ggmx_sell_ranking_handler``.

        Args:
            time_range: 时间范围：1m / 3m / 6m / 1y / 2y，默认 1m，别名 timeRange (type: string; required: N).
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
        request_params = {'time_range': time_range}
        request_params.update(kwargs)
        path = ENDPOINTS['stock_ggmx_sell_ranking'].path
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

    def stock_holders(
        self,
        stock_code: Any | None = None,
        is_last: Any | None = None,
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
        """十大股东.

        Endpoint: ``api/v1/market/data/holder/stock-holder-ten``.
        Method: ``GET``.
        Documented endpoint: ``get_stock_holder_top10``.

        Args:
            stock_code: 标的代码，指定时返回该标的全部历史数据 (type: string; required: N).
            is_last: 是否取所有标的最新一期，true 时按 page/page_size 分页 (type: bool; required: N).
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
        request_params = {'stock_code': stock_code, 'is_last': is_last}
        request_params.update(kwargs)
        path = ENDPOINTS['stock_holders'].path
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

    def stock_holders_number(
        self,
        stock_code: Any | None = None,
        is_last: Any | None = None,
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
        """股东人数.

        Endpoint: ``api/v1/market/data/holder/stock-holder-nums``.
        Method: ``GET``.
        Documented endpoint: ``get_stock_holder_nums``.

        Args:
            stock_code: 标的代码，指定时返回该标的全部历史数据 (type: string; required: N).
            is_last: 是否取所有标的最新一期，true 时按 page/page_size 分页 (type: bool; required: N).
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
        request_params = {'stock_code': stock_code, 'is_last': is_last}
        request_params.update(kwargs)
        path = ENDPOINTS['stock_holders_number'].path
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

    def stock_ggcg_em(
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
        """东方财富股东增减持.

        Endpoint: ``api/v1/market/data/holder/stock-ggcg-em``.
        Method: ``GET``.
        Documented endpoint: ``stock_ggcg_em``.

        Args:
            symbol: 数据类型：全部 / 股东增持 / 股东减持，默认全部 (type: string; required: N).
            page: Page number, starting from 1. If omitted, the server default is used unless ``limit`` or ``all_pages`` is set.
            page_size: Rows per page. The SDK validates this against the endpoint-specific maximum.
            limit: Maximum number of rows to return. The SDK may fetch multiple pages to satisfy this limit.
            all_pages: Fetch and combine pages until the server reports the last page.
            max_pages: Optional safety cap for ``all_pages``.
            raw: Return the decoded JSON payload without tabular extraction.
            fields: Optional field list or comma-separated field string applied after extraction.
            as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
            **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.
        """
        request_params = {'symbol': symbol}
        request_params.update(kwargs)
        path = ENDPOINTS['stock_ggcg_em'].path
        return self.get_paginated(
            path,
            page=page,
            page_size=page_size,
            limit=limit,
            all_pages=all_pages,
            max_pages=max_pages,
            max_page_size=200,
            raw=raw,
            fields=fields,
            as_dataframe=as_dataframe,
            **request_params,
        )

    def stock_share_chg(
        self,
        stock_code: Any | None = None,
        is_last: Any | None = None,
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
        """股东增减持.

        Endpoint: ``api/v1/market/data/holder/stock-share-chg``.
        Method: ``GET``.
        Documented endpoint: ``get_stock_share_chg``.

        Args:
            stock_code: 标的代码，指定时返回该标的分页历史数据 (type: string; required: N).
            is_last: 是否取所有标的最新一期，true 时按 page/page_size 分页 (type: bool; required: N).
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
        request_params = {'stock_code': stock_code, 'is_last': is_last}
        request_params.update(kwargs)
        path = ENDPOINTS['stock_share_chg'].path
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

    def auction_results(
        self,
        ts_code: Any | None = None,
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
        """集合竞价结果.

        Endpoint: ``api/v1/market/data/auction-results``.
        Method: ``GET``.
        Documented endpoint: ``auction_results``.

        Args:
            ts_code: 股票代码，如 000001.XSHE (type: string; required: N).
            trade_date: 交易日，格式 YYYYMMDD (type: string; required: N).
            start_date: 起始日期，格式 YYYYMMDD (type: string; required: N).
            end_date: 结束日期，格式 YYYYMMDD (type: string; required: N).
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
        request_params = {'ts_code': ts_code, 'trade_date': trade_date, 'start_date': start_date, 'end_date': end_date}
        request_params.update(kwargs)
        path = ENDPOINTS['auction_results'].path
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

    def bse_mapping(
        self,
        o_code: Any | None = None,
        n_code: Any | None = None,
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
        """北交所映射.

        Endpoint: ``api/v1/market/data/bse-mapping``.
        Method: ``GET``.
        Documented endpoint: ``get_bse_mapping``.

        Args:
            o_code: 旧代码（如 `838163.BJ`） (type: string; required: N).
            n_code: 新代码（如 `920163.BJ`） (type: string; required: N).
            page: Page number, starting from 1.
            page_size: Rows per page, up to the endpoint-specific maximum.
            limit: Maximum number of rows to return. The SDK may fetch multiple pages to satisfy this limit.
            all_pages: Fetch and combine pages until the server reports the last page.
            max_pages: Optional safety cap for ``all_pages``.
            raw: Return the decoded JSON payload without tabular extraction.
            fields: Optional field list or comma-separated field string applied after extraction.
            as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
            **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.
        """
        request_params = {'o_code': o_code, 'n_code': n_code}
        request_params.update(kwargs)
        path = ENDPOINTS['bse_mapping'].path
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

    def company_list(
        self,
        stock_name: Any | None = None,
        stock_code: Any | None = None,
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
        """公司列表.

        Endpoint: ``api/v1/market/data/company-list``.
        Method: ``GET``.
        Documented endpoint: ``get_company_list``.

        Args:
            stock_name: 股票名称，精确匹配 (type: string; required: N).
            stock_code: 股票代码，精确匹配 (type: string; required: N).
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
        request_params = {'stock_name': stock_name, 'stock_code': stock_code}
        request_params.update(kwargs)
        path = ENDPOINTS['company_list'].path
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

    def eastmoney_board_constituents(
        self,
        board_code: Any | None = None,
        *,
        raw: bool = False,
        fields: Sequence[str] | str | None = None,
        as_dataframe: bool = True,
        **kwargs: Any,
    ) -> Any:
        """东方财富板块成份股.

        Endpoint: ``api/v1/market/data/eastmoney-board-constituents``.
        Method: ``GET``.
        Documented endpoint: ``eastmoney_board_constituents``.

        Args:
            board_code: 板块代码，如 BK1024 (type: string; required: Y).
            raw: Return the decoded JSON payload without tabular extraction.
            fields: Optional field list or comma-separated field string applied after extraction.
            as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
            **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

        Returns:
            A pandas ``DataFrame`` by default, Python rows when
            ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
            payloads when multi-page fetching is used with ``raw=True``.
        """
        request_params = {'board_code': board_code}
        request_params.update(kwargs)
        return self._call_endpoint(
            'eastmoney_board_constituents',
            raw=raw,
            fields=fields,
            as_dataframe=as_dataframe,
            **request_params,
        )

    def eastmoney_board_daily_kline(
        self,
        board_code: Any | None = None,
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
        """东方财富板块日线OHLC.

        Endpoint: ``api/v1/market/data/eastmoney-board-daily-ohlc``.
        Method: ``GET``.
        Documented endpoint: ``eastmoney_board_daily_kline``.

        Args:
            board_code: 板块代码，如 BK1024 (type: string; required: Y).
            start_date: 起始日期（含），YYYY-MM-DD 或 YYYYMMDD (type: string; required: N).
            end_date: 截止日期（含），YYYY-MM-DD 或 YYYYMMDD (type: string; required: N).
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
        request_params = {'board_code': board_code, 'start_date': start_date, 'end_date': end_date}
        request_params.update(kwargs)
        path = ENDPOINTS['eastmoney_board_daily_kline'].path
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

    def eastmoney_concept_boards(
        self,
        *,
        raw: bool = False,
        fields: Sequence[str] | str | None = None,
        as_dataframe: bool = True,
        **kwargs: Any,
    ) -> Any:
        """东方财富概念板块.

        Endpoint: ``api/v1/market/data/eastmoney-concept-boards``.
        Method: ``GET``.
        Documented endpoint: ``eastmoney_concept_boards``.

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
            'eastmoney_concept_boards',
            raw=raw,
            fields=fields,
            as_dataframe=as_dataframe,
            **request_params,
        )

    def eastmoney_dapan_flow(
        self,
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
        """东方财富大盘资金流.

        Endpoint: ``api/v1/market/data/eastmoney-dapan-flow``.
        Method: ``GET``.
        Documented endpoint: ``get_eastmoney_dapan_flow``.

        Args:
            trade_date: 交易日 YYYYMMDD；与 start_date/end_date 互斥 (type: string; required: N).
            start_date: 区间起始日 YYYYMMDD；需与 end_date 同时提供 (type: string; required: N).
            end_date: 区间结束日 YYYYMMDD；需与 start_date 同时提供 (type: string; required: N).
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
        request_params = {'trade_date': trade_date, 'start_date': start_date, 'end_date': end_date}
        request_params.update(kwargs)
        path = ENDPOINTS['eastmoney_dapan_flow'].path
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

    def eastmoney_market_valuation(
        self,
        market_code: Any | None = None,
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
        """东方财富市场估值.

        Endpoint: ``api/v1/market/data/eastmoney-market-valuation``.
        Method: ``GET``.
        Documented endpoint: ``get_eastmoney_market_valuation``.

        Args:
            market_code: 市场代码，如 000001=上证指数、000300=沪深300；不传返回全部 (type: string; required: N).
            trade_date: 交易日 YYYYMMDD；与 start_date/end_date 互斥 (type: string; required: N).
            start_date: 区间起始日 YYYYMMDD；需与 end_date 同时提供 (type: string; required: N).
            end_date: 区间结束日 YYYYMMDD；需与 start_date 同时提供 (type: string; required: N).
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
        request_params = {'market_code': market_code, 'trade_date': trade_date, 'start_date': start_date, 'end_date': end_date}
        request_params.update(kwargs)
        path = ENDPOINTS['eastmoney_market_valuation'].path
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

    def eastmoney_rank(
        self,
        rank_group: Any | None = None,
        market: Any | None = None,
        trade_date: Any | None = None,
        *,
        raw: bool = False,
        fields: Sequence[str] | str | None = None,
        as_dataframe: bool = True,
        **kwargs: Any,
    ) -> Any:
        """东方财富股票排名.

        Endpoint: ``api/v1/market/data/eastmoney-rank``.
        Method: ``GET``.
        Documented endpoint: ``eastmoney_rank``.

        Args:
            rank_group: 榜单组：`hot`（人气榜）/ `up`（飙升榜） (type: string; required: N).
            market: 市场：`A`（A股）/ `HK`（港股）/ `US`（美股） (type: string; required: N).
            trade_date: 交易日期，格式 `YYYY-MM-DD`，不传默认取最新 (type: string; required: N).
            raw: Return the decoded JSON payload without tabular extraction.
            fields: Optional field list or comma-separated field string applied after extraction.
            as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
            **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

        Returns:
            A pandas ``DataFrame`` by default, Python rows when
            ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
            payloads when multi-page fetching is used with ``raw=True``.
        """
        request_params = {'rank_group': rank_group, 'market': market, 'trade_date': trade_date}
        request_params.update(kwargs)
        return self._call_endpoint(
            'eastmoney_rank',
            raw=raw,
            fields=fields,
            as_dataframe=as_dataframe,
            **request_params,
        )

    def eastmoney_sector_flow(
        self,
        sector_code: Any | None = None,
        sector_type: Any | None = None,
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
        """东方财富板块资金流.

        Endpoint: ``api/v1/market/data/eastmoney-sector-flow``.
        Method: ``GET``.
        Documented endpoint: ``get_eastmoney_sector_flow``.

        Args:
            sector_code: 板块代码，如 BK0488 (type: string; required: N).
            sector_type: 板块类型：industry / concept / regional (type: string; required: N).
            trade_date: 交易日 YYYYMMDD；与 start_date/end_date 互斥 (type: string; required: N).
            start_date: 区间起始日 YYYYMMDD；需与 end_date 同时提供 (type: string; required: N).
            end_date: 区间结束日 YYYYMMDD；需与 start_date 同时提供 (type: string; required: N).
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
        request_params = {'sector_code': sector_code, 'sector_type': sector_type, 'trade_date': trade_date, 'start_date': start_date, 'end_date': end_date}
        request_params.update(kwargs)
        path = ENDPOINTS['eastmoney_sector_flow'].path
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

    def eastmoney_stock_flow(
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
        """东方财富个股资金流.

        Endpoint: ``api/v1/market/data/eastmoney-stock-flow``.
        Method: ``GET``.
        Documented endpoint: ``get_eastmoney_stock_flow``.

        Args:
            symbol: 股票代码，如 600522 (type: string; required: N).
            trade_date: 交易日 YYYYMMDD；与 start_date/end_date 互斥 (type: string; required: N).
            start_date: 区间起始日 YYYYMMDD；需与 end_date 同时提供 (type: string; required: N).
            end_date: 区间结束日 YYYYMMDD；需与 start_date 同时提供 (type: string; required: N).
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
        request_params = {'symbol': symbol, 'trade_date': trade_date, 'start_date': start_date, 'end_date': end_date}
        request_params.update(kwargs)
        path = ENDPOINTS['eastmoney_stock_flow'].path
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

    def eastmoney_stock_valuation(
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
        """东方财富个股估值.

        Endpoint: ``api/v1/market/data/eastmoney-stock-valuation``.
        Method: ``GET``.
        Documented endpoint: ``get_eastmoney_stock_valuation``.

        Args:
            symbol: 股票代码，如 000001；不传返回全部 (type: string; required: N).
            trade_date: 交易日 YYYYMMDD；与 start_date/end_date 互斥 (type: string; required: N).
            start_date: 区间起始日 YYYYMMDD；需与 end_date 同时提供 (type: string; required: N).
            end_date: 区间结束日 YYYYMMDD；需与 start_date 同时提供 (type: string; required: N).
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
        request_params = {'symbol': symbol, 'trade_date': trade_date, 'start_date': start_date, 'end_date': end_date}
        request_params.update(kwargs)
        path = ENDPOINTS['eastmoney_stock_valuation'].path
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

    def northbound(
        self,
        date: Any | None = None,
        *,
        raw: bool = False,
        fields: Sequence[str] | str | None = None,
        as_dataframe: bool = True,
        **kwargs: Any,
    ) -> Any:
        """北向资金交易.

        Endpoint: ``api/v1/market/data/northbound``.
        Method: ``GET``.
        Documented endpoint: ``northbound``.

        Args:
            date: 交易日，格式 YYYYMMDD (type: string; required: Y).
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
            'northbound',
            raw=raw,
            fields=fields,
            as_dataframe=as_dataframe,
            **request_params,
        )

    def stk_code_change(
        self,
        trade_code: Any | None = None,
        start_date: Any | None = None,
        end_date: Any | None = None,
        *,
        raw: bool = False,
        fields: Sequence[str] | str | None = None,
        as_dataframe: bool = True,
        **kwargs: Any,
    ) -> Any:
        """A股代码变更.

        Endpoint: ``api/v1/market/data/stk-code-change``.
        Method: ``GET``.
        Documented endpoint: ``get_stk_code_change``.

        Args:
            trade_code: 股票代码，支持逗号分隔多个 (type: string; required: Y).
            start_date: 过滤区间起始日期，YYYYMMDD 格式 (type: string; required: N).
            end_date: 过滤区间结束日期，YYYYMMDD 格式 (type: string; required: N).
            raw: Return the decoded JSON payload without tabular extraction.
            fields: Optional field list or comma-separated field string applied after extraction.
            as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
            **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.
        """
        request_params = {'trade_code': trade_code, 'start_date': start_date, 'end_date': end_date}
        request_params.update(kwargs)
        return self._call_endpoint('stk_code_change', raw=raw, fields=fields, as_dataframe=as_dataframe, **request_params)

    def stk_status_change(
        self,
        trade_code: Any | None = None,
        change_date: Any | None = None,
        change_type: Any | None = None,
        *,
        raw: bool = False,
        fields: Sequence[str] | str | None = None,
        as_dataframe: bool = True,
        **kwargs: Any,
    ) -> Any:
        """A股状态变更.

        Endpoint: ``api/v1/market/data/stk-status-change``.
        Method: ``GET``.
        Documented endpoint: ``get_stk_status_change``.

        Args:
            trade_code: 股票代码，支持逗号分隔多个 (type: string; required: N).
            change_date: 变更日期，YYYYMMDD 格式 (type: string; required: N).
            change_type: 变更类型，如上市、退市、暂停上市 (type: string; required: N).
            raw: Return the decoded JSON payload without tabular extraction.
            fields: Optional field list or comma-separated field string applied after extraction.
            as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
            **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.
        """
        request_params = {'trade_code': trade_code, 'change_date': change_date, 'change_type': change_type}
        request_params.update(kwargs)
        return self._call_endpoint('stk_status_change', raw=raw, fields=fields, as_dataframe=as_dataframe, **request_params)

    def nth_trade_date(
        self,
        n: Any | None = None,
        *,
        raw: bool = False,
        fields: Sequence[str] | str | None = None,
        as_dataframe: bool = True,
        **kwargs: Any,
    ) -> Any:
        """第N个交易日.

        Endpoint: ``api/v1/market/data/time/get-nth-trade-date``.
        Method: ``GET``.
        Documented endpoint: ``get_nth_trade_date``.

        Args:
            n: 需要获取的前 N 个交易日，N >= 1 (type: uint32; required: Y).
            raw: Return the decoded JSON payload without tabular extraction.
            fields: Optional field list or comma-separated field string applied after extraction.
            as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
            **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.
        """
        request_params = {'n': n}
        request_params.update(kwargs)
        return self._call_endpoint('nth_trade_date', raw=raw, fields=fields, as_dataframe=as_dataframe, **request_params)

    def namechange(
        self,
        trade_code: Any | None = None,
        start_date: Any | None = None,
        end_date: Any | None = None,
        *,
        raw: bool = False,
        fields: Sequence[str] | str | None = None,
        as_dataframe: bool = True,
        **kwargs: Any,
    ) -> Any:
        """股票曾用名.

        Endpoint: ``api/v1/market/data/namechange``.
        Method: ``GET``.
        Documented endpoint: ``get_namechange``.

        Args:
            trade_code: 股票代码（带 .SZ/.SH 后缀），支持逗号分隔多个 (type: string; required: Y).
            start_date: 过滤区间起始日期，``YYYYMMDD`` 格式 (type: string; required: N).
            end_date: 过滤区间结束日期，``YYYYMMDD`` 格式；与 ``start_date`` 同时提供时须 ``start_date`` ≤ ``end_date`` (type: string; required: N).
            raw: Return the decoded JSON payload without tabular extraction.
            fields: Optional field list or comma-separated field string applied after extraction.
            as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
            **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

        Returns:
            A pandas ``DataFrame`` by default, Python rows when
            ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
            payloads when multi-page fetching is used with ``raw=True``.
        """
        request_params = {'trade_code': trade_code, 'start_date': start_date, 'end_date': end_date}
        request_params.update(kwargs)
        return self._call_endpoint(
            'namechange',
            raw=raw,
            fields=fields,
            as_dataframe=as_dataframe,
            **request_params,
        )

    def trading_calendar(
        self,
        market: Any | None = None,
        start_date: Any | None = None,
        end_date: Any | None = None,
        *,
        raw: bool = False,
        fields: Sequence[str] | str | None = None,
        as_dataframe: bool = True,
        **kwargs: Any,
    ) -> Any:
        """交易日历.

        Endpoint: ``api/v1/market/data/time/trading-calendar``.
        Method: ``GET``.
        Documented endpoint: ``trading_calendar``.

        Args:
            market: 市场标识 (type: string; required: N).
            start_date: 起始日期 (type: string; required: N).
            end_date: 截止日期 (type: string; required: N).
            raw: Return the decoded JSON payload without tabular extraction.
            fields: Optional field list or comma-separated field string applied after extraction.
            as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
            **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

        Returns:
            A pandas ``DataFrame`` by default, Python rows when
            ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
            payloads when multi-page fetching is used with ``raw=True``.
        """
        request_params = {'market': market, 'start_date': start_date, 'end_date': end_date}
        request_params.update(kwargs)
        return self._call_endpoint(
            'trading_calendar',
            raw=raw,
            fields=fields,
            as_dataframe=as_dataframe,
            **request_params,
        )

    def price_change(
        self,
        stock_code: Any | None = None,
        base_date: Any | None = None,
        n: Any | None = None,
        direction: Any | None = None,
        *,
        raw: bool = False,
        fields: Sequence[str] | str | None = None,
        as_dataframe: bool = True,
        **kwargs: Any,
    ) -> Any:
        """价格变动.

        Endpoint: ``api/v1/market/data/price/get-price-change``.
        Method: ``GET``.
        Documented endpoint: ``get_price_change``.

        Args:
            stock_code: 目标股票 6 位纯数字代码，兼容沪市/深市/创业板/科创板 (type: string; required: Y).
            base_date: 涨跌幅计算基准日，格式 YYYYMMDD (type: string; required: Y).
            n: 需计算的有效交易日数量，建议不超过 365 (type: uint32; required: Y).
            direction: 计算方向：forward（基准日为结束日）/ backward（基准日为开始日） (type: string; required: Y).
            raw: Return the decoded JSON payload without tabular extraction.
            fields: Optional field list or comma-separated field string applied after extraction.
            as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
            **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

        Returns:
            A pandas ``DataFrame`` by default, Python rows when
            ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
            payloads when multi-page fetching is used with ``raw=True``.
        """
        request_params = {'stock_code': stock_code, 'base_date': base_date, 'n': n, 'direction': direction}
        request_params.update(kwargs)
        return self._call_endpoint(
            'price_change',
            raw=raw,
            fields=fields,
            as_dataframe=as_dataframe,
            **request_params,
        )

    def search(
        self,
        query: Any | None = None,
        limit: Any | None = None,
        *,
        raw: bool = False,
        fields: Sequence[str] | str | None = None,
        as_dataframe: bool = True,
        **kwargs: Any,
    ) -> Any:
        """标的搜索.

        Endpoint: ``api/v1/market/security/search/``.
        Method: ``GET``.
        Documented endpoint: ``search``.

        Args:
            query: 搜索关键词；支持名称、标的代码、拼音全拼/首字母；大小写不敏感，自动 trim (type: string; required: Y).
            limit: 返回最大条数，默认 1 (type: int; required: N).
            raw: Return the decoded JSON payload without tabular extraction.
            fields: Optional field list or comma-separated field string applied after extraction.
            as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
            **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

        Returns:
            A pandas ``DataFrame`` by default, Python rows when
            ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
            payloads when multi-page fetching is used with ``raw=True``.
        """
        request_params = {'q': query, 'limit': limit}
        request_params.update(kwargs)
        return self._call_endpoint(
            'search',
            raw=raw,
            fields=fields,
            as_dataframe=as_dataframe,
            **request_params,
        )

    def southbound(
        self,
        date: Any | None = None,
        *,
        raw: bool = False,
        fields: Sequence[str] | str | None = None,
        as_dataframe: bool = True,
        **kwargs: Any,
    ) -> Any:
        """南向资金交易.

        Endpoint: ``api/v1/market/data/southbound``.
        Method: ``GET``.
        Documented endpoint: ``southbound``.

        Args:
            date: 交易日，格式 YYYYMMDD (type: string; required: Y).
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
            'southbound',
            raw=raw,
            fields=fields,
            as_dataframe=as_dataframe,
            **request_params,
        )

    def suspension_list(
        self,
        trade_date: Any | None = None,
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
        """停牌列表.

        Endpoint: ``api/v1/market/data/suspension-list``.
        Method: ``GET``.
        Documented endpoint: ``suspension_list``.

        Args:
            trade_date: 交易日，格式 YYYYMMDD，默认当天 (type: string; required: N).
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
        request_params = {'trade_date': trade_date}
        request_params.update(kwargs)
        path = ENDPOINTS['suspension_list'].path
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

    def ths_board_kline(
        self,
        board_code: Any | None = None,
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
        """同花顺板块K线.

        Endpoint: ``api/v1/market/data/ths-board-kline``.
        Method: ``GET``.
        Documented endpoint: ``ths_board_kline``.

        Args:
            board_code: 板块代码，如 886056 (type: string; required: Y).
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
        request_params = {'board_code': board_code}
        request_params.update(kwargs)
        path = ENDPOINTS['ths_board_kline'].path
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

    def xueqiu_rank(
        self,
        rank_group: Any | None = None,
        period: Any | None = None,
        trade_date: Any | None = None,
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
        """雪球股票排名.

        Endpoint: ``api/v1/market/data/xueqiu-rank``.
        Method: ``GET``.
        Documented endpoint: ``xueqiu_rank``.

        Args:
            rank_group: 榜单组：`follow`（关注）/ `tweet`（讨论）/ `deal`（交易） (type: string; required: N).
            period: 周期：`7d`（本周新增）/ `total`（最热门） (type: string; required: N).
            trade_date: 交易日期，格式 `YYYY-MM-DD`，不传默认取最新 (type: string; required: N).
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
        request_params = {'rank_group': rank_group, 'period': period, 'trade_date': trade_date}
        request_params.update(kwargs)
        path = ENDPOINTS['xueqiu_rank'].path
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

    def yzxdr_detail(
        self,
        year: Any | None = None,
        quarter: Any | None = None,
        stock_code: Any | None = None,
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
        """一致行动人明细.

        Endpoint: ``api/v1/market/data/yzxdr-detail``.
        Method: ``GET``.
        Documented endpoint: ``get_yzxdr_detail``.

        Args:
            year: 年份（如 2026） (type: uint32; required: Y).
            quarter: 季度，1-4 (type: uint32; required: Y).
            stock_code: 股票代码，6 位数字 (type: string; required: N).
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
        request_params = {'year': year, 'quarter': quarter, 'stock_code': stock_code}
        request_params.update(kwargs)
        path = ENDPOINTS['yzxdr_detail'].path
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

    def pledge_summary(
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
        """股权质押汇总.

        Endpoint: ``api/v1/market/data/pledge/pledge-summary``.
        Method: ``GET``.
        Documented endpoint: ``stock_pledge_summary``.

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
        path = ENDPOINTS['pledge_summary'].path
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

    def stock_pledge_detail(
        self,
        stock_code: Any | None = None,
        is_last: Any | None = None,
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
        """股权质押明细.

        Endpoint: ``api/v1/market/data/pledge/pledge-detail``.
        Method: ``GET``.
        Documented endpoint: ``stock_pledge_detail``.

        Args:
            stock_code: 股票代码（symbol.suffix 格式或纯代码）；不传时需配合 `is_last=true` (type: string; required: N).
            is_last: 是否仅获取最新一期（无 `stock_code` 时必填为 true） (type: bool; required: N).
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
        request_params = {'stock_code': stock_code, 'is_last': is_last}
        request_params.update(kwargs)
        path = ENDPOINTS['stock_pledge_detail'].path
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

    def abnormal_trading_details(
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
        """龙虎榜明细.

        Endpoint: ``api/v1/market/data/abnormal-trading-details``.
        Method: ``GET``.
        Documented endpoint: ``abnormal_trading_details``.

        Args:
            date: 查询日期 YYYYMMDD；不传则使用当前内存快照 (type: string; required: N).
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
        path = ENDPOINTS['abnormal_trading_details'].path
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

    def abnormal_trading_overview(
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
        """龙虎榜总览.

        Endpoint: ``api/v1/market/data/abnormal-trading-overview``.
        Method: ``GET``.
        Documented endpoint: ``abnormal_trading_overview``.

        Args:
            date: 查询日期 YYYYMMDD；不传则使用当前内存快照 (type: string; required: N).
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
        path = ENDPOINTS['abnormal_trading_overview'].path
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

    def block_trades(
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
        """大宗交易.

        Endpoint: ``api/v1/market/data/block-trades``.
        Method: ``GET``.
        Documented endpoint: ``block_trades``.

        Args:
            date: 查询日期 YYYYMMDD；不传则使用当前内存快照 (type: string; required: N).
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
        path = ENDPOINTS['block_trades'].path
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

    def limit_event_timeline_3s(
        self,
        symbol: Any | None = None,
        trade_date: Any | None = None,
        *,
        raw: bool = False,
        fields: Sequence[str] | str | None = None,
        as_dataframe: bool = True,
        **kwargs: Any,
    ) -> Any:
        """涨跌停事件时间线.

        Endpoint: ``api/v1/market/data/limit-event-timeline-3s``.
        Method: ``GET``.
        Documented endpoint: ``limit_event_timeline_3s``.

        Args:
            symbol: 标的代码，如 000001.XSHE；不传返回全市场 (type: string; required: N).
            trade_date: 交易日期，格式 YYYYMMDD；不传或传当日时查询实时数据 (type: string; required: N).
            raw: Return the decoded JSON payload without tabular extraction.
            fields: Optional field list or comma-separated field string applied after extraction.
            as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
            **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

        Returns:
            A pandas ``DataFrame`` by default, Python rows when
            ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
            payloads when multi-page fetching is used with ``raw=True``.
        """
        request_params = {'symbol': symbol, 'trade_date': trade_date}
        request_params.update(kwargs)
        return self._call_endpoint(
            'limit_event_timeline_3s',
            raw=raw,
            fields=fields,
            as_dataframe=as_dataframe,
            **request_params,
        )

    def margin_trading_details(
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
        """融资融券明细.

        Endpoint: ``api/v1/market/data/margin-trading-details``.
        Method: ``GET``.
        Documented endpoint: ``margin_trading_details``.

        Args:
            date: 查询日期 YYYYMMDD；不传则使用当前内存快照 (type: string; required: N).
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
        path = ENDPOINTS['margin_trading_details'].path
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

    def risk_warning_stocks(
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
        """风险警示股.

        Endpoint: ``api/v1/market/data/risk-warning-stocks``.
        Method: ``GET``.
        Documented endpoint: ``risk_warning_stocks``.

        Args:
            date: 交易日，格式 YYYYMMDD (type: string; required: Y).
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
        path = ENDPOINTS['risk_warning_stocks'].path
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

    def stk_limit(
        self,
        instrument_type: Any | None = None,
        symbol: Any | None = None,
        symbol_id: Any | None = None,
        market_id: Any | None = None,
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
        """涨跌停价.

        Endpoint: ``api/v1/market/data/stk-limit``.
        Method: ``GET``.
        Documented endpoint: ``stk_limit``.

        Args:
            instrument_type: 标的类型：stock / etf / cb；不传返回三类（排除指数） (type: string; required: N).
            symbol: 标的代码，支持 000001.SZ / 000001.XSHE / 600519.SH 等；存在时忽略 symbol_id+market_id (type: string; required: N).
            symbol_id: 标的 ID，与 market_id 配合使用 (type: int32; required: N).
            market_id: 市场 ID，与 symbol_id 配合使用 (type: int16; required: N).
            trade_date: 交易日 YYYYMMDD，查单日全市场时使用 (type: int32; required: N).
            start_date: 单票历史区间起始日 YYYYMMDD（需配 symbol 或 symbol_id+market_id） (type: int32; required: N).
            end_date: 单票历史区间结束日 YYYYMMDD (type: int32; required: N).
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
        request_params = {'instrument_type': instrument_type, 'symbol': symbol, 'symbol_id': symbol_id, 'market_id': market_id, 'trade_date': trade_date, 'start_date': start_date, 'end_date': end_date}
        request_params.update(kwargs)
        path = ENDPOINTS['stk_limit'].path
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

    def stk_manager_hold(
        self,
        trade_code: Any | None = None,
        end_date: Any | None = None,
        *,
        raw: bool = False,
        fields: Sequence[str] | str | None = None,
        as_dataframe: bool = True,
        **kwargs: Any,
    ) -> Any:
        """上市公司管理层持股.

        Endpoint: ``api/v1/market/data/stk-manager-hold``.
        Method: ``GET``.
        Documented endpoint: ``get_stk_manager_hold``.

        Args:
            trade_code: 股票代码（带 .SZ/.SH 后缀），支持逗号分隔多个 (type: string; required: Y).
            end_date: 截止日期，精确匹配，``YYYYMMDD`` 格式 (type: string; required: N).
            raw: Return the decoded JSON payload without tabular extraction.
            fields: Optional field list or comma-separated field string applied after extraction.
            as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
            **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

        Returns:
            A pandas ``DataFrame`` by default, Python rows when
            ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
            payloads when multi-page fetching is used with ``raw=True``.
        """
        request_params = {'trade_code': trade_code, 'end_date': end_date}
        request_params.update(kwargs)
        return self._call_endpoint(
            'stk_manager_hold',
            raw=raw,
            fields=fields,
            as_dataframe=as_dataframe,
            **request_params,
        )

    def stk_manager_pay(
        self,
        trade_code: Any | None = None,
        end_date: Any | None = None,
        *,
        raw: bool = False,
        fields: Sequence[str] | str | None = None,
        as_dataframe: bool = True,
        **kwargs: Any,
    ) -> Any:
        """上市公司管理层薪酬.

        Endpoint: ``api/v1/market/data/stk-manager-pay``.
        Method: ``GET``.
        Documented endpoint: ``get_stk_manager_pay``.

        Args:
            trade_code: 股票代码（带 .SZ/.SH 后缀），支持逗号分隔多个 (type: string; required: Y).
            end_date: 截止日期，精确匹配，``YYYYMMDD`` 格式 (type: string; required: N).
            raw: Return the decoded JSON payload without tabular extraction.
            fields: Optional field list or comma-separated field string applied after extraction.
            as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
            **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

        Returns:
            A pandas ``DataFrame`` by default, Python rows when
            ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
            payloads when multi-page fetching is used with ``raw=True``.
        """
        request_params = {'trade_code': trade_code, 'end_date': end_date}
        request_params.update(kwargs)
        return self._call_endpoint(
            'stk_manager_pay',
            raw=raw,
            fields=fields,
            as_dataframe=as_dataframe,
            **request_params,
        )

    def stk_managers(
        self,
        trade_code: Any | None = None,
        candi_date: Any | None = None,
        begin_date: Any | None = None,
        end_date: Any | None = None,
        *,
        raw: bool = False,
        fields: Sequence[str] | str | None = None,
        as_dataframe: bool = True,
        **kwargs: Any,
    ) -> Any:
        """上市公司管理层.

        Endpoint: ``api/v1/market/data/stk-managers``.
        Method: ``GET``.
        Documented endpoint: ``get_stk_managers``.

        Args:
            trade_code: 股票代码（带 .SZ/.SH 后缀），支持逗号分隔多个 (type: string; required: Y).
            candi_date: 候选日期，精确匹配，``YYYYMMDD`` 格式 (type: string; required: N).
            begin_date: 任职起始日过滤，``YYYYMMDD`` 格式 (type: string; required: N).
            end_date: 任职截止日过滤，``YYYYMMDD`` 格式；与 ``begin_date`` 同时提供时须 ``begin_date`` ≤ ``end_date`` (type: string; required: N).
            raw: Return the decoded JSON payload without tabular extraction.
            fields: Optional field list or comma-separated field string applied after extraction.
            as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
            **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

        Returns:
            A pandas ``DataFrame`` by default, Python rows when
            ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
            payloads when multi-page fetching is used with ``raw=True``.
        """
        request_params = {'trade_code': trade_code, 'candi_date': candi_date, 'begin_date': begin_date, 'end_date': end_date}
        request_params.update(kwargs)
        return self._call_endpoint(
            'stk_managers',
            raw=raw,
            fields=fields,
            as_dataframe=as_dataframe,
            **request_params,
        )

    def stk_premarket(
        self,
        ts_code: Any | None = None,
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
        """盘前数据.

        Endpoint: ``api/v1/market/data/stk-premarket``.
        Method: ``GET``.
        Documented endpoint: ``stk_premarket``.

        Args:
            ts_code: 股票代码，如 000001.SZ / 600519.SH (type: string; required: N).
            trade_date: 交易日 YYYYMMDD，查单日全市场时使用 (type: int32; required: N).
            start_date: 单票历史区间起始日 YYYYMMDD（需配 ts_code） (type: int32; required: N).
            end_date: 单票历史区间结束日 YYYYMMDD (type: int32; required: N).
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
        request_params = {'ts_code': ts_code, 'trade_date': trade_date, 'start_date': start_date, 'end_date': end_date}
        request_params.update(kwargs)
        path = ENDPOINTS['stk_premarket'].path
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

    def stock_adjust_factor(
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
        """股票复权因子.

        Endpoint: ``api/v1/market/data/stock-adjust-factor``.
        Method: ``GET``.
        Documented endpoint: ``stock_adjust_factor``.

        Args:
            symbol: 股票代码，支持纯数字或带后缀格式；区间扫描必填 (type: string; required: N).
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
            'stock_adjust_factor',
            raw=raw,
            fields=fields,
            as_dataframe=as_dataframe,
            **request_params,
        )

    def stock_candlesticks(
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
        """股票K线.

        Endpoint: ``api/v1/market/data/stock-candlesticks``.
        Method: ``GET``.
        Documented endpoint: ``stock_candlesticks``.

        Args:
            symbol: 标的代码，如 000001.SZ、600519.XSHG；长短市场后缀均支持 (type: SymbolKey; required: Y).
            interval_unit: 周期单位：Minute/Day/Week/Month/Year (type: enum; required: Y).
            interval_value: 间隔数值（默认 1，如 Day+1=日 K，Minute+5=5 分钟） (type: int; required: N).
            adjust_kind: 复权：None（默认，除权）/Forward（前复权）/Backward（后复权） (type: enum; required: N).
            since_ts_millis: 开始时间戳，单位毫秒；分钟 K 线与 until 跨度 ≤3 天 (type: DateTime(ms); required: N).
            until_ts_millis: 结束时间戳，单位毫秒 (type: DateTime(ms); required: Y).
            limit: 返回条数上限；未传 since 和 limit 时默认 50 (type: int; required: N).
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
            'stock_candlesticks',
            raw=raw,
            fields=fields,
            as_dataframe=as_dataframe,
            **request_params,
        )

    def stock_capital_flows(
        self,
        date: Any | None = None,
        time: Any | None = None,
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
        """股票资金流向.

        Endpoint: ``api/v1/market/data/stock-capital-flows``.
        Method: ``GET``.
        Documented endpoint: ``stock_capital_flows_paginated``.

        Args:
            date: 查询日期 YYYYMMDD；传入时查询该日 15:30 快照 (type: string; required: N).
            time: 15 分钟切片，格式 HHMM；必须与 date 同时使用 (type: string; required: N).
            symbol: 精确股票代码，例如 600000.SH、000001.SZ、830001.BJ (type: string; required: N).
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
        request_params = {'date': date, 'time': time, 'symbol': symbol}
        request_params.update(kwargs)
        path = ENDPOINTS['stock_capital_flows'].path
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

    def stock_comment_desire_em(
        self,
        symbol: Any | None = None,
        *,
        raw: bool = False,
        fields: Sequence[str] | str | None = None,
        as_dataframe: bool = True,
        **kwargs: Any,
    ) -> Any:
        """千股千评意愿度.

        Endpoint: ``api/v1/market/data/stock-comment/desire``.
        Method: ``GET``.
        Documented endpoint: ``stock_comment_desire_em``.

        Args:
            symbol: 证券代码（纯数字，如 600000） (type: string; required: Y).
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
            'stock_comment_desire_em',
            raw=raw,
            fields=fields,
            as_dataframe=as_dataframe,
            **request_params,
        )

    def stock_comment_em(
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
        """千股千评.

        Endpoint: ``api/v1/market/data/stock-comment/index``.
        Method: ``GET``.
        Documented endpoint: ``stock_comment_em``.

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
        path = ENDPOINTS['stock_comment_em'].path
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

    def stock_comment_focus_em(
        self,
        symbol: Any | None = None,
        *,
        raw: bool = False,
        fields: Sequence[str] | str | None = None,
        as_dataframe: bool = True,
        **kwargs: Any,
    ) -> Any:
        """千股千评关注度.

        Endpoint: ``api/v1/market/data/stock-comment/focus``.
        Method: ``GET``.
        Documented endpoint: ``stock_comment_focus_em``.

        Args:
            symbol: 证券代码（纯数字，如 600000） (type: string; required: Y).
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
            'stock_comment_focus_em',
            raw=raw,
            fields=fields,
            as_dataframe=as_dataframe,
            **request_params,
        )

    def stock_comment_org_participate_em(
        self,
        symbol: Any | None = None,
        *,
        raw: bool = False,
        fields: Sequence[str] | str | None = None,
        as_dataframe: bool = True,
        **kwargs: Any,
    ) -> Any:
        """机构参与度.

        Endpoint: ``api/v1/market/data/stock-comment/org-participate``.
        Method: ``GET``.
        Documented endpoint: ``stock_comment_org_participate_em``.

        Args:
            symbol: 证券代码（纯数字，如 600000） (type: string; required: Y).
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
            'stock_comment_org_participate_em',
            raw=raw,
            fields=fields,
            as_dataframe=as_dataframe,
            **request_params,
        )

    def stock_comment_score_em(
        self,
        symbol: Any | None = None,
        *,
        raw: bool = False,
        fields: Sequence[str] | str | None = None,
        as_dataframe: bool = True,
        **kwargs: Any,
    ) -> Any:
        """千股千评评分.

        Endpoint: ``api/v1/market/data/stock-comment/score``.
        Method: ``GET``.
        Documented endpoint: ``stock_comment_score_em``.

        Args:
            symbol: 证券代码（纯数字，如 600000） (type: string; required: Y).
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
            'stock_comment_score_em',
            raw=raw,
            fields=fields,
            as_dataframe=as_dataframe,
            **request_params,
        )

    def stock_filter(
        self,
        symbol: Any | None = None,
        board: Any | None = None,
        listing_date_since: Any | None = None,
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
        """股票筛选.

        Endpoint: ``api/v1/market/data/stock-list/filter``.
        Method: ``GET``.
        Documented endpoint: ``get_stock_filter``.

        Args:
            symbol: 单标的代码（如 `600519`、`600519.SH`、`600519.XSHG`）；传入后忽略 board 与 listing_date_since (type: string; required: N).
            board: 板块/交易所筛选：`star` / `chi_next` / `bjse` / `xshg` / `xshe` / `main` (type: string; required: N).
            listing_date_since: 上市日期起点 YYYYMMDD，筛选此后上市的股票 (type: string; required: N).
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
        request_params = {'symbol': symbol, 'board': board, 'listing_date_since': listing_date_since}
        request_params.update(kwargs)
        path = ENDPOINTS['stock_filter'].path
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

    def stock_institution_holdings(
        self,
        year: Any | None = None,
        report_type: Any | None = None,
        inst_type: Any | None = None,
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
        """机构持股.

        Endpoint: ``api/v2/market/data/share/stock-institution-holdings``.
        Method: ``GET``.
        Documented endpoint: ``get_stock_institution_holdings``.

        Args:
            year: 年份 (type: int; required: Y).
            report_type: 报告类型：q1 / q2 / q3 / annual / announcement (type: ReportType; required: Y).
            inst_type: 机构类型：all_inst / fund / qfii / insurance / social_security / securities / trust / other (type: InstitutionType; required: Y).
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
        request_params = {'year': year, 'report_type': report_type, 'institution_type': inst_type}
        request_params.update(kwargs)
        path = ENDPOINTS['stock_institution_holdings'].path
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

    def stock_institution_holdings_detail(
        self,
        stock_code: Any | None = None,
        year: Any | None = None,
        report_type: Any | None = None,
        inst_type: Any | None = None,
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
        """机构持股明细.

        Endpoint: ``api/v2/market/data/share/stock-institution-holdings-detail``.
        Method: ``GET``.
        Documented endpoint: ``get_stock_institution_holdings_detail``.

        Args:
            stock_code: 股票代码 (type: string; required: Y).
            year: 年份 (type: int; required: Y).
            report_type: 报告类型：q1 / q2 / q3 / annual / announcement (type: ReportType; required: Y).
            inst_type: 机构类型：all_inst / fund / qfii / insurance / social_security / securities / trust / other (type: InstitutionType; required: Y).
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
        request_params = {'stock_code': stock_code, 'year': year, 'report_type': report_type, 'institution_type': inst_type}
        request_params.update(kwargs)
        path = ENDPOINTS['stock_institution_holdings_detail'].path
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

    def stock_institution_share_holdings(
        self,
        institution_id: Any | None = None,
        year: Any | None = None,
        report_type: Any | None = None,
        invest_type: Any | None = None,
        *,
        raw: bool = False,
        fields: Sequence[str] | str | None = None,
        as_dataframe: bool = True,
        **kwargs: Any,
    ) -> Any:
        """机构股本持股.

        Endpoint: ``api/v2/market/data/institution/institution-share-holdings``.
        Method: ``GET``.
        Documented endpoint: ``get_stock_institution_share_holdings``.

        Args:
            institution_id: 机构 ID (type: string; required: Y).
            year: 年份 (type: int; required: Y).
            report_type: 报告类型：q1 / q2 / q3 / annual / announcement (type: ReportType; required: Y).
            invest_type: 持仓类型：all / stock / fund / bond / other (type: InvestType; required: Y).
            raw: Return the decoded JSON payload without tabular extraction.
            fields: Optional field list or comma-separated field string applied after extraction.
            as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
            **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

        Returns:
            A pandas ``DataFrame`` by default, Python rows when
            ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
            payloads when multi-page fetching is used with ``raw=True``.
        """
        request_params = {'institution_id': institution_id, 'year': year, 'report_type': report_type, 'invest_type': invest_type}
        request_params.update(kwargs)
        return self._call_endpoint(
            'stock_institution_share_holdings',
            raw=raw,
            fields=fields,
            as_dataframe=as_dataframe,
            **request_params,
        )

    def stock_intraday_auction_volume(
        self,
        trade_date: Any | None = None,
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
        """集合竞价成交量.

        Endpoint: ``api/v1/market/data/intraday-auction-volume``.
        Method: ``GET``.
        Documented endpoint: ``stock_intraday_auction_volume``.

        Args:
            trade_date: 交易日期 YYYYMMDD；不传返回当日实时数据 (type: string; required: N).
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
        request_params = {'trade_date': trade_date}
        request_params.update(kwargs)
        path = ENDPOINTS['stock_intraday_auction_volume'].path
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

    def stock_ipos(
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
        """股票IPO.

        Endpoint: ``api/v1/market/data/stock-ipos``.
        Method: ``GET``.
        Documented endpoint: ``stock_ipos``.

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
        path = ENDPOINTS['stock_ipos'].path
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

    def stock_list(
        self,
        page: int | None = None,
        page_size: int | None = None,
        *,
        raw: bool = False,
        fields: Sequence[str] | str | None = None,
        as_dataframe: bool = True,
        **kwargs: Any,
    ) -> Any:
        """股票列表.

        Endpoint: ``api/v1/market/data/stock-list``.
        Method: ``GET``.
        Documented endpoint: ``get_stock_list``.

        Args:
            page: Page number, starting from 1.
            page_size: Rows per page, up to the endpoint-specific maximum.
            raw: Return the decoded JSON payload without tabular extraction.
            fields: Optional field list or comma-separated field string applied after extraction.
            as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
            **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.
        """
        request_params = {'page': page, 'page_size': page_size}
        request_params.update(kwargs)
        return self._call_endpoint(
            'stock_list',
            raw=raw,
            fields=fields,
            as_dataframe=as_dataframe,
            **request_params,
        )

    def stock_daec_stocks(
        self,
        board: Any | None = None,
        page: int | None = None,
        page_size: int | None = None,
        limit: int | None = None,
        all_pages: bool = False,
        max_pages: int | None = None,
        filter: Any | None = None,
        order_by: Any | None = None,
        *,
        raw: bool = False,
        fields: Sequence[str] | str | None = None,
        as_dataframe: bool = True,
        **kwargs: Any,
    ) -> Any:
        """A股行情列表（DAEC 全字段族）.

        Endpoint: ``api/v1/market/data/daec/stocks/{board}``.
        Method: ``GET``.
        Documented endpoint: ``stock_daec_stocks``.

        Args:
            board: 板块路径参数，如 all / xshg / xshe / bjse (type: string; required: Y).
            page: Page number, starting from 1. If omitted, the server default is used unless ``limit`` or ``all_pages`` is set.
            page_size: Rows per page. The SDK validates this against the endpoint-specific maximum.
            limit: Maximum number of rows to return. The SDK may fetch multiple pages to satisfy this limit.
            all_pages: Fetch and combine pages until the server reports the last page.
            max_pages: Optional safety cap for ``all_pages``.
            filter: 筛选表达式，如 ``close > 10`` 或 ``name.contains("银行")`` (type: string; required: N).
            order_by: 排序表达式，如 ``change_rate desc`` (type: string; required: N).
            raw: Return the decoded JSON payload without tabular extraction.
            fields: Optional field list or comma-separated field string applied after extraction.
            as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
            **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

        Returns:
            A pandas ``DataFrame`` by default, Python rows when
            ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
            payloads when multi-page fetching is used with ``raw=True``.
        """
        request_params = {'filter': filter, 'order_by': order_by}
        request_params.update(kwargs)
        path = self._format_path(ENDPOINTS['stock_daec_stocks'].path, {'board': board})
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

    def stock_realtime_list(
        self,
        board: Any | None = None,
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
        """A股行情列表（stock-list 实时行情族）.

        Endpoint: ``api/v1/market/data/stock-list/{board}``.
        Method: ``GET``.
        Documented endpoint: ``stock_realtime_list``.

        Args:
            board: 板块路径参数，如 chi-next / star / new (type: string; required: Y).
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
        path = self._format_path(ENDPOINTS['stock_realtime_list'].path, {'board': board})
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

    def stock_market(
        self,
        scope: Any | None = None,
        *,
        raw: bool = False,
        fields: Sequence[str] | str | None = None,
        as_dataframe: bool = True,
        **kwargs: Any,
    ) -> Any:
        """股票市场行情.

        Endpoint: ``api/v1/market/data/daec/market/snapshot``.
        Method: ``GET``.
        Documented endpoint: ``stock_market``.

        Args:
            scope: 市场范围：ChinaStock(默认) / Xshg / Xshe / Bjse (type: string; required: N).
            raw: Return the decoded JSON payload without tabular extraction.
            fields: Optional field list or comma-separated field string applied after extraction.
            as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
            **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

        Returns:
            A pandas ``DataFrame`` by default, Python rows when
            ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
            payloads when multi-page fetching is used with ``raw=True``.
        """
        request_params = {'scope': scope}
        request_params.update(kwargs)
        return self._call_endpoint(
            'stock_market',
            raw=raw,
            fields=fields,
            as_dataframe=as_dataframe,
            **request_params,
        )

    def stock_market_distribution_intraday(
        self,
        *,
        raw: bool = False,
        fields: Sequence[str] | str | None = None,
        as_dataframe: bool = True,
        **kwargs: Any,
    ) -> Any:
        """市场涨跌分布分时.

        Endpoint: ``api/v2/market/data/market-distribution-intraday``.
        Method: ``GET``.
        Documented endpoint: ``stock_market_distribution_intraday``.

        Args:
            raw: Return the decoded JSON payload without tabular extraction.
            fields: Optional field list or comma-separated field string applied after extraction.
            as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
            **kwargs: Extra request parameters forwarded unchanged.

        Returns:
            A pandas ``DataFrame`` by default, Python rows when ``as_dataframe=False``, or raw JSON when ``raw=True``.
        """
        request_params = dict(kwargs)
        return self._call_endpoint(
            'stock_market_distribution_intraday',
            raw=raw,
            fields=fields,
            as_dataframe=as_dataframe,
            **request_params,
        )

    def stock_prev_close(
        self,
        symbol: Any | None = None,
        since: Any | None = None,
        until: Any | None = None,
        *,
        raw: bool = False,
        fields: Sequence[str] | str | None = None,
        as_dataframe: bool = True,
        **kwargs: Any,
    ) -> Any:
        """股票前收盘价.

        Endpoint: ``api/v1/market/data/daec/history/prev-closes``.
        Method: ``GET``.
        Documented endpoint: ``stock_prev_close``.

        Args:
            symbol: 标的代码 (type: SymbolKey; required: Y).
            since: 开始日期，格式 YYYYMMDD (type: date; required: Y).
            until: 结束日期，格式 YYYYMMDD (type: date; required: Y).
            raw: Return the decoded JSON payload without tabular extraction.
            fields: Optional field list or comma-separated field string applied after extraction.
            as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
            **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

        Returns:
            A pandas ``DataFrame`` by default, Python rows when
            ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
            payloads when multi-page fetching is used with ``raw=True``.
        """
        request_params = {'symbol': symbol, 'since': since, 'until': until}
        request_params.update(kwargs)
        return self._call_endpoint(
            'stock_prev_close',
            raw=raw,
            fields=fields,
            as_dataframe=as_dataframe,
            **request_params,
        )

    def stock_intraday_prices(
        self,
        symbol: Any | None = None,
        range: Any | None = None,
        days: Any | None = None,
        ts_ms: Any | None = None,
        *,
        raw: bool = False,
        fields: Sequence[str] | str | None = None,
        as_dataframe: bool = True,
        **kwargs: Any,
    ) -> Any:
        """标的分时数据.

        Endpoint: ``api/v4/market/data/daec/history/prices``.
        Method: ``GET``.
        Documented endpoint: ``daec_history_prices``.

        Args:
            symbol: 标的代码，如 600000.XSHG (type: string; required: Y).
            range: 预置时间区间：Today / FiveDays (type: string; required: N).
            days: 近 N 个交易日至今 (type: uint32; required: N).
            ts_ms: 起始毫秒时间戳 (type: int64; required: N).
            raw: Return the decoded JSON payload without tabular extraction.
            fields: Optional field list or comma-separated field string applied after extraction.
            as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
            **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

        Returns:
            A pandas ``DataFrame`` by default, Python rows when
            ``as_dataframe=False``, or raw JSON when ``raw=True``.
        """
        request_params = {'symbol': symbol}
        if ts_ms is not None:
            request_params['ts_ms'] = ts_ms
        elif days is not None:
            request_params['days'] = days
        elif range is not None:
            request_params['range'] = range
        request_params.update(kwargs)
        return self._call_endpoint(
            'stock_intraday_prices',
            raw=raw,
            fields=fields,
            as_dataframe=as_dataframe,
            **request_params,
        )

    def stock_share(
        self,
        stock_code: Any | None = None,
        date: Any | None = None,
        *,
        raw: bool = False,
        fields: Sequence[str] | str | None = None,
        as_dataframe: bool = True,
        **kwargs: Any,
    ) -> Any:
        """股本.

        Endpoint: ``api/v1/market/data/share/get-stock-share``.
        Method: ``GET``.
        Documented endpoint: ``get_stock_share``.

        Args:
            stock_code: 股票代码 (type: string; required: Y).
            date: 日期 YYYYMMDD (type: string; required: Y).
            raw: Return the decoded JSON payload without tabular extraction.
            fields: Optional field list or comma-separated field string applied after extraction.
            as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
            **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

        Returns:
            A pandas ``DataFrame`` by default, Python rows when
            ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
            payloads when multi-page fetching is used with ``raw=True``.
        """
        request_params = {'stock_code': stock_code, 'date': date}
        request_params.update(kwargs)
        return self._call_endpoint(
            'stock_share',
            raw=raw,
            fields=fields,
            as_dataframe=as_dataframe,
            **request_params,
        )

    def stock_unlock(
        self,
        stock_code: Any | None = None,
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
        """限售解禁.

        Endpoint: ``api/v1/market/data/unlock/stock-unlock``.
        Method: ``GET``.
        Documented endpoint: ``stock_unlock_handler``.

        Args:
            stock_code: 证券代码 (type: string; required: Y).
            start_date: 解禁日期起始值 (type: string; required: N).
            end_date: 解禁日期结束值 (type: string; required: N).
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
        request_params = {'stock_code': stock_code, 'start_date': start_date, 'end_date': end_date}
        request_params.update(kwargs)
        path = ENDPOINTS['stock_unlock'].path
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
    def stock_description(
        self,
        symbol_id: Any | None = None,
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
        """股票基础信息.

        Endpoint: ``api/v1/market/data/stock-description``.
        Method: ``GET``.
        Documented endpoint: ``stock_description``.
        """
        params = {'symbol_id': symbol_id}
        params.update(kwargs)
        return self.get_paginated(
            ENDPOINTS['stock_description'].path,
            page=page,
            page_size=page_size,
            limit=limit,
            all_pages=all_pages,
            max_pages=max_pages,
            max_page_size=ENDPOINTS['stock_description'].max_page_size,
            raw=raw,
            fields=fields,
            as_dataframe=as_dataframe,
            **params,
        )


    def tdx_board_index(self, ts_code: Any | None = None, idx_name: Any | None = None, idx_type: Any | None = None, idx_type_code: Any | None = None, market: Any | None = None, page: int | None = None, page_size: int | None = None, *, raw: bool = False, fields: Sequence[str] | str | None = None, as_dataframe: bool = True, **kwargs: Any) -> Any:
        """通达信板块指数最新快照."""
        params = {'ts_code': ts_code, 'idx_name': idx_name, 'idx_type': idx_type, 'idx_type_code': idx_type_code, 'market': market, 'page': page, 'page_size': page_size}
        params.update(kwargs)
        return self._call_endpoint('tdx_board_index', raw=raw, fields=fields, as_dataframe=as_dataframe, **params)


    def tdx_board_daily(self, start_date: Any | None = None, end_date: Any | None = None, ts_code: Any | None = None, idx_name: Any | None = None, idx_type: Any | None = None, idx_type_code: Any | None = None, market: Any | None = None, page: int | None = None, page_size: int | None = None, *, raw: bool = False, fields: Sequence[str] | str | None = None, as_dataframe: bool = True, **kwargs: Any) -> Any:
        """通达信板块日线."""
        params = {'start_date': start_date, 'end_date': end_date, 'ts_code': ts_code, 'idx_name': idx_name, 'idx_type': idx_type, 'idx_type_code': idx_type_code, 'market': market, 'page': page, 'page_size': page_size}
        params.update(kwargs)
        return self._call_endpoint('tdx_board_daily', raw=raw, fields=fields, as_dataframe=as_dataframe, **params)


    def tdx_board_members(self, ts_code: Any | None = None, idx_name: Any | None = None, idx_type: Any | None = None, idx_type_code: Any | None = None, market: Any | None = None, con_code: Any | None = None, con_name: Any | None = None, page: Any | None = None, page_size: Any | None = None, limit: int | None = None, all_pages: bool = False, max_pages: int | None = None, *, raw: bool = False, fields: Sequence[str] | str | None = None, as_dataframe: bool = True, **kwargs: Any) -> Any:
        """通达信板块成分股最新快照."""
        params = {'ts_code': ts_code, 'idx_name': idx_name, 'idx_type': idx_type, 'idx_type_code': idx_type_code, 'market': market, 'con_code': con_code, 'con_name': con_name}
        params.update(kwargs)
        path = ENDPOINTS['tdx_board_members'].path
        return self.get_paginated(path, page=page, page_size=page_size, limit=limit, all_pages=all_pages, max_pages=max_pages, raw=raw, fields=fields, as_dataframe=as_dataframe, **params)


    def stock_dividends(
        self,
        symbol: Any | None = None,
        since_date: Any | None = None,
        until_date: Any | None = None,
        page: int | None = None,
        page_size: int | None = None,
        *,
        raw: bool = False,
        fields: Sequence[str] | str | None = None,
        as_dataframe: bool = True,
        **kwargs: Any,
    ) -> Any:
        """股票分红记录."""
        params = {'symbol': symbol, 'since_date': since_date, 'until_date': until_date, 'page': page, 'page_size': page_size}
        params.update(kwargs)
        return self._call_endpoint('stock_dividends', raw=raw, fields=fields, as_dataframe=as_dataframe, **params)


    def stock_history_list(self, trade_date: Any | None = None, code: Any | None = None, page: int | None = None, page_size: int | None = None, *, raw: bool = False, fields: Sequence[str] | str | None = None, as_dataframe: bool = True, **kwargs: Any) -> Any:
        """股票历史列表."""
        params = {'trade_date': trade_date, 'code': code, 'page': page, 'page_size': page_size}
        params.update(kwargs)
        return self._call_endpoint('stock_history_list', raw=raw, fields=fields, as_dataframe=as_dataframe, **params)


    def stock_connect_members(self, direction: Any | None = None, channel: Any | None = None, page: int | None = None, page_size: int | None = None, *, raw: bool = False, fields: Sequence[str] | str | None = None, as_dataframe: bool = True, **kwargs: Any) -> Any:
        """互联互通成份."""
        params = {'direction': direction, 'channel': channel, 'page': page, 'page_size': page_size}
        params.update(kwargs)
        return self._call_endpoint('stock_connect_members', raw=raw, fields=fields, as_dataframe=as_dataframe, **params)


    def limit_list(self, limit_type: Any | None = None, trade_date: Any | None = None, *, raw: bool = False, fields: Sequence[str] | str | None = None, as_dataframe: bool = True, **kwargs: Any) -> Any:
        """涨跌停池."""
        params = {'limit_type': limit_type, 'trade_date': trade_date}
        params.update(kwargs)
        return self._call_endpoint('limit_list', raw=raw, fields=fields, as_dataframe=as_dataframe, **params)


    def stk_surv(self, ts_code: Any | None = None, trade_date: Any | None = None, start_date: Any | None = None, end_date: Any | None = None, page: Any | None = None, page_size: Any | None = None, limit: int | None = None, all_pages: bool = False, max_pages: int | None = None, *, raw: bool = False, fields: Sequence[str] | str | None = None, as_dataframe: bool = True, **kwargs: Any) -> Any:
        """个股严重异常波动."""
        params = {'ts_code': ts_code, 'trade_date': trade_date, 'start_date': start_date, 'end_date': end_date}
        params.update(kwargs)
        path = ENDPOINTS['stk_surv'].path
        return self.get_paginated(path, page=page, page_size=page_size, limit=limit, all_pages=all_pages, max_pages=max_pages, raw=raw, fields=fields, as_dataframe=as_dataframe, **params)


    def stk_shock(self, ts_code: Any | None = None, trade_date: Any | None = None, start_date: Any | None = None, end_date: Any | None = None, page: Any | None = None, page_size: Any | None = None, limit: int | None = None, all_pages: bool = False, max_pages: int | None = None, *, raw: bool = False, fields: Sequence[str] | str | None = None, as_dataframe: bool = True, **kwargs: Any) -> Any:
        """个股异常波动."""
        params = {'ts_code': ts_code, 'trade_date': trade_date, 'start_date': start_date, 'end_date': end_date}
        params.update(kwargs)
        path = ENDPOINTS['stk_shock'].path
        return self.get_paginated(path, page=page, page_size=page_size, limit=limit, all_pages=all_pages, max_pages=max_pages, raw=raw, fields=fields, as_dataframe=as_dataframe, **params)


    def stk_alert_broker(self, ts_code: Any | None = None, start_date: Any | None = None, end_date: Any | None = None, page: Any | None = None, page_size: Any | None = None, limit: int | None = None, all_pages: bool = False, max_pages: int | None = None, *, raw: bool = False, fields: Sequence[str] | str | None = None, as_dataframe: bool = True, **kwargs: Any) -> Any:
        """交易所重点提示证券."""
        params = {'ts_code': ts_code, 'start_date': start_date, 'end_date': end_date}
        params.update(kwargs)
        path = ENDPOINTS['stk_alert_broker'].path
        return self.get_paginated(path, page=page, page_size=page_size, limit=limit, all_pages=all_pages, max_pages=max_pages, raw=raw, fields=fields, as_dataframe=as_dataframe, **params)


    def limit_up_public_report(self, date: Any | None = None, security_code: Any | None = None, *, raw: bool = False, fields: Sequence[str] | str | None = None, as_dataframe: bool = True, **kwargs: Any) -> Any:
        """涨停对外归因报告."""
        params = {'date': date, 'security_code': security_code}
        params.update(kwargs)
        return self._call_endpoint('limit_up_public_report', raw=raw, fields=fields, as_dataframe=as_dataframe, **params)


    def limit_up_briefs(self, date: Any | None = None, *, raw: bool = False, fields: Sequence[str] | str | None = None, as_dataframe: bool = True, **kwargs: Any) -> Any:
        """涨停简报."""
        params = {'date': date}
        params.update(kwargs)
        return self._call_endpoint('limit_up_briefs', raw=raw, fields=fields, as_dataframe=as_dataframe, **params)


    def ths_hot_list(self, list_type: Any | None = None, trade_date: Any | None = None, page: Any | None = None, page_size: Any | None = None, limit: int | None = None, all_pages: bool = False, max_pages: int | None = None, *, raw: bool = False, fields: Sequence[str] | str | None = None, as_dataframe: bool = True, **kwargs: Any) -> Any:
        """同花顺热榜."""
        params = {'list_type': list_type, 'trade_date': trade_date}
        params.update(kwargs)
        path = ENDPOINTS['ths_hot_list'].path
        return self.get_paginated(path, page=page, page_size=page_size, limit=limit, all_pages=all_pages, max_pages=max_pages, raw=raw, fields=fields, as_dataframe=as_dataframe, **params)


    def ashare_news_sentiment_factors(self, trade_code: Any | None = None, start_date: Any | None = None, end_date: Any | None = None, page: Any | None = None, page_size: Any | None = None, limit: int | None = None, all_pages: bool = False, max_pages: int | None = None, *, raw: bool = False, fields: Sequence[str] | str | None = None, as_dataframe: bool = True, **kwargs: Any) -> Any:
        """A股新闻情绪因子."""
        params = {'trade_code': trade_code, 'start_date': start_date, 'end_date': end_date}
        params.update(kwargs)
        path = ENDPOINTS['ashare_news_sentiment_factors'].path
        return self.get_paginated(path, page=page, page_size=page_size, limit=limit, all_pages=all_pages, max_pages=max_pages, raw=raw, fields=fields, as_dataframe=as_dataframe, **params)


    def kline_pattern_annotations(self, date: Any | None = None, symbol: Any | None = None, pattern: Any | None = None, page: Any | None = None, page_size: Any | None = None, limit: int | None = None, all_pages: bool = False, max_pages: int | None = None, *, raw: bool = False, fields: Sequence[str] | str | None = None, as_dataframe: bool = True, **kwargs: Any) -> Any:
        """K线形态标注."""
        params = {'date': date, 'symbol': symbol, 'pattern': pattern}
        params.update(kwargs)
        path = ENDPOINTS['kline_pattern_annotations'].path
        return self.get_paginated(path, page=page, page_size=page_size, limit=limit, all_pages=all_pages, max_pages=max_pages, raw=raw, fields=fields, as_dataframe=as_dataframe, **params)


    def ashare_interactions(self, start_date: Any | None = None, end_date: Any | None = None, trade_code: Any | None = None, company_name: Any | None = None, industry_code: Any | None = None, industry_name: Any | None = None, data_source: Any | None = None, page: Any | None = None, page_size: Any | None = None, limit: int | None = None, all_pages: bool = False, max_pages: int | None = None, *, raw: bool = False, fields: Sequence[str] | str | None = None, as_dataframe: bool = True, **kwargs: Any) -> Any:
        """e互动."""
        params = {'start_date': start_date, 'end_date': end_date, 'trade_code': trade_code, 'company_name': company_name, 'industry_code': industry_code, 'industry_name': industry_name, 'data_source': data_source}
        params.update(kwargs)
        path = ENDPOINTS['ashare_interactions'].path
        return self.get_paginated(path, page=page, page_size=page_size, limit=limit, all_pages=all_pages, max_pages=max_pages, raw=raw, fields=fields, as_dataframe=as_dataframe, **params)


    def supply_chain_subindustry_supply_chain(self, industry_name: Any | None = None, direction: Any | None = None, *, raw: bool = False, fields: Sequence[str] | str | None = None, as_dataframe: bool = True, **kwargs: Any) -> Any:
        """供应链一跳关系."""
        params = {'industry_name': industry_name, 'direction': direction}
        params.update(kwargs)
        return self._call_endpoint('supply_chain_subindustry_supply_chain', raw=raw, fields=fields, as_dataframe=as_dataframe, **params)


    def supply_chain_company_supply_chain_companies(self, trade_code: Any | None = None, direction: Any | None = None, page: Any | None = None, page_size: Any | None = None, limit: int | None = None, all_pages: bool = False, max_pages: int | None = None, *, raw: bool = False, fields: Sequence[str] | str | None = None, as_dataframe: bool = True, **kwargs: Any) -> Any:
        """供应链公司候选."""
        params = {'trade_code': trade_code, 'direction': direction}
        params.update(kwargs)
        path = ENDPOINTS['supply_chain_company_supply_chain_companies'].path
        return self.get_paginated(path, page=page, page_size=page_size, limit=limit, all_pages=all_pages, max_pages=max_pages, raw=raw, fields=fields, as_dataframe=as_dataframe, **params)


    def supply_chain_subsubindustry_companies(self, subindustry_name: Any | None = None, *, raw: bool = False, fields: Sequence[str] | str | None = None, as_dataframe: bool = True, **kwargs: Any) -> Any:
        """供应链子子行业公司映射."""
        params = {'subindustry_name': subindustry_name}
        params.update(kwargs)
        return self._call_endpoint('supply_chain_subsubindustry_companies', raw=raw, fields=fields, as_dataframe=as_dataframe, **params)


    def supply_chain_subsubindustry_parent_subindustries(self, subindustry_name: Any | None = None, *, raw: bool = False, fields: Sequence[str] | str | None = None, as_dataframe: bool = True, **kwargs: Any) -> Any:
        """供应链子子行业父行业反查."""
        params = {'subindustry_name': subindustry_name}
        params.update(kwargs)
        return self._call_endpoint('supply_chain_subsubindustry_parent_subindustries', raw=raw, fields=fields, as_dataframe=as_dataframe, **params)


    def supply_chain_subindustry_subsubindustries(self, industry_name: Any | None = None, *, raw: bool = False, fields: Sequence[str] | str | None = None, as_dataframe: bool = True, **kwargs: Any) -> Any:
        """供应链子行业层级展开."""
        params = {'industry_name': industry_name}
        params.update(kwargs)
        return self._call_endpoint('supply_chain_subindustry_subsubindustries', raw=raw, fields=fields, as_dataframe=as_dataframe, **params)


    def exchange_margin_summaries(self, start_date: Any | None = None, end_date: Any | None = None, exchange: Any | None = None, page: int | None = None, page_size: int | None = None, *, raw: bool = False, fields: Sequence[str] | str | None = None, as_dataframe: bool = True, **kwargs: Any) -> Any:
        """交易所融资融券汇总日度."""
        params = {'start_date': start_date, 'end_date': end_date, 'exchange': exchange, 'page': page, 'page_size': page_size}
        params.update(kwargs)
        return self._call_endpoint('exchange_margin_summaries', raw=raw, fields=fields, as_dataframe=as_dataframe, **params)


    def ashare_rating_factor_snapshot(self, trade_code: Any | None = None, date: Any | None = None, top_k: Any | None = None, *, raw: bool = False, fields: Sequence[str] | str | None = None, as_dataframe: bool = True, **kwargs: Any) -> Any:
        """A股相关性 Top-K."""
        params = {'trade_code': trade_code, 'date': date, 'top_k': top_k}
        params.update(kwargs)
        return self._call_endpoint('ashare_rating_factor_snapshot', raw=raw, fields=fields, as_dataframe=as_dataframe, **params)


    def stock_minutes(self, symbol: Any | None = None, interval_value: Any | None = None, adjust_kind: Any | None = None, since_ts_millis: Any | None = None, until_ts_millis: Any | None = None, limit: Any | None = None, *, raw: bool = False, fields: Sequence[str] | str | None = None, as_dataframe: bool = True, **kwargs: Any) -> Any:
        """股票历史分钟行情."""
        params = {'symbol': symbol, 'interval_value': interval_value, 'adjust_kind': adjust_kind, 'since_ts_millis': since_ts_millis, 'until_ts_millis': until_ts_millis, 'limit': limit}
        params.update(kwargs)
        return self._call_endpoint('stock_minutes', raw=raw, fields=fields, as_dataframe=as_dataframe, **params)


    def stock_signal_latest_snapshot(self, signal_type: Any | None = None, page: int | None = None, page_size: int | None = None, limit: int | None = None, all_pages: bool = False, max_pages: int | None = None, *, raw: bool = False, fields: Sequence[str] | str | None = None, as_dataframe: bool = True, **kwargs: Any) -> Any:
        """信号最新快照."""
        params = {'signal_type': signal_type}
        params.update(kwargs)
        path = ENDPOINTS['stock_signal_latest_snapshot'].path
        return self.get_paginated(path, page=page, page_size=page_size, limit=limit, all_pages=all_pages, max_pages=max_pages, raw=raw, fields=fields, as_dataframe=as_dataframe, **params)


    def ths_stock_daily_flow(self, start_date: Any | None = None, end_date: Any | None = None, code: Any | None = None, name: Any | None = None, page: int | None = None, page_size: int | None = None, limit: int | None = None, all_pages: bool = False, max_pages: int | None = None, *, raw: bool = False, fields: Sequence[str] | str | None = None, as_dataframe: bool = True, **kwargs: Any) -> Any:
        """同花顺个股资金流日度."""
        params = {'start_date': start_date, 'end_date': end_date, 'code': code, 'name': name}
        params.update(kwargs)
        path = ENDPOINTS['ths_stock_daily_flow'].path
        return self.get_paginated(path, page=page, page_size=page_size, limit=limit, all_pages=all_pages, max_pages=max_pages, max_page_size=1000, raw=raw, fields=fields, as_dataframe=as_dataframe, **params)


    def ths_concept_daily_flow(self, start_date: Any | None = None, end_date: Any | None = None, sector_name: Any | None = None, page: int | None = None, page_size: int | None = None, limit: int | None = None, all_pages: bool = False, max_pages: int | None = None, *, raw: bool = False, fields: Sequence[str] | str | None = None, as_dataframe: bool = True, **kwargs: Any) -> Any:
        """同花顺概念板块资金流日度."""
        params = {'start_date': start_date, 'end_date': end_date, 'sector_name': sector_name}
        params.update(kwargs)
        path = ENDPOINTS['ths_concept_daily_flow'].path
        return self.get_paginated(path, page=page, page_size=page_size, limit=limit, all_pages=all_pages, max_pages=max_pages, max_page_size=1000, raw=raw, fields=fields, as_dataframe=as_dataframe, **params)


    def ths_industry_daily_flow(self, start_date: Any | None = None, end_date: Any | None = None, sector_name: Any | None = None, page: int | None = None, page_size: int | None = None, limit: int | None = None, all_pages: bool = False, max_pages: int | None = None, *, raw: bool = False, fields: Sequence[str] | str | None = None, as_dataframe: bool = True, **kwargs: Any) -> Any:
        """同花顺行业板块资金流日度."""
        params = {'start_date': start_date, 'end_date': end_date, 'sector_name': sector_name}
        params.update(kwargs)
        path = ENDPOINTS['ths_industry_daily_flow'].path
        return self.get_paginated(path, page=page, page_size=page_size, limit=limit, all_pages=all_pages, max_pages=max_pages, max_page_size=1000, raw=raw, fields=fields, as_dataframe=as_dataframe, **params)


    def ths_industry_constituents(self, industry_code: Any | None = None, industry_name: Any | None = None, stock_code: Any | None = None, stock_name: Any | None = None, page: int | None = None, page_size: int | None = None, limit: int | None = None, all_pages: bool = False, max_pages: int | None = None, *, raw: bool = False, fields: Sequence[str] | str | None = None, as_dataframe: bool = True, **kwargs: Any) -> Any:
        """同花顺行业成分股列表."""
        params = {'industry_code': industry_code, 'industry_name': industry_name, 'stock_code': stock_code, 'stock_name': stock_name}
        params.update(kwargs)
        path = ENDPOINTS['ths_industry_constituents'].path
        return self.get_paginated(path, page=page, page_size=page_size, limit=limit, all_pages=all_pages, max_pages=max_pages, max_page_size=1000, raw=raw, fields=fields, as_dataframe=as_dataframe, **params)


    def stock_realtime_minute_kline(self, symbols: Any | None = None, *, raw: bool = False, fields: Sequence[str] | str | None = None, as_dataframe: bool = True, **kwargs: Any) -> Any:
        """股票实时分钟K线."""
        params = {'symbols': symbols}
        params.update(kwargs)
        return self._call_endpoint('stock_realtime_minute_kline', raw=raw, fields=fields, as_dataframe=as_dataframe, **params)


    def stock_realtime_day_kline(self, symbols: Any | None = None, *, raw: bool = False, fields: Sequence[str] | str | None = None, as_dataframe: bool = True, **kwargs: Any) -> Any:
        """股票实时日K线."""
        params = {'symbols': symbols}
        params.update(kwargs)
        return self._call_endpoint('stock_realtime_day_kline', raw=raw, fields=fields, as_dataframe=as_dataframe, **params)


    def ths_board_list(self, *, raw: bool = False, fields: Sequence[str] | str | None = None, as_dataframe: bool = True, **kwargs: Any) -> Any:
        """同花顺板块列表."""
        params = {}
        params.update(kwargs)
        return self._call_endpoint('ths_board_list', raw=raw, fields=fields, as_dataframe=as_dataframe, **params)

    def eastmoney_all_board_daily_kline(self, start_date: Any | None = None, end_date: Any | None = None, page: int | None = None, page_size: int | None = None, limit: int | None = None, all_pages: bool = False, max_pages: int | None = None, *, raw: bool = False, fields: Sequence[str] | str | None = None, as_dataframe: bool = True, **kwargs: Any) -> Any:
        """东方财富全板块日线OHLC."""
        params = {'start_date': start_date, 'end_date': end_date}
        params.update(kwargs)
        return self.get_paginated(ENDPOINTS['eastmoney_all_board_daily_kline'].path, page=page, page_size=page_size, limit=limit, all_pages=all_pages, max_pages=max_pages, raw=raw, fields=fields, as_dataframe=as_dataframe, **params)

    def stock_ggmx(self, stock_code: Any | None = None, change_direction: Any | None = None, start_date: Any | None = None, end_date: Any | None = None, page: int | None = None, page_size: int | None = None, limit: int | None = None, all_pages: bool = False, max_pages: int | None = None, *, raw: bool = False, fields: Sequence[str] | str | None = None, as_dataframe: bool = True, **kwargs: Any) -> Any:
        """董监高持股变动."""
        params = {'stock_code': stock_code, 'change_direction': change_direction, 'start_date': start_date, 'end_date': end_date}
        params.update(kwargs)
        return self.get_paginated(ENDPOINTS['stock_ggmx'].path, page=page, page_size=page_size, limit=limit, all_pages=all_pages, max_pages=max_pages, raw=raw, fields=fields, as_dataframe=as_dataframe, **params)

    def report_announcement_list(self, date: Any | None = None, sec_code: Any | None = None, page: int | None = None, page_size: int | None = None, limit: int | None = None, all_pages: bool = False, max_pages: int | None = None, *, raw: bool = False, fields: Sequence[str] | str | None = None, as_dataframe: bool = True, **kwargs: Any) -> Any:
        """报告公告列表."""
        params = {'date': date, 'sec_code': sec_code}
        params.update(kwargs)
        return self.get_paginated(ENDPOINTS['report_announcement_list'].path, page=page, page_size=page_size, limit=limit, all_pages=all_pages, max_pages=max_pages, raw=raw, fields=fields, as_dataframe=as_dataframe, **params)

    def report_announcement_summary(self, announcement_id: Any | None = None, *, raw: bool = False, fields: Sequence[str] | str | None = None, as_dataframe: bool = True, **kwargs: Any) -> Any:
        """报告公告摘要."""
        params = {'announcement_id': announcement_id}
        params.update(kwargs)
        return self._call_endpoint('report_announcement_summary', raw=raw, fields=fields, as_dataframe=as_dataframe, **params)

    def stock_intraday_auction_volume_symbol(self, symbol: Any | None = None, trade_date: Any | None = None, page: int | None = None, page_size: int | None = None, limit: int | None = None, all_pages: bool = False, max_pages: int | None = None, *, raw: bool = False, fields: Sequence[str] | str | None = None, as_dataframe: bool = True, **kwargs: Any) -> Any:
        """单标的连续竞价成交量."""
        params = {'symbol': symbol, 'trade_date': trade_date}
        params.update(kwargs)
        return self.get_paginated(ENDPOINTS['stock_intraday_auction_volume_symbol'].path, page=page, page_size=page_size, limit=limit, all_pages=all_pages, max_pages=max_pages, raw=raw, fields=fields, as_dataframe=as_dataframe, **params)

    def ths_all_board_kline(self, start_date: Any | None = None, end_date: Any | None = None, page: int | None = None, page_size: int | None = None, limit: int | None = None, all_pages: bool = False, max_pages: int | None = None, *, raw: bool = False, fields: Sequence[str] | str | None = None, as_dataframe: bool = True, **kwargs: Any) -> Any:
        """同花顺全板块K线."""
        params = {'start_date': start_date, 'end_date': end_date}
        params.update(kwargs)
        return self.get_paginated(ENDPOINTS['ths_all_board_kline'].path, page=page, page_size=page_size, limit=limit, all_pages=all_pages, max_pages=max_pages, raw=raw, fields=fields, as_dataframe=as_dataframe, **params)

    def stock_candlesticks_batch(self, symbols: Any | None = None, interval_unit: Any | None = None, interval_value: Any | None = None, adjust_kind: Any | None = None, since_ts_millis: Any | None = None, until_ts_millis: Any | None = None, limit: Any | None = None, *, raw: bool = False, fields: Sequence[str] | str | None = None, as_dataframe: bool = True, **kwargs: Any) -> Any:
        """批量股票K线."""
        params = {'symbols': symbols, 'interval_unit': interval_unit, 'interval_value': interval_value, 'adjust_kind': adjust_kind, 'since_ts_millis': since_ts_millis, 'until_ts_millis': until_ts_millis, 'limit': limit}
        params.update(kwargs)
        return self._call_endpoint('stock_candlesticks_batch', raw=raw, fields=fields, as_dataframe=as_dataframe, **params)

    def stock_minutes_batch(self, symbols: Any | None = None, interval_value: Any | None = None, adjust_kind: Any | None = None, since_ts_millis: Any | None = None, until_ts_millis: Any | None = None, limit: Any | None = None, *, raw: bool = False, fields: Sequence[str] | str | None = None, as_dataframe: bool = True, **kwargs: Any) -> Any:
        """批量股票历史分钟行情."""
        params = {'symbols': symbols, 'interval_value': interval_value, 'adjust_kind': adjust_kind, 'since_ts_millis': since_ts_millis, 'until_ts_millis': until_ts_millis, 'limit': limit}
        params.update(kwargs)
        return self._call_endpoint('stock_minutes_batch', raw=raw, fields=fields, as_dataframe=as_dataframe, **params)
