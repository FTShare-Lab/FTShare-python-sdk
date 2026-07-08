# FTShare Python SDK

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![Tests](https://github.com/ftshare-lab/FTShare-python-sdk/actions/workflows/ci.yml/badge.svg)](https://github.com/ftshare-lab/FTShare-python-sdk/actions/workflows/ci.yml)

`FTShare-python-sdk` 是 FTShare 金融数据能力的 Python SDK，面向需要接入行情、财务、宏观、基金、期货等数据的开发者。

它提供统一的 Python 调用方式，默认返回 pandas `DataFrame`，方便开发者在数据分析、量化研究、金融应用开发、MCP 工具封装、Skill 构建和 Agent 投研流程中使用 FTShare 数据。

## 在 FTShare 生态中的位置

`FTShare-python-sdk` 是 FTShare 生态的数据接入层。它向下连接 FTShare 数据服务，向上为 MCP、Skill 和 Agent 应用提供稳定的数据基础。

```text
FTShare 数据服务
    ↓
FTShare-python-sdk        # Python 数据访问层
    ↓
FTShare-mcp              # Agent 可调用工具层
    ↓
FTShare-skills           # 投研任务与业务工作流层
    ↓
Agent 应用                # 面向最终用户的投研分析体验
```

## 安装

本地开发时，克隆仓库并以可编辑模式安装（含测试依赖）：

```bash
git clone git@github.com:ftshare-lab/FTShare-python-sdk.git
cd FTShare-python-sdk
pip install -e ".[test]"
```

`pandas` 和 `requests` 是运行依赖，会随 SDK 默认安装。

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
# https://market.ft.tech/gateway/
```

全局修改，影响之后创建的新客户端：

```python
ft.set_base_url("https://market.ft.tech/gateway/")
market = ft.market_api()
```

只修改某个客户端：

```python
market = ft.market_api(base_url="https://market.ft.tech/gateway/")
```

SDK 会规范化 URL，`https://host/gateway` 和 `https://host/gateway/` 都可以。

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
  endpoints/           # 按 ftshare-doc 专题拆分的接口注册表
  exceptions.py        # SDK 异常类型
  fields.py            # fields 参数解析和列筛选
  pagination.py        # page/page_size/limit/max_pages 校验
  response.py          # API 业务错误、records/items 提取、总页数解析
  apis/                # 按 ftshare-doc 专题拆分的接口 mixin
```

## 社区交流

欢迎加入 FTShare 社区交流群，一起讨论 Python SDK 使用、接口问题、数据接入、量化研究和 Agent / MCP / Skill 相关实践。

<img src="docs/assets/wechat-group-20260715.png" alt="FTShare 微信交流群" width="320" />

> **群规说明**：
> - 仅限 FTShare 项目、金融数据接口、Python SDK、MCP、Skill 和 Agent 使用相关讨论
> - 禁止广告、推广、无关闲聊
> - Bug、功能需求和接口问题，建议优先在 GitHub Issues 中提交，群内用于快速交流和补充说明

**二维码有效期至 2026 年 7 月 15 日。** 如二维码失效，请在 Issues 中留言，维护者会更新入群方式。
