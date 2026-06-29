"""US market endpoints generated from ftshare-doc."""

from __future__ import annotations

from .types import Endpoint, build_endpoints


ENDPOINTS: dict[str, Endpoint] = build_endpoints({
    'eastmoney_us_stock_daily_kline': {
        'path': 'api/v1/market/data/eastmoney-us-stock-daily-ohlc',
        'title': '东方财富美股日OHLC',
        'doc_file': '东方财富美股日OHLC.md',
        'original_api': 'eastmoney_us_stock_daily_kline',
        'params': ('stock_code', 'start_date', 'end_date', 'page', 'page_size'),
    },
    'eastmoney_us_stock_latest_kline': {
        'path': 'api/v1/market/data/eastmoney-us-stock-latest-ohlc',
        'title': '东方财富美股最新OHLC',
        'doc_file': '东方财富美股最新OHLC.md',
        'original_api': 'eastmoney_us_stock_latest_kline',
        'params': ('stock_code', 'page', 'page_size'),
    },
    'eastmoney_us_stock_list': {
        'path': 'api/v1/market/data/eastmoney-us-stock-list',
        'title': '东方财富美股列表',
        'doc_file': '东方财富美股列表.md',
        'original_api': 'eastmoney_us_stock_list',
        'params': ('refresh', 'page', 'page_size'),
    },
    'us_balance': {
        'path': 'api/v1/market/data/us/us-balance',
        'title': '美股资产负债表',
        'doc_file': '美股资产负债表.md',
        'original_api': 'us_balance',
        'params': ('stock_code', 'period', 'report_type', 'start_date', 'end_date', 'page', 'page_size'),
        'max_page_size': 500,
    },
    'us_basic': {
        'path': 'api/v1/market/data/us/us-basic',
        'title': '美股基础信息',
        'doc_file': '美股基础信息.md',
        'original_api': 'us_basic',
        'params': ('stock_code', 'page', 'page_size'),
        'max_page_size': 500,
    },
    'us_cashflow': {
        'path': 'api/v1/market/data/us/us-cashflow',
        'title': '美股现金流',
        'doc_file': '美股现金流.md',
        'original_api': 'us_cashflow',
        'params': ('stock_code', 'period', 'report_type', 'start_date', 'end_date', 'page', 'page_size'),
        'max_page_size': 500,
    },
    'us_income': {
        'path': 'api/v1/market/data/us/us-income',
        'title': '美股利润表',
        'doc_file': '美股利润表.md',
        'original_api': 'us_income',
        'params': ('stock_code', 'period', 'report_type', 'start_date', 'end_date', 'page', 'page_size'),
        'max_page_size': 500,
    },
    'eastmoney_us_stock_daily_ohlc': {
        'path': 'api/v1/market/data/eastmoney-us-stock-daily-ohlc',
        'title': '东方财富美股日OHLC',
        'doc_file': '东方财富美股日OHLC.md',
        'original_api': 'eastmoney_us_stock_daily_kline',
        'params': ('stock_code', 'start_date', 'end_date', 'page', 'page_size'),
    },
    'eastmoney_us_stock_latest_ohlc': {
        'path': 'api/v1/market/data/eastmoney-us-stock-latest-ohlc',
        'title': '东方财富美股最新OHLC',
        'doc_file': '东方财富美股最新OHLC.md',
        'original_api': 'eastmoney_us_stock_latest_kline',
        'params': ('stock_code', 'page', 'page_size'),
    },
})
