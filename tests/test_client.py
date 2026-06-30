from __future__ import annotations

import pytest
import pandas as pd

import ftshare as ft
from ftshare import FtshareAPIError, FtshareDecodeError, FtshareHTTPError
from ftshare.client import FtshareClient
from ftshare.endpoints import ENDPOINTS


class FakeResponse:
    def __init__(self, status_code=200, payload=None, text="{}", json_error=False):
        self.status_code = status_code
        self._payload = payload
        self.text = text
        self._json_error = json_error

    def json(self):
        if self._json_error:
            raise ValueError("not json")
        return self._payload


class FakeSession:
    def __init__(self, responses):
        self.responses = list(responses)
        self.calls = []

    def get(self, url, params=None, timeout=None, headers=None):
        self.calls.append(
            {
                "url": url,
                "params": params,
                "timeout": timeout,
                "headers": headers,
            }
        )
        return self.responses.pop(0)


def paginated_records(records, page=1, pages=1):
    return {
        "code": 0,
        "message": "success",
        "data": {
            "pageNum": page,
            "pageSize": 2,
            "total": len(records),
            "pages": pages,
            "records": records,
        },
    }


def test_default_base_url_and_set_base_url():
    assert ft.BASE_URL == "https://market.ft.tech/gateway/"
    assert ft.set_base_url("https://example.com/gateway") == "https://example.com/gateway/"
    assert ft.BASE_URL == "https://example.com/gateway/"
    client = ft.market_api()
    assert client.base_url == "https://example.com/gateway/"
    ft.set_base_url("https://market.ft.tech/gateway/")


def test_package_base_url_assignment_is_used_by_market_api():
    original = ft.BASE_URL
    ft.BASE_URL = "https://assigned.example.com/data/"
    try:
        assert ft.market_api().base_url == "https://assigned.example.com/data/"
    finally:
        ft.set_base_url(original)


def test_url_join_and_none_params_are_filtered():
    session = FakeSession([FakeResponse(payload={"items": [], "total_pages": 0, "total_items": 0})])
    client = FtshareClient(base_url="https://market.ft.tech/gateway/", session=session)

    client.stk_limit(symbol="000001.SZ", trade_date=None, page=1)

    assert session.calls[0]["url"] == "https://market.ft.tech/gateway/api/v1/market/data/stk-limit"
    assert session.calls[0]["params"] == {"symbol": "000001.SZ", "page": 1}


def test_data_prefix_is_not_duplicated():
    session = FakeSession([FakeResponse(payload={})])
    client = FtshareClient(base_url="https://market.ft.tech/gateway/", session=session)

    client.get("/data/api/v1/market/data/demo")

    assert session.calls[0]["url"] == "https://market.ft.tech/gateway/api/v1/market/data/demo"


def test_gateway_prefix_is_not_duplicated():
    session = FakeSession([FakeResponse(payload={})])
    client = FtshareClient(base_url="https://market.ft.tech/gateway/", session=session)

    client.get("/gateway/api/v1/market/data/demo")

    assert session.calls[0]["url"] == "https://market.ft.tech/gateway/api/v1/market/data/demo"


def test_get_defaults_to_extracted_records():
    session = FakeSession([FakeResponse(payload=paginated_records([{"id": 1}]))])
    client = FtshareClient(session=session)

    df = client.get("api/v1/market/data/demo")

    assert isinstance(df, pd.DataFrame)
    assert df.to_dict("records") == [{"id": 1}]


def test_get_as_dataframe_false_returns_records():
    session = FakeSession([FakeResponse(payload=paginated_records([{"id": 1}]))])
    client = FtshareClient(session=session)

    rows = client.get("api/v1/market/data/demo", as_dataframe=False)

    assert rows == [{"id": 1}]


def test_get_raw_true_returns_full_payload():
    payload = paginated_records([{"id": 1}])
    session = FakeSession([FakeResponse(payload=payload)])
    client = FtshareClient(session=session)

    assert client.get("api/v1/market/data/demo", raw=True) == payload


