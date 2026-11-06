"""LLM corpus API methods grouped by ftshare-doc."""

from __future__ import annotations

import os
from collections.abc import Sequence
from typing import Any

from ..endpoints import ENDPOINTS


class LlmCorpusApiMixin:
    """Endpoint methods for the llm_corpus ftshare-doc topic."""

    def market_announcements(
        self,
        keyword: Any | None = None,
        category: Any | None = None,
        stock_code: Any | None = None,
        start_date: Any | None = None,
        end_date: Any | None = None,
        plate: Any | None = None,
        column_type: Any | None = None,
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
        """全市场公告列表.

        Endpoint: ``api/v2/market/data/announcements/market-announcements``.
        Method: ``GET``.
        Documented endpoint: ``market_v2_announcements_market_announcements``.

        Args:
            keyword: 公告标题关键字，子串匹配；去首尾空格后最长 60 字符 (type: string; required: N).
            category: 公告分类，22 个允许值逗号分隔多选，任一命中即返回 (type: string; required: N).
            stock_code: 股票代码；支持裸代码、短后缀、长后缀与冒号格式 (type: string; required: N).
            start_date: 起始日期 YYYYMMDD；单独提供时查询该单日 (type: string; required: N).
            end_date: 结束日期 YYYYMMDD；不能单独提供，须与 start_date 成对使用 (type: string; required: N).
            plate: 板块，取值 ``sh`` / ``sz`` / ``sz_chi_next`` / ``sh_star`` / ``bj``，逗号分隔多选 (type: string; required: N).
            column_type: 栏目，取值 ``stock`` / ``hke`` / ``fund`` / ``bond``，逗号分隔多选 (type: string; required: N).
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
            'keyword': keyword,
            'category': category,
            'stock_code': stock_code,
            'start_date': start_date,
            'end_date': end_date,
            'plate': plate,
            'column_type': column_type,
        }
        request_params.update(kwargs)
        path = ENDPOINTS['market_announcements'].path
        return self.get_paginated(
            path,
            page=page,
            page_size=page_size,
            limit=limit,
            all_pages=all_pages,
            max_pages=max_pages,
            max_page_size=ENDPOINTS['market_announcements'].max_page_size,
            raw=raw,
            fields=fields,
            as_dataframe=as_dataframe,
            **request_params,
        )

    def periodic_reports(
        self,
        stock_code: Any | None = None,
        report_type: Any | None = None,
        report_year: Any | None = None,
        document_variant: Any | None = None,
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
        """定期报告列表.

        Endpoint: ``api/v2/market/data/announcements/periodic-reports``.
        Method: ``GET``.
        Documented endpoint: ``market_v2_announcements_periodic_reports``.

        Args:
            stock_code: 股票代码；支持裸代码、短后缀与长后缀（不支持冒号格式） (type: string; required: N).
            report_type: 报告类型：``annual`` / ``semi_annual`` / ``q1`` / ``q3`` (type: string; required: N).
            report_year: 报告年份，如 2025 (type: integer; required: N).
            document_variant: 文件版本类型：``full`` / ``summary`` / ``english`` (type: string; required: N).
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
            'stock_code': stock_code,
            'report_type': report_type,
            'report_year': report_year,
            'document_variant': document_variant,
        }
        request_params.update(kwargs)
        path = ENDPOINTS['periodic_reports'].path
        return self.get_paginated(
            path,
            page=page,
            page_size=page_size,
            limit=limit,
            all_pages=all_pages,
            max_pages=max_pages,
            max_page_size=ENDPOINTS['periodic_reports'].max_page_size,
            raw=raw,
            fields=fields,
            as_dataframe=as_dataframe,
            **request_params,
        )

    def shareholders_meeting(
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
        """股东大会.

        Endpoint: ``api/v1/market/data/corporate/meeting``.
        Method: ``GET``.
        Documented endpoint: ``shareholders_meeting``.

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
        path = ENDPOINTS['shareholders_meeting'].path
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

    def semantic_search_news(
        self,
        query: Any | None = None,
        limit: Any | None = None,
        year: Any | None = None,
        start_time: Any | None = None,
        end_time: Any | None = None,
        *,
        raw: bool = False,
        fields: Sequence[str] | str | None = None,
        as_dataframe: bool = True,
        **kwargs: Any,
    ) -> Any:
        """新闻语义搜索.

        Endpoint: ``api/v1/market/data/semantic-search-news``.
        Method: ``GET``.
        Documented endpoint: ``semantic_search_news_handler``.

        Args:
            query: 搜索文字 (type: string; required: Y).
            limit: 返回条数，默认由服务端决定 (type: int; required: N).
            year: 年份，限定搜索范围 (type: int; required: N).
            start_time: 起始时间（带时区），与 end_time 同传时区间不超过 3 天 (type: datetime; required: N).
            end_time: 结束时间（带时区），与 start_time 同传时区间不超过 3 天 (type: datetime; required: N).
            raw: Return the decoded JSON payload without tabular extraction.
            fields: Optional field list or comma-separated field string applied after extraction.
            as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
            **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

        Returns:
            A pandas ``DataFrame`` by default, Python rows when
            ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
            payloads when multi-page fetching is used with ``raw=True``.
        """
        request_params = {'query': query, 'limit': limit, 'year': year, 'start_time': start_time, 'end_time': end_time}
        request_params.update(kwargs)
        return self._call_endpoint(
            'semantic_search_news',
            raw=raw,
            fields=fields,
            as_dataframe=as_dataframe,
            **request_params,
        )

    def stock_announcements(
        self,
        stock_code: Any | None = None,
        start_date: Any | None = None,
        end_date: Any | None = None,
        type: Any | None = None,
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
        """公告列表.

        Endpoint: ``api/v2/market/data/announcements/stock-announcements``.
        Method: ``GET``.
        Documented endpoint: ``stock_announcements``.

        Args:
            stock_code: 证券代码（按标的查询时必填） (type: string; required: N).
            start_date: 开始日期 YYYYMMDD（按日期范围查询时必填） (type: string; required: N).
            end_date: 结束日期 YYYYMMDD，不填默认当前时间 (type: string; required: N).
            type: 查询类型，当前只支持 `stock` (type: string; required: Y).
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
        request_params = {'stock_code': stock_code, 'start_date': start_date, 'end_date': end_date, 'type': type}
        request_params.update(kwargs)
        path = ENDPOINTS['stock_announcements'].path
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

    def stock_announcements_download(
        self,
        url_hash: Any,
        save_dir: str | os.PathLike[str] = ".",
    ) -> str:
        """下载公告正文.

        Endpoint: ``api/v2/market/data/announcements/stock-announcements/{url_hash}``.
        Method: ``GET``.

        Args:
            url_hash: 公告文件 URL 哈希，取自 ``stock_announcements`` 列表响应的 `url_hash` 字段 (type: string; required: Y).
            save_dir: 保存目录（默认为当前目录），目录不存在时自动创建；文件名固定为 `{url_hash}.pdf`。

        Returns:
            落盘后的文件路径；服务端返回 2xx 但正文为空时返回空字符串。

        Raises:
            FtshareHTTPError: If the server returns a non-2xx HTTP status.
        """
        path = self._format_path(ENDPOINTS['stock_announcements'].path + '/{url_hash}', {'url_hash': url_hash})
        return self.download(path, save_dir=save_dir, filename=f"{url_hash}.pdf")

    def stock_reports(
        self,
        stock_code: Any | None = None,
        start_date: Any | None = None,
        end_date: Any | None = None,
        type: Any | None = None,
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
        """研报列表.

        Endpoint: ``api/v2/market/data/report/stock-reports``.
        Method: ``GET``.
        Documented endpoint: ``stock_reports``.

        Args:
            stock_code: 证券代码（按标的查询时必填） (type: string; required: N).
            start_date: 开始日期 YYYYMMDD（按日期范围查询时必填） (type: string; required: N).
            end_date: 结束日期 YYYYMMDD，不填默认当前时间 (type: string; required: N).
            type: 查询类型，当前只支持 `stock` (type: string; required: Y).
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
        request_params = {'stock_code': stock_code, 'start_date': start_date, 'end_date': end_date, 'type': type}
        request_params.update(kwargs)
        path = ENDPOINTS['stock_reports'].path
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

    def stock_prospectuses(
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
        """招股书列表.

        Endpoint: ``api/v2/market/data/announcements/stock-prospectuses``.
        Method: ``GET``.
        Documented endpoint: ``stock_prospectuses``.

        Args:
            stock_code: 股票代码；按标的查询时必填，支持裸代码、短后缀和长后缀 (type: string; required: N).
            start_date: 披露日期 YYYYMMDD；未提供 stock_code 时必填 (type: string; required: N).
            end_date: 披露日期 YYYYMMDD；不填默认等于 start_date，传入时必须等于 start_date (type: string; required: N).
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
        path = ENDPOINTS['stock_prospectuses'].path
        return self.get_paginated(
            path,
            page=page,
            page_size=page_size,
            limit=limit,
            all_pages=all_pages,
            max_pages=max_pages,
            max_page_size=ENDPOINTS['stock_prospectuses'].max_page_size,
            raw=raw,
            fields=fields,
            as_dataframe=as_dataframe,
            **request_params,
        )
