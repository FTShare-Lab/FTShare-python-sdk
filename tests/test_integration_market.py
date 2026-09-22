from __future__ import annotations

import os
from typing import Any

import pandas as pd
import pytest

import ftshare as ft

from test_endpoint_contracts import PUBLIC_CONTRACTS, _call_kwargs


pytestmark = pytest.mark.integration


# Endpoints that return HTTP 200 with an empty payload on the test server for
# every parameter combination, or fail before reaching the data layer. Verified
# against http://xz09:10103 on 2026-09-22; re-check these when the server moves.
KNOWN_SERVER_ISSUES: dict[str, str] = {
    "ashare_news_sentiment_factors": "HTTP 502 下游服务请求失败 for every parameter combination",
    "futures_minutes_batch": "HTTP 404 请求的资源不存在 — route absent on the test server",
    "szse_convertible_bond_declaration_snapshots": "HTTP 200 but empty for every date range, while sibling exchange tables return rows",
}


def _skip_unless_enabled() -> None:
    if os.getenv("FTSHARE_RUN_INTEGRATION") != "1":
        pytest.skip("set FTSHARE_RUN_INTEGRATION=1 to call the real FTShare API")


def _assert_success_with_data(payload: Any) -> None:
    """Assert an HTTP 200 business envelope whose ``data`` actually carries rows."""
    assert isinstance(payload, dict), payload
    assert payload.get("code") in (0, "0", 200, "200"), payload
    data = payload.get("data")
    assert data is not None, "data is null"
    if isinstance(data, dict):
        for key in ("records", "items", "index_descriptions"):
            if isinstance(data.get(key), list):
                assert data[key], f"data.{key} is empty"
                return
        assert data, "data object is empty"
        return
    if isinstance(data, (list, str)):
        assert len(data) > 0, "data is empty"


def test_real_baidu_financial_calendar_default_rows_shape():
    _skip_unless_enabled()
    market = ft.market_api(timeout=20)

    df = market.baidu_financial_calendar(
        start_date="2026-05-26",
        end_date="2026-05-27",
        page=1,
        page_size=5,
        category="economic",
    )

    assert isinstance(df, pd.DataFrame)


def test_real_baidu_financial_calendar_raw_payload_shape():
    _skip_unless_enabled()
    market = ft.market_api(timeout=20)

    payload = market.baidu_financial_calendar(
        start_date="2026-05-26",
        end_date="2026-05-27",
        page=1,
        page_size=5,
        category="economic",
        raw=True,
    )

    assert isinstance(payload, dict)
    assert payload.get("code") in (0, "0", 200, "200")
    assert isinstance(payload.get("data"), dict)
    assert isinstance(payload["data"].get("records"), list)


def test_real_eastmoney_us_stock_daily_ohlc_tabular_extract():
    _skip_unless_enabled()
    market = ft.market_api(timeout=20)

    df = market.eastmoney_us_stock_daily_ohlc(
        stock_code="AAPL",
        start_date="2026-08-18",
        end_date="2026-08-20",
        page=1,
        page_size=5,
    )

    assert isinstance(df, pd.DataFrame)


@pytest.mark.parametrize(
    "method_name",
    [
        pytest.param(name, marks=pytest.mark.xfail(reason=KNOWN_SERVER_ISSUES[name], strict=True))
        if name in KNOWN_SERVER_ISSUES
        else name
        for name in sorted(PUBLIC_CONTRACTS)
    ],
)
def test_real_public_endpoint_returns_rows(method_name):
    _skip_unless_enabled()
    market = ft.market_api(timeout=20)

    kwargs = _call_kwargs(method_name)

    payload = getattr(market, method_name)(raw=True, **kwargs)

    _assert_success_with_data(payload)