@pytest.mark.parametrize(
    ("method_name", "kwargs"),
    [
        ("stock_unlock_by_date", {"start_date": "2025-06-01", "end_date": "2025-06-30"}),
        ("stock_unlock", {"stock_code": "000001"}),
        ("yzxdr_detail", {"year": 2026, "quarter": 2}),
        (
            "eastmoney_futures_strange",
            {"exchange": "gfex", "variety": "多晶硅", "contract": "ps2609", "trade_date": "20260612"},
        ),
        ("eastmoney_us_stock_list", {}),
        ("eastmoney_us_stock_daily_ohlc", {"stock_code": "ADV"}),
        ("eastmoney_us_stock_latest_ohlc", {}),
        ("futures_kline", {"symbol": "A2605.DCE"}),
        ("company_list", {}),
        ("wallstreetcn_financial_calendar", {"start_date": "2026-05-01", "end_date": "2026-05-07"}),
        ("stk_limit", {}),
        ("stk_premarket", {}),
        ("baidu_financial_calendar", {"start_date": "2026-05-01", "end_date": "2026-05-07"}),
        ("stock_capital_flows", {}),
        ("stock_ggmx_sell_ranking", {}),
        ("stock_ggmx_buy_ranking", {}),
        ("stock_ggmx", {}),
        ("pledge_summary", {}),
        ("index_weight_summary", {"index_code": "000300"}),
    ],
)
def test_endpoint_methods_map_to_expected_paths(method_name, kwargs):
    session = FakeSession([FakeResponse(payload={"code": 0, "message": "success", "data": {"records": []}})])
    client = FtshareClient(session=session)

    getattr(client, method_name)(**kwargs)

    assert session.calls[0]["url"] == "https://market.ft.tech/gateway/" + ENDPOINTS[method_name].path


def test_all_documented_endpoints_are_available_as_client_methods():
    client = FtshareClient(session=FakeSession([]))
    assert len(ENDPOINTS) >= 180

    missing = [
        name
        for name, endpoint in ENDPOINTS.items()
        if endpoint.original_api and not hasattr(client, name)
    ]

    assert missing == []


def test_generated_method_docstring_includes_parameter_metadata():
    doc = FtshareClient.baidu_financial_calendar.__doc__ or ""

    assert "Endpoint: ``api/v1/market/data/finance/financial-calendar/baidu``" in doc
    assert "start_date: 起始日期 (type: string; required: Y)." in doc
    assert "category: 筛选大类" in doc
    assert "page_size: Rows per page." in doc


def test_http_error():
    session = FakeSession([FakeResponse(status_code=500, text="server error")])
    client = FtshareClient(session=session)

    with pytest.raises(FtshareHTTPError):
        client.stk_limit()


def test_decode_error():
    session = FakeSession([FakeResponse(text="<html>", json_error=True)])
    client = FtshareClient(session=session)

    with pytest.raises(FtshareDecodeError):
        client.stk_limit()


def test_api_error():
    session = FakeSession([FakeResponse(payload={"code": 1001, "message": "bad request"})])
    client = FtshareClient(session=session)

    with pytest.raises(FtshareAPIError):
        client.stk_limit()


def test_http_like_code_200_is_treated_as_success():
    session = FakeSession([FakeResponse(payload={"code": 200, "msg": "OK", "data": {"items": [{"id": 1}]}})])
    client = FtshareClient(session=session)

    df = client.etf_fund_export(request_id="demo-1")

    assert isinstance(df, pd.DataFrame)
    assert df.to_dict("records") == [{"id": 1}]


def test_search_uses_public_path_without_trailing_slash_and_q_param():
    session = FakeSession([FakeResponse(payload=[{"symbol": "600519.SH"}])])
    client = FtshareClient(session=session)

    rows = client.search(query="maotai", limit=1, as_dataframe=False)

    assert rows == [{"symbol": "600519.SH"}]
    assert session.calls[0]["url"] == "https://market.ft.tech/gateway/api/v1/market/security/search"
    assert session.calls[0]["params"] == {"q": "maotai", "limit": 1}


def test_path_parameter_is_substituted_into_endpoint_url():
    session = FakeSession([FakeResponse(payload=[])])
    client = FtshareClient(session=session)

    rows = client.stock_intraday(symbol="600000.XSHG", as_dataframe=False)

    assert rows == []
    assert session.calls[0]["url"] == "https://market.ft.tech/gateway/api/v1/market/security/600000.XSHG/intraday"
    assert session.calls[0]["params"] == {}


def test_path_parameter_and_query_parameters_are_separated():
    session = FakeSession([FakeResponse(payload=[])])
    client = FtshareClient(session=session)

    client.stock_related(symbol="000300.XSHG", limit=3)

    assert session.calls[0]["url"] == "https://market.ft.tech/gateway/api/v1/market/security/000300.XSHG/related"
    assert session.calls[0]["params"] == {"limit": 3}


def test_missing_path_parameter_raises_value_error():
    client = FtshareClient(session=FakeSession([]))

    with pytest.raises(ValueError, match="symbol is required in endpoint path"):
        client.stock_intraday()


