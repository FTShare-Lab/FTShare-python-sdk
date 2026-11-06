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
    'sge_spot_description_all': {
        'path': 'api/v1/market/data/sge-spot-description-all',
        'title': '上金所现货品种',
        'doc_file': '上金所现货品种.md',
        'original_api': 'sge_spot_description_all',
        'params': ('category', 'active_only'),
    },
})
