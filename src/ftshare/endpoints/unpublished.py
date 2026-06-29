"""Unpublished endpoints that still have SDK coverage."""

from __future__ import annotations

from .types import Endpoint, build_endpoints


ENDPOINTS: dict[str, Endpoint] = build_endpoints({
    'stock_dividends_paginated': {
        'path': 'api/v1/market/data/dividends',
        'title': '股票分红记录分页',
        'doc_file': '股票分红记录分页.md',
        'original_api': 'stock_dividends_paginated',
        'params': ('page', 'page_size'),
    },
    'stock_intraday': {
        'path': 'api/v1/market/security/{symbol}/intraday',
        'title': '股票日内分时',
        'doc_file': '股票日内分时.md',
        'original_api': 'stock_intraday',
        'params': ('symbol',),
        'path_params': ('symbol',),
    },
    'stock_ipos_paginated': {
        'path': 'api/v1/market/data/stock-ipos',
        'title': '股票IPO分页',
        'doc_file': '股票IPO分页.md',
        'original_api': 'stock_ipos_paginated',
        'params': ('page', 'page_size'),
    },
    'stock_related': {
        'path': 'api/v1/market/security/{symbol}/related',
        'title': '相关股票',
        'doc_file': '相关股票.md',
        'original_api': 'stock_related',
        'params': ('symbol', 'limit'),
        'path_params': ('symbol',),
    },
})
