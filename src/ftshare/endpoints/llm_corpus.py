"""LLM corpus endpoints generated from ftshare-doc."""

from __future__ import annotations

from .types import Endpoint, build_endpoints


ENDPOINTS: dict[str, Endpoint] = build_endpoints({
    'semantic_search_news': {
        'path': 'api/v1/market/data/semantic-search-news',
        'title': '新闻语义搜索',
        'doc_file': '新闻语义搜索.md',
        'original_api': 'semantic_search_news_handler',
        'params': ('query', 'limit', 'year', 'start_time', 'end_time'),
    },
    'shareholders_meeting': {
        'path': 'api/v1/market/data/corporate/meeting',
        'title': '股东大会',
        'doc_file': '股东大会.md',
        'original_api': 'shareholders_meeting',
        'params': ('page', 'page_size'),
    },
    'stock_announcements': {
        'path': 'api/v1/market/data/announcements/stock-announcements',
        'title': '公告列表',
        'doc_file': '公告列表.md',
        'original_api': 'stock_announcements',
        'params': ('stock_code', 'start_date', 'end_date', 'type', 'page', 'page_size'),
    },
    'stock_reports': {
        'path': 'api/v1/market/data/report/stock-reports',
        'title': '研报列表',
        'doc_file': '研报列表.md',
        'original_api': 'stock_reports',
        'params': ('stock_code', 'start_date', 'end_date', 'type', 'page', 'page_size'),
    },
    'type_reports': {
        'path': 'api/v1/market/data/report/type-reports',
        'title': '研报分类',
        'doc_file': '研报分类.md',
        'original_api': 'type_reports',
        'params': ('rept_type', 'start_date', 'end_date', 'page', 'page_size'),
    },
})
