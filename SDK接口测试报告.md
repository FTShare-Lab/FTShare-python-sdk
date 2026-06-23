# FTShare Python SDK 接口测试报告

测试时间：2026-06-22

测试对象：`ftshare-python-sdk`

测试方式：使用当前 SDK 的公开入口按示例方式调用：

```python
import ftshare as ft

market = ft.market_api()
df = market.xxx(...)
```

本地验证命令：

```bash
python3 -m pytest
python3 -m compileall src tests
```

## 总体统计

| 指标 | 数量 | 说明 |
|---|---:|---|
| SDK 方法总数 | 176 | `ENDPOINTS` 中登记且有文档来源的方法 |
| 可正常调用 | 161 | 使用当前 SDK 默认归一化返回模式调用成功 |
| 真实调用失败 | 15 | 有 public path，但公网真实调用失败 |
| 本地单元测试 | 57 passed, 3 skipped | `python3 -m pytest` |
| 语法检查 | passed | `compileall src tests` |

## 当前判断

SDK 侧当前核心能力正常：

- `import ftshare as ft` 可以正常导入。
- `ft.market_api()` 可以创建客户端。
- 默认返回 pandas `DataFrame`。
- `raw=True` 可以返回完整 JSON。
- `as_dataframe=False` 可以返回 Python 行数据。
- `fields` 字段筛选可用。
- 分页参数、`limit`、`all_pages` 可用。
- 动态路径参数，例如 `/market/security/{symbol}/intraday` 可用。

剩余问题主要集中在服务端或公网网关：

- HTTP 500：服务端 handler 或底层数据源异常。
- HTTP 429：公网限流。
- `ChunkedEncodingError`：响应体传输被截断，多见于大响应接口，疑似公网网关或服务端传输配置问题。

## 有 public path 但真实调用失败

以下 15 个接口已有 public path，但通过公网真实调用失败。

| 接口 | 当前问题 | 判断 |
|---|---|---|
| `abnormal_trading_details` | `ChunkedEncodingError`，响应体传输截断 | 疑似公网网关或服务端大响应传输问题 |
| `bse_mapping` | HTTP 500，服务端返回系统错误 | 服务端或数据源异常 |
| `cashflow_stock_code` | `ChunkedEncodingError`，响应体传输截断 | 疑似公网网关或服务端大响应传输问题 |
| `cb_lists` | `ChunkedEncodingError`，响应体传输截断 | 疑似公网网关或服务端大响应传输问题，表现不稳定 |
| `etf_components_all` | HTTP 429，服务端返回请求过于频繁 | 公网限流 |
| `etf_description_all` | `ChunkedEncodingError`，响应体传输截断 | 疑似公网网关或服务端大响应传输问题 |
| `etf_pre` | `ChunkedEncodingError`，响应体传输截断 | 疑似公网网关或服务端大响应传输问题 |
| `hk_basinfo_get` | HTTP 500，服务端返回系统错误 | 服务端或数据源异常 |
| `hk_basinfo_post` | HTTP 500，服务端返回系统错误 | 服务端或数据源异常 |
| `lpr_monthly` | `ChunkedEncodingError`，响应体传输截断 | 疑似公网网关或服务端大响应传输问题 |
| `risk_warning_stock_quotes` | `ChunkedEncodingError`，响应体传输截断 | 疑似公网网关或服务端大响应传输问题 |
| `stock_announcements` | HTTP 500，服务端返回系统错误 | 服务端或数据源异常 |
| `stock_list` | `ChunkedEncodingError`，响应体传输截断 | 疑似公网网关或服务端大响应传输问题 |
| `stock_share` | HTTP 500，服务端返回系统错误 | 服务端或数据源异常 |
| `stock_trade` | `ChunkedEncodingError`，响应体传输截断 | 疑似公网网关或服务端大响应传输问题 |

## 后续建议

1. 对 HTTP 500 接口，优先在服务端对应 handler 和下游数据源中定位错误日志。
2. 对 HTTP 429 接口，降低测试频率，或为测试环境配置更高限流阈值。
3. 对 `ChunkedEncodingError` 接口，建议后端优先支持分页或限制默认返回体大小，同时检查公网网关的 chunk、压缩、超时和响应体大小配置。
