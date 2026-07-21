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
    'fund_share': {
        'path': 'api/v1/market/data/fund/fund-share',
        'title': '基金份额',
        'doc_file': '基金份额.md',
        'original_api': 'get_fund_share',
        'params': ('fund_code', 'stati_perd', 'start_date', 'end_date', 'page', 'page_size'),
    },
    'fund_company': {
        'path': 'api/v1/market/data/fund/fund-company',
        'title': '基金公司',
        'doc_file': '基金公司.md',
        'original_api': 'get_fund_company',
        'params': ('fund_company', 'page', 'page_size'),
    },
    'fund_net_value_performance': {
        'path': 'api/v1/market/data/fund/fund-net-value-performance',
        'title': '基金净值收益表现',
        'doc_file': '基金净值收益表现.md',
        'original_api': 'get_fund_net_value_performance',
        'params': ('fund_code', 'stat_date', 'start_date', 'end_date', 'page', 'page_size'),
    },
    'fund_net_value': {
        'path': 'api/v1/market/data/fund/fund-net-value',
        'title': '基金净值明细',
        'doc_file': '基金净值明细.md',
        'original_api': 'get_fund_net_value',
        'params': ('fund_code', 'nav_date', 'start_date', 'end_date', 'page', 'page_size'),
    },
    'fund_classification': {
        'path': 'api/v1/market/data/fund/fund-classification',
        'title': '基金分类',
        'doc_file': '基金分类.md',
        'original_api': 'get_fund_classification',
        'params': ('fund_code', 'classify_std'),
    },
    'fund_list': {
        'path': 'api/v1/market/data/fund/fund-list',
        'title': '基金列表',
        'doc_file': '基金列表.md',
        'original_api': 'get_fund_list',
        'params': ('fund_code', 'fund_type', 'page', 'page_size'),
    },
    'fund_portfolio': {
        'path': 'api/v1/market/data/fund/fund-portfolio',
        'title': '基金持仓明细',
        'doc_file': '基金持仓明细.md',
        'original_api': 'get_fund_portfolio',
        'params': ('fund_code', 'report_date', 'publish_date', 'start_date', 'end_date', 'page', 'page_size'),
    },
    'fund_holder_structure': {
        'path': 'api/v1/market/data/fund/fund-holder-structure',
        'title': '基金持有人结构',
        'doc_file': '基金持有人结构.md',
        'original_api': 'get_fund_holder_structure',
        'params': ('fund_code', 'report_type', 'start_date', 'end_date'),
    },
    'fund_new_found': {
        'path': 'api/v1/market/data/fund/fund-new-found',
        'title': '基金新发',
        'doc_file': '基金新发.md',
        'original_api': 'get_fund_new_found',
        'params': ('start_date', 'end_date', 'fund_type', 'page', 'page_size'),
    },
    'fund_manager': {
        'path': 'api/v1/market/data/fund/fund-manager',
        'title': '基金经理任职关系',
        'doc_file': '基金经理任职关系.md',
        'original_api': 'get_fund_manager',
        'params': ('fund_code', 'fund_manager', 'is_inoffice', 'page', 'page_size'),
    },
    'fund_daily': {
        'path': 'api/v1/market/data/fund/fund-daily',
        'title': '基金行情日线',
        'doc_file': '基金行情日线.md',
        'original_api': 'get_fund_daily',
        'params': ('fund_code', 'trade_date', 'start_date', 'end_date', 'page', 'page_size'),
    },
    'fund_fee': {
        'path': 'api/v1/market/data/fund/fund-fee',
        'title': '基金费率',
        'doc_file': '基金费率.md',
        'original_api': 'get_fund_fee',
        'params': ('fund_code', 'charge_type', 'client_type', 'page', 'page_size'),
    },
    'fund_asset_allocation': {
        'path': 'api/v1/market/data/fund/fund-asset-allocation',
        'title': '基金资产配置',
        'doc_file': '基金资产配置.md',
        'original_api': 'get_fund_asset_allocation',
        'params': ('fund_code', 'report_date', 'publish_date', 'start_date', 'end_date', 'page', 'page_size'),
    },
    'fund_risk_level': {
        'path': 'api/v1/market/data/fund/fund-risk-level',
        'title': '基金风险等级',
        'doc_file': '基金风险等级.md',
        'original_api': 'get_fund_risk_level',
        'params': ('fund_code', 'history'),
    },
    'fund_index_fund': {
        'path': 'api/v1/market/data/fund/index-fund',
        'title': '指数跟踪基金',
        'doc_file': '指数跟踪基金.md',
        'original_api': 'get_fund_index_fund',
        'params': ('index_code', 'scope'),
    },
})
