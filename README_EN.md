# FTShare Python SDK

[中文](README.md) | [English](README_EN.md)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![Tests](https://github.com/ftshare-lab/FTShare-python-sdk/actions/workflows/ci.yml/badge.svg)](https://github.com/ftshare-lab/FTShare-python-sdk/actions/workflows/ci.yml)

`FTShare-python-sdk` is the Python access layer for FTShare financial data. It is designed for developers who need structured access to market data, financial data, macro data, funds, futures, and related financial datasets.

The SDK provides a unified Python interface and returns pandas `DataFrame` objects by default, making it convenient for data analysis, quantitative research, financial application development, MCP tool wrapping, Skill building, and Agent-based investment research workflows.

For international developers, this project can be understood as the **FTShare financial data Python SDK** for market data, quantitative research, MCP tools, Agent Skills, and AI finance workflows.

## Position in the FTShare Ecosystem

`FTShare-python-sdk` is the data access layer in the FTShare ecosystem. It connects to FTShare data services and provides a stable data foundation for MCP tools, Skills, quantitative research scripts, and Agent applications.

```text
FTShare Data Service
    ↓
FTShare-python-sdk        # Python data access layer
    ├── FTShare-MCP        # MCP tool documentation and integration guide
    ├── FTShare-skills     # Agent Skills and investment research workflows
    └── Developer Apps      # Data analysis, quantitative research, financial apps
```

## Installation

Install from PyPI:

```bash
pip install ftshare
```

For local development, clone this repository and install it in editable mode with test dependencies:

```bash
git clone git@github.com:ftshare-lab/FTShare-python-sdk.git
cd FTShare-python-sdk
pip install -e ".[test]"
```

`pandas` and `requests` are runtime dependencies and are installed with the SDK.

## Quick Start

```python
import ftshare as ft

market = ft.market_api()

df = market.baidu_financial_calendar(
    start_date="2026-05-26",
    end_date="2026-05-27",
    category="economic",
    limit=5,
)

print(df)
```

The output is a pandas `DataFrame`. For example, the financial calendar endpoint returns a table-like result.

## Use in Another Project

Install the SDK first:

```bash
pip install -e .
```

Then use it from any Python project:

```python
import ftshare as ft

market = ft.market_api()
df = market.eastmoney_us_stock_list(limit=5)
print(df)
```

## Client Entry Point

Create a client:

```python
import ftshare as ft

market = ft.market_api(timeout=20)
```

Customize request headers:

```python
market = ft.market_api(headers={"User-Agent": "my-app"})
```

Use the client as a context manager:

```python
with ft.market_api(timeout=20) as market:
    df = market.stk_limit(limit=10)
```

## Base URL Configuration

Default value:

```python
import ftshare as ft

print(ft.BASE_URL)
# https://market.ft.tech/gateway/
```

Change the global base URL for clients created afterwards:

```python
ft.set_base_url("https://market.ft.tech/gateway/")
market = ft.market_api()
```

Override the base URL for a single client:

```python
market = ft.market_api(base_url="https://market.ft.tech/gateway/")
```

The SDK normalizes URLs, so both `https://host/gateway` and `https://host/gateway/` are accepted.

## Response Types

Return a pandas `DataFrame` by default:

```python
df = market.stk_limit(trade_date=20260608, limit=10)
```

Return Python row data:

```python
rows = market.stk_limit(
    trade_date=20260608,
    limit=10,
    as_dataframe=False,
)
```

Return the full server JSON payload:

```python
payload = market.stk_limit(
    trade_date=20260608,
    limit=10,
    raw=True,
)
```

The SDK extracts table data from common response structures first:

- `data.records`
- `data.items`
- top-level `items`
- top-level arrays

If the response is not table-shaped, the SDK keeps the original structure and converts it into a single-row `DataFrame` to avoid dropping fields.

## Field Selection

`fields` accepts either a list or a comma-separated string:

```python
df = market.eastmoney_us_stock_list(
    limit=5,
    fields=["code", "name", "latest_price", "change_pct"],
)
```

```python
df = market.eastmoney_us_stock_list(
    limit=5,
    fields="code,name,latest_price,change_pct",
)
```

Field selection is applied after the SDK extracts table data.

## Pagination

Paginated endpoints support both traditional `page/page_size` parameters and the more convenient `limit/all_pages` parameters.

Fetch up to N rows:

```python
df = market.baidu_financial_calendar(
    start_date="2026-05-26",
    end_date="2026-05-27",
    category="economic",
    limit=300,
)
```

When `limit` is larger than the single-page maximum, the SDK automatically paginates and merges results.

Fetch multiple pages automatically:

```python
df = market.baidu_financial_calendar(
    start_date="2026-05-26",
    end_date="2026-05-27",
    category="economic",
    all_pages=True,
    page_size=200,
    max_pages=5,
)
```

Fetch an exact page:

```python
df = market.baidu_financial_calendar(
    start_date="2026-05-26",
    end_date="2026-05-27",
    page=2,
    page_size=50,
)
```

Use the generic pagination helper:

```python
df = market.fetch_all(
    "baidu_financial_calendar",
    start_date="2026-05-26",
    end_date="2026-05-27",
    category="economic",
    page_size=200,
)
```

Pagination constraints:

- Most endpoints use `200` as the default maximum page size.
- `stk_limit` and `stk_premarket` use `500` as the maximum page size.
- If `page_size` exceeds the endpoint limit, the SDK raises `ValueError`.
- `limit` means the maximum number of rows to return and may be larger than a single page. The SDK will request multiple pages when needed.

## Common Examples

Financial calendar:

```python
df = market.baidu_financial_calendar(
    start_date="2026-05-26",
    end_date="2026-05-27",
    category="economic",
    limit=20,
)
```

US stock list:

```python
df = market.eastmoney_us_stock_list(
    limit=10,
    fields=["code", "name", "latest_price", "change_pct"],
)
```

A-share limit-up and limit-down prices:

```python
df = market.stk_limit(
    trade_date=20260608,
    limit=100,
    fields=["ts_code", "up_limit", "down_limit"],
)
```

Intraday stock prices:

```python
df = market.stock_intraday(symbol="600000.XSHG")
```

Previous stock close:

```python
df = market.stock_prev_close(
    symbol="600000.XSHG",
    since="20240501",
    until="20240531",
)
```

## Available Endpoints

List all generated SDK methods:

```python
from ftshare.endpoints import ENDPOINTS

print(len(ENDPOINTS))
print(sorted(ENDPOINTS))
```

Inspect endpoint metadata:

```python
from ftshare.endpoints import ENDPOINTS

endpoint = ENDPOINTS["baidu_financial_calendar"]
print(endpoint.path)
print(endpoint.params)
print(endpoint.doc_file)
```

The SDK generates a Python method for each open endpoint.

## Error Handling

```python
import ftshare as ft

market = ft.market_api(timeout=20)

try:
    df = market.baidu_financial_calendar(
        start_date="2026-05-26",
        end_date="2026-05-27",
        limit=5,
    )
except ft.FtshareHTTPError as exc:
    print("HTTP error:", exc.status_code, exc.url)
except ft.FtshareDecodeError as exc:
    print("JSON decode error:", exc.url)
except ft.FtshareAPIError as exc:
    print("API error:", exc.code, exc.message)
```

Exception types:

- `FtshareHTTPError`: non-2xx HTTP response.
- `FtshareDecodeError`: response body is not valid JSON.
- `FtshareAPIError`: server-side business error.

## Testing

Unit tests use mock HTTP and do not depend on the live service:

```bash
python3 -m pytest
```

Live integration tests are skipped by default. Enable them explicitly when internet access is available:

```bash
FTSHARE_RUN_INTEGRATION=1 python3 -m pytest tests/test_integration_market.py
```

## Project Structure

```text
src/ftshare/
  __init__.py          # package entry point: market_api, BASE_URL, exceptions
  base.py              # BaseClient, request flow, session lifecycle, pagination
  client.py            # FtshareClient composition and market_api factory
  config.py            # BASE_URL, default page size, global configuration
  dataframe.py         # pandas DataFrame conversion
  endpoints/           # endpoint registries grouped by FTShare doc topic
  exceptions.py        # SDK exception types
  fields.py            # fields parsing and column selection
  pagination.py        # page/page_size/limit/max_pages validation
  response.py          # API business errors, records/items extraction, total page parsing
  apis/                # API mixins grouped by FTShare doc topic
```

## Related Projects

- [FTShare-MCP](https://github.com/FTShare-Lab/FTShare-MCP): FTShare financial data MCP tool documentation and integration guide for Agent tool calls
- [FTShare-skills](https://github.com/FTShare-Lab/FTShare-skills): FTShare Agent Skills repository for data-level Skills and investment research workflow Skills

## Community

Chinese users are welcome to join the FTShare WeChat community group to discuss SDK usage, interface issues, data access, quantitative research, and Agent / MCP / Skill practices.

<img src="docs/assets/wechat-group-20260729.png" alt="FTShare WeChat community group" width="320" />

> **Community rules**:
> - Discussions should be related to FTShare, financial data interfaces, the Python SDK, MCP, Skills, or Agent usage
> - Advertising, promotion, and unrelated off-topic chat are not allowed
> - For bugs, feature requests, and interface issues, please open a GitHub Issue first. The group is for quick discussion and follow-up context

**The QR code is valid until July 29, 2026.** If it expires, please open an Issue and the maintainers will update the invitation.
