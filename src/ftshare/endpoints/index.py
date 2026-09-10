"""Index endpoints generated from ftshare-doc."""

from __future__ import annotations

from .types import Endpoint, build_endpoints


ENDPOINTS: dict[str, Endpoint] = build_endpoints({
    'global_index_daily_kline': {
        'path': 'api/v1/market/data/global-index/daily-kline',
        'title': '全球指数日K线',
        'doc_file': '全球指数日K线.md',
        'original_api': 'global_index_daily_kline',
        'params': ('secid', 'start_date', 'end_date', 'limit'),
    },
    'index_candlesticks': {
        'path': 'api/v1/market/data/index-candlesticks',
        'title': '指数K线',
        'doc_file': '指数K线.md',
        'original_api': 'index_candlesticks',
        'method': 'GET',
        'params': ('symbol', 'interval_unit', 'interval_value', 'adjust_kind', 'since_ts_millis', 'until_ts_millis', 'limit'),
    },
    'index_description_all': {
        'path': 'api/v1/market/data/index-description-all',
        'title': '指数基础信息',
        'doc_file': '指数基础信息.md',
        'original_api': 'index_description_all',
        'params': ('page', 'page_size'),
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
        'params': ('index_code', 'page', 'page_size'),
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
    'index_minutes': {
        'path': 'api/v2/market/data/index_minutes',
        'title': '指数历史分钟行情',
        'doc_file': '指数历史分钟行情.md',
        'original_api': 'index_minutes',
        'params': ('symbol', 'interval_value', 'since_ts_millis', 'until_ts_millis', 'limit'),
    },

    'index_realtime_minute_kline': {
        'path': 'api/v4/market/data/index-realtime-minute-kline',
        'title': '指数实时分钟K线',
        'doc_file': '指数实时分钟K线.md',
        'original_api': 'index_realtime_minute_kline',
        'params': ('symbols',),
    },

    'index_realtime_day_kline': {
        'path': 'api/v4/market/data/index-realtime-day-kline',
        'title': '指数实时日K线',
        'doc_file': '指数实时日K线.md',
        'original_api': 'index_realtime_day_kline',
        'params': ('symbols',),
    },

    'sw_index_history_minutes': {
        'path': 'api/v1/market/data/sw-index/history-minutes',
        'title': '申万指数历史分钟K线',
        'doc_file': '申万指数历史分钟K线.md',
        'original_api': 'sw_index_history_minutes',
        'params': ('index_code', 'start_date', 'end_date', 'page', 'page_size'),
    },
    'index_minutes_batch': {
        'path': 'api/v2/market/data/index_minutes/batch',
        'title': '批量指数历史分钟行情',
        'doc_file': '批量指数历史分钟行情.md',
        'original_api': 'index_minutes_batch',
        'params': ('symbols', 'interval_value', 'since_ts_millis', 'until_ts_millis', 'limit'),
    },

    'index_candlesticks_batch': {
        'path': 'api/v2/market/data/index-candlesticks/batch',
        'title': '批量指数K线',
        'doc_file': '批量指数K线.md',
        'original_api': 'index_candlesticks_batch',
        'params': ('symbols', 'interval_unit', 'adjust_kind', 'since_ts_millis', 'until_ts_millis', 'limit'),
    },

})
