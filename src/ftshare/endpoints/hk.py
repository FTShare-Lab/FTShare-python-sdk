"""Hong Kong market endpoints generated from ftshare-doc."""

from __future__ import annotations

from .types import Endpoint, build_endpoints


ENDPOINTS: dict[str, Endpoint] = build_endpoints({
    'hk_candlesticks': {
        'path': 'api/v2/market/data/hk/hk-candlesticks',
        'title': '港股K线',
        'doc_file': '港股K线.md',
        'original_api': 'get_hk_candlesticks',
        'params': ('trade_code', 'interval_unit', 'until_date', 'since_date', 'interval_value', 'limit', 'adjust_kind'),
    },
    'hsi_daily_weight': {
        'path': 'api/v1/market/data/hk/hsi-daily-weight',
        'title': '恒生指数每日权重',
        'doc_file': '恒生指数每日权重.md',
        'original_api': 'hsi_daily_weight',
        'params': ('trade_date', 'start_date', 'end_date', 'index_slug', 'stock_code', 'page', 'page_size'),
    },
    'stk_ah_comparison': {
        'path': 'api/v1/market/data/hk/stk-ah-comparison',
        'title': 'AH股对比',
        'doc_file': 'AH股对比.md',
        'original_api': 'stk_ah_comparison',
        'params': ('hk_code', 'ts_code', 'trade_date', 'start_date', 'end_date', 'page', 'page_size'),
        'max_page_size': 1000,
    },

})
