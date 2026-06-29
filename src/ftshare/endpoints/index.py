"""Index endpoints generated from ftshare-doc."""

from __future__ import annotations

from .types import Endpoint, build_endpoints


ENDPOINTS: dict[str, Endpoint] = build_endpoints({
    'global_index_daily_kline': {
        'path': 'api/v1/market/data/global-index/daily-kline',
        'title': '全球指数日K线',
        'doc_file': '全球指数日K线.md',
        'original_api': 'global_index_daily_kline',
        'params': ('secid', 'start_date', 'end_date'),
    },
    'index_description_all': {
        'path': 'api/v1/market/data/index-description-all',
        'title': '指数基础信息',
        'doc_file': '指数基础信息.md',
        'original_api': 'index_description_all',
    },
    'index_description_list': {
        'path': 'api/v1/market/data/index/index_description',
        'title': '中证指数描述列表',
        'doc_file': '中证指数描述列表.md',
        'original_api': 'index_description_list_handler',
        'params': ('page', 'page_size'),
        'max_page_size': 100,
    },
    'index_weight_list': {
        'path': 'api/v1/market/data/index/index_weight',
        'title': '指数权重列表',
        'doc_file': '指数权重列表.md',
        'original_api': 'index_weight_list_handler',
        'params': ('index_code', 'date', 'page', 'page_size'),
        'max_page_size': 100,
    },
    'index_weight_summary': {
        'path': 'api/v1/market/data/index/index_weight_summary',
        'title': '指数权重汇总',
        'doc_file': '指数权重汇总.md',
        'original_api': 'index_weight_summary_handler',
        'params': ('page', 'page_size'),
        'max_page_size': 100,
    },
    'sw_industry_constituent_history': {
        'path': 'api/v1/market/data/sw-industry/constituent-history',
        'title': '申万行业成份股历史',
        'doc_file': '申万行业成份股历史.md',
        'original_api': 'sw_industry_constituent_history',
        'params': ('industry_code',),
    },
    'sw_industry_daily_metrics': {
        'path': 'api/v1/market/data/sw-industry/daily-metrics',
        'title': '申万行业日度指标',
        'doc_file': '申万行业日度指标.md',
        'original_api': 'sw_industry_daily_metrics',
        'params': ('level', 'start_date', 'end_date', 'industry_code', 'page', 'page_size'),
    },
    'sw_industry_overview': {
        'path': 'api/v1/market/data/sw-industry/overview',
        'title': '申万行业总览',
        'doc_file': '申万行业总览.md',
        'original_api': 'sw_industry_overview',
        'params': ('date', 'level', 'page', 'page_size'),
    },
})
