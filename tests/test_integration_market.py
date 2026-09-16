from __future__ import annotations

import os

import pandas as pd
import pytest

import ftshare as ft

from test_endpoint_contracts import PUBLIC_CONTRACTS, _call_kwargs


pytestmark = pytest.mark.integration


def _skip_unless_enabled() -> None:
    if os.getenv("FTSHARE_RUN_INTEGRATION") != "1":
        pytest.skip("set FTSHARE_RUN_INTEGRATION=1 to call the real FTShare API")


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


@pytest.mark.parametrize("method_name", sorted(PUBLIC_CONTRACTS))
def test_real_public_endpoint_returns_rows(method_name):
    _skip_unless_enabled()
    market = ft.market_api(timeout=20)

    kwargs = _call_kwargs(method_name)

    rows = getattr(market, method_name)(as_dataframe=False, **kwargs)

    assert rows is not None
