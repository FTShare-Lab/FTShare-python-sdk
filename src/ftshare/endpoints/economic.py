"""Economic endpoints generated from ftshare-doc."""

from __future__ import annotations

from .types import Endpoint, build_endpoints


ENDPOINTS: dict[str, Endpoint] = build_endpoints({
    'baidu_financial_calendar': {
        'path': 'api/v1/market/data/finance/financial-calendar/baidu',
        'title': '百度财经日历',
        'doc_file': '百度财经日历.md',
        'original_api': 'baidu_financial_calendar',
        'params': ('start_date', 'end_date', 'category', 'page', 'page_size'),
    },
    'consumer_credit_monthly': {
        'path': 'api/v1/market/data/economic/china-credit-loans',
        'title': '社融信贷',
        'doc_file': '社融信贷.md',
        'original_api': 'consumer_credit_monthly',
        'params': ('page', 'page_size'),
        'max_page_size': 200,
    },
    'consumer_customs_trade_monthly': {
        'path': 'api/v1/market/data/economic/china-customs-trade',
        'title': '进出口',
        'doc_file': '进出口.md',
        'original_api': 'consumer_customs_trade_monthly',
    },
    'consumer_fiscal_revenue_monthly': {
        'path': 'api/v1/market/data/economic/china-fiscal-revenue',
        'title': '财政收入',
        'doc_file': '财政收入.md',
        'original_api': 'consumer_fiscal_revenue_monthly',
    },
    'consumer_fixed_asset_monthly': {
        'path': 'api/v1/market/data/economic/china-fixed-asset-investment',
        'title': '固定资产投资',
        'doc_file': '固定资产投资.md',
        'original_api': 'consumer_fixed_asset_monthly',
    },
    'consumer_gdp_quarterly': {
        'path': 'api/v1/market/data/economic/china-gdp',
        'title': 'GDP',
        'doc_file': 'GDP.md',
        'original_api': 'consumer_gdp_quarterly',
    },
    'consumer_industrial_added_value_monthly': {
        'path': 'api/v1/market/data/economic/china-industrial-added-value',
        'title': '工业增加值',
        'doc_file': '工业增加值.md',
        'original_api': 'consumer_industrial_added_value_monthly',
    },
    'consumer_money_supply_monthly': {
        'path': 'api/v1/market/data/economic/china-money-supply',
        'title': '货币供应',
        'doc_file': '货币供应.md',
        'original_api': 'consumer_money_supply_monthly',
        'params': ('page', 'page_size'),
        'max_page_size': 200,
    },
    'consumer_pmi_monthly': {
        'path': 'api/v1/market/data/economic/china-pmi',
        'title': 'PMI',
        'doc_file': 'PMI.md',
        'original_api': 'consumer_pmi_monthly',
        'params': ('page', 'page_size'),
        'max_page_size': 200,
    },
    'consumer_ppi_monthly': {
        'path': 'api/v1/market/data/economic/china-ppi',
        'title': 'PPI',
        'doc_file': 'PPI.md',
        'original_api': 'consumer_ppi_monthly',
        'params': ('page', 'page_size'),
        'max_page_size': 200,
    },
    'consumer_price_index_monthly': {
        'path': 'api/v1/market/data/economic/china-cpi',
        'title': 'CPI',
        'doc_file': 'CPI.md',
        'original_api': 'consumer_price_index_monthly',
        'params': ('page', 'page_size'),
        'max_page_size': 200,
    },
    'consumer_retail_sales_monthly': {
        'path': 'api/v1/market/data/economic/china-retail-sales',
        'title': '社零',
        'doc_file': '社零.md',
        'original_api': 'consumer_retail_sales_monthly',
    },
    'lpr_monthly': {
        'path': 'api/v1/market/data/economic/china-lpr',
        'title': 'LPR',
        'doc_file': 'LPR.md',
        'original_api': 'lpr_monthly',
    },
    'reserve_ratio_monthly': {
        'path': 'api/v1/market/data/economic/china-reserve-ratio',
        'title': '存款准备金率',
        'doc_file': '存款准备金率.md',
        'original_api': 'reserve_ratio_monthly',
    },
    'tax_revenue_monthly': {
        'path': 'api/v1/market/data/economic/china-tax-revenue',
        'title': '税收',
        'doc_file': '税收.md',
        'original_api': 'tax_revenue_monthly',
    },
    'us_economic': {
        'path': 'api/v1/market/data/economic/us-economic',
        'title': '美国经济指标',
        'doc_file': '美国经济指标.md',
        'original_api': 'us_economic',
        'params': ('type',),
    },
    'wallstreetcn_financial_calendar': {
        'path': 'api/v1/market/data/finance/financial-calendar/wallstreetcn',
        'title': '华尔街见闻财经日历',
        'doc_file': '华尔街见闻财经日历.md',
        'original_api': 'wallstreetcn_financial_calendar',
        'params': ('start_date', 'end_date', 'page', 'page_size'),
    },
    'hibor_daily': {
        'path': 'api/v1/market/data/hibor-daily',
        'title': 'HIBOR日度利率',
        'doc_file': 'HIBOR日度利率.md',
        'original_api': 'hibor_daily',
        'params': ('start_date', 'end_date', 'page', 'page_size'),
    },

    'shibor_quote_daily': {
        'path': 'api/v1/market/data/shibor-quote-daily',
        'title': 'SHIBOR报价日度',
        'doc_file': 'SHIBOR报价日度.md',
        'original_api': 'shibor_quote_daily',
        'params': ('start_date', 'end_date', 'bank', 'page', 'page_size'),
    },

    'shibor_daily': {
        'path': 'api/v1/market/data/shibor-daily',
        'title': 'SHIBOR日度利率',
        'doc_file': 'SHIBOR日度利率.md',
        'original_api': 'shibor_daily',
        'params': ('start_date', 'end_date', 'page', 'page_size'),
    },

    'chinabond_yield_daily': {
        'path': 'api/v1/market/data/chinabond-yield-daily',
        'title': '中债收益率曲线日度',
        'doc_file': '中债收益率曲线日度.md',
        'original_api': 'chinabond_yield_daily',
        'params': ('start_date', 'end_date', 'curve_name', 'page', 'page_size'),
    },

    'libor_daily': {
        'path': 'api/v1/market/data/libor-daily',
        'title': '国际基准利率日度',
        'doc_file': '国际基准利率日度.md',
        'original_api': 'libor_daily',
        'params': ('start_date', 'end_date', 'currency', 'tenor', 'page', 'page_size'),
    },

    'wz_index_daily': {
        'path': 'api/v1/market/data/wz-index-daily',
        'title': '温州民间融资综合利率指数日度',
        'doc_file': '温州民间融资综合利率指数日度.md',
        'original_api': 'wz_index_daily',
        'params': ('start_date', 'end_date', 'page', 'page_size'),
    },

})
