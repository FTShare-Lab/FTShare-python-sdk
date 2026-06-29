"""Hong Kong market endpoints generated from ftshare-doc."""

from __future__ import annotations

from .types import Endpoint, build_endpoints


ENDPOINTS: dict[str, Endpoint] = build_endpoints({
    'company_hk': {
        'path': 'api/v1/market/data/hk/company-hk',
        'title': '港股公司信息',
        'doc_file': '港股公司信息.md',
        'original_api': 'get_company_hk',
        'params': ('trade_code',),
    },
    'eastmoney_hk_index_daily_kline': {
        'path': 'api/v1/market/data/eastmoney-hk-index-daily-kline',
        'title': '东方财富港股指数日K',
        'doc_file': '东方财富港股指数日K.md',
        'original_api': 'get_eastmoney_hk_index_daily_kline',
        'params': ('index_code', 'trade_date', 'start_date', 'end_date', 'page', 'page_size'),
    },
    'hk_balance_bank': {
        'path': 'api/v1/market/data/hk/hk-balance-bank',
        'title': '港股资产负债表',
        'doc_file': '港股资产负债表.md',
        'original_api': 'hk_balance_bank',
        'params': ('trade_code', 'year', 'report_type', 'start_date', 'end_date', 'page', 'page_size'),
    },
    'hk_balance_gene': {
        'path': 'api/v1/market/data/hk/hk-balance-gene',
        'title': '港股资产负债表',
        'doc_file': '港股资产负债表.md',
        'original_api': 'hk_balance_gene',
        'params': ('trade_code', 'year', 'report_type', 'start_date', 'end_date', 'page', 'page_size'),
    },
    'hk_balance_insur': {
        'path': 'api/v1/market/data/hk/hk-balance-insur',
        'title': '港股资产负债表',
        'doc_file': '港股资产负债表.md',
        'original_api': 'hk_balance_insur',
        'params': ('trade_code', 'year', 'report_type', 'start_date', 'end_date', 'page', 'page_size'),
    },
    'hk_basinfo_get': {
        'path': 'api/v1/market/data/hk/hk-view',
        'title': '港股个股信息',
        'doc_file': '港股个股信息.md',
        'original_api': 'get_hk_basinfo_get',
        'params': ('hk_code',),
    },
    'hk_basinfo_post': {
        'path': 'api/v1/market/data/hk/hk-view',
        'title': '港股个股信息',
        'doc_file': '港股个股信息.md',
        'original_api': 'get_hk_basinfo_post',
        'params': ('hk_code',),
    },
    'hk_candlesticks': {
        'path': 'api/v1/market/data/hk/hk-candlesticks',
        'title': '港股K线',
        'doc_file': '港股K线.md',
        'original_api': 'get_hk_candlesticks',
        'params': ('trade_code', 'interval_unit', 'until_date', 'since_date', 'interval_value', 'limit', 'adjust_kind'),
    },
    'hk_cashflow': {
        'path': 'api/v1/market/data/hk/hk-cashflow',
        'title': '港股现金流量表',
        'doc_file': '港股现金流量表.md',
        'original_api': 'hk_cashflow',
        'params': ('stock_code', 'year', 'report_type', 'start_date', 'end_date', 'page', 'page_size'),
    },
    'hk_income_bank': {
        'path': 'api/v1/market/data/hk/hk-income-bank',
        'title': '港股利润表',
        'doc_file': '港股利润表.md',
        'original_api': 'hk_income_bank',
        'params': ('trade_code', 'year', 'report_type', 'start_date', 'end_date', 'page', 'page_size'),
    },
    'hk_income_gene': {
        'path': 'api/v1/market/data/hk/hk-income-gene',
        'title': '港股利润表',
        'doc_file': '港股利润表.md',
        'original_api': 'hk_income_gene',
        'params': ('trade_code', 'year', 'report_type', 'start_date', 'end_date', 'page', 'page_size'),
    },
    'hk_income_insur': {
        'path': 'api/v1/market/data/hk/hk-income-insur',
        'title': '港股利润表',
        'doc_file': '港股利润表.md',
        'original_api': 'hk_income_insur',
        'params': ('trade_code', 'year', 'report_type', 'start_date', 'end_date', 'page', 'page_size'),
    },
    'hk_valuatnanalyd': {
        'path': 'api/v1/market/data/hk/hk-valuatnanalyd',
        'title': '港股估值分析',
        'doc_file': '港股估值分析.md',
        'original_api': 'get_hk_valuatnanalyd',
        'params': ('trade_code', 'page', 'page_size'),
    },
    'market_cap_hk': {
        'path': 'api/v1/market/data/hk/market-cap-hk',
        'title': '港股市值',
        'doc_file': '港股市值.md',
        'original_api': 'get_market_cap_hk',
        'params': ('trade_code',),
    },
})