def test_confirmed_todo_endpoints_map_to_public_server_paths():
    cases = [
        ("stock_trade", {"symbol": "600000.XSHG"}, "api/v1/market/data/daec/history/trades", {"symbol": "600000.XSHG"}),
        (
            "stock_prev_close",
            {"symbol": "600000.XSHG", "since": "20240501", "until": "20240531"},
            "api/v1/market/data/daec/history/prev-closes",
            {"symbol": "600000.XSHG", "since": "20240501", "until": "20240531"},
        ),
        (
            "stock_market",
            {"scope": "ChinaStock"},
            "api/v1/market/data/daec/market/snapshot",
            {"scope": "ChinaStock"},
        ),
        (
            "stock_market_distribution_intraday",
            {"scope": "ChinaStock"},
            "api/v1/market/data/daec/market/distribution-history",
            {"scope": "ChinaStock"},
        ),
        (
            "stock_intraday_prices",
            {"symbol": "600000.XSHG", "compat": "v2", "since": "TODAY"},
            "api/v1/market/data/daec/history/prices",
            {"symbol": "600000.XSHG", "compat": "v2", "since": "TODAY"},
        ),
        (
            "stock_ohlcs",
            {"symbol": "600000.XSHG", "compat": "v2", "span": "DAY1", "limit": 5},
            "api/v1/market/data/daec/history/ohlcs",
            {"symbol": "600000.XSHG", "compat": "v2", "span": "DAY1", "limit": 5},
        ),
    ]

    for method_name, kwargs, path, expected_params in cases:
        session = FakeSession([FakeResponse(payload=[])])
        client = FtshareClient(session=session)

        getattr(client, method_name)(**kwargs)

        assert session.calls[0]["url"] == "https://market.ft.tech/gateway/" + path
        assert session.calls[0]["params"] == expected_params


@pytest.mark.parametrize(
    ("kwargs", "message"),
    [
        (
            {"symbol": "600000.XSHG", "compat": "v2", "range": "Today", "since": "TODAY"},
            "cannot be combined with raw time parameters",
        ),
        (
            {"symbol": "600000.XSHG", "since": "TODAY"},
            "require compat='v2'",
        ),
        (
            {"symbol": "600000.XSHG", "range": "Today", "days": 5},
            "raw time parameters are mutually exclusive",
        ),
        (
            {"symbol": "600000.XSHG", "compat": "v2", "since": "TODAY", "since_ts_ms": 1782696600000},
            "v2 time parameters are mutually exclusive",
        ),
    ],
)
def test_stock_intraday_prices_rejects_mixed_daec_time_modes(kwargs, message):
    client = FtshareClient(session=FakeSession([]))

    with pytest.raises(ValueError, match=message):
        client.stock_intraday_prices(**kwargs)


@pytest.mark.parametrize(
    ("kwargs", "message"),
    [
        (
            {"symbol": "600000.XSHG", "span": "DAY1", "limit": 5},
            "require compat='v2'",
        ),
        (
            {"symbol": "600000.XSHG", "compat": "v2", "span": "DAY1", "interval": "Day"},
            "uses span instead of interval",
        ),
    ],
)
def test_stock_ohlcs_rejects_mixed_daec_modes(kwargs, message):
    client = FtshareClient(session=FakeSession([]))

    with pytest.raises(ValueError, match=message):
        client.stock_ohlcs(**kwargs)


def test_stock_market_list_families_format_board_path_parameters():
    cases = [
        (
            "stock_daec_stocks",
            {"board": "all", "page": 1, "page_size": 5, "filter": "close > 10", "order_by": "change_rate desc"},
            "api/v1/market/data/daec/stocks/all",
            {"filter": "close > 10", "order_by": "change_rate desc", "page": 1, "page_size": 5},
        ),
        (
            "stock_realtime_list",
            {"board": "chi-next", "page": 1, "page_size": 5},
            "api/v1/market/data/stock-list/chi-next",
            {"page": 1, "page_size": 5},
        ),
    ]

    for method_name, kwargs, path, expected_params in cases:
        session = FakeSession([FakeResponse(payload={"items": [], "total_pages": 0, "total_items": 0})])
        client = FtshareClient(session=session)

        getattr(client, method_name)(**kwargs)

        assert session.calls[0]["url"] == "https://market.ft.tech/gateway/" + path
        assert session.calls[0]["params"] == expected_params


