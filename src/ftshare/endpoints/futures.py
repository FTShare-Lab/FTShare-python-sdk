"""Futures endpoints generated from ftshare-doc."""

from __future__ import annotations

from .types import Endpoint, build_endpoints


ENDPOINTS: dict[str, Endpoint] = build_endpoints({
    'china_futures_base_data': {
        'path': 'api/v1/market/data/futures/futures-base-data',
        'title': '中国期货基础数据',
        'doc_file': '中国期货基础数据.md',
        'original_api': 'get_china_futures_base_data_handler',
        'params': ('trade_date', 'symbol'),
    },
    'china_futures_lists': {
        'path': 'api/v1/market/data/futures/futures-lists',
        'title': '中国期货列表',
        'doc_file': '中国期货列表.md',
        'original_api': 'get_china_futures_lists_handler',
        'params': ('trade_date',),
    },
    'eastmoney_futures_position': {
        'path': 'api/v1/market/data/eastmoney-futures-position',
        'title': '东方财富期货持仓',
        'doc_file': '东方财富期货持仓.md',
        'original_api': 'get_eastmoney_futures_position',
        'params': ('exchange', 'variety_code', 'contract_code', 'trade_date', 'start_date', 'end_date', 'member_name_abbr', 'page', 'page_size'),
    },
    'futures_contract_kline': {
        'path': 'api/v1/market/data/futures/kline',
        'title': '期货合约K线',
        'doc_file': '期货合约K线.md',
        'original_api': 'futures_contract_kline',
        'params': ('symbol', 'interval', 'start', 'end', 'limit'),
    },
    'major_contract': {
        'path': 'api/v1/market/data/corporate/contract',
        'title': '重大合同',
        'doc_file': '重大合同.md',
        'original_api': 'major_contract',
        'params': ('start_date', 'end_date'),
        'max_page_size': 3,
    },
    'major_contract_by_symbol': {
        'path': 'api/v1/market/data/corporate/contract/by-symbol',
        'title': '重大合同按标的',
        'doc_file': '重大合同按标的.md',
        'original_api': 'major_contract_by_symbol',
        'params': ('symbol', 'page', 'page_size'),
    },
    'major_contract_summary': {
        'path': 'api/v1/market/data/corporate/contract/summary',
        'title': '重大合同汇总',
        'doc_file': '重大合同汇总.md',
        'original_api': 'major_contract_summary',
        'params': ('page', 'page_size'),
    },
    'eastmoney_futures_strange': {
        'path': 'api/v1/market/data/eastmoney-futures-position',
        'title': '东方财富期货持仓',
        'doc_file': '东方财富期货持仓.md',
        'original_api': 'get_eastmoney_futures_position',
        'params': ('exchange', 'variety_code', 'contract_code', 'trade_date', 'start_date', 'end_date', 'member_name_abbr', 'page', 'page_size'),
    },
    'futures_kline': {
        'path': 'api/v1/market/data/futures/kline',
        'title': '期货合约K线',
        'doc_file': '期货合约K线.md',
        'original_api': 'futures_contract_kline',
        'params': ('symbol', 'interval', 'start', 'end', 'limit'),
    },
})
