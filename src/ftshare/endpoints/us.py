"""US market endpoints generated from ftshare-doc."""

from __future__ import annotations

from .types import Endpoint, build_endpoints


ENDPOINTS: dict[str, Endpoint] = build_endpoints({
    'eastmoney_us_stock_list': {
        'path': 'api/v1/market/data/eastmoney-us-stock-list',
        'title': '东方财富美股列表',
        'doc_file': '东方财富美股列表.md',
        'original_api': 'eastmoney_us_stock_list',
        'params': ('refresh', 'page', 'page_size'),
    },
    'eastmoney_us_stock_daily_ohlc': {
        'path': 'api/v1/market/data/eastmoney-us-stock-daily-ohlc',
        'title': '东方财富美股日OHLC',
        'doc_file': '东方财富美股日OHLC.md',
        'original_api': 'eastmoney_us_stock_daily_kline',
        'params': ('stock_code', 'start_date', 'end_date', 'page', 'page_size'),
    },
})
