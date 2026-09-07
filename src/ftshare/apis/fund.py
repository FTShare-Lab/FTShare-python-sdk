"""Public fund API methods grouped by ftshare-doc."""

from __future__ import annotations

from collections.abc import Sequence
from typing import Any

from ..endpoints import ENDPOINTS


class FundApiMixin:
    """Endpoint methods for the fund ftshare-doc topic."""

    def fund_basicinfo(
        self,
        fund_code: Any | None = None,
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
        """基金基础信息.

        Endpoint: ``api/v1/market/data/fund/fund-basicinfo``.
        Method: ``GET``.
        Documented endpoint: ``get_fund_basicinfo``.

        Args:
            fund_code: 基金代码；不传时查询全市场数据的默认分页 (type: string; required: N).
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
        request_params = {'fund_code': fund_code}
        request_params.update(kwargs)
        endpoint = ENDPOINTS['fund_basicinfo']
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

    def fund_cal_return(
        self,
        fund_code: Any | None = None,
        cal_type: Any | None = None,
        *,
        raw: bool = False,
        fields: Sequence[str] | str | None = None,
        as_dataframe: bool = True,
        **kwargs: Any,
    ) -> Any:
        """基金收益.

        Endpoint: ``api/v1/market/data/fund/fund-cal-return``.
        Method: ``GET``.
        Documented endpoint: ``get_fund_cal_return``.

        Args:
            fund_code: 基金代码（6位数字） (type: string; required: Y).
            cal_type: 查询区间：1M / 3M / 6M / 1Y / 3Y / 5Y / YTD（请求字段名为 `cal-type`） (type: string; required: Y). Request key: ``cal-type``.
            raw: Return the decoded JSON payload without tabular extraction.
            fields: Optional field list or comma-separated field string applied after extraction.
            as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
            **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

        Returns:
            A pandas ``DataFrame`` by default, Python rows when
            ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
            payloads when multi-page fetching is used with ``raw=True``.
        """
        request_params = {'fund_code': fund_code, 'cal-type': cal_type}
        request_params.update(kwargs)
        return self._call_endpoint(
            'fund_cal_return',
            raw=raw,
            fields=fields,
            as_dataframe=as_dataframe,
            **request_params,
        )

    def fund_overview(
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
        """基金总览.

        Endpoint: ``api/v1/market/data/fund/fund-overview``.
        Method: ``GET``.
        Documented endpoint: ``get_fund_overview``.

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
        path = ENDPOINTS['fund_overview'].path
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

    def fund_support_symbols(
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
        """基金支持标的.

        Endpoint: ``api/v1/market/data/fund/fund-support-symbols``.
        Method: ``GET``.
        Documented endpoint: ``get_fund_support_symbols``.

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
        path = ENDPOINTS['fund_support_symbols'].path
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

    def fund_share(
        self,
        fund_code: Any | None = None,
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
        """基金份额.

        Endpoint: ``api/v1/market/data/fund/fund-share``.
        Method: ``GET``.
        Documented endpoint: ``get_fund_share``.

        Args:
            fund_code: 基金代码 (type: string; required: Y).
            stati_perd: 统计周期：日/季度/年度/截止时点/半年/全部，默认日 (type: string; required: N).
            start_date: 开始日期 YYYYMMDD（按 trade_date 过滤） (type: int; required: N).
            end_date: 结束日期 YYYYMMDD (type: int; required: N).
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
        request_params = {
            'fund_code': fund_code,
            'stati_perd': stati_perd,
            'start_date': start_date,
            'end_date': end_date,
        }
        request_params.update(kwargs)
        path = ENDPOINTS['fund_share'].path
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

    def fund_company(
        self,
        fund_company: Any | None = None,
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
        """基金公司.

        Endpoint: ``api/v1/market/data/fund/fund-company``.
        Method: ``GET``.
        Documented endpoint: ``get_fund_company``.

        Args:
            fund_company: 基金公司名称，精确匹配 (type: string; required: N).
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
        request_params = {'fund_company': fund_company}
        request_params.update(kwargs)
        path = ENDPOINTS['fund_company'].path
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

    def fund_net_value_performance(
        self,
        fund_code: Any | None = None,
        stat_date: Any | None = None,
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
        """基金净值收益表现.

        Endpoint: ``api/v1/market/data/fund/fund-net-value-performance``.
        Method: ``GET``.
        Documented endpoint: ``get_fund_net_value_performance``.

        Args:
            fund_code: 基金代码 (type: string; required: Y).
            stat_date: 统计日期 YYYYMMDD（与 start/end 互斥） (type: int; required: N).
            start_date: 统计开始日期（需与 end_date 同传） (type: int; required: N).
            end_date: 统计结束日期 (type: int; required: N).
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
        request_params = {
            'fund_code': fund_code,
            'stat_date': stat_date,
            'start_date': start_date,
            'end_date': end_date,
        }
        request_params.update(kwargs)
        path = ENDPOINTS['fund_net_value_performance'].path
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

    def fund_net_value(
        self,
        fund_code: Any | None = None,
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
        """基金净值明细.

        Endpoint: ``api/v1/market/data/fund/fund-net-value``.
        Method: ``GET``.
        Documented endpoint: ``get_fund_net_value``.

        Args:
            fund_code: 基金代码 (type: string; required: Y).
            nav_date: 净值日期 YYYYMMDD（与 start/end 互斥） (type: int; required: N).
            start_date: 净值开始日期 YYYYMMDD（需与 end_date 同传） (type: int; required: N).
            end_date: 净值结束日期 YYYYMMDD (type: int; required: N).
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
        request_params = {
            'fund_code': fund_code,
            'nav_date': nav_date,
            'start_date': start_date,
            'end_date': end_date,
        }
        request_params.update(kwargs)
        path = ENDPOINTS['fund_net_value'].path
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

    def fund_classification(
        self,
        fund_code: Any | None = None,
        classify_std: Any | None = None,
        *,
        raw: bool = False,
        fields: Sequence[str] | str | None = None,
        as_dataframe: bool = True,
        **kwargs: Any,
    ) -> Any:
        """基金分类.

        Endpoint: ``api/v1/market/data/fund/fund-classification``.
        Method: ``GET``.
        Documented endpoint: ``get_fund_classification``.

        Args:
            fund_code: 基金代码 (type: string; required: Y).
            classify_std: 分类标准：证监会基金分类/晨星基金分类/银河证券分类2017版/Gangtise基金分类/Gangtise基金概念分类，缺省全部 (type: string; required: N).
            raw: Return the decoded JSON payload without tabular extraction.
            fields: Optional field list or comma-separated field string applied after extraction.
            as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
            **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

        Returns:
            A pandas ``DataFrame`` by default, Python rows when
            ``as_dataframe=False``, raw JSON when ``raw=True``.
        """
        request_params = {'fund_code': fund_code, 'classify_std': classify_std}
        request_params.update(kwargs)
        return self._call_endpoint(
            'fund_classification',
            raw=raw,
            fields=fields,
            as_dataframe=as_dataframe,
            **request_params,
        )

    def fund_list(
        self,
        fund_code: Any | None = None,
        fund_type: Any | None = None,
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
        """基金列表.

        Endpoint: ``api/v1/market/data/fund/fund-list``.
        Method: ``GET``.
        Documented endpoint: ``get_fund_list``.

        Args:
            fund_code: 基金代码 (type: string; required: N).
            fund_type: 基金类型，精确匹配（股票型/混合型/债券型/货币型/保本型/其他型/REITs） (type: string; required: N).
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
        request_params = {'fund_code': fund_code, 'fund_type': fund_type}
        request_params.update(kwargs)
        path = ENDPOINTS['fund_list'].path
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

    def fund_portfolio(
        self,
        fund_code: Any | None = None,
        report_date: Any | None = None,
        publish_date: Any | None = None,
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
        """基金持仓明细.

        Endpoint: ``api/v1/market/data/fund/fund-portfolio``.
        Method: ``GET``.
        Documented endpoint: ``get_fund_portfolio``.

        Args:
            fund_code: 基金代码 (type: string; required: Y).
            report_date: 报告期 YYYYMMDD（与 start/end 互斥） (type: int; required: N).
            publish_date: 发布日期 YYYYMMDD (type: int; required: N).
            start_date: 报告期起始日期（需与 end_date 同传） (type: int; required: N).
            end_date: 报告期结束日期 (type: int; required: N).
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
        request_params = {
            'fund_code': fund_code,
            'report_date': report_date,
            'publish_date': publish_date,
            'start_date': start_date,
            'end_date': end_date,
        }
        request_params.update(kwargs)
        path = ENDPOINTS['fund_portfolio'].path
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

    def fund_holder_structure(
        self,
        fund_code: Any | None = None,
        report_type: Any | None = None,
        start_date: Any | None = None,
        end_date: Any | None = None,
        *,
        raw: bool = False,
        fields: Sequence[str] | str | None = None,
        as_dataframe: bool = True,
        **kwargs: Any,
    ) -> Any:
        """基金持有人结构.

        Endpoint: ``api/v1/market/data/fund/fund-holder-structure``.
        Method: ``GET``.
        Documented endpoint: ``get_fund_holder_structure``.

        Args:
            fund_code: 基金代码 (type: string; required: Y).
            report_type: 报告类型：年度报告/中期报告/上市公告书/基金合同生效公告，缺省全部 (type: string; required: N).
            start_date: 报告期起始日期 YYYYMMDD (type: int; required: N).
            end_date: 报告期截止日期 YYYYMMDD (type: int; required: N).
            raw: Return the decoded JSON payload without tabular extraction.
            fields: Optional field list or comma-separated field string applied after extraction.
            as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
            **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

        Returns:
            A pandas ``DataFrame`` by default, Python rows when
            ``as_dataframe=False``, raw JSON when ``raw=True``.
        """
        request_params = {
            'fund_code': fund_code,
            'report_type': report_type,
            'start_date': start_date,
            'end_date': end_date,
        }
        request_params.update(kwargs)
        return self._call_endpoint(
            'fund_holder_structure',
            raw=raw,
            fields=fields,
            as_dataframe=as_dataframe,
            **request_params,
        )

    def fund_new_found(
        self,
        start_date: Any | None = None,
        end_date: Any | None = None,
        fund_type: Any | None = None,
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
        """基金新发.

        Endpoint: ``api/v1/market/data/fund/fund-new-found``.
        Method: ``GET``.
        Documented endpoint: ``get_fund_new_found``.

        Args:
            start_date: 成立日起始日期 YYYYMMDD（不传默认近 1 年） (type: int; required: N).
            end_date: 成立日截止日期 YYYYMMDD（不传默认今天） (type: int; required: N).
            fund_type: 基金类型过滤：混合型/债券型/股票型/货币型/其他型/保本型/REITs (type: string; required: N).
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
        request_params = {
            'start_date': start_date,
            'end_date': end_date,
            'fund_type': fund_type,
        }
        request_params.update(kwargs)
        path = ENDPOINTS['fund_new_found'].path
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

    def fund_manager(
        self,
        fund_code: Any | None = None,
        fund_manager: Any | None = None,
        is_inoffice: Any | None = None,
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
        """基金经理任职关系.

        Endpoint: ``api/v1/market/data/fund/fund-manager``.
        Method: ``GET``.
        Documented endpoint: ``get_fund_manager``.

        Args:
            fund_code: 基金代码（与 fund_manager 二选一） (type: string; required: N).
            fund_manager: 基金经理姓名（与 fund_code 二选一） (type: string; required: N).
            is_inoffice: 1 在任 / 0 离任 (type: string; required: N).
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
        request_params = {
            'fund_code': fund_code,
            'fund_manager': fund_manager,
            'is_inoffice': is_inoffice,
        }
        request_params.update(kwargs)
        path = ENDPOINTS['fund_manager'].path
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

    def fund_fee(
        self,
        fund_code: Any | None = None,
        charge_type: Any | None = None,
        client_type: Any | None = None,
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
        """基金费率.

        Endpoint: ``api/v1/market/data/fund/fund-fee``.
        Method: ``GET``.
        Documented endpoint: ``get_fund_fee``.

        Args:
            fund_code: 基金代码 (type: string; required: Y).
            charge_type: 费率类型：日常申购费/日常赎回费/认购费/管理费/托管费/销售服务费 (type: string; required: N).
            client_type: 客户类型：一般/机构/养老金/REITs (type: string; required: N).
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
        request_params = {
            'fund_code': fund_code,
            'charge_type': charge_type,
            'client_type': client_type,
        }
        request_params.update(kwargs)
        path = ENDPOINTS['fund_fee'].path
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

    def fund_asset_allocation(
        self,
        fund_code: Any | None = None,
        report_date: Any | None = None,
        publish_date: Any | None = None,
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
        """基金资产配置.

        Endpoint: ``api/v1/market/data/fund/fund-asset-allocation``.
        Method: ``GET``.
        Documented endpoint: ``get_fund_asset_allocation``.

        Args:
            fund_code: 基金代码 (type: string; required: Y).
            report_date: 报告期 YYYYMMDD（与 start/end 互斥） (type: int; required: N).
            publish_date: 发布日期 YYYYMMDD (type: int; required: N).
            start_date: 报告期起始日期（需与 end_date 同传） (type: int; required: N).
            end_date: 报告期结束日期 (type: int; required: N).
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
        request_params = {
            'fund_code': fund_code,
            'report_date': report_date,
            'publish_date': publish_date,
            'start_date': start_date,
            'end_date': end_date,
        }
        request_params.update(kwargs)
        path = ENDPOINTS['fund_asset_allocation'].path
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

    def fund_risk_level(
        self,
        fund_code: Any | None = None,
        history: Any | None = None,
        *,
        raw: bool = False,
        fields: Sequence[str] | str | None = None,
        as_dataframe: bool = True,
        **kwargs: Any,
    ) -> Any:
        """基金风险等级.

        Endpoint: ``api/v1/market/data/fund/fund-risk-level``.
        Method: ``GET``.
        Documented endpoint: ``get_fund_risk_level``.

        Args:
            fund_code: 基金代码 (type: string; required: Y).
            history: true 返回全部变更历史，缺省/false 仅当前有效 (type: bool; required: N).
            raw: Return the decoded JSON payload without tabular extraction.
            fields: Optional field list or comma-separated field string applied after extraction.
            as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
            **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

        Returns:
            A pandas ``DataFrame`` by default, Python rows when
            ``as_dataframe=False``, raw JSON when ``raw=True``.
        """
        request_params = {'fund_code': fund_code, 'history': history}
        request_params.update(kwargs)
        return self._call_endpoint(
            'fund_risk_level',
            raw=raw,
            fields=fields,
            as_dataframe=as_dataframe,
            **request_params,
        )

    def fund_index_fund(
        self,
        index_code: Any | None = None,
        scope: Any | None = None,
        *,
        raw: bool = False,
        fields: Sequence[str] | str | None = None,
        as_dataframe: bool = True,
        **kwargs: Any,
    ) -> Any:
        """指数跟踪基金.

        Endpoint: ``api/v1/market/data/fund/index-fund``.
        Method: ``GET``.
        Documented endpoint: ``get_fund_index_fund``.

        Args:
            index_code: 指数代码，支持裸码或带后缀 (type: string; required: Y).
            scope: `all` 全市场（默认）/ `etf` 仅场内 ETF (type: string; required: N).
            raw: Return the decoded JSON payload without tabular extraction.
            fields: Optional field list or comma-separated field string applied after extraction.
            as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
            **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

        Returns:
            A pandas ``DataFrame`` by default, Python rows when
            ``as_dataframe=False``, raw JSON when ``raw=True``.
        """
        request_params = {'index_code': index_code, 'scope': scope}
        request_params.update(kwargs)
        return self._call_endpoint(
            'fund_index_fund',
            raw=raw,
            fields=fields,
            as_dataframe=as_dataframe,
            **request_params,
        )
