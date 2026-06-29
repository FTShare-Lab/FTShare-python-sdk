"""Foreign exchange endpoints generated from ftshare-doc."""

from __future__ import annotations

from .types import Endpoint, build_endpoints


ENDPOINTS: dict[str, Endpoint] = build_endpoints({
    'consumer_forex_gold_monthly': {
        'path': 'api/v1/market/data/economic/china-forex-gold',
        'title': '外汇黄金',
        'doc_file': '外汇黄金.md',
        'original_api': 'consumer_forex_gold_monthly',
    },
})
