"""FTShare global_index endpoint methods for FTShare market data."""

from __future__ import annotations

from collections.abc import Sequence
from typing import Any

from ..endpoints import ENDPOINTS


class GlobalIndexApiMixin:
    """Endpoint methods for the global_index API group."""

    def global_index_daily_kline(
        self,
        secid: Any | None = None,
        start_date: Any | None = None,
        end_date: Any | None = None,
        *,
        raw: bool = False,
        fields: Sequence[str] | str | None = None,
        as_dataframe: bool = True,
        **kwargs: Any,
    ) -> Any:
        """全球指数日K线.

        Endpoint: ``api/v1/market/data/global-index/daily-kline``.
        Method: ``GET``.
        Documented endpoint: ``global_index_daily_kline``.

        Args:
            secid: 东方财富全球指数编码，如 100.NDX、100.DJIA、100.SPX、100.HSI、100.N225 (type: string; required: Y).
            start_date: 开始日期 YYYY-MM-DD（含） (type: string; required: N).
            end_date: 结束日期 YYYY-MM-DD（含） (type: string; required: N).
            raw: Return the decoded JSON payload without tabular extraction.
            fields: Optional field list or comma-separated field string applied after extraction.
            as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
            **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

        Returns:
            A pandas ``DataFrame`` by default, Python rows when
            ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
            payloads when multi-page fetching is used with ``raw=True``.
        """
        request_params = {'secid': secid, 'start_date': start_date, 'end_date': end_date}
        request_params.update(kwargs)
        return self._call_endpoint(
            'global_index_daily_kline',
            raw=raw,
            fields=fields,
            as_dataframe=as_dataframe,
            **request_params,
        )

