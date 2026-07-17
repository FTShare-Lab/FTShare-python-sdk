"""Bond endpoints generated from ftshare-doc."""

from __future__ import annotations

from .types import Endpoint, build_endpoints


ENDPOINTS: dict[str, Endpoint] = build_endpoints({
    'cb_base_data': {
        'path': 'api/v1/market/data/cb/cb-base-data',
        'title': '可转债基础数据',
        'doc_file': '可转债基础数据.md',
        'original_api': 'get_cb_base_data_handler',
        'params': ('symbol_code',),
    },
    'cb_lists': {
        'path': 'api/v1/market/data/cb/cb-lists',
        'title': '可转债列表',
        'doc_file': '可转债列表.md',
        'original_api': 'get_cb_lists_handler',
    },
    'convertible_bond_candlesticks': {
        'path': 'api/v1/market/data/convertible-bond-candlesticks',
        'title': '可转债K线',
        'doc_file': '可转债K线.md',
        'original_api': 'convertible_bond_candlesticks',
        'method': 'POST',
        'params': ('symbol', 'interval_unit', 'interval_value', 'adjust_kind', 'since_ts_millis', 'until_ts_millis', 'limit'),
    },
    'convertible_bond_candlesticks_batch': {
        'path': 'api/v1/market/data/convertible-bond-candlesticks/batch',
        'title': '批量可转债K线',
        'doc_file': '批量可转债K线.md',
        'original_api': 'convertible_bond_candlesticks_batch',
        'method': 'POST',
        'params': ('symbols', 'interval_unit', 'interval_value', 'adjust_kind', 'since_ts_millis', 'until_ts_millis', 'limit'),
    },
})
