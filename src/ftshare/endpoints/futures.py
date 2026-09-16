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
    'futures_minutes': {
        'path': 'api/v2/market/data/futures_minutes',
        'title': '期货历史分钟行情',
        'doc_file': '期货历史分钟行情.md',
        'original_api': 'futures_minutes',
        'params': ('symbol', 'interval', 'start', 'end', 'limit'),
    },
    'futures_contract_kline': {
        'path': 'api/v1/market/data/futures/kline',
        'title': '期货行情',
        'doc_file': '期货行情.md',
        'original_api': 'futures_contract_kline',
        'params': ('symbol', 'interval', 'start', 'end', 'limit'),
    },
    'futures_minutes_realtime': {
        'path': 'api/v4/market/data/futures_minutes/realtime',
        'title': '期货实时分钟K线',
        'doc_file': '期货实时分钟K线.md',
        'original_api': 'futures_minutes_realtime',
        'params': ('symbols',),
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
    'fut_wsr': {
        'path': 'api/v1/market/data/futures/fut-wsr',
        'title': '期货仓单日报',
        'doc_file': '期货仓单日报.md',
        'original_api': 'fut_wsr',
        'params': ('trade_date', 'start_date', 'end_date', 'symbol', 'exchange', 'page', 'page_size'),
    },

    'fut_weekly_detail': {
        'path': 'api/v1/market/data/futures/fut-weekly-detail',
        'title': '期货主要品种交易周报',
        'doc_file': '期货主要品种交易周报.md',
        'original_api': 'fut_weekly_detail',
        'params': ('week', 'prd', 'start_week', 'end_week', 'exchange', 'page', 'page_size'),
    },

    'fut_settle': {
        'path': 'api/v1/market/data/futures/fut-settle',
        'title': '期货每日结算参数',
        'doc_file': '期货每日结算参数.md',
        'original_api': 'fut_settle',
        'params': ('ts_code', 'trade_date', 'start_date', 'end_date', 'exchange', 'page', 'page_size'),
    },

    'ft_limit': {
        'path': 'api/v1/market/data/futures/ft-limit',
        'title': '期货合约涨跌停价',
        'doc_file': '期货合约涨跌停价.md',
        'original_api': 'ft_limit',
        'params': ('ts_code', 'trade_date', 'start_date', 'end_date', 'cont', 'exchange', 'page', 'page_size'),
    },

    'futures_nanhua_index_kline': {
        'path': 'api/v1/market/data/futures/nanhua-index-kline',
        'title': '南华期货指数日K线',
        'doc_file': '南华期货指数日K线.md',
        'original_api': 'futures_nanhua_index_kline',
        'params': ('code', 'trade_date', 'start_date', 'end_date', 'page', 'page_size'),
    },

    'eastmoney_futures_strange': {
        'path': 'api/v1/market/data/eastmoney-futures-strange',
        'title': '东方财富期货龙虎榜',
        'doc_file': '东方财富期货龙虎榜.md',
        'original_api': 'eastmoney_futures_strange',
        'params': ('exchange', 'variety', 'contract', 'trade_date'),
    },
    'member_build_process': {
        'path': 'api/v2/market/data/member-build-process',
        'title': '会员建仓过程',
        'doc_file': '会员建仓过程.md',
        'original_api': 'member_build_process',
        'params': ('exchange', 'member_name', 'instrument_id', 'start_date', 'end_date', 'contract_multiplier', 'page', 'page_size'),
    },
    'member_position_ranking': {
        'path': 'api/v2/market/data/member-position-ranking',
        'title': '会员持仓排名',
        'doc_file': '会员持仓排名.md',
        'original_api': 'member_position_ranking',
        'params': ('exchange', 'instrument_id', 'trade_date', 'direction', 'page', 'page_size'),
    },
    'futures_minutes_batch': {
        'path': 'api/v2/market/data/futures_minutes/batch',
        'title': '批量期货历史分钟行情',
        'doc_file': '批量期货历史分钟行情.md',
        'original_api': 'futures_minutes_batch',
        'params': ('symbols', 'interval', 'start', 'end', 'limit'),
    },

})
