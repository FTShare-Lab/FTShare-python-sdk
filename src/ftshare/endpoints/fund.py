"""Public fund endpoints generated from ftshare-doc."""

from __future__ import annotations

from .types import Endpoint, build_endpoints


ENDPOINTS: dict[str, Endpoint] = build_endpoints({
    'fund_basicinfo': {
        'path': 'api/v1/market/data/fund/fund-basicinfo',
        'title': '基金基础信息',
        'doc_file': '基金基础信息.md',
        'original_api': 'get_fund_basicinfo',
        'params': ('institution_code', 'page', 'page_size'),
    },
    'fund_cal_return': {
        'path': 'api/v1/market/data/fund/fund-cal-return',
        'title': '基金收益',
        'doc_file': '基金收益.md',
        'original_api': 'get_fund_cal_return',
        'params': ('institution_code', 'cal-type'),
    },
    'fund_nav': {
        'path': 'api/v1/market/data/fund/fund-nav',
        'title': '基金净值',
        'doc_file': '基金净值.md',
        'original_api': 'get_fund_nav',
        'params': ('institution_code', 'page', 'page_size'),
    },
    'fund_overview': {
        'path': 'api/v1/market/data/fund/fund-overview',
        'title': '基金总览',
        'doc_file': '基金总览.md',
        'original_api': 'get_fund_overview',
        'params': ('page', 'page_size'),
    },
    'fund_support_symbols': {
        'path': 'api/v1/market/data/fund/fund-support-symbols',
        'title': '基金支持标的',
        'doc_file': '基金支持标的.md',
        'original_api': 'get_fund_support_symbols',
        'params': ('page', 'page_size'),
    },
})
