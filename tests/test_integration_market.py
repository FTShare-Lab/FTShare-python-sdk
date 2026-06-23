from __future__ import annotations

import os

import pandas as pd
import pytest

import ftshare as ft


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
    assert payload.get("code") in (0, "0")
    assert isinstance(payload.get("data"), dict)
    assert isinstance(payload["data"].get("records"), list)


def test_real_eastmoney_us_stock_list_tabular_extract():
    _skip_unless_enabled()
    market = ft.market_api(timeout=20)

    df = market.eastmoney_us_stock_list(page=1, page_size=5)

    assert isinstance(df, pd.DataFrame)
