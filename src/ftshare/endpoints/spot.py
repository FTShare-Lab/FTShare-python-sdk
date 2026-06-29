"""Spot commodity endpoints generated from ftshare-doc."""

from __future__ import annotations

from .types import Endpoint, build_endpoints


ENDPOINTS: dict[str, Endpoint] = build_endpoints({
    'bullion_price': {
        'path': 'api/v1/market/data/bullion/price',
        'title': '贵金属价格',
        'doc_file': '贵金属价格.md',
        'original_api': 'get_bullion_price',
        'params': ('symbol', 'start_date', 'end_date', 'page', 'page_size'),
    },
    'bullion_support_symbol': {
        'path': 'api/v1/market/data/bullion/support-symbol',
        'title': '贵金属支持标的',
        'doc_file': '贵金属支持标的.md',
        'original_api': 'get_bullion_support_symbol',
    },
})
