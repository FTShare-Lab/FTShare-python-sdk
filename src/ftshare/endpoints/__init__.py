"""Endpoint registry assembled from ftshare-doc topic modules."""

from __future__ import annotations

from .types import Endpoint
from .stock import ENDPOINTS as STOCK_ENDPOINTS
from .hk import ENDPOINTS as HK_ENDPOINTS
from .us import ENDPOINTS as US_ENDPOINTS
from .index import ENDPOINTS as INDEX_ENDPOINTS
from .etf import ENDPOINTS as ETF_ENDPOINTS
from .fund import ENDPOINTS as FUND_ENDPOINTS
from .futures import ENDPOINTS as FUTURES_ENDPOINTS
from .bond import ENDPOINTS as BOND_ENDPOINTS
from .economic import ENDPOINTS as ECONOMIC_ENDPOINTS
from .llm_corpus import ENDPOINTS as LLM_CORPUS_ENDPOINTS
from .spot import ENDPOINTS as SPOT_ENDPOINTS
from .forex import ENDPOINTS as FOREX_ENDPOINTS
from .unpublished import ENDPOINTS as UNPUBLISHED_ENDPOINTS


ENDPOINTS: dict[str, Endpoint] = {}
ENDPOINTS.update(STOCK_ENDPOINTS)
ENDPOINTS.update(HK_ENDPOINTS)
ENDPOINTS.update(US_ENDPOINTS)
ENDPOINTS.update(INDEX_ENDPOINTS)
ENDPOINTS.update(ETF_ENDPOINTS)
ENDPOINTS.update(FUND_ENDPOINTS)
ENDPOINTS.update(FUTURES_ENDPOINTS)
ENDPOINTS.update(BOND_ENDPOINTS)
ENDPOINTS.update(ECONOMIC_ENDPOINTS)
ENDPOINTS.update(LLM_CORPUS_ENDPOINTS)
ENDPOINTS.update(SPOT_ENDPOINTS)
ENDPOINTS.update(FOREX_ENDPOINTS)
ENDPOINTS.update(UNPUBLISHED_ENDPOINTS)


__all__ = ["ENDPOINTS", "Endpoint"]
