"""Foreign exchange API methods grouped by ftshare-doc."""

from __future__ import annotations

from collections.abc import Sequence
from typing import Any

from ..endpoints import ENDPOINTS


class ForexApiMixin:
    """Endpoint methods for the forex ftshare-doc topic."""

    def consumer_forex_gold_monthly(
        self,
        *,
        raw: bool = False,
        fields: Sequence[str] | str | None = None,
        as_dataframe: bool = True,
        **kwargs: Any,
    ) -> Any:
        """外汇黄金.

        Endpoint: ``api/v1/market/data/economic/china-forex-gold``.
        Method: ``GET``.
        Documented endpoint: ``consumer_forex_gold_monthly``.

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
            'consumer_forex_gold_monthly',
            raw=raw,
            fields=fields,
            as_dataframe=as_dataframe,
            **request_params,
        )