def test_paginated_aliases_resolved_from_server_routes():
    session = FakeSession(
        [
            FakeResponse(payload={"items": [], "total_pages": 0, "total_items": 0}),
            FakeResponse(payload={"items": [], "total_pages": 0, "total_items": 0}),
        ]
    )
    client = FtshareClient(session=session)

    client.stock_ipos_paginated(page=1, page_size=50)
    client.stock_dividends_paginated(page=1, page_size=50)

    assert session.calls[0]["url"] == "https://market.ft.tech/gateway/api/v1/market/data/stock-ipos"
    assert session.calls[0]["params"] == {"page": 1, "page_size": 50}
    assert session.calls[1]["url"] == "https://market.ft.tech/gateway/api/v1/market/data/dividends"
    assert session.calls[1]["params"] == {"page": 1, "page_size": 50}


def test_endpoint_default_returns_dataframe_from_records():
    session = FakeSession([FakeResponse(payload=paginated_records([{"ts_code": "000001.SZ"}]))])
    client = FtshareClient(session=session)

    df = client.stk_limit()

    assert isinstance(df, pd.DataFrame)
    assert df.to_dict("records") == [{"ts_code": "000001.SZ"}]


def test_endpoint_default_returns_dataframe_from_items():
    session = FakeSession(
        [
            FakeResponse(
                payload={
                    "items": [{"ts_code": "000001.SZ"}],
                    "total_pages": 1,
                    "total_items": 1,
                }
            )
        ]
    )
    client = FtshareClient(session=session)

    df = client.stk_limit()

    assert isinstance(df, pd.DataFrame)
    assert df.to_dict("records") == [{"ts_code": "000001.SZ"}]


def test_endpoint_as_dataframe_false_returns_rows():
    session = FakeSession([FakeResponse(payload=paginated_records([{"ts_code": "000001.SZ"}]))])
    client = FtshareClient(session=session)

    rows = client.stk_limit(as_dataframe=False)

    assert rows == [{"ts_code": "000001.SZ"}]


def test_endpoint_raw_true_returns_full_payload():
    payload = paginated_records([{"ts_code": "000001.SZ"}])
    session = FakeSession([FakeResponse(payload=payload)])
    client = FtshareClient(session=session)

    assert client.stk_limit(raw=True) == payload


def test_fields_extract_and_filter_tabular_data():
    session = FakeSession([FakeResponse(payload=paginated_records([{"ts_code": "000001.SZ", "up_limit": "11.55"}]))])
    client = FtshareClient(session=session)

    df = client.stk_limit(fields=["ts_code"])

    assert isinstance(df, pd.DataFrame)
    assert df.to_dict("records") == [{"ts_code": "000001.SZ"}]


def test_limit_sets_total_rows_and_uses_page_size_for_first_page():
    session = FakeSession([FakeResponse(payload=paginated_records([{"id": 1}]))])
    client = FtshareClient(session=session)

    df = client.baidu_financial_calendar(
        start_date="2026-05-01",
        end_date="2026-05-02",
        limit=5,
    )

    assert isinstance(df, pd.DataFrame)
    assert session.calls[0]["params"] == {
        "start_date": "2026-05-01",
        "end_date": "2026-05-02",
        "page": 1,
        "page_size": 5,
    }


def test_limit_caps_requested_page_size_when_smaller():
    session = FakeSession([FakeResponse(payload=paginated_records([{"id": 1}]))])
    client = FtshareClient(session=session)

    client.baidu_financial_calendar(
        start_date="2026-05-01",
        end_date="2026-05-02",
        limit=5,
        page_size=10,
    )

    assert session.calls[0]["params"]["page_size"] == 5


def test_limit_above_single_page_fetches_multiple_pages():
    session = FakeSession(
        [
            FakeResponse(payload=paginated_records([{"id": i} for i in range(1, 201)], page=1, pages=2)),
            FakeResponse(payload=paginated_records([{"id": i} for i in range(201, 301)], page=2, pages=2)),
        ]
    )
    client = FtshareClient(session=session)

    df = client.baidu_financial_calendar(
        start_date="2026-05-01",
        end_date="2026-05-02",
        limit=300,
    )

    assert isinstance(df, pd.DataFrame)
    assert len(df) == 300
    assert session.calls[0]["params"]["page"] == 1
    assert session.calls[0]["params"]["page_size"] == 200
    assert session.calls[1]["params"]["page"] == 2
    assert session.calls[1]["params"]["page_size"] == 100


