"""ETF endpoints generated from ftshare-doc."""

from __future__ import annotations

from .types import Endpoint, build_endpoints


ENDPOINTS: dict[str, Endpoint] = build_endpoints({
    'etf_adjust_factor': {
        'path': 'api/v1/market/data/etf-adjust-factor',
        'title': 'ETF复权因子',
        'doc_file': 'ETF复权因子.md',
        'original_api': 'etf_adjust_factor',
        'params': ('symbol', 'trade_date', 'start_date', 'end_date', 'offset', 'limit'),
    },
    'etf_components': {
        'path': 'api/v1/market/data/etf-component',
        'title': 'ETF成份股',
        'doc_file': 'ETF成份股.md',
        'original_api': 'get_etf_components_handler',
        'params': ('symbol',),
    },
    'etf_components_all': {
        'path': 'api/v1/market/data/etf-components-all',
        'title': 'ETF成份列表',
        'doc_file': 'ETF成份列表.md',
        'original_api': 'etf_components_all',
    },
    'etf_description_all': {
        'path': 'api/v1/market/data/etf-description-all',
        'title': 'ETF基础信息',
        'doc_file': 'ETF基础信息.md',
        'original_api': 'etf_description_all',
    },
    'etf_fund_export': {
        'path': 'api/v1/market/data/etf/zhitou-etf',
        'title': '指数ETF基金导出',
        'doc_file': '指数ETF基金导出.md',
        'original_api': 'etf_fund_export',
        'params': ('request_id', 'page', 'page_size'),
    },
    'etf_pcf_list': {
        'path': 'api/v1/market/data/etf-pcf/etf-pcfs',
        'title': 'ETF-PCF清单列表',
        'doc_file': 'ETF-PCF清单列表.md',
        'original_api': 'etf_pcf_list_handler',
        'params': ('date', 'page', 'page_size'),
        'max_page_size': 100,
    },
    'etf_pre': {
        'path': 'api/v1/market/data/etf-pre-data',
        'title': 'ETF盘前数据',
        'doc_file': 'ETF盘前数据.md',
        'original_api': 'get_etf_pre',
        'params': ('date',),
    },
    'etf_pre_single': {
        'path': 'api/v1/market/data/etf-pre-single',
        'title': '单只ETF盘前数据',
        'doc_file': '单只ETF盘前数据.md',
        'original_api': 'get_etf_pre_single_handler',
        'params': ('symbol', 'date'),
    },
})
