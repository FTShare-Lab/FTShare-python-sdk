"""ETF endpoints generated from ftshare-doc."""

from __future__ import annotations

from .types import Endpoint, build_endpoints


ENDPOINTS: dict[str, Endpoint] = build_endpoints({
    'etf_adjust_factor': {
        'path': 'api/v1/market/data/etf-adjust-factor',
        'title': 'ETF复权因子',
        'doc_file': 'ETF复权因子.md',
        'original_api': 'etf_adjust_factor',
        'params': ('symbol', 'trade_date', 'start_date', 'end_date', 'page', 'page_size'),
    },
    'etf_candlesticks': {
        'path': 'api/v1/market/data/etf-candlesticks',
        'title': 'ETFK线',
        'doc_file': 'ETFK线.md',
        'original_api': 'etf_candlesticks',
        'method': 'GET',
        'params': ('symbol', 'interval_unit', 'interval_value', 'adjust_kind', 'since_ts_millis', 'until_ts_millis', 'limit'),
    },
    'etf_components_all': {
        'path': 'api/v2/market/data/etf-components-all',
        'title': 'ETF成份列表',
        'doc_file': 'ETF成份列表.md',
        'original_api': 'etf_components_all',
        'params': ('symbol',),
    },
    'etf_description_all': {
        'path': 'api/v2/market/data/etf-description-all',
        'title': 'ETF基础信息',
        'doc_file': 'ETF基础信息.md',
        'original_api': 'etf_description_all',
    },
    'etf_pcf_list': {
        'path': 'api/v2/market/data/etf-pcf/etf-pcfs',
        'title': 'ETF-PCF清单列表',
        'doc_file': 'ETF-PCF清单列表.md',
        'original_api': 'etf_pcf_list_handler',
        'params': ('date', 'page', 'page_size'),
        'max_page_size': 100,
    },
    'etf_pre': {
        'path': 'api/v2/market/data/etf-pre-data',
        'title': 'ETF盘前数据',
        'doc_file': 'ETF盘前数据.md',
        'original_api': 'get_etf_pre',
        'params': ('date',),
    },
    'etf_pre_single': {
        'path': 'api/v2/market/data/etf-pre-single',
        'title': '单只ETF盘前数据',
        'doc_file': '单只ETF盘前数据.md',
        'original_api': 'get_etf_pre_single_handler',
        'params': ('symbol', 'date'),
    },
    'etf_minutes': {
        'path': 'api/v2/market/data/etf_minutes',
        'title': 'ETF历史分钟行情',
        'doc_file': 'ETF历史分钟行情.md',
        'original_api': 'etf_minutes',
        'params': ('symbol', 'interval_value', 'adjust_kind', 'since_ts_millis', 'until_ts_millis', 'limit'),
    },

    'etf_realtime_minute_kline': {
        'path': 'api/v4/market/data/etf-realtime-minute-kline',
        'title': 'ETF实时分钟K线',
        'doc_file': 'ETF实时分钟K线.md',
        'original_api': 'etf_realtime_minute_kline',
        'params': ('symbols',),
    },

    'etf_realtime_day_kline': {
        'path': 'api/v4/market/data/etf-realtime-day-kline',
        'title': 'ETF实时日K线',
        'doc_file': 'ETF实时日K线.md',
        'original_api': 'etf_realtime_day_kline',
        'params': ('symbols',),
    },

    'etf_minutes_batch': {
        'path': 'api/v2/market/data/etf_minutes/batch',
        'title': '批量ETF历史分钟行情',
        'doc_file': '批量ETF历史分钟行情.md',
        'original_api': 'etf_minutes_batch',
        'params': ('symbols', 'interval_value', 'adjust_kind', 'since_ts_millis', 'until_ts_millis', 'limit'),
    },

    'etf_announcements': {
        'path': 'api/v2/market/data/announcements/etf-announcements',
        'title': 'ETF公告列表',
        'doc_file': 'ETF公告列表.md',
        'original_api': 'etf_announcements',
        'params': ('etf_code', 'start_date', 'end_date', 'page', 'page_size'),
    },

    'etf_candlesticks_batch': {
        'path': 'api/v2/market/data/etf-candlesticks/batch',
        'title': '批量ETFK线',
        'doc_file': '批量ETFK线.md',
        'original_api': 'etf_candlesticks_batch',
        'params': ('symbols', 'interval_unit', 'adjust_kind', 'since_ts_millis', 'until_ts_millis', 'limit'),
    },

    'etf_component_details': {
        'path': 'api/v2/market/data/etf-component-details',
        'title': 'ETF成分证券明细',
        'doc_file': 'ETF成分证券明细.md',
        'original_api': 'etf_component_details',
        'params': ('symbol', 'trade_date'),
    },

    'etf_net_value': {
        'path': 'api/v2/market/data/etf-net-value',
        'title': 'ETF净值',
        'doc_file': 'ETF净值.md',
        'original_api': 'etf_net_value',
        'params': ('etf_code', 'nav_date', 'start_date', 'end_date', 'page', 'page_size'),
        'max_page_size': 200,
    },

    'etf_pcf_infos': {
        'path': 'api/v2/market/data/etf-pcf/etf-pcf-infos',
        'title': 'ETF申赎清单',
        'doc_file': 'ETF-PCF信息.md',
        'original_api': 'etf_pcf_infos',
        'params': ('symbol', 'trade_date', 'start_date', 'end_date', 'page', 'page_size'),
        'max_page_size': 500,
    },

    'etf_share': {
        'path': 'api/v2/market/data/etf-share',
        'title': 'ETF份额',
        'doc_file': 'ETF份额.md',
        'original_api': 'etf_share',
        'params': ('etf_code', 'stati_perd', 'start_date', 'end_date', 'page', 'page_size'),
        'max_page_size': 200,
    },

})
