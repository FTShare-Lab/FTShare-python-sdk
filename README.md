# ftshare Python SDK

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![Tests](https://github.com/ftshare-lab/ftshare-python-sdk/actions/workflows/ci.yml/badge.svg)](https://github.com/ftshare-lab/ftshare-python-sdk/actions/workflows/ci.yml)

`ftshare` 是 FTShare 行情与金融数据接口的 Python SDK。它把 `ftshare-doc/api-doc/` 中的接口封装成 Python 方法，默认访问：

```text
https://market.ft.tech/data/
```

SDK 默认返回 pandas `DataFrame`，也支持返回 Python 行数据或服务端原始 JSON。

## 安装

从项目根目录安装：

```bash
pip install -e .
```

`pandas` 和 `requests` 是运行依赖，会随 SDK 默认安装。

开发或测试时安装测试依赖：

```bash
pip install -e ".[test]"
```

## 快速开始

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

输出是 pandas `DataFrame`。例如财经日历接口会返回类似：

```text
   category   stat_date region   time  ... star negative positive capitalization
0  economic  2026-05-26     英国  07:01  ...    1                                0
1  economic  2026-05-26    新加坡  13:00  ...    1                                0
```

## 在另一个项目中使用

方式一：先安装 SDK。

```bash
pip install -e .
```

然后在任意 Python 项目中：

```python
import ftshare as ft

market = ft.market_api()
df = market.eastmoney_us_stock_list(limit=5)
print(df)
```

## 客户端入口

创建客户端：

```python
import ftshare as ft

market = ft.market_api(timeout=20)
```

自定义请求头：

```python
market = ft.market_api(headers={"User-Agent": "my-app"})
```

上下文管理：

```python
with ft.market_api(timeout=20) as market:
    df = market.stk_limit(limit=10)
```

## Base URL 配置

默认值：

```python
import ftshare as ft

print(ft.BASE_URL)
# https://market.ft.tech/data/
```

全局修改，影响之后创建的新客户端：

```python
ft.set_base_url("https://market.ft.tech/data/")
market = ft.market_api()
```

只修改某个客户端：

```python
market = ft.market_api(base_url="https://market.ft.tech/data/")
```

SDK 会规范化 URL，`https://host/data` 和 `https://host/data/` 都可以。

## 返回类型

默认返回 pandas `DataFrame`：

```python
df = market.stk_limit(trade_date=20260608, limit=10)
```

返回 Python 行数据：

```python
rows = market.stk_limit(
    trade_date=20260608,
    limit=10,
    as_dataframe=False,
)
```

返回服务端完整 JSON：

```python
payload = market.stk_limit(
    trade_date=20260608,
    limit=10,
    raw=True,
)
```

SDK 默认会优先从常见响应结构中提取表格数据：

- `data.records`
- `data.items`
- 顶层 `items`
- 顶层数组

如果响应不是表格结构，SDK 会保留数据结构并转换为单行 `DataFrame`，避免丢失字段。

## 字段筛选

`fields` 可以传列表或逗号分隔字符串：

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

字段筛选在 SDK 提取表格数据之后执行。

## 分页

分页接口同时支持传统 `page/page_size` 和更方便的 `limit/all_pages`。

取最多 N 条：

```python
df = market.baidu_financial_calendar(
    start_date="2026-05-26",
    end_date="2026-05-27",
    category="economic",
    limit=300,
)
```

当 `limit` 大于单页上限时，SDK 会自动分页并合并结果。

自动翻页：

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

精确指定页码：

```python
df = market.baidu_financial_calendar(
    start_date="2026-05-26",
    end_date="2026-05-27",
    page=2,
    page_size=50,
)
```

通用翻页入口：

```python
df = market.fetch_all(
    "baidu_financial_calendar",
    start_date="2026-05-26",
    end_date="2026-05-27",
    category="economic",
    page_size=200,
)
```

分页约束：

- 大多数接口默认单页最大 `200`。
- `stk_limit` 和 `stk_premarket` 单页最大 `500`。
- `page_size` 超过接口上限时，SDK 会直接抛出 `ValueError`。
- `limit` 表示最终最多返回多少条，允许大于单页上限，SDK 会分多页请求。

## 常用调用示例

财经日历：

```python
df = market.baidu_financial_calendar(
    start_date="2026-05-26",
    end_date="2026-05-27",
    category="economic",
    limit=20,
)
```

美股列表：

```python
df = market.eastmoney_us_stock_list(
    limit=10,
    fields=["code", "name", "latest_price", "change_pct"],
)
```

A 股涨跌停价：

```python
df = market.stk_limit(
    trade_date=20260608,
    limit=100,
    fields=["ts_code", "up_limit", "down_limit"],
)
```

股票日内分时：

```python
df = market.stock_intraday(symbol="600000.XSHG")
```

股票前收盘价：

```python
df = market.stock_prev_close(
    symbol="600000.XSHG",
    since="20240501",
    until="20240531",
)
```

## 查看可用接口

查看所有 SDK 方法：

```python
from ftshare.endpoints import ENDPOINTS

print(len(ENDPOINTS))
print(sorted(ENDPOINTS))
```

查看某个接口的元数据：

```python
from ftshare.endpoints import ENDPOINTS

endpoint = ENDPOINTS["baidu_financial_calendar"]
print(endpoint.path)
print(endpoint.params)
print(endpoint.doc_file)
```

当前 SDK 会为每个已开放的接口生成对应的 Python 方法。

## 异常处理

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

异常类型：

- `FtshareHTTPError`：HTTP 非 2xx。
- `FtshareDecodeError`：响应不是合法 JSON。
- `FtshareAPIError`：服务端业务状态码失败。

## 测试

本地单元测试使用 mock HTTP，不依赖线上服务：

```bash
python3 -m pytest
```

真实接口集成测试默认跳过。需要访问公网时显式开启：

```bash
FTSHARE_RUN_INTEGRATION=1 python3 -m pytest tests/test_integration_market.py
```

## 项目结构

```text
src/ftshare/
  __init__.py          # 包入口，导出 market_api、BASE_URL 和异常类型
  base.py              # BaseClient，请求编排、会话生命周期、分页拉取流程
  client.py            # FtshareClient 组合类和 market_api 工厂
  config.py            # BASE_URL、默认分页大小和全局配置
  dataframe.py         # pandas DataFrame 转换
  endpoints.py         # 接口 path 注册表
  exceptions.py        # SDK 异常类型
  fields.py            # fields 参数解析和列筛选
  pagination.py        # page/page_size/limit/max_pages 校验
  response.py          # API 业务错误、records/items 提取、总页数解析
  apis/                # 从 ftshare-doc/api-doc 按业务域生成的接口 mixin
```
