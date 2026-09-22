"""Bond endpoints generated from ftshare-doc."""

from __future__ import annotations

from .types import Endpoint, build_endpoints


ENDPOINTS: dict[str, Endpoint] = build_endpoints({
    'convertible_bond_candlesticks': {
        'path': 'api/v1/market/data/convertible-bond-candlesticks',
        'title': '可转债历史K线',
        'doc_file': '可转债历史K线.md',
        'original_api': 'convertible_bond_candlesticks',
        'method': 'GET',
        'params': ('symbol', 'interval_unit', 'adjust_kind', 'since_ts_millis', 'until_ts_millis', 'limit'),
    },

    'convertible_bond_candlesticks_batch': {
        'path': 'api/v2/market/data/convertible-bond-candlesticks/batch',
        'title': '批量可转债历史K线',
        'doc_file': '批量可转债历史K线.md',
        'original_api': 'convertible_bond_candlesticks_batch',
        'params': ('symbols', 'interval_unit', 'adjust_kind', 'since_ts_millis', 'until_ts_millis', 'limit'),
    },

    'convertible_bond_minute_candlesticks': {
        'path': 'api/v2/market/data/convertible-bond-minute-candlesticks',
        'title': '可转债历史分钟K线',
        'doc_file': '可转债历史分钟K线.md',
        'original_api': 'convertible_bond_minute_candlesticks',
        'params': ('symbol', 'symbols', 'interval_value', 'since_ts_millis', 'until_ts_millis', 'limit'),
    },

    'convertible_bond_realtime_day_kline': {
        'path': 'api/v4/market/data/convertible-bond-realtime-day-kline',
        'title': '可转债实时日K线',
        'doc_file': '可转债实时日K线.md',
        'original_api': 'convertible_bond_realtime_day_kline',
        'params': ('symbols',),
    },

    'convertible_bond_realtime_minute_kline': {
        'path': 'api/v4/market/data/convertible-bond-realtime-minute-kline',
        'title': '可转债实时分钟K线',
        'doc_file': '可转债实时分钟K线.md',
        'original_api': 'convertible_bond_realtime_minute_kline',
        'params': ('symbols',),
    },

    'szse_convertible_bond_matching_trades': {
        'path': 'api/v1/market/data/convertible-bond/szse/matching-trades',
        'title': '深交所可转债匹配成交',
        'doc_file': '深交所可转债匹配成交.md',
        'original_api': 'szse_convertible_bond_matching_trades',
        'params': ('security_code', 'trade_date', 'start_date', 'end_date', 'page', 'page_size'),
    },

    'szse_convertible_bond_negotiated_trades': {
        'path': 'api/v1/market/data/convertible-bond/szse/negotiated-trades',
        'title': '深交所可转债协议成交',
        'doc_file': '深交所可转债协议成交.md',
        'original_api': 'szse_convertible_bond_negotiated_trades',
        'params': ('security_code', 'trade_date', 'start_date', 'end_date', 'page', 'page_size'),
    },

    'szse_convertible_bond_directed_trades': {
        'path': 'api/v1/market/data/convertible-bond/szse/directed-trades',
        'title': '深交所可转债定向成交',
        'doc_file': '深交所可转债定向成交.md',
        'original_api': 'szse_convertible_bond_directed_trades',
        'params': ('security_code', 'trade_date', 'start_date', 'end_date', 'page', 'page_size'),
    },

    'szse_convertible_bond_declaration_snapshots': {
        'path': 'api/v1/market/data/convertible-bond/szse/declaration-snapshots',
        'title': '深交所可转债申报快照',
        'doc_file': '深交所可转债申报快照.md',
        'original_api': 'szse_convertible_bond_declaration_snapshots',
        'params': ('security_code', 'trade_date', 'start_date', 'end_date', 'page', 'page_size'),
    },

    'cb_lists': {
        'path': 'api/v1/market/data/cb/cb-lists',
        'title': '可转债列表',
        'doc_file': '可转债列表.md',
        'original_api': 'cb_lists',
    },

})