@pytest.mark.parametrize(
    ("kwargs", "message"),
    [
        ({"page": 0}, "page must be >= 1"),
        ({"limit": 0}, "limit must be >= 1"),
        ({"page_size": 201}, "page_size must be between 1 and 200"),
        ({"all_pages": True, "max_pages": 0}, "max_pages must be >= 1"),
    ],
)
def test_paginated_endpoint_validates_pagination_controls(kwargs, message):
    client = FtshareClient(session=FakeSession([]))

    with pytest.raises(ValueError, match=message):
        client.baidu_financial_calendar(
            start_date="2026-05-01",
            end_date="2026-05-02",
            **kwargs,
        )


def test_stk_limit_uses_500_as_default_request_page_size():
    session = FakeSession(
        [
            FakeResponse(payload=paginated_records([{"id": i} for i in range(1, 501)], page=1, pages=2)),
            FakeResponse(payload=paginated_records([{"id": 501}], page=2, pages=2)),
        ]
    )
    client = FtshareClient(session=session)

    df = client.stk_limit(limit=501)

    assert isinstance(df, pd.DataFrame)
    assert len(df) == 501
    assert session.calls[0]["params"]["page_size"] == 500
    assert session.calls[1]["params"]["page_size"] == 1


def test_stk_limit_allows_500_page_size():
    session = FakeSession([FakeResponse(payload=paginated_records([{"id": 1}]))])
    client = FtshareClient(session=session)

    client.stk_limit(page_size=500)

    assert session.calls[0]["params"]["page_size"] == 500


def test_stk_limit_rejects_page_size_above_500():
    client = FtshareClient(session=FakeSession([]))

    with pytest.raises(ValueError, match="page_size must be between 1 and 500"):
        client.stk_limit(page_size=501)


def test_all_pages_combines_paginated_endpoint_rows():
    session = FakeSession(
        [
            FakeResponse(payload=paginated_records([{"id": 1}, {"id": 2}], page=1, pages=2)),
            FakeResponse(payload=paginated_records([{"id": 3}], page=2, pages=2)),
        ]
    )
    client = FtshareClient(session=session)

    df = client.baidu_financial_calendar(
        start_date="2026-05-01",
        end_date="2026-05-02",
        page_size=2,
        all_pages=True,
    )

    assert isinstance(df, pd.DataFrame)
    assert df.to_dict("records") == [{"id": 1}, {"id": 2}, {"id": 3}]
    assert session.calls[0]["params"]["page"] == 1
    assert session.calls[0]["params"]["page_size"] == 2
    assert session.calls[1]["params"]["page"] == 2
    assert session.calls[1]["params"]["page_size"] == 2


def test_all_pages_raw_true_returns_page_payloads():
    first = paginated_records([{"id": 1}], page=1, pages=2)
    second = paginated_records([{"id": 2}], page=2, pages=2)
    session = FakeSession([FakeResponse(payload=first), FakeResponse(payload=second)])
    client = FtshareClient(session=session)

    payloads = client.baidu_financial_calendar(
        start_date="2026-05-01",
        end_date="2026-05-02",
        page_size=1,
        all_pages=True,
        raw=True,
    )

    assert payloads == [first, second]


def test_fetch_all_combines_pages():
    session = FakeSession(
        [
            FakeResponse(payload=paginated_records([{"id": 1}, {"id": 2}], page=1, pages=2)),
            FakeResponse(payload=paginated_records([{"id": 3}], page=2, pages=2)),
        ]
    )
    client = FtshareClient(session=session)

    df = client.fetch_all("baidu_financial_calendar", start_date="2026-05-01", end_date="2026-05-02", page_size=2)

    assert isinstance(df, pd.DataFrame)
    assert df.to_dict("records") == [{"id": 1}, {"id": 2}, {"id": 3}]
    assert session.calls[0]["params"]["page"] == 1
    assert session.calls[1]["params"]["page"] == 2


def test_fetch_all_as_dataframe_false_returns_rows():
    session = FakeSession(
        [
            FakeResponse(payload=paginated_records([{"id": 1}, {"id": 2}], page=1, pages=2)),
            FakeResponse(payload=paginated_records([{"id": 3}], page=2, pages=2)),
        ]
    )
    client = FtshareClient(session=session)

    rows = client.fetch_all(
        "baidu_financial_calendar",
        start_date="2026-05-01",
        end_date="2026-05-02",
        page_size=2,
        as_dataframe=False,
    )

    assert rows == [{"id": 1}, {"id": 2}, {"id": 3}]


def test_as_dataframe_true_returns_dataframe():
    session = FakeSession([FakeResponse(payload=paginated_records([{"ts_code": "000001.SZ"}]))])
    client = FtshareClient(session=session)

    df = client.stk_limit(as_dataframe=True)

    assert list(df.columns) == ["ts_code"]
    assert df.iloc[0]["ts_code"] == "000001.SZ"
