"""Spot commodity API methods grouped by ftshare-doc."""

from __future__ import annotations

from collections.abc import Sequence
from typing import Any

from ..endpoints import ENDPOINTS


class SpotApiMixin:
    """Endpoint methods for the spot ftshare-doc topic."""

    def bullion_price(
        self,
        symbol: Any | None = None,
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
        """贵金属价格.

        Endpoint: ``api/v1/market/data/bullion/price``.
        Method: ``GET``.
        Documented endpoint: ``get_bullion_price``.

        Args:
            symbol: 标的代码，如 XAUUSD、AU9999 (type: string; required: Y).
            start_date: 查询起始日期 YYYYMMDD (type: int; required: Y).
            end_date: 查询结束日期 YYYYMMDD；与 start_date 跨度 ≤3 天 (type: int; required: Y).
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
        request_params = {'symbol': symbol, 'start_date': start_date, 'end_date': end_date}
        request_params.update(kwargs)
        path = ENDPOINTS['bullion_price'].path
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

    def sge_spot_description_all(
        self,
        category: Any | None = None,
        active_only: Any | None = None,
        *,
        raw: bool = False,
        fields: Sequence[str] | str | None = None,
        as_dataframe: bool = True,
        **kwargs: Any,
    ) -> Any:
        """上金所现货品种.

        Endpoint: ``api/v1/market/data/sge-spot-description-all``.
        Method: ``GET``.
        Documented endpoint: ``sge_spot_description_all``.

        Args:
            category: 品种分类筛选：``spot_full`` 现货实盘 / ``spot_forward`` 现货即期 / ``spot_deferred`` 现货延期交收；不传返回全部分类 (type: string; required: N).
            active_only: ``true`` 仅返回活跃品种（17 只）；不传、``false`` 或空串返回全部（含已下架品种） (type: bool; required: N).
            raw: Return the decoded JSON payload without tabular extraction.
            fields: Optional field list or comma-separated field string applied after extraction.
            as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
            **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

        Returns:
            A pandas ``DataFrame`` by default, Python rows when
            ``as_dataframe=False``, or raw JSON when ``raw=True``.
        """
        request_params = {'category': category, 'active_only': active_only}
        request_params.update(kwargs)
        return self._call_endpoint(
            'sge_spot_description_all',
            raw=raw,
            fields=fields,
            as_dataframe=as_dataframe,
            **request_params,
        )
