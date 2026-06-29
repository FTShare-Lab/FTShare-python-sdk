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
})
