# FTShare Python SDK API Reference

本文档由 SDK 方法 docstring 和 `ftshare.endpoints.ENDPOINTS` 生成。接口分组与 `ftshare-doc/api-doc` 顶层专题保持一致。

## 汇总

| 指标 | 数量 |
|---|---:|
| SDK 方法总数 | 179 |

## 专题分布

接口分组、`src/ftshare/apis/` 方法模块和 `src/ftshare/endpoints/` 注册表模块均按 `ftshare-doc/api-doc` 顶层专题对齐。

| ftshare-doc 专题 | SDK 方法数 | API mixin 模块 | Endpoint 模块 |
|---|---:|---|---|
| 股票数据 | 95 | `ftshare.apis.stock` | `ftshare.endpoints.stock` |
| 港股数据 | 14 | `ftshare.apis.hk` | `ftshare.endpoints.hk` |
| 美股数据 | 9 | `ftshare.apis.us` | `ftshare.endpoints.us` |
| 指数专题 | 8 | `ftshare.apis.index` | `ftshare.endpoints.index` |
| ETF专题 | 8 | `ftshare.apis.etf` | `ftshare.endpoints.etf` |
| 公募基金 | 5 | `ftshare.apis.fund` | `ftshare.endpoints.fund` |
| 期货数据 | 9 | `ftshare.apis.futures` | `ftshare.endpoints.futures` |
| 债券专题 | 2 | `ftshare.apis.bond` | `ftshare.endpoints.bond` |
| 宏观经济 | 17 | `ftshare.apis.economic` | `ftshare.endpoints.economic` |
| 大模型语料 | 5 | `ftshare.apis.llm_corpus` | `ftshare.endpoints.llm_corpus` |
| 现货数据 | 2 | `ftshare.apis.spot` | `ftshare.endpoints.spot` |
| 外汇数据 | 1 | `ftshare.apis.forex` | `ftshare.endpoints.forex` |
| 未发布 | 4 | `ftshare.apis.unpublished` | `ftshare.endpoints.unpublished` |

## 使用方式

```python
import ftshare as ft

market = ft.market_api()
df = market.baidu_financial_calendar(
    start_date="2026-05-26",
    end_date="2026-05-27",
    category="economic",
    limit=5,
)
```

## 接口索引

### 股票数据

| SDK 方法 | 接口名称 | HTTP | Path | 参数 | 来源文档 |
|---|---|---|---|---|---|
| [`abnormal_trading_details`](#api-abnormal-trading-details) | 龙虎榜明细 | `GET` | `api/v1/market/data/abnormal-trading-details` | `date` | `龙虎榜明细.md` |
| [`abnormal_trading_overview`](#api-abnormal-trading-overview) | 龙虎榜总览 | `GET` | `api/v1/market/data/abnormal-trading-overview` | `date` | `龙虎榜总览.md` |
| [`auction_results`](#api-auction-results) | 集合竞价结果 | `GET` | `api/v1/market/data/auction-results` | `ts_code`, `trade_date`, `start_date`, `end_date`, `page`, `page_size` | `集合竞价结果.md` |
| [`balance`](#api-balance) | A股资产负债表 | `GET` | `api/v1/market/data/finance/balance` | `stock_code`, `year`, `report_type`, `page`, `page_size` | `A股资产负债表.md` |
| [`block_trades`](#api-block-trades) | 大宗交易 | `GET` | `api/v1/market/data/block-trades` | `date` | `大宗交易.md` |
| [`bse_mapping`](#api-bse-mapping) | 北交所映射 | `GET` | `api/v1/market/data/bse-mapping` | `o_code`, `n_code` | `北交所映射.md` |
| [`cashflow`](#api-cashflow) | A股现金流量表 | `GET` | `api/v1/market/data/finance/cashflow` | `stock_code`, `year`, `report_type`, `page`, `page_size` | `A股现金流量表.md` |
| [`cashflow_stock_code`](#api-cashflow-stock-code) | 现金流支持股票代码 | `GET` | `api/v1/market/data/finance/cashflow-stock-code` | - | `现金流支持股票代码.md` |
| [`company_list`](#api-company-list) | 公司列表 | `GET` | `api/v1/market/data/company-list` | `stock_name`, `stock_code`, `page`, `page_size` | `公司列表.md` |
| [`earnings_reports_paginated`](#api-earnings-reports-paginated) | 业绩快报 | `GET` | `api/v1/market/data/finance/stock-performance-express` | `stock_code`, `year`, `report_type`, `page`, `page_size` | `业绩快报.md` |
| [`eastmoney_board_constituents`](#api-eastmoney-board-constituents) | 东方财富板块成份股 | `GET` | `api/v1/market/data/eastmoney-board-constituents` | `board_code` | `东方财富板块成份股.md` |
| [`eastmoney_board_daily_kline`](#api-eastmoney-board-daily-kline) | 东方财富板块日线OHLC | `GET` | `api/v1/market/data/eastmoney-board-daily-ohlc` | `board_code`, `start_date`, `end_date`, `page`, `page_size` | `东方财富板块日线OHLC.md` |
| [`eastmoney_board_latest_kline`](#api-eastmoney-board-latest-kline) | 东方财富板块最新OHLC | `GET` | `api/v1/market/data/eastmoney-board-latest-ohlc` | `board_code`, `page`, `page_size` | `东方财富板块最新OHLC.md` |
| [`eastmoney_concept_boards`](#api-eastmoney-concept-boards) | 东方财富概念板块 | `GET` | `api/v1/market/data/eastmoney-concept-boards` | - | `东方财富概念板块.md` |
| [`eastmoney_dapan_flow`](#api-eastmoney-dapan-flow) | 东方财富大盘资金流 | `GET` | `api/v1/market/data/eastmoney-dapan-flow` | `trade_date`, `start_date`, `end_date`, `page`, `page_size` | `东方财富大盘资金流.md` |
| [`eastmoney_market_valuation`](#api-eastmoney-market-valuation) | 东方财富市场估值 | `GET` | `api/v1/market/data/eastmoney-market-valuation` | `market_code`, `trade_date`, `start_date`, `end_date`, `page`, `page_size` | `东方财富市场估值.md` |
| [`eastmoney_rank`](#api-eastmoney-rank) | 东方财富股票排名 | `GET` | `api/v1/market/data/eastmoney-rank` | `rank_group`, `market`, `trade_date` | `东方财富股票排名.md` |
| [`eastmoney_sector_flow`](#api-eastmoney-sector-flow) | 东方财富板块资金流 | `GET` | `api/v1/market/data/eastmoney-sector-flow` | `sector_code`, `sector_type`, `trade_date`, `start_date`, `end_date`, `page`, `page_size` | `东方财富板块资金流.md` |
| [`eastmoney_stock_flow`](#api-eastmoney-stock-flow) | 东方财富个股资金流 | `GET` | `api/v1/market/data/eastmoney-stock-flow` | `symbol`, `trade_date`, `start_date`, `end_date`, `page`, `page_size` | `东方财富个股资金流.md` |
| [`eastmoney_stock_valuation`](#api-eastmoney-stock-valuation) | 东方财富个股估值 | `GET` | `api/v1/market/data/eastmoney-stock-valuation` | `symbol`, `trade_date`, `start_date`, `end_date`, `page`, `page_size` | `东方财富个股估值.md` |
| [`goodwill_industry`](#api-goodwill-industry) | 商誉行业 | `GET` | `api/v1/market/data/goodwill/industry` | `date`, `page`, `page_size` | `商誉行业.md` |
| [`goodwill_market_overview`](#api-goodwill-market-overview) | 商誉市场总览 | `GET` | `api/v1/market/data/goodwill/market-overview` | - | `商誉市场总览.md` |
| [`goodwill_predict`](#api-goodwill-predict) | 商誉预测 | `GET` | `api/v1/market/data/goodwill/predict` | `date`, `page`, `page_size` | `商誉预测.md` |
| [`goodwill_stock_detail`](#api-goodwill-stock-detail) | 商誉个股明细 | `GET` | `api/v1/market/data/goodwill/stock-detail` | `date`, `page`, `page_size` | `商誉个股明细.md` |
| [`goodwill_stock_impairment`](#api-goodwill-stock-impairment) | 商誉减值 | `GET` | `api/v1/market/data/goodwill/stock-impairment` | `date`, `page`, `page_size` | `商誉减值.md` |
| [`hk_sh_stock_connect_members`](#api-hk-sh-stock-connect-members) | 沪港通成份 | `GET` | `api/v1/market/data/hk-sh-stock-connect-members` | - | `沪港通成份.md` |
| [`hk_sz_stock_connect_members`](#api-hk-sz-stock-connect-members) | 深港通成份 | `GET` | `api/v1/market/data/hk-sz-stock-connect-members` | - | `深港通成份.md` |
| [`income`](#api-income) | A股利润表 | `GET` | `api/v1/market/data/finance/income` | `stock_code`, `year`, `report_type`, `page`, `page_size` | `A股利润表.md` |
| [`limit_down_pool`](#api-limit-down-pool) | 跌停池 | `GET` | `api/v1/market/data/limit-down-pool` | - | `跌停池.md` |
| [`limit_event_timeline_3s`](#api-limit-event-timeline-3s) | 涨跌停事件时间线 | `GET` | `api/v1/market/data/limit-event-timeline-3s` | `symbol` | `涨跌停事件时间线.md` |
| [`limit_up_break_pool`](#api-limit-up-break-pool) | 炸板池 | `GET` | `api/v1/market/data/limit-up-break-pool` | - | `炸板池.md` |
| [`limit_up_pool`](#api-limit-up-pool) | 涨停池 | `GET` | `api/v1/market/data/limit-up-pool` | - | `涨停池.md` |
| [`limit_up_pool_yesterday`](#api-limit-up-pool-yesterday) | 昨日涨停池 | `GET` | `api/v1/market/data/limit-up-pool-yesterday` | - | `昨日涨停池.md` |
| [`margin_trading_details`](#api-margin-trading-details) | 融资融券明细 | `GET` | `api/v1/market/data/margin-trading-details` | `date`, `page`, `page_size` | `融资融券明细.md` |
| [`margin_trading_details_paginated`](#api-margin-trading-details-paginated) | 融资融券明细分页 | `GET` | `api/v1/market/data/margin-trading-details` | `date`, `page`, `page_size` | `融资融券明细分页.md` |
| [`northbound`](#api-northbound) | 北向资金交易 | `GET` | `api/v1/market/data/northbound` | `date` | `北向资金交易.md` |
| [`nth_trade_date`](#api-nth-trade-date) | 第N个交易日 | `GET` | `api/v1/market/data/time/get-nth-trade-date` | `n` | `第N个交易日.md` |
| [`performance_forecasts_paginated`](#api-performance-forecasts-paginated) | 业绩预告 | `GET` | `api/v1/market/data/finance/stock-performance-forecast` | `stock_code`, `year`, `report_type`, `page`, `page_size` | `业绩预告.md` |
| [`price_change`](#api-price-change) | 价格变动 | `GET` | `api/v1/market/data/price/get-price-change` | `stock_code`, `base_date`, `n`, `direction` | `价格变动.md` |
| [`risk_warning_stock_quotes`](#api-risk-warning-stock-quotes) | 风险警示股行情 | `GET` | `api/v1/market/data/risk-warning-stocks/quotes` | `date` | `风险警示股行情.md` |
| [`risk_warning_stocks`](#api-risk-warning-stocks) | 风险警示股 | `GET` | `api/v1/market/data/risk-warning-stocks` | `date` | `风险警示股.md` |
| [`search`](#api-search) | 标的搜索 | `GET` | `api/v1/market/security/search` | `query`, `limit` | `标的搜索.md` |
| [`sh_hk_stock_connect_members`](#api-sh-hk-stock-connect-members) | 沪股通成份 | `GET` | `api/v1/market/data/sh-hk-stock-connect-members` | - | `沪股通成份.md` |
| [`southbound`](#api-southbound) | 南向资金交易 | `GET` | `api/v1/market/data/southbound` | `date` | `南向资金交易.md` |
| [`stk_ah_comparison`](#api-stk-ah-comparison) | AH股对比 | `GET` | `api/v1/market/data/hk/stk-ah-comparison` | `hk_code`, `ts_code`, `trade_date`, `start_date`, `end_date`, `page`, `page_size` | `AH股对比.md` |
| [`stk_limit`](#api-stk-limit) | 涨跌停价 | `GET` | `api/v1/market/data/stk-limit` | `instrument_type`, `symbol`, `symbol_id`, `market_id`, `trade_date`, `start_date`, `end_date`, `page`, `page_size` | `涨跌停价.md` |
| [`stk_premarket`](#api-stk-premarket) | 盘前数据 | `GET` | `api/v1/market/data/stk-premarket` | `ts_code`, `trade_date`, `start_date`, `end_date`, `page`, `page_size` | `盘前数据.md` |
| [`stock_adjust_factor`](#api-stock-adjust-factor) | 股票复权因子 | `GET` | `api/v1/market/data/stock-adjust-factor` | `symbol`, `trade_date`, `start_date`, `end_date`, `offset`, `limit` | `股票复权因子.md` |
| [`stock_candlesticks`](#api-stock-candlesticks) | 股票K线 | `POST` | `api/v1/market/data/stock-candlesticks` | `symbol`, `interval_unit`, `interval_value`, `adjust_kind`, `since_ts_millis`, `until_ts_millis`, `limit` | `股票K线.md` |
| [`stock_candlesticks_batch`](#api-stock-candlesticks-batch) | 批量股票K线 | `POST` | `api/v1/market/data/stock-candlesticks/batch` | `symbols`, `interval_unit`, `interval_value`, `adjust_kind`, `since_ts_millis`, `until_ts_millis`, `limit` | `批量股票K线.md` |
| [`stock_capital_flows_paginated`](#api-stock-capital-flows-paginated) | 股票资金流向 | `GET` | `api/v1/market/data/stock-capital-flows` | `date`, `page`, `page_size` | `股票资金流向.md` |
| [`stock_comment_desire_em`](#api-stock-comment-desire-em) | 千股千评意愿度 | `GET` | `api/v1/market/data/stock-comment/desire` | `symbol` | `千股千评意愿度.md` |
| [`stock_comment_em`](#api-stock-comment-em) | 千股千评 | `GET` | `api/v1/market/data/stock-comment/index` | `page`, `page_size` | `千股千评.md` |
| [`stock_comment_focus_em`](#api-stock-comment-focus-em) | 千股千评关注度 | `GET` | `api/v1/market/data/stock-comment/focus` | `symbol` | `千股千评关注度.md` |
| [`stock_comment_org_participate_em`](#api-stock-comment-org-participate-em) | 机构参与度 | `GET` | `api/v1/market/data/stock-comment/org-participate` | `symbol` | `机构参与度.md` |
| [`stock_comment_score_em`](#api-stock-comment-score-em) | 千股千评评分 | `GET` | `api/v1/market/data/stock-comment/score` | `symbol` | `千股千评评分.md` |
| [`stock_filter`](#api-stock-filter) | 股票筛选 | `GET` | `api/v1/market/data/stock-list/filter` | `board`, `listing_date_since`, `page`, `page_size` | `股票筛选.md` |
| [`stock_float_holders`](#api-stock-float-holders) | 十大流通股东 | `GET` | `api/v1/market/data/holder/stock-holder-ften` | `stock_code`, `is_last`, `page`, `page_size` | `十大流通股东.md` |
| [`stock_ggcg_em`](#api-stock-ggcg-em) | 东方财富股东增减持 | `GET` | `api/v1/market/data/holder/stock-ggcg-em` | `symbol`, `page`, `page_size` | `东方财富股东增减持.md` |
| [`stock_ggmx`](#api-stock-ggmx) | 董监高持股变动 | `GET` | `api/v1/market/data/holder/stock-ggmx` | `stock_code`, `change_direction`, `start_date`, `end_date`, `page`, `page_size` | `董监高持股变动.md` |
| [`stock_ggmx_buy_ranking`](#api-stock-ggmx-buy-ranking) | 董监高增持排名 | `GET` | `api/v1/market/data/holder/stock-ggmx-buy-ranking` | `time_range`, `page`, `page_size` | `董监高增持排名.md` |
| [`stock_ggmx_sell_ranking`](#api-stock-ggmx-sell-ranking) | 董监高减持排名 | `GET` | `api/v1/market/data/holder/stock-ggmx-sell-ranking` | `time_range`, `page`, `page_size` | `董监高减持排名.md` |
| [`stock_holders`](#api-stock-holders) | 十大股东 | `GET` | `api/v1/market/data/holder/stock-holder-ten` | `stock_code`, `is_last`, `page`, `page_size` | `十大股东.md` |
| [`stock_holders_number`](#api-stock-holders-number) | 股东人数 | `GET` | `api/v1/market/data/holder/stock-holder-nums` | `stock_code`, `is_last`, `page`, `page_size` | `股东人数.md` |
| [`stock_institution_holdings`](#api-stock-institution-holdings) | 机构持股 | `GET` | `api/v1/market/data/share/stock-institution-holdings` | `year`, `report_type`, `inst_type`, `page`, `page_size` | `机构持股.md` |
| [`stock_institution_holdings_detail`](#api-stock-institution-holdings-detail) | 机构持股明细 | `GET` | `api/v1/market/data/share/stock-institution-holdings-detail` | `stock_code`, `year`, `report_type`, `inst_type`, `page`, `page_size` | `机构持股明细.md` |
| [`stock_institution_share_holdings`](#api-stock-institution-share-holdings) | 机构股本持股 | `GET` | `api/v1/market/data/institution/institution-share-holdings` | `institution_id`, `year`, `report_type`, `invest_type` | `机构股本持股.md` |
| [`stock_intraday_auction_volume`](#api-stock-intraday-auction-volume) | 集合竞价成交量 | `GET` | `api/v1/market/data/intraday-auction-volume` | `trade_date`, `page`, `page_size` | `集合竞价成交量.md` |
| [`stock_intraday_auction_volume_symbol`](#api-stock-intraday-auction-volume-symbol) | 单标的集合竞价成交量 | `GET` | `api/v1/market/data/intraday-auction-volume/symbol` | `symbol`, `trade_date`, `page`, `page_size` | `单标的集合竞价成交量.md` |
| [`stock_ipos`](#api-stock-ipos) | 股票IPO | `GET` | `api/v1/market/data/stock-ipos` | `page`, `page_size` | `股票IPO.md` |
| [`stock_list`](#api-stock-list) | 股票列表 | `GET` | `api/v1/market/data/stock-list` | - | `股票列表.md` |
| [`stock_market`](#api-stock-market) | 市场行情快照 | `GET` | `api/v1/market/data/daec/market/snapshot` | `scope` | `市场行情快照.md` |
| [`stock_market_distribution_intraday`](#api-stock-market-distribution-intraday) | 日内涨跌停分布历史 | `GET` | `api/v1/market/data/daec/market/distribution-history` | `scope` | `日内涨跌停分布历史.md` |
| [`stock_daec_stocks`](#api-stock-daec-stocks) | A股行情列表 | `GET` | `api/v1/market/data/daec/stocks/{board}` | `board`, `page`, `page_size`, `filter`, `order_by` | `A股行情列表.md` |
| [`stock_realtime_list`](#api-stock-realtime-list) | A股行情列表 | `GET` | `api/v1/market/data/stock-list/{board}` | `board`, `page`, `page_size` | `A股行情列表.md` |
| [`stock_pledge_detail`](#api-stock-pledge-detail) | 股权质押明细 | `GET` | `api/v1/market/data/pledge/pledge-detail` | `stock_code`, `is_last`, `page`, `page_size` | `股权质押明细.md` |
| [`stock_pledge_summary`](#api-stock-pledge-summary) | 股权质押汇总 | `GET` | `api/v1/market/data/pledge/pledge-summary` | `page`, `page_size` | `股权质押汇总.md` |
| [`stock_prev_close`](#api-stock-prev-close) | 标的昨收价 | `GET` | `api/v1/market/data/daec/history/prev-closes` | `symbol`, `since`, `until` | `标的昨收价.md` |
| [`stock_intraday_prices`](#api-stock-intraday-prices) | 标的分时数据 | `GET` | `api/v1/market/data/daec/history/prices` | `symbol`, `range`, `days`, `ts_ms` | `标得分时数据.md` |
| [`stock_rating_top5`](#api-stock-rating-top5) | 飞兔股票评级Top5 | `GET` | `api/v1/market/data/feitu/stock-rating-top5` | `date`, `variant`, `type` | `飞兔股票评级Top5.md` |
| [`stock_share`](#api-stock-share) | 股本 | `GET` | `api/v1/market/data/share/get-stock-share` | `stock_code`, `date` | `股本.md` |
| [`stock_share_chg`](#api-stock-share-chg) | 股东增减持 | `GET` | `api/v1/market/data/holder/stock-share-chg` | `stock_code`, `is_last`, `page`, `page_size` | `股东增减持.md` |
| [`stock_signal_latest_snapshot`](#api-stock-signal-latest-snapshot) | 信号最新快照 | `GET` | `api/v1/market/data/stock-signal-latest-snapshot` | `signal_type`, `page`, `page_size` | `信号最新快照.md` |
| [`stock_trade`](#api-stock-trade) | 标的逐笔成交 | `GET` | `api/v1/market/data/daec/history/trades` | `symbol` | `标的逐笔成交.md` |
| [`stock_unlock`](#api-stock-unlock) | 限售解禁 | `GET` | `api/v1/market/data/unlock/stock-unlock` | `stock_code`, `page`, `page_size` | `限售解禁.md` |
| [`stock_unlock_by_date`](#api-stock-unlock-by-date) | 限售解禁按日期 | `GET` | `api/v1/market/data/unlock/stock-unlock-by-date` | `start_date`, `end_date`, `page`, `page_size` | `限售解禁按日期.md` |
| [`suspension_list`](#api-suspension-list) | 停牌列表 | `GET` | `api/v1/market/data/suspension-list` | `trade_date`, `page`, `page_size` | `停牌列表.md` |
| [`sz_hk_stock_connect_members`](#api-sz-hk-stock-connect-members) | 深股通成份 | `GET` | `api/v1/market/data/sz-hk-stock-connect-members` | - | `深股通成份.md` |
| [`ths_all_board_kline`](#api-ths-all-board-kline) | 同花顺全板块K线 | `GET` | `api/v1/market/data/ths-all-board-kline` | `start_date`, `end_date`, `page`, `page_size` | `同花顺全板块K线.md` |
| [`ths_board_kline`](#api-ths-board-kline) | 同花顺板块K线 | `GET` | `api/v1/market/data/ths-board-kline` | `board_code`, `page`, `page_size` | `同花顺板块K线.md` |
| [`ths_board_list`](#api-ths-board-list) | 同花顺板块列表 | `GET` | `api/v1/market/data/ths-board-list` | - | `同花顺板块列表.md` |
| [`xueqiu_rank`](#api-xueqiu-rank) | 雪球股票排名 | `GET` | `api/v1/market/data/xueqiu-rank` | `rank_group`, `period`, `trade_date`, `page`, `page_size` | `雪球股票排名.md` |
| [`yzxdr_detail`](#api-yzxdr-detail) | 除权除息明细 | `GET` | `api/v1/market/data/yzxdr-detail` | `year`, `quarter`, `stock_code`, `page`, `page_size` | `除权除息明细.md` |
| [`pledge_summary`](#api-pledge-summary) | 股权质押汇总 | `GET` | `api/v1/market/data/pledge/pledge-summary` | `page`, `page_size` | `股权质押汇总.md` |
| [`stock_capital_flows`](#api-stock-capital-flows) | 股票资金流向 | `GET` | `api/v1/market/data/stock-capital-flows` | `date`, `page`, `page_size` | `股票资金流向.md` |

### 港股数据

| SDK 方法 | 接口名称 | HTTP | Path | 参数 | 来源文档 |
|---|---|---|---|---|---|
| [`company_hk`](#api-company-hk) | 港股公司信息 | `GET` | `api/v1/market/data/hk/company-hk` | `trade_code` | `港股公司信息.md` |
| [`eastmoney_hk_index_daily_kline`](#api-eastmoney-hk-index-daily-kline) | 东方财富港股指数日K | `GET` | `api/v1/market/data/eastmoney-hk-index-daily-kline` | `index_code`, `trade_date`, `start_date`, `end_date`, `page`, `page_size` | `东方财富港股指数日K.md` |
| [`hk_balance_bank`](#api-hk-balance-bank) | 港股资产负债表 | `GET` | `api/v1/market/data/hk/hk-balance-bank` | `trade_code`, `year`, `report_type`, `start_date`, `end_date`, `page`, `page_size` | `港股资产负债表.md` |
| [`hk_balance_gene`](#api-hk-balance-gene) | 港股资产负债表 | `GET` | `api/v1/market/data/hk/hk-balance-gene` | `trade_code`, `year`, `report_type`, `start_date`, `end_date`, `page`, `page_size` | `港股资产负债表.md` |
| [`hk_balance_insur`](#api-hk-balance-insur) | 港股资产负债表 | `GET` | `api/v1/market/data/hk/hk-balance-insur` | `trade_code`, `year`, `report_type`, `start_date`, `end_date`, `page`, `page_size` | `港股资产负债表.md` |
| [`hk_basinfo_get`](#api-hk-basinfo-get) | 港股个股信息 | `GET` | `api/v1/market/data/hk/hk-view` | `hk_code` | `港股个股信息.md` |
| [`hk_basinfo_post`](#api-hk-basinfo-post) | 港股个股信息 | `GET` | `api/v1/market/data/hk/hk-view` | `hk_code` | `港股个股信息.md` |
| [`hk_candlesticks`](#api-hk-candlesticks) | 港股K线 | `GET` | `api/v1/market/data/hk/hk-candlesticks` | `trade_code`, `interval_unit`, `until_date`, `since_date`, `interval_value`, `limit`, `adjust_kind` | `港股K线.md` |
| [`hk_cashflow`](#api-hk-cashflow) | 港股现金流量表 | `GET` | `api/v1/market/data/hk/hk-cashflow` | `stock_code`, `year`, `report_type`, `start_date`, `end_date`, `page`, `page_size` | `港股现金流量表.md` |
| [`hk_income_bank`](#api-hk-income-bank) | 港股利润表 | `GET` | `api/v1/market/data/hk/hk-income-bank` | `trade_code`, `year`, `report_type`, `start_date`, `end_date`, `page`, `page_size` | `港股利润表.md` |
| [`hk_income_gene`](#api-hk-income-gene) | 港股利润表 | `GET` | `api/v1/market/data/hk/hk-income-gene` | `trade_code`, `year`, `report_type`, `start_date`, `end_date`, `page`, `page_size` | `港股利润表.md` |
| [`hk_income_insur`](#api-hk-income-insur) | 港股利润表 | `GET` | `api/v1/market/data/hk/hk-income-insur` | `trade_code`, `year`, `report_type`, `start_date`, `end_date`, `page`, `page_size` | `港股利润表.md` |
| [`hk_valuatnanalyd`](#api-hk-valuatnanalyd) | 港股估值分析 | `GET` | `api/v1/market/data/hk/hk-valuatnanalyd` | `trade_code`, `page`, `page_size` | `港股估值分析.md` |
| [`market_cap_hk`](#api-market-cap-hk) | 港股市值 | `GET` | `api/v1/market/data/hk/market-cap-hk` | `trade_code` | `港股市值.md` |

### 美股数据

| SDK 方法 | 接口名称 | HTTP | Path | 参数 | 来源文档 |
|---|---|---|---|---|---|
| [`eastmoney_us_stock_daily_kline`](#api-eastmoney-us-stock-daily-kline) | 东方财富美股日OHLC | `GET` | `api/v1/market/data/eastmoney-us-stock-daily-ohlc` | `stock_code`, `start_date`, `end_date`, `page`, `page_size` | `东方财富美股日OHLC.md` |
| [`eastmoney_us_stock_latest_kline`](#api-eastmoney-us-stock-latest-kline) | 东方财富美股最新OHLC | `GET` | `api/v1/market/data/eastmoney-us-stock-latest-ohlc` | `stock_code`, `page`, `page_size` | `东方财富美股最新OHLC.md` |
| [`eastmoney_us_stock_list`](#api-eastmoney-us-stock-list) | 东方财富美股列表 | `GET` | `api/v1/market/data/eastmoney-us-stock-list` | `refresh`, `page`, `page_size` | `东方财富美股列表.md` |
| [`us_balance`](#api-us-balance) | 美股资产负债表 | `GET` | `api/v1/market/data/us/us-balance` | `stock_code`, `period`, `report_type`, `start_date`, `end_date`, `page`, `page_size` | `美股资产负债表.md` |
| [`us_basic`](#api-us-basic) | 美股基础信息 | `GET` | `api/v1/market/data/us/us-basic` | `stock_code`, `page`, `page_size` | `美股基础信息.md` |
| [`us_cashflow`](#api-us-cashflow) | 美股现金流 | `GET` | `api/v1/market/data/us/us-cashflow` | `stock_code`, `period`, `report_type`, `start_date`, `end_date`, `page`, `page_size` | `美股现金流.md` |
| [`us_income`](#api-us-income) | 美股利润表 | `GET` | `api/v1/market/data/us/us-income` | `stock_code`, `period`, `report_type`, `start_date`, `end_date`, `page`, `page_size` | `美股利润表.md` |
| [`eastmoney_us_stock_daily_ohlc`](#api-eastmoney-us-stock-daily-ohlc) | 东方财富美股日OHLC | `GET` | `api/v1/market/data/eastmoney-us-stock-daily-ohlc` | `stock_code`, `start_date`, `end_date`, `page`, `page_size` | `东方财富美股日OHLC.md` |
| [`eastmoney_us_stock_latest_ohlc`](#api-eastmoney-us-stock-latest-ohlc) | 东方财富美股最新OHLC | `GET` | `api/v1/market/data/eastmoney-us-stock-latest-ohlc` | `stock_code`, `page`, `page_size` | `东方财富美股最新OHLC.md` |

### 指数专题

| SDK 方法 | 接口名称 | HTTP | Path | 参数 | 来源文档 |
|---|---|---|---|---|---|
| [`global_index_daily_kline`](#api-global-index-daily-kline) | 全球指数日K线 | `GET` | `api/v1/market/data/global-index/daily-kline` | `secid`, `start_date`, `end_date` | `全球指数日K线.md` |
| [`index_description_all`](#api-index-description-all) | 指数基础信息 | `GET` | `api/v1/market/data/index-description-all` | - | `指数基础信息.md` |
| [`index_description_list`](#api-index-description-list) | 中证指数描述列表 | `GET` | `api/v1/market/data/index/index_description` | `page`, `page_size` | `中证指数描述列表.md` |
| [`index_weight_list`](#api-index-weight-list) | 指数权重列表 | `GET` | `api/v1/market/data/index/index_weight` | `index_code`, `date`, `page`, `page_size` | `指数权重列表.md` |
| [`index_weight_summary`](#api-index-weight-summary) | 指数权重汇总 | `GET` | `api/v1/market/data/index/index_weight_summary` | `page`, `page_size` | `指数权重汇总.md` |
| [`sw_industry_constituent_history`](#api-sw-industry-constituent-history) | 申万行业成份股历史 | `GET` | `api/v1/market/data/sw-industry/constituent-history` | `industry_code` | `申万行业成份股历史.md` |
| [`sw_industry_daily_metrics`](#api-sw-industry-daily-metrics) | 申万行业日度指标 | `GET` | `api/v1/market/data/sw-industry/daily-metrics` | `level`, `start_date`, `end_date`, `industry_code`, `page`, `page_size` | `申万行业日度指标.md` |
| [`sw_industry_overview`](#api-sw-industry-overview) | 申万行业总览 | `GET` | `api/v1/market/data/sw-industry/overview` | `date`, `level`, `page`, `page_size` | `申万行业总览.md` |

### ETF专题

| SDK 方法 | 接口名称 | HTTP | Path | 参数 | 来源文档 |
|---|---|---|---|---|---|
| [`etf_adjust_factor`](#api-etf-adjust-factor) | ETF复权因子 | `GET` | `api/v1/market/data/etf-adjust-factor` | `symbol`, `trade_date`, `start_date`, `end_date`, `offset`, `limit` | `ETF复权因子.md` |
| [`etf_components`](#api-etf-components) | ETF成份股 | `GET` | `api/v1/market/data/etf-component` | `symbol` | `ETF成份股.md` |
| [`etf_components_all`](#api-etf-components-all) | ETF成份列表 | `GET` | `api/v1/market/data/etf-components-all` | - | `ETF成份列表.md` |
| [`etf_description_all`](#api-etf-description-all) | ETF基础信息 | `GET` | `api/v1/market/data/etf-description-all` | - | `ETF基础信息.md` |
| [`etf_fund_export`](#api-etf-fund-export) | 指数ETF基金导出 | `GET` | `api/v1/market/data/etf/zhitou-etf` | `request_id`, `page`, `page_size` | `指数ETF基金导出.md` |
| [`etf_pcf_list`](#api-etf-pcf-list) | ETF-PCF清单列表 | `GET` | `api/v1/market/data/etf-pcf/etf-pcfs` | `date`, `page`, `page_size` | `ETF-PCF清单列表.md` |
| [`etf_pre`](#api-etf-pre) | ETF盘前数据 | `GET` | `api/v1/market/data/etf-pre-data` | `date` | `ETF盘前数据.md` |
| [`etf_pre_single`](#api-etf-pre-single) | 单只ETF盘前数据 | `GET` | `api/v1/market/data/etf-pre-single` | `symbol`, `date` | `单只ETF盘前数据.md` |

### 公募基金

| SDK 方法 | 接口名称 | HTTP | Path | 参数 | 来源文档 |
|---|---|---|---|---|---|
| [`fund_basicinfo`](#api-fund-basicinfo) | 基金基础信息 | `GET` | `api/v1/market/data/fund/fund-basicinfo` | `institution_code`, `page`, `page_size` | `基金基础信息.md` |
| [`fund_cal_return`](#api-fund-cal-return) | 基金收益 | `GET` | `api/v1/market/data/fund/fund-cal-return` | `institution_code`, `cal-type` | `基金收益.md` |
| [`fund_nav`](#api-fund-nav) | 基金净值 | `GET` | `api/v1/market/data/fund/fund-nav` | `institution_code`, `page`, `page_size` | `基金净值.md` |
| [`fund_overview`](#api-fund-overview) | 基金总览 | `GET` | `api/v1/market/data/fund/fund-overview` | `page`, `page_size` | `基金总览.md` |
| [`fund_support_symbols`](#api-fund-support-symbols) | 基金支持标的 | `GET` | `api/v1/market/data/fund/fund-support-symbols` | `page`, `page_size` | `基金支持标的.md` |

### 期货数据

| SDK 方法 | 接口名称 | HTTP | Path | 参数 | 来源文档 |
|---|---|---|---|---|---|
| [`china_futures_base_data`](#api-china-futures-base-data) | 中国期货基础数据 | `GET` | `api/v1/market/data/futures/futures-base-data` | `trade_date`, `symbol` | `中国期货基础数据.md` |
| [`china_futures_lists`](#api-china-futures-lists) | 中国期货列表 | `GET` | `api/v1/market/data/futures/futures-lists` | `trade_date` | `中国期货列表.md` |
| [`eastmoney_futures_position`](#api-eastmoney-futures-position) | 东方财富期货持仓 | `GET` | `api/v1/market/data/eastmoney-futures-position` | `exchange`, `variety_code`, `contract_code`, `trade_date`, `start_date`, `end_date`, `member_name_abbr`, `page`, `page_size` | `东方财富期货持仓.md` |
| [`futures_contract_kline`](#api-futures-contract-kline) | 期货合约K线 | `GET` | `api/v1/market/data/futures/kline` | `symbol`, `interval`, `start`, `end`, `limit` | `期货合约K线.md` |
| [`major_contract`](#api-major-contract) | 重大合同 | `GET` | `api/v1/market/data/corporate/contract` | `start_date`, `end_date` | `重大合同.md` |
| [`major_contract_by_symbol`](#api-major-contract-by-symbol) | 重大合同按标的 | `GET` | `api/v1/market/data/corporate/contract/by-symbol` | `symbol`, `page`, `page_size` | `重大合同按标的.md` |
| [`major_contract_summary`](#api-major-contract-summary) | 重大合同汇总 | `GET` | `api/v1/market/data/corporate/contract/summary` | `page`, `page_size` | `重大合同汇总.md` |
| [`eastmoney_futures_strange`](#api-eastmoney-futures-strange) | 东方财富期货持仓 | `GET` | `api/v1/market/data/eastmoney-futures-position` | `exchange`, `variety_code`, `contract_code`, `trade_date`, `start_date`, `end_date`, `member_name_abbr`, `page`, `page_size` | `东方财富期货持仓.md` |
| [`futures_kline`](#api-futures-kline) | 期货合约K线 | `GET` | `api/v1/market/data/futures/kline` | `symbol`, `interval`, `start`, `end`, `limit` | `期货合约K线.md` |

### 债券专题

| SDK 方法 | 接口名称 | HTTP | Path | 参数 | 来源文档 |
|---|---|---|---|---|---|
| [`cb_base_data`](#api-cb-base-data) | 可转债基础数据 | `GET` | `api/v1/market/data/cb/cb-base-data` | `symbol_code` | `可转债基础数据.md` |
| [`cb_lists`](#api-cb-lists) | 可转债列表 | `GET` | `api/v1/market/data/cb/cb-lists` | - | `可转债列表.md` |

### 宏观经济

| SDK 方法 | 接口名称 | HTTP | Path | 参数 | 来源文档 |
|---|---|---|---|---|---|
| [`baidu_financial_calendar`](#api-baidu-financial-calendar) | 百度财经日历 | `GET` | `api/v1/market/data/finance/financial-calendar/baidu` | `start_date`, `end_date`, `category`, `page`, `page_size` | `百度财经日历.md` |
| [`consumer_credit_monthly`](#api-consumer-credit-monthly) | 社融信贷 | `GET` | `api/v1/market/data/economic/china-credit-loans` | - | `社融信贷.md` |
| [`consumer_customs_trade_monthly`](#api-consumer-customs-trade-monthly) | 进出口 | `GET` | `api/v1/market/data/economic/china-customs-trade` | - | `进出口.md` |
| [`consumer_fiscal_revenue_monthly`](#api-consumer-fiscal-revenue-monthly) | 财政收入 | `GET` | `api/v1/market/data/economic/china-fiscal-revenue` | - | `财政收入.md` |
| [`consumer_fixed_asset_monthly`](#api-consumer-fixed-asset-monthly) | 固定资产投资 | `GET` | `api/v1/market/data/economic/china-fixed-asset-investment` | - | `固定资产投资.md` |
| [`consumer_gdp_quarterly`](#api-consumer-gdp-quarterly) | GDP | `GET` | `api/v1/market/data/economic/china-gdp` | - | `GDP.md` |
| [`consumer_industrial_added_value_monthly`](#api-consumer-industrial-added-value-monthly) | 工业增加值 | `GET` | `api/v1/market/data/economic/china-industrial-added-value` | - | `工业增加值.md` |
| [`consumer_money_supply_monthly`](#api-consumer-money-supply-monthly) | 货币供应 | `GET` | `api/v1/market/data/economic/china-money-supply` | - | `货币供应.md` |
| [`consumer_pmi_monthly`](#api-consumer-pmi-monthly) | PMI | `GET` | `api/v1/market/data/economic/china-pmi` | - | `PMI.md` |
| [`consumer_ppi_monthly`](#api-consumer-ppi-monthly) | PPI | `GET` | `api/v1/market/data/economic/china-ppi` | - | `PPI.md` |
| [`consumer_price_index_monthly`](#api-consumer-price-index-monthly) | CPI | `GET` | `api/v1/market/data/economic/china-cpi` | - | `CPI.md` |
| [`consumer_retail_sales_monthly`](#api-consumer-retail-sales-monthly) | 社零 | `GET` | `api/v1/market/data/economic/china-retail-sales` | - | `社零.md` |
| [`lpr_monthly`](#api-lpr-monthly) | LPR | `GET` | `api/v1/market/data/economic/china-lpr` | - | `LPR.md` |
| [`reserve_ratio_monthly`](#api-reserve-ratio-monthly) | 存款准备金率 | `GET` | `api/v1/market/data/economic/china-reserve-ratio` | - | `存款准备金率.md` |
| [`tax_revenue_monthly`](#api-tax-revenue-monthly) | 税收 | `GET` | `api/v1/market/data/economic/china-tax-revenue` | - | `税收.md` |
| [`us_economic`](#api-us-economic) | 美国经济指标 | `GET` | `api/v1/market/data/economic/us-economic` | `type` | `美国经济指标.md` |
| [`wallstreetcn_financial_calendar`](#api-wallstreetcn-financial-calendar) | 华尔街见闻财经日历 | `GET` | `api/v1/market/data/finance/financial-calendar/wallstreetcn` | `start_date`, `end_date`, `page`, `page_size` | `华尔街见闻财经日历.md` |

### 大模型语料

| SDK 方法 | 接口名称 | HTTP | Path | 参数 | 来源文档 |
|---|---|---|---|---|---|
| [`semantic_search_news`](#api-semantic-search-news) | 新闻语义搜索 | `GET` | `api/v1/market/data/semantic-search-news` | `query`, `limit`, `year`, `start_time`, `end_time` | `新闻语义搜索.md` |
| [`shareholders_meeting`](#api-shareholders-meeting) | 股东大会 | `GET` | `api/v1/market/data/corporate/meeting` | `page`, `page_size` | `股东大会.md` |
| [`stock_announcements`](#api-stock-announcements) | 公告列表 | `GET` | `api/v1/market/data/announcements/stock-announcements` | `stock_code`, `start_date`, `end_date`, `type`, `page`, `page_size` | `公告列表.md` |
| [`stock_reports`](#api-stock-reports) | 研报列表 | `GET` | `api/v1/market/data/report/stock-reports` | `stock_code`, `start_date`, `end_date`, `type`, `page`, `page_size` | `研报列表.md` |
| [`type_reports`](#api-type-reports) | 研报分类 | `GET` | `api/v1/market/data/report/type-reports` | `rept_type`, `start_date`, `end_date`, `page`, `page_size` | `研报分类.md` |

### 现货数据

| SDK 方法 | 接口名称 | HTTP | Path | 参数 | 来源文档 |
|---|---|---|---|---|---|
| [`bullion_price`](#api-bullion-price) | 贵金属价格 | `GET` | `api/v1/market/data/bullion/price` | `symbol`, `start_date`, `end_date`, `page`, `page_size` | `贵金属价格.md` |
| [`bullion_support_symbol`](#api-bullion-support-symbol) | 贵金属支持标的 | `GET` | `api/v1/market/data/bullion/support-symbol` | - | `贵金属支持标的.md` |

### 外汇数据

| SDK 方法 | 接口名称 | HTTP | Path | 参数 | 来源文档 |
|---|---|---|---|---|---|
| [`consumer_forex_gold_monthly`](#api-consumer-forex-gold-monthly) | 外汇黄金 | `GET` | `api/v1/market/data/economic/china-forex-gold` | - | `外汇黄金.md` |

### 未发布

| SDK 方法 | 接口名称 | HTTP | Path | 参数 | 来源文档 |
|---|---|---|---|---|---|
| [`stock_dividends_paginated`](#api-stock-dividends-paginated) | 股票分红记录分页 | `GET` | `api/v1/market/data/dividends` | `page`, `page_size` | `股票分红记录分页.md` |
| [`stock_intraday`](#api-stock-intraday) | 股票日内分时 | `GET` | `api/v1/market/security/{symbol}/intraday` | `symbol` | `股票日内分时.md` |
| [`stock_ipos_paginated`](#api-stock-ipos-paginated) | 股票IPO分页 | `GET` | `api/v1/market/data/stock-ipos` | `page`, `page_size` | `股票IPO分页.md` |
| [`stock_related`](#api-stock-related) | 相关股票 | `GET` | `api/v1/market/security/{symbol}/related` | `symbol`, `limit` | `相关股票.md` |

## 接口详情

### 股票数据

<h4 id="api-abnormal-trading-details"><code>abnormal_trading_details</code></h4>

- 接口名称：龙虎榜明细
- HTTP：`GET`
- Path：`api/v1/market/data/abnormal-trading-details`
- 参数：`date`
- 来源文档：`龙虎榜明细.md`
- 原始接口：`abnormal_trading_details`

```text
龙虎榜明细.

Endpoint: ``api/v1/market/data/abnormal-trading-details``.
Method: ``GET``.
Documented endpoint: ``abnormal_trading_details``.

Args:
    date: 查询日期 YYYYMMDD；不传则使用当前内存快照 (type: string; required: N).
    raw: Return the decoded JSON payload without tabular extraction.
    fields: Optional field list or comma-separated field string applied after extraction.
    as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
    **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

Returns:
    A pandas ``DataFrame`` by default, Python rows when
    ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
    payloads when multi-page fetching is used with ``raw=True``.
```

<h4 id="api-abnormal-trading-overview"><code>abnormal_trading_overview</code></h4>

- 接口名称：龙虎榜总览
- HTTP：`GET`
- Path：`api/v1/market/data/abnormal-trading-overview`
- 参数：`date`
- 来源文档：`龙虎榜总览.md`
- 原始接口：`abnormal_trading_overview`

```text
龙虎榜总览.

Endpoint: ``api/v1/market/data/abnormal-trading-overview``.
Method: ``GET``.
Documented endpoint: ``abnormal_trading_overview``.

Args:
    date: 查询日期 YYYYMMDD；不传则使用当前内存快照 (type: string; required: N).
    raw: Return the decoded JSON payload without tabular extraction.
    fields: Optional field list or comma-separated field string applied after extraction.
    as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
    **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

Returns:
    A pandas ``DataFrame`` by default, Python rows when
    ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
    payloads when multi-page fetching is used with ``raw=True``.
```

<h4 id="api-auction-results"><code>auction_results</code></h4>

- 接口名称：集合竞价结果
- HTTP：`GET`
- Path：`api/v1/market/data/auction-results`
- 参数：`ts_code`, `trade_date`, `start_date`, `end_date`, `page`, `page_size`
- 来源文档：`集合竞价结果.md`
- 原始接口：`auction_results`

```text
集合竞价结果.

Endpoint: ``api/v1/market/data/auction-results``.
Method: ``GET``.
Documented endpoint: ``auction_results``.

Args:
    ts_code: 股票代码，如 000001.XSHE (type: string; required: N).
    trade_date: 交易日，格式 YYYYMMDD (type: string; required: N).
    start_date: 起始日期，格式 YYYYMMDD (type: string; required: N).
    end_date: 结束日期，格式 YYYYMMDD (type: string; required: N).
    page: Page number, starting from 1. If omitted, the server default is used unless ``limit`` or ``all_pages`` is set.
    page_size: Rows per page. The SDK validates this against the endpoint-specific maximum.
    limit: Maximum number of rows to return. The SDK may fetch multiple pages to satisfy this limit.
    all_pages: Fetch and combine pages until the server reports the last page.
    max_pages: Optional safety cap for ``all_pages``.
    raw: Return the decoded JSON payload without tabular extraction.
    fields: Optional field list or comma-separated field string applied after extraction.
    as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
    **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

Returns:
    A pandas ``DataFrame`` by default, Python rows when
    ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
    payloads when multi-page fetching is used with ``raw=True``.
```

<h4 id="api-balance"><code>balance</code></h4>

- 接口名称：A股资产负债表
- HTTP：`GET`
- Path：`api/v1/market/data/finance/balance`
- 参数：`stock_code`, `year`, `report_type`, `page`, `page_size`
- 来源文档：`A股资产负债表.md`
- 原始接口：`balance`

```text
A股资产负债表.

Endpoint: ``api/v1/market/data/finance/balance``.
Method: ``GET``.
Documented endpoint: ``balance``.

Args:
    stock_code: A 股代码，6 位数字 + 后缀（如 600519.SH）；存在则进入模式A 单票查询 (type: string; required: N).
    year: 年份（模式B 必填），如 2024 (type: int; required: N).
    report_type: 报告期类型（模式B 必填）：q1 / q2 / q3 / annual（兼容 h1） (type: string; required: N).
    page: Page number, starting from 1. If omitted, the server default is used unless ``limit`` or ``all_pages`` is set.
    page_size: Rows per page. The SDK validates this against the endpoint-specific maximum.
    limit: Maximum number of rows to return. The SDK may fetch multiple pages to satisfy this limit.
    all_pages: Fetch and combine pages until the server reports the last page.
    max_pages: Optional safety cap for ``all_pages``.
    raw: Return the decoded JSON payload without tabular extraction.
    fields: Optional field list or comma-separated field string applied after extraction.
    as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
    **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

Returns:
    A pandas ``DataFrame`` by default, Python rows when
    ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
    payloads when multi-page fetching is used with ``raw=True``.
```

<h4 id="api-block-trades"><code>block_trades</code></h4>

- 接口名称：大宗交易
- HTTP：`GET`
- Path：`api/v1/market/data/block-trades`
- 参数：`date`
- 来源文档：`大宗交易.md`
- 原始接口：`block_trades`

```text
大宗交易.

Endpoint: ``api/v1/market/data/block-trades``.
Method: ``GET``.
Documented endpoint: ``block_trades``.

Args:
    date: 查询日期 YYYYMMDD；不传则使用当前内存快照 (type: string; required: N).
    raw: Return the decoded JSON payload without tabular extraction.
    fields: Optional field list or comma-separated field string applied after extraction.
    as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
    **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

Returns:
    A pandas ``DataFrame`` by default, Python rows when
    ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
    payloads when multi-page fetching is used with ``raw=True``.
```

<h4 id="api-bse-mapping"><code>bse_mapping</code></h4>

- 接口名称：北交所映射
- HTTP：`GET`
- Path：`api/v1/market/data/bse-mapping`
- 参数：`o_code`, `n_code`
- 来源文档：`北交所映射.md`
- 原始接口：`get_bse_mapping`

```text
北交所映射.

Endpoint: ``api/v1/market/data/bse-mapping``.
Method: ``GET``.
Documented endpoint: ``get_bse_mapping``.

Args:
    o_code: 旧代码（如 `838163.BJ`） (type: string; required: N).
    n_code: 新代码（如 `920163.BJ`） (type: string; required: N).
    raw: Return the decoded JSON payload without tabular extraction.
    fields: Optional field list or comma-separated field string applied after extraction.
    as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
    **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

Returns:
    A pandas ``DataFrame`` by default, Python rows when
    ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
    payloads when multi-page fetching is used with ``raw=True``.
```

<h4 id="api-cashflow"><code>cashflow</code></h4>

- 接口名称：A股现金流量表
- HTTP：`GET`
- Path：`api/v1/market/data/finance/cashflow`
- 参数：`stock_code`, `year`, `report_type`, `page`, `page_size`
- 来源文档：`A股现金流量表.md`
- 原始接口：`cashflow`

```text
A股现金流量表.

Endpoint: ``api/v1/market/data/finance/cashflow``.
Method: ``GET``.
Documented endpoint: ``cashflow``.

Args:
    stock_code: A 股代码，6 位数字 + 后缀（如 000001.SZ）；存在则进入模式A 单票查询 (type: string; required: N).
    year: 年份（模式B 必填），如 2024 (type: int; required: N).
    report_type: 报告期类型（模式B 必填）：q1 / q2 / q3 / annual (type: string; required: N).
    page: Page number, starting from 1. If omitted, the server default is used unless ``limit`` or ``all_pages`` is set.
    page_size: Rows per page. The SDK validates this against the endpoint-specific maximum.
    limit: Maximum number of rows to return. The SDK may fetch multiple pages to satisfy this limit.
    all_pages: Fetch and combine pages until the server reports the last page.
    max_pages: Optional safety cap for ``all_pages``.
    raw: Return the decoded JSON payload without tabular extraction.
    fields: Optional field list or comma-separated field string applied after extraction.
    as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
    **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

Returns:
    A pandas ``DataFrame`` by default, Python rows when
    ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
    payloads when multi-page fetching is used with ``raw=True``.
```

<h4 id="api-cashflow-stock-code"><code>cashflow_stock_code</code></h4>

- 接口名称：现金流支持股票代码
- HTTP：`GET`
- Path：`api/v1/market/data/finance/cashflow-stock-code`
- 参数：-
- 来源文档：`现金流支持股票代码.md`
- 原始接口：`get_cashflow_stock_code`

```text
现金流支持股票代码.

Endpoint: ``api/v1/market/data/finance/cashflow-stock-code``.
Method: ``GET``.
Documented endpoint: ``get_cashflow_stock_code``.

Args:
    raw: Return the decoded JSON payload without tabular extraction.
    fields: Optional field list or comma-separated field string applied after extraction.
    as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
    **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

Returns:
    A pandas ``DataFrame`` by default, Python rows when
    ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
    payloads when multi-page fetching is used with ``raw=True``.
```

<h4 id="api-company-list"><code>company_list</code></h4>

- 接口名称：公司列表
- HTTP：`GET`
- Path：`api/v1/market/data/company-list`
- 参数：`stock_name`, `stock_code`, `page`, `page_size`
- 来源文档：`公司列表.md`
- 原始接口：`get_company_list`

```text
公司列表.

Endpoint: ``api/v1/market/data/company-list``.
Method: ``GET``.
Documented endpoint: ``get_company_list``.

Args:
    stock_name: 股票名称，精确匹配 (type: string; required: N).
    stock_code: 股票代码，精确匹配 (type: string; required: N).
    page: Page number, starting from 1. If omitted, the server default is used unless ``limit`` or ``all_pages`` is set.
    page_size: Rows per page. The SDK validates this against the endpoint-specific maximum.
    limit: Maximum number of rows to return. The SDK may fetch multiple pages to satisfy this limit.
    all_pages: Fetch and combine pages until the server reports the last page.
    max_pages: Optional safety cap for ``all_pages``.
    raw: Return the decoded JSON payload without tabular extraction.
    fields: Optional field list or comma-separated field string applied after extraction.
    as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
    **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

Returns:
    A pandas ``DataFrame`` by default, Python rows when
    ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
    payloads when multi-page fetching is used with ``raw=True``.
```

<h4 id="api-earnings-reports-paginated"><code>earnings_reports_paginated</code></h4>

- 接口名称：业绩快报
- HTTP：`GET`
- Path：`api/v1/market/data/finance/stock-performance-express`
- 参数：`stock_code`, `year`, `report_type`, `page`, `page_size`
- 来源文档：`业绩快报.md`
- 原始接口：`earnings_reports_paginated`

```text
业绩快报.

Endpoint: ``api/v1/market/data/finance/stock-performance-express``.
Method: ``GET``.
Documented endpoint: ``earnings_reports_paginated``.

Args:
    stock_code: A 股代码（如 000001.SZ）；传则查单票全部业绩快报 (type: string; required: N).
    year: 年份（按报告期查询时必填），如 2024 (type: int; required: N).
    report_type: 报告类型枚举（按报告期查询时必填）：q1 / q2 / q3 / annual / announcement (type: string; required: N).
    page: Page number, starting from 1. If omitted, the server default is used unless ``limit`` or ``all_pages`` is set.
    page_size: Rows per page. The SDK validates this against the endpoint-specific maximum.
    limit: Maximum number of rows to return. The SDK may fetch multiple pages to satisfy this limit.
    all_pages: Fetch and combine pages until the server reports the last page.
    max_pages: Optional safety cap for ``all_pages``.
    raw: Return the decoded JSON payload without tabular extraction.
    fields: Optional field list or comma-separated field string applied after extraction.
    as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
    **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

Returns:
    A pandas ``DataFrame`` by default, Python rows when
    ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
    payloads when multi-page fetching is used with ``raw=True``.
```

<h4 id="api-eastmoney-board-constituents"><code>eastmoney_board_constituents</code></h4>

- 接口名称：东方财富板块成份股
- HTTP：`GET`
- Path：`api/v1/market/data/eastmoney-board-constituents`
- 参数：`board_code`
- 来源文档：`东方财富板块成份股.md`
- 原始接口：`eastmoney_board_constituents`

```text
东方财富板块成份股.

Endpoint: ``api/v1/market/data/eastmoney-board-constituents``.
Method: ``GET``.
Documented endpoint: ``eastmoney_board_constituents``.

Args:
    board_code: 板块代码，如 BK1024 (type: string; required: Y).
    raw: Return the decoded JSON payload without tabular extraction.
    fields: Optional field list or comma-separated field string applied after extraction.
    as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
    **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

Returns:
    A pandas ``DataFrame`` by default, Python rows when
    ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
    payloads when multi-page fetching is used with ``raw=True``.
```

<h4 id="api-eastmoney-board-daily-kline"><code>eastmoney_board_daily_kline</code></h4>

- 接口名称：东方财富板块日线OHLC
- HTTP：`GET`
- Path：`api/v1/market/data/eastmoney-board-daily-ohlc`
- 参数：`board_code`, `start_date`, `end_date`, `page`, `page_size`
- 来源文档：`东方财富板块日线OHLC.md`
- 原始接口：`eastmoney_board_daily_kline`

```text
东方财富板块日线OHLC.

Endpoint: ``api/v1/market/data/eastmoney-board-daily-ohlc``.
Method: ``GET``.
Documented endpoint: ``eastmoney_board_daily_kline``.

Args:
    board_code: 板块代码，如 BK1024 (type: string; required: Y).
    start_date: 起始日期（含），YYYY-MM-DD 或 YYYYMMDD (type: string; required: N).
    end_date: 截止日期（含），YYYY-MM-DD 或 YYYYMMDD (type: string; required: N).
    page: Page number, starting from 1. If omitted, the server default is used unless ``limit`` or ``all_pages`` is set.
    page_size: Rows per page. The SDK validates this against the endpoint-specific maximum.
    limit: Maximum number of rows to return. The SDK may fetch multiple pages to satisfy this limit.
    all_pages: Fetch and combine pages until the server reports the last page.
    max_pages: Optional safety cap for ``all_pages``.
    raw: Return the decoded JSON payload without tabular extraction.
    fields: Optional field list or comma-separated field string applied after extraction.
    as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
    **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

Returns:
    A pandas ``DataFrame`` by default, Python rows when
    ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
    payloads when multi-page fetching is used with ``raw=True``.
```

<h4 id="api-eastmoney-board-latest-kline"><code>eastmoney_board_latest_kline</code></h4>

- 接口名称：东方财富板块最新OHLC
- HTTP：`GET`
- Path：`api/v1/market/data/eastmoney-board-latest-ohlc`
- 参数：`board_code`, `page`, `page_size`
- 来源文档：`东方财富板块最新OHLC.md`
- 原始接口：`eastmoney_board_latest_kline`

```text
东方财富板块最新OHLC.

Endpoint: ``api/v1/market/data/eastmoney-board-latest-ohlc``.
Method: ``GET``.
Documented endpoint: ``eastmoney_board_latest_kline``.

Args:
    board_code: 板块代码，如 BK1024；不传则返回全部板块最新K线 (type: string; required: N).
    page: Page number, starting from 1. If omitted, the server default is used unless ``limit`` or ``all_pages`` is set.
    page_size: Rows per page. The SDK validates this against the endpoint-specific maximum.
    limit: Maximum number of rows to return. The SDK may fetch multiple pages to satisfy this limit.
    all_pages: Fetch and combine pages until the server reports the last page.
    max_pages: Optional safety cap for ``all_pages``.
    raw: Return the decoded JSON payload without tabular extraction.
    fields: Optional field list or comma-separated field string applied after extraction.
    as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
    **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

Returns:
    A pandas ``DataFrame`` by default, Python rows when
    ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
    payloads when multi-page fetching is used with ``raw=True``.
```

<h4 id="api-eastmoney-concept-boards"><code>eastmoney_concept_boards</code></h4>

- 接口名称：东方财富概念板块
- HTTP：`GET`
- Path：`api/v1/market/data/eastmoney-concept-boards`
- 参数：-
- 来源文档：`东方财富概念板块.md`
- 原始接口：`eastmoney_concept_boards`

```text
东方财富概念板块.

Endpoint: ``api/v1/market/data/eastmoney-concept-boards``.
Method: ``GET``.
Documented endpoint: ``eastmoney_concept_boards``.

Args:
    raw: Return the decoded JSON payload without tabular extraction.
    fields: Optional field list or comma-separated field string applied after extraction.
    as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
    **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

Returns:
    A pandas ``DataFrame`` by default, Python rows when
    ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
    payloads when multi-page fetching is used with ``raw=True``.
```

<h4 id="api-eastmoney-dapan-flow"><code>eastmoney_dapan_flow</code></h4>

- 接口名称：东方财富大盘资金流
- HTTP：`GET`
- Path：`api/v1/market/data/eastmoney-dapan-flow`
- 参数：`trade_date`, `start_date`, `end_date`, `page`, `page_size`
- 来源文档：`东方财富大盘资金流.md`
- 原始接口：`get_eastmoney_dapan_flow`

```text
东方财富大盘资金流.

Endpoint: ``api/v1/market/data/eastmoney-dapan-flow``.
Method: ``GET``.
Documented endpoint: ``get_eastmoney_dapan_flow``.

Args:
    trade_date: 交易日 YYYYMMDD；与 start_date/end_date 互斥 (type: string; required: N).
    start_date: 区间起始日 YYYYMMDD；需与 end_date 同时提供 (type: string; required: N).
    end_date: 区间结束日 YYYYMMDD；需与 start_date 同时提供 (type: string; required: N).
    page: Page number, starting from 1. If omitted, the server default is used unless ``limit`` or ``all_pages`` is set.
    page_size: Rows per page. The SDK validates this against the endpoint-specific maximum.
    limit: Maximum number of rows to return. The SDK may fetch multiple pages to satisfy this limit.
    all_pages: Fetch and combine pages until the server reports the last page.
    max_pages: Optional safety cap for ``all_pages``.
    raw: Return the decoded JSON payload without tabular extraction.
    fields: Optional field list or comma-separated field string applied after extraction.
    as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
    **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

Returns:
    A pandas ``DataFrame`` by default, Python rows when
    ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
    payloads when multi-page fetching is used with ``raw=True``.
```

<h4 id="api-eastmoney-market-valuation"><code>eastmoney_market_valuation</code></h4>

- 接口名称：东方财富市场估值
- HTTP：`GET`
- Path：`api/v1/market/data/eastmoney-market-valuation`
- 参数：`market_code`, `trade_date`, `start_date`, `end_date`, `page`, `page_size`
- 来源文档：`东方财富市场估值.md`
- 原始接口：`get_eastmoney_market_valuation`

```text
东方财富市场估值.

Endpoint: ``api/v1/market/data/eastmoney-market-valuation``.
Method: ``GET``.
Documented endpoint: ``get_eastmoney_market_valuation``.

Args:
    market_code: 市场代码，如 000001=上证指数、000300=沪深300；不传返回全部 (type: string; required: N).
    trade_date: 交易日 YYYYMMDD；与 start_date/end_date 互斥 (type: string; required: N).
    start_date: 区间起始日 YYYYMMDD；需与 end_date 同时提供 (type: string; required: N).
    end_date: 区间结束日 YYYYMMDD；需与 start_date 同时提供 (type: string; required: N).
    page: Page number, starting from 1. If omitted, the server default is used unless ``limit`` or ``all_pages`` is set.
    page_size: Rows per page. The SDK validates this against the endpoint-specific maximum.
    limit: Maximum number of rows to return. The SDK may fetch multiple pages to satisfy this limit.
    all_pages: Fetch and combine pages until the server reports the last page.
    max_pages: Optional safety cap for ``all_pages``.
    raw: Return the decoded JSON payload without tabular extraction.
    fields: Optional field list or comma-separated field string applied after extraction.
    as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
    **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

Returns:
    A pandas ``DataFrame`` by default, Python rows when
    ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
    payloads when multi-page fetching is used with ``raw=True``.
```

<h4 id="api-eastmoney-rank"><code>eastmoney_rank</code></h4>

- 接口名称：东方财富股票排名
- HTTP：`GET`
- Path：`api/v1/market/data/eastmoney-rank`
- 参数：`rank_group`, `market`, `trade_date`
- 来源文档：`东方财富股票排名.md`
- 原始接口：`eastmoney_rank`

```text
东方财富股票排名.

Endpoint: ``api/v1/market/data/eastmoney-rank``.
Method: ``GET``.
Documented endpoint: ``eastmoney_rank``.

Args:
    rank_group: 榜单组：`hot`（人气榜）/ `up`（飙升榜） (type: string; required: N).
    market: 市场：`A`（A股）/ `HK`（港股）/ `US`（美股） (type: string; required: N).
    trade_date: 交易日期，格式 `YYYY-MM-DD`，不传默认取最新 (type: string; required: N).
    raw: Return the decoded JSON payload without tabular extraction.
    fields: Optional field list or comma-separated field string applied after extraction.
    as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
    **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

Returns:
    A pandas ``DataFrame`` by default, Python rows when
    ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
    payloads when multi-page fetching is used with ``raw=True``.
```

<h4 id="api-eastmoney-sector-flow"><code>eastmoney_sector_flow</code></h4>

- 接口名称：东方财富板块资金流
- HTTP：`GET`
- Path：`api/v1/market/data/eastmoney-sector-flow`
- 参数：`sector_code`, `sector_type`, `trade_date`, `start_date`, `end_date`, `page`, `page_size`
- 来源文档：`东方财富板块资金流.md`
- 原始接口：`get_eastmoney_sector_flow`

```text
东方财富板块资金流.

Endpoint: ``api/v1/market/data/eastmoney-sector-flow``.
Method: ``GET``.
Documented endpoint: ``get_eastmoney_sector_flow``.

Args:
    sector_code: 板块代码，如 BK0488 (type: string; required: N).
    sector_type: 板块类型：industry / concept / regional (type: string; required: N).
    trade_date: 交易日 YYYYMMDD；与 start_date/end_date 互斥 (type: string; required: N).
    start_date: 区间起始日 YYYYMMDD；需与 end_date 同时提供 (type: string; required: N).
    end_date: 区间结束日 YYYYMMDD；需与 start_date 同时提供 (type: string; required: N).
    page: Page number, starting from 1. If omitted, the server default is used unless ``limit`` or ``all_pages`` is set.
    page_size: Rows per page. The SDK validates this against the endpoint-specific maximum.
    limit: Maximum number of rows to return. The SDK may fetch multiple pages to satisfy this limit.
    all_pages: Fetch and combine pages until the server reports the last page.
    max_pages: Optional safety cap for ``all_pages``.
    raw: Return the decoded JSON payload without tabular extraction.
    fields: Optional field list or comma-separated field string applied after extraction.
    as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
    **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

Returns:
    A pandas ``DataFrame`` by default, Python rows when
    ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
    payloads when multi-page fetching is used with ``raw=True``.
```

<h4 id="api-eastmoney-stock-flow"><code>eastmoney_stock_flow</code></h4>

- 接口名称：东方财富个股资金流
- HTTP：`GET`
- Path：`api/v1/market/data/eastmoney-stock-flow`
- 参数：`symbol`, `trade_date`, `start_date`, `end_date`, `page`, `page_size`
- 来源文档：`东方财富个股资金流.md`
- 原始接口：`get_eastmoney_stock_flow`

```text
东方财富个股资金流.

Endpoint: ``api/v1/market/data/eastmoney-stock-flow``.
Method: ``GET``.
Documented endpoint: ``get_eastmoney_stock_flow``.

Args:
    symbol: 股票代码，如 600522 (type: string; required: N).
    trade_date: 交易日 YYYYMMDD；与 start_date/end_date 互斥 (type: string; required: N).
    start_date: 区间起始日 YYYYMMDD；需与 end_date 同时提供 (type: string; required: N).
    end_date: 区间结束日 YYYYMMDD；需与 start_date 同时提供 (type: string; required: N).
    page: Page number, starting from 1. If omitted, the server default is used unless ``limit`` or ``all_pages`` is set.
    page_size: Rows per page. The SDK validates this against the endpoint-specific maximum.
    limit: Maximum number of rows to return. The SDK may fetch multiple pages to satisfy this limit.
    all_pages: Fetch and combine pages until the server reports the last page.
    max_pages: Optional safety cap for ``all_pages``.
    raw: Return the decoded JSON payload without tabular extraction.
    fields: Optional field list or comma-separated field string applied after extraction.
    as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
    **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

Returns:
    A pandas ``DataFrame`` by default, Python rows when
    ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
    payloads when multi-page fetching is used with ``raw=True``.
```

<h4 id="api-eastmoney-stock-valuation"><code>eastmoney_stock_valuation</code></h4>

- 接口名称：东方财富个股估值
- HTTP：`GET`
- Path：`api/v1/market/data/eastmoney-stock-valuation`
- 参数：`symbol`, `trade_date`, `start_date`, `end_date`, `page`, `page_size`
- 来源文档：`东方财富个股估值.md`
- 原始接口：`get_eastmoney_stock_valuation`

```text
东方财富个股估值.

Endpoint: ``api/v1/market/data/eastmoney-stock-valuation``.
Method: ``GET``.
Documented endpoint: ``get_eastmoney_stock_valuation``.

Args:
    symbol: 股票代码，如 000001；不传返回全部 (type: string; required: N).
    trade_date: 交易日 YYYYMMDD；与 start_date/end_date 互斥 (type: string; required: N).
    start_date: 区间起始日 YYYYMMDD；需与 end_date 同时提供 (type: string; required: N).
    end_date: 区间结束日 YYYYMMDD；需与 start_date 同时提供 (type: string; required: N).
    page: Page number, starting from 1. If omitted, the server default is used unless ``limit`` or ``all_pages`` is set.
    page_size: Rows per page. The SDK validates this against the endpoint-specific maximum.
    limit: Maximum number of rows to return. The SDK may fetch multiple pages to satisfy this limit.
    all_pages: Fetch and combine pages until the server reports the last page.
    max_pages: Optional safety cap for ``all_pages``.
    raw: Return the decoded JSON payload without tabular extraction.
    fields: Optional field list or comma-separated field string applied after extraction.
    as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
    **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

Returns:
    A pandas ``DataFrame`` by default, Python rows when
    ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
    payloads when multi-page fetching is used with ``raw=True``.
```

<h4 id="api-goodwill-industry"><code>goodwill_industry</code></h4>

- 接口名称：商誉行业
- HTTP：`GET`
- Path：`api/v1/market/data/goodwill/industry`
- 参数：`date`, `page`, `page_size`
- 来源文档：`商誉行业.md`
- 原始接口：`goodwill_industry`

```text
商誉行业.

Endpoint: ``api/v1/market/data/goodwill/industry``.
Method: ``GET``.
Documented endpoint: ``goodwill_industry``.

Args:
    date: 报告期，如 20250331 (type: string; required: Y).
    page: Page number, starting from 1. If omitted, the server default is used unless ``limit`` or ``all_pages`` is set.
    page_size: Rows per page. The SDK validates this against the endpoint-specific maximum.
    limit: Maximum number of rows to return. The SDK may fetch multiple pages to satisfy this limit.
    all_pages: Fetch and combine pages until the server reports the last page.
    max_pages: Optional safety cap for ``all_pages``.
    raw: Return the decoded JSON payload without tabular extraction.
    fields: Optional field list or comma-separated field string applied after extraction.
    as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
    **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

Returns:
    A pandas ``DataFrame`` by default, Python rows when
    ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
    payloads when multi-page fetching is used with ``raw=True``.
```

<h4 id="api-goodwill-market-overview"><code>goodwill_market_overview</code></h4>

- 接口名称：商誉市场总览
- HTTP：`GET`
- Path：`api/v1/market/data/goodwill/market-overview`
- 参数：-
- 来源文档：`商誉市场总览.md`
- 原始接口：`goodwill_market_overview`

```text
商誉市场总览.

Endpoint: ``api/v1/market/data/goodwill/market-overview``.
Method: ``GET``.
Documented endpoint: ``goodwill_market_overview``.

Args:
    raw: Return the decoded JSON payload without tabular extraction.
    fields: Optional field list or comma-separated field string applied after extraction.
    as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
    **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

Returns:
    A pandas ``DataFrame`` by default, Python rows when
    ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
    payloads when multi-page fetching is used with ``raw=True``.
```

<h4 id="api-goodwill-predict"><code>goodwill_predict</code></h4>

- 接口名称：商誉预测
- HTTP：`GET`
- Path：`api/v1/market/data/goodwill/predict`
- 参数：`date`, `page`, `page_size`
- 来源文档：`商誉预测.md`
- 原始接口：`goodwill_predict`

```text
商誉预测.

Endpoint: ``api/v1/market/data/goodwill/predict``.
Method: ``GET``.
Documented endpoint: ``goodwill_predict``.

Args:
    date: 报告期，如 20250331 (type: string; required: Y).
    page: Page number, starting from 1. If omitted, the server default is used unless ``limit`` or ``all_pages`` is set.
    page_size: Rows per page. The SDK validates this against the endpoint-specific maximum.
    limit: Maximum number of rows to return. The SDK may fetch multiple pages to satisfy this limit.
    all_pages: Fetch and combine pages until the server reports the last page.
    max_pages: Optional safety cap for ``all_pages``.
    raw: Return the decoded JSON payload without tabular extraction.
    fields: Optional field list or comma-separated field string applied after extraction.
    as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
    **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

Returns:
    A pandas ``DataFrame`` by default, Python rows when
    ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
    payloads when multi-page fetching is used with ``raw=True``.
```

<h4 id="api-goodwill-stock-detail"><code>goodwill_stock_detail</code></h4>

- 接口名称：商誉个股明细
- HTTP：`GET`
- Path：`api/v1/market/data/goodwill/stock-detail`
- 参数：`date`, `page`, `page_size`
- 来源文档：`商誉个股明细.md`
- 原始接口：`goodwill_stock_detail`

```text
商誉个股明细.

Endpoint: ``api/v1/market/data/goodwill/stock-detail``.
Method: ``GET``.
Documented endpoint: ``goodwill_stock_detail``.

Args:
    date: 报告期，如 20250331 (type: string; required: Y).
    page: Page number, starting from 1. If omitted, the server default is used unless ``limit`` or ``all_pages`` is set.
    page_size: Rows per page. The SDK validates this against the endpoint-specific maximum.
    limit: Maximum number of rows to return. The SDK may fetch multiple pages to satisfy this limit.
    all_pages: Fetch and combine pages until the server reports the last page.
    max_pages: Optional safety cap for ``all_pages``.
    raw: Return the decoded JSON payload without tabular extraction.
    fields: Optional field list or comma-separated field string applied after extraction.
    as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
    **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

Returns:
    A pandas ``DataFrame`` by default, Python rows when
    ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
    payloads when multi-page fetching is used with ``raw=True``.
```

<h4 id="api-goodwill-stock-impairment"><code>goodwill_stock_impairment</code></h4>

- 接口名称：商誉减值
- HTTP：`GET`
- Path：`api/v1/market/data/goodwill/stock-impairment`
- 参数：`date`, `page`, `page_size`
- 来源文档：`商誉减值.md`
- 原始接口：`goodwill_stock_impairment`

```text
商誉减值.

Endpoint: ``api/v1/market/data/goodwill/stock-impairment``.
Method: ``GET``.
Documented endpoint: ``goodwill_stock_impairment``.

Args:
    date: 报告期，如 20250331 (type: string; required: Y).
    page: Page number, starting from 1. If omitted, the server default is used unless ``limit`` or ``all_pages`` is set.
    page_size: Rows per page. The SDK validates this against the endpoint-specific maximum.
    limit: Maximum number of rows to return. The SDK may fetch multiple pages to satisfy this limit.
    all_pages: Fetch and combine pages until the server reports the last page.
    max_pages: Optional safety cap for ``all_pages``.
    raw: Return the decoded JSON payload without tabular extraction.
    fields: Optional field list or comma-separated field string applied after extraction.
    as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
    **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

Returns:
    A pandas ``DataFrame`` by default, Python rows when
    ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
    payloads when multi-page fetching is used with ``raw=True``.
```

<h4 id="api-hk-sh-stock-connect-members"><code>hk_sh_stock_connect_members</code></h4>

- 接口名称：沪港通成份
- HTTP：`GET`
- Path：`api/v1/market/data/hk-sh-stock-connect-members`
- 参数：-
- 来源文档：`沪港通成份.md`
- 原始接口：`hk_sh_stock_connect_members`

```text
沪港通成份.

Endpoint: ``api/v1/market/data/hk-sh-stock-connect-members``.
Method: ``GET``.
Documented endpoint: ``hk_sh_stock_connect_members``.

Args:
    raw: Return the decoded JSON payload without tabular extraction.
    fields: Optional field list or comma-separated field string applied after extraction.
    as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
    **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

Returns:
    A pandas ``DataFrame`` by default, Python rows when
    ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
    payloads when multi-page fetching is used with ``raw=True``.
```

<h4 id="api-hk-sz-stock-connect-members"><code>hk_sz_stock_connect_members</code></h4>

- 接口名称：深港通成份
- HTTP：`GET`
- Path：`api/v1/market/data/hk-sz-stock-connect-members`
- 参数：-
- 来源文档：`深港通成份.md`
- 原始接口：`hk_sz_stock_connect_members`

```text
深港通成份.

Endpoint: ``api/v1/market/data/hk-sz-stock-connect-members``.
Method: ``GET``.
Documented endpoint: ``hk_sz_stock_connect_members``.

Args:
    raw: Return the decoded JSON payload without tabular extraction.
    fields: Optional field list or comma-separated field string applied after extraction.
    as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
    **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

Returns:
    A pandas ``DataFrame`` by default, Python rows when
    ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
    payloads when multi-page fetching is used with ``raw=True``.
```

<h4 id="api-income"><code>income</code></h4>

- 接口名称：A股利润表
- HTTP：`GET`
- Path：`api/v1/market/data/finance/income`
- 参数：`stock_code`, `year`, `report_type`, `page`, `page_size`
- 来源文档：`A股利润表.md`
- 原始接口：`income`

```text
A股利润表.

Endpoint: ``api/v1/market/data/finance/income``.
Method: ``GET``.
Documented endpoint: ``income``.

Args:
    stock_code: A 股代码，6 位数字 + 后缀（如 000001.SZ）；存在则进入模式A 单票查询 (type: string; required: N).
    year: 年份（模式B 必填），如 2024 (type: int; required: N).
    report_type: 报告期类型（模式B 必填）：q1 / q2 / q3 / annual（兼容 h1） (type: string; required: N).
    page: Page number, starting from 1. If omitted, the server default is used unless ``limit`` or ``all_pages`` is set.
    page_size: Rows per page. The SDK validates this against the endpoint-specific maximum.
    limit: Maximum number of rows to return. The SDK may fetch multiple pages to satisfy this limit.
    all_pages: Fetch and combine pages until the server reports the last page.
    max_pages: Optional safety cap for ``all_pages``.
    raw: Return the decoded JSON payload without tabular extraction.
    fields: Optional field list or comma-separated field string applied after extraction.
    as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
    **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

Returns:
    A pandas ``DataFrame`` by default, Python rows when
    ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
    payloads when multi-page fetching is used with ``raw=True``.
```

<h4 id="api-limit-down-pool"><code>limit_down_pool</code></h4>

- 接口名称：跌停池
- HTTP：`GET`
- Path：`api/v1/market/data/limit-down-pool`
- 参数：-
- 来源文档：`跌停池.md`
- 原始接口：`limit_down_pool`

```text
跌停池.

Endpoint: ``api/v1/market/data/limit-down-pool``.
Method: ``GET``.
Documented endpoint: ``limit_down_pool``.

Args:
    raw: Return the decoded JSON payload without tabular extraction.
    fields: Optional field list or comma-separated field string applied after extraction.
    as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
    **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

Returns:
    A pandas ``DataFrame`` by default, Python rows when
    ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
    payloads when multi-page fetching is used with ``raw=True``.
```

<h4 id="api-limit-event-timeline-3s"><code>limit_event_timeline_3s</code></h4>

- 接口名称：涨跌停事件时间线
- HTTP：`GET`
- Path：`api/v1/market/data/limit-event-timeline-3s`
- 参数：`symbol`
- 来源文档：`涨跌停事件时间线.md`
- 原始接口：`limit_event_timeline_3s`

```text
涨跌停事件时间线.

Endpoint: ``api/v1/market/data/limit-event-timeline-3s``.
Method: ``GET``.
Documented endpoint: ``limit_event_timeline_3s``.

Args:
    symbol: 标的代码，如 000001.XSHE；不传返回全市场 (type: string; required: N).
    raw: Return the decoded JSON payload without tabular extraction.
    fields: Optional field list or comma-separated field string applied after extraction.
    as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
    **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

Returns:
    A pandas ``DataFrame`` by default, Python rows when
    ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
    payloads when multi-page fetching is used with ``raw=True``.
```

<h4 id="api-limit-up-break-pool"><code>limit_up_break_pool</code></h4>

- 接口名称：炸板池
- HTTP：`GET`
- Path：`api/v1/market/data/limit-up-break-pool`
- 参数：-
- 来源文档：`炸板池.md`
- 原始接口：`limit_up_break_pool`

```text
炸板池.

Endpoint: ``api/v1/market/data/limit-up-break-pool``.
Method: ``GET``.
Documented endpoint: ``limit_up_break_pool``.

Args:
    raw: Return the decoded JSON payload without tabular extraction.
    fields: Optional field list or comma-separated field string applied after extraction.
    as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
    **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

Returns:
    A pandas ``DataFrame`` by default, Python rows when
    ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
    payloads when multi-page fetching is used with ``raw=True``.
```

<h4 id="api-limit-up-pool"><code>limit_up_pool</code></h4>

- 接口名称：涨停池
- HTTP：`GET`
- Path：`api/v1/market/data/limit-up-pool`
- 参数：-
- 来源文档：`涨停池.md`
- 原始接口：`limit_up_pool`

```text
涨停池.

Endpoint: ``api/v1/market/data/limit-up-pool``.
Method: ``GET``.
Documented endpoint: ``limit_up_pool``.

Args:
    raw: Return the decoded JSON payload without tabular extraction.
    fields: Optional field list or comma-separated field string applied after extraction.
    as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
    **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

Returns:
    A pandas ``DataFrame`` by default, Python rows when
    ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
    payloads when multi-page fetching is used with ``raw=True``.
```

<h4 id="api-limit-up-pool-yesterday"><code>limit_up_pool_yesterday</code></h4>

- 接口名称：昨日涨停池
- HTTP：`GET`
- Path：`api/v1/market/data/limit-up-pool-yesterday`
- 参数：-
- 来源文档：`昨日涨停池.md`
- 原始接口：`limit_up_pool_yesterday`

```text
昨日涨停池.

Endpoint: ``api/v1/market/data/limit-up-pool-yesterday``.
Method: ``GET``.
Documented endpoint: ``limit_up_pool_yesterday``.

Args:
    raw: Return the decoded JSON payload without tabular extraction.
    fields: Optional field list or comma-separated field string applied after extraction.
    as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
    **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

Returns:
    A pandas ``DataFrame`` by default, Python rows when
    ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
    payloads when multi-page fetching is used with ``raw=True``.
```

<h4 id="api-margin-trading-details"><code>margin_trading_details</code></h4>

- 接口名称：融资融券明细
- HTTP：`GET`
- Path：`api/v1/market/data/margin-trading-details`
- 参数：`date`, `page`, `page_size`
- 来源文档：`融资融券明细.md`
- 原始接口：`margin_trading_details`

```text
融资融券明细.

Endpoint: ``api/v1/market/data/margin-trading-details``.
Method: ``GET``.
Documented endpoint: ``margin_trading_details``.

Args:
    date: 查询日期 YYYYMMDD；不传则使用当前内存快照 (type: string; required: N).
    page: Page number, starting from 1. If omitted, the server default is used unless ``limit`` or ``all_pages`` is set.
    page_size: Rows per page. The SDK validates this against the endpoint-specific maximum.
    limit: Maximum number of rows to return. The SDK may fetch multiple pages to satisfy this limit.
    all_pages: Fetch and combine pages until the server reports the last page.
    max_pages: Optional safety cap for ``all_pages``.
    raw: Return the decoded JSON payload without tabular extraction.
    fields: Optional field list or comma-separated field string applied after extraction.
    as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
    **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

Returns:
    A pandas ``DataFrame`` by default, Python rows when
    ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
    payloads when multi-page fetching is used with ``raw=True``.
```

<h4 id="api-margin-trading-details-paginated"><code>margin_trading_details_paginated</code></h4>

- 接口名称：融资融券明细分页
- HTTP：`GET`
- Path：`api/v1/market/data/margin-trading-details`
- 参数：`date`, `page`, `page_size`
- 来源文档：`融资融券明细分页.md`
- 原始接口：`margin_trading_details_paginated`

```text
融资融券明细分页.

Endpoint: ``api/v1/market/data/margin-trading-details``.
Method: ``GET``.
Documented endpoint: ``margin_trading_details_paginated``.

Args:
    date: 查询日期 YYYYMMDD；不传则使用当前内存快照 (type: string; required: N).
    page: Page number, starting from 1. If omitted, the server default is used unless ``limit`` or ``all_pages`` is set.
    page_size: Rows per page. The SDK validates this against the endpoint-specific maximum.
    limit: Maximum number of rows to return. The SDK may fetch multiple pages to satisfy this limit.
    all_pages: Fetch and combine pages until the server reports the last page.
    max_pages: Optional safety cap for ``all_pages``.
    raw: Return the decoded JSON payload without tabular extraction.
    fields: Optional field list or comma-separated field string applied after extraction.
    as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
    **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

Returns:
    A pandas ``DataFrame`` by default, Python rows when
    ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
    payloads when multi-page fetching is used with ``raw=True``.
```

<h4 id="api-northbound"><code>northbound</code></h4>

- 接口名称：北向资金交易
- HTTP：`GET`
- Path：`api/v1/market/data/northbound`
- 参数：`date`
- 来源文档：`北向资金交易.md`
- 原始接口：`northbound`

```text
北向资金交易.

Endpoint: ``api/v1/market/data/northbound``.
Method: ``GET``.
Documented endpoint: ``northbound``.

Args:
    date: 交易日，格式 YYYYMMDD (type: string; required: Y).
    raw: Return the decoded JSON payload without tabular extraction.
    fields: Optional field list or comma-separated field string applied after extraction.
    as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
    **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

Returns:
    A pandas ``DataFrame`` by default, Python rows when
    ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
    payloads when multi-page fetching is used with ``raw=True``.
```

<h4 id="api-nth-trade-date"><code>nth_trade_date</code></h4>

- 接口名称：第N个交易日
- HTTP：`GET`
- Path：`api/v1/market/data/time/get-nth-trade-date`
- 参数：`n`
- 来源文档：`第N个交易日.md`
- 原始接口：`get_nth_trade_date`

```text
第N个交易日.

Endpoint: ``api/v1/market/data/time/get-nth-trade-date``.
Method: ``GET``.
Documented endpoint: ``get_nth_trade_date``.

Args:
    n: 需要获取的前 N 个交易日，N >= 1 (type: uint32; required: Y).
    raw: Return the decoded JSON payload without tabular extraction.
    fields: Optional field list or comma-separated field string applied after extraction.
    as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
    **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

Returns:
    A pandas ``DataFrame`` by default, Python rows when
    ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
    payloads when multi-page fetching is used with ``raw=True``.
```

<h4 id="api-performance-forecasts-paginated"><code>performance_forecasts_paginated</code></h4>

- 接口名称：业绩预告
- HTTP：`GET`
- Path：`api/v1/market/data/finance/stock-performance-forecast`
- 参数：`stock_code`, `year`, `report_type`, `page`, `page_size`
- 来源文档：`业绩预告.md`
- 原始接口：`performance_forecasts_paginated`

```text
业绩预告.

Endpoint: ``api/v1/market/data/finance/stock-performance-forecast``.
Method: ``GET``.
Documented endpoint: ``performance_forecasts_paginated``.

Args:
    stock_code: A 股代码，6 位数字 + 后缀（如 000001.SZ）；存在则进入模式A 单票查询 (type: string; required: N).
    year: 年份（模式B 必填），如 2024 (type: int; required: N).
    report_type: 报告期类型（模式B 必填）：q1 / q2 / q3 / annual (type: string; required: N).
    page: Page number, starting from 1. If omitted, the server default is used unless ``limit`` or ``all_pages`` is set.
    page_size: Rows per page. The SDK validates this against the endpoint-specific maximum.
    limit: Maximum number of rows to return. The SDK may fetch multiple pages to satisfy this limit.
    all_pages: Fetch and combine pages until the server reports the last page.
    max_pages: Optional safety cap for ``all_pages``.
    raw: Return the decoded JSON payload without tabular extraction.
    fields: Optional field list or comma-separated field string applied after extraction.
    as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
    **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

Returns:
    A pandas ``DataFrame`` by default, Python rows when
    ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
    payloads when multi-page fetching is used with ``raw=True``.
```

<h4 id="api-price-change"><code>price_change</code></h4>

- 接口名称：价格变动
- HTTP：`GET`
- Path：`api/v1/market/data/price/get-price-change`
- 参数：`stock_code`, `base_date`, `n`, `direction`
- 来源文档：`价格变动.md`
- 原始接口：`get_price_change`

```text
价格变动.

Endpoint: ``api/v1/market/data/price/get-price-change``.
Method: ``GET``.
Documented endpoint: ``get_price_change``.

Args:
    stock_code: 目标股票 6 位纯数字代码，兼容沪市/深市/创业板/科创板 (type: string; required: Y).
    base_date: 涨跌幅计算基准日，格式 YYYYMMDD (type: string; required: Y).
    n: 需计算的有效交易日数量，建议不超过 365 (type: uint32; required: Y).
    direction: 计算方向：forward（基准日为结束日）/ backward（基准日为开始日） (type: string; required: Y).
    raw: Return the decoded JSON payload without tabular extraction.
    fields: Optional field list or comma-separated field string applied after extraction.
    as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
    **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

Returns:
    A pandas ``DataFrame`` by default, Python rows when
    ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
    payloads when multi-page fetching is used with ``raw=True``.
```

<h4 id="api-risk-warning-stock-quotes"><code>risk_warning_stock_quotes</code></h4>

- 接口名称：风险警示股行情
- HTTP：`GET`
- Path：`api/v1/market/data/risk-warning-stocks/quotes`
- 参数：`date`
- 来源文档：`风险警示股行情.md`
- 原始接口：`risk_warning_stock_quotes`

```text
风险警示股行情.

Endpoint: ``api/v1/market/data/risk-warning-stocks/quotes``.
Method: ``GET``.
Documented endpoint: ``risk_warning_stock_quotes``.

Args:
    date: 交易日，格式 YYYYMMDD (type: string; required: Y).
    raw: Return the decoded JSON payload without tabular extraction.
    fields: Optional field list or comma-separated field string applied after extraction.
    as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
    **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

Returns:
    A pandas ``DataFrame`` by default, Python rows when
    ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
    payloads when multi-page fetching is used with ``raw=True``.
```

<h4 id="api-risk-warning-stocks"><code>risk_warning_stocks</code></h4>

- 接口名称：风险警示股
- HTTP：`GET`
- Path：`api/v1/market/data/risk-warning-stocks`
- 参数：`date`
- 来源文档：`风险警示股.md`
- 原始接口：`risk_warning_stocks`

```text
风险警示股.

Endpoint: ``api/v1/market/data/risk-warning-stocks``.
Method: ``GET``.
Documented endpoint: ``risk_warning_stocks``.

Args:
    date: 交易日，格式 YYYYMMDD (type: string; required: Y).
    raw: Return the decoded JSON payload without tabular extraction.
    fields: Optional field list or comma-separated field string applied after extraction.
    as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
    **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

Returns:
    A pandas ``DataFrame`` by default, Python rows when
    ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
    payloads when multi-page fetching is used with ``raw=True``.
```

<h4 id="api-search"><code>search</code></h4>

- 接口名称：标的搜索
- HTTP：`GET`
- Path：`api/v1/market/security/search`
- 参数：`query`, `limit`
- 来源文档：`标的搜索.md`
- 原始接口：`search`

```text
标的搜索.

Endpoint: ``api/v1/market/security/search``.
Method: ``GET``.
Documented endpoint: ``search``.

Args:
    query: 搜索关键词；支持名称、标的代码、拼音全拼/首字母；大小写不敏感，自动 trim (type: string; required: Y).
    limit: 返回最大条数，默认 1 (type: int; required: N).
    raw: Return the decoded JSON payload without tabular extraction.
    fields: Optional field list or comma-separated field string applied after extraction.
    as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
    **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

Returns:
    A pandas ``DataFrame`` by default, Python rows when
    ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
    payloads when multi-page fetching is used with ``raw=True``.
```

<h4 id="api-sh-hk-stock-connect-members"><code>sh_hk_stock_connect_members</code></h4>

- 接口名称：沪股通成份
- HTTP：`GET`
- Path：`api/v1/market/data/sh-hk-stock-connect-members`
- 参数：-
- 来源文档：`沪股通成份.md`
- 原始接口：`sh_hk_stock_connect_members`

```text
沪股通成份.

Endpoint: ``api/v1/market/data/sh-hk-stock-connect-members``.
Method: ``GET``.
Documented endpoint: ``sh_hk_stock_connect_members``.

Args:
    raw: Return the decoded JSON payload without tabular extraction.
    fields: Optional field list or comma-separated field string applied after extraction.
    as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
    **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

Returns:
    A pandas ``DataFrame`` by default, Python rows when
    ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
    payloads when multi-page fetching is used with ``raw=True``.
```

<h4 id="api-southbound"><code>southbound</code></h4>

- 接口名称：南向资金交易
- HTTP：`GET`
- Path：`api/v1/market/data/southbound`
- 参数：`date`
- 来源文档：`南向资金交易.md`
- 原始接口：`southbound`

```text
南向资金交易.

Endpoint: ``api/v1/market/data/southbound``.
Method: ``GET``.
Documented endpoint: ``southbound``.

Args:
    date: 交易日，格式 YYYYMMDD (type: string; required: Y).
    raw: Return the decoded JSON payload without tabular extraction.
    fields: Optional field list or comma-separated field string applied after extraction.
    as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
    **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

Returns:
    A pandas ``DataFrame`` by default, Python rows when
    ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
    payloads when multi-page fetching is used with ``raw=True``.
```

<h4 id="api-stk-ah-comparison"><code>stk_ah_comparison</code></h4>

- 接口名称：AH股对比
- HTTP：`GET`
- Path：`api/v1/market/data/hk/stk-ah-comparison`
- 参数：`hk_code`, `ts_code`, `trade_date`, `start_date`, `end_date`, `page`, `page_size`
- 来源文档：`AH股对比.md`
- 原始接口：`get_stk_ah_comparison`

```text
AH股对比.

Endpoint: ``api/v1/market/data/hk/stk-ah-comparison``.
Method: ``GET``.
Documented endpoint: ``get_stk_ah_comparison``.

Args:
    hk_code: 港股股票代码，支持 `700` 或 `00700.HK` (type: string; required: N).
    ts_code: A 股股票代码，格式 `xxxxxx.SH/SZ/BJ` (type: string; required: N).
    trade_date: 交易日期 YYYYMMDD (type: int32; required: N).
    start_date: 起始日期 YYYYMMDD (type: int32; required: N).
    end_date: 结束日期 YYYYMMDD (type: int32; required: N).
    page: Page number, starting from 1. If omitted, the server default is used unless ``limit`` or ``all_pages`` is set.
    page_size: Rows per page. The SDK validates this against the endpoint-specific maximum.
    limit: Maximum number of rows to return. The SDK may fetch multiple pages to satisfy this limit.
    all_pages: Fetch and combine pages until the server reports the last page.
    max_pages: Optional safety cap for ``all_pages``.
    raw: Return the decoded JSON payload without tabular extraction.
    fields: Optional field list or comma-separated field string applied after extraction.
    as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
    **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

Returns:
    A pandas ``DataFrame`` by default, Python rows when
    ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
    payloads when multi-page fetching is used with ``raw=True``.
```

<h4 id="api-stk-limit"><code>stk_limit</code></h4>

- 接口名称：涨跌停价
- HTTP：`GET`
- Path：`api/v1/market/data/stk-limit`
- 参数：`instrument_type`, `symbol`, `symbol_id`, `market_id`, `trade_date`, `start_date`, `end_date`, `page`, `page_size`
- 来源文档：`涨跌停价.md`
- 原始接口：`stk_limit`

```text
涨跌停价.

Endpoint: ``api/v1/market/data/stk-limit``.
Method: ``GET``.
Documented endpoint: ``stk_limit``.

Args:
    instrument_type: 标的类型：stock / etf / cb；不传返回三类（排除指数） (type: string; required: N).
    symbol: 标的代码，支持 000001.SZ / 000001.XSHE / 600519.SH 等；存在时忽略 symbol_id+market_id (type: string; required: N).
    symbol_id: 标的 ID，与 market_id 配合使用 (type: int32; required: N).
    market_id: 市场 ID，与 symbol_id 配合使用 (type: int16; required: N).
    trade_date: 交易日 YYYYMMDD，查单日全市场时使用 (type: int32; required: N).
    start_date: 单票历史区间起始日 YYYYMMDD（需配 symbol 或 symbol_id+market_id） (type: int32; required: N).
    end_date: 单票历史区间结束日 YYYYMMDD (type: int32; required: N).
    page: Page number, starting from 1. If omitted, the server default is used unless ``limit`` or ``all_pages`` is set.
    page_size: Rows per page. The SDK validates this against the endpoint-specific maximum.
    limit: Maximum number of rows to return. The SDK may fetch multiple pages to satisfy this limit.
    all_pages: Fetch and combine pages until the server reports the last page.
    max_pages: Optional safety cap for ``all_pages``.
    raw: Return the decoded JSON payload without tabular extraction.
    fields: Optional field list or comma-separated field string applied after extraction.
    as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
    **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

Returns:
    A pandas ``DataFrame`` by default, Python rows when
    ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
    payloads when multi-page fetching is used with ``raw=True``.
```

<h4 id="api-stk-premarket"><code>stk_premarket</code></h4>

- 接口名称：盘前数据
- HTTP：`GET`
- Path：`api/v1/market/data/stk-premarket`
- 参数：`ts_code`, `trade_date`, `start_date`, `end_date`, `page`, `page_size`
- 来源文档：`盘前数据.md`
- 原始接口：`stk_premarket`

```text
盘前数据.

Endpoint: ``api/v1/market/data/stk-premarket``.
Method: ``GET``.
Documented endpoint: ``stk_premarket``.

Args:
    ts_code: 股票代码，如 000001.SZ / 600519.SH (type: string; required: N).
    trade_date: 交易日 YYYYMMDD，查单日全市场时使用 (type: int32; required: N).
    start_date: 单票历史区间起始日 YYYYMMDD（需配 ts_code） (type: int32; required: N).
    end_date: 单票历史区间结束日 YYYYMMDD (type: int32; required: N).
    page: Page number, starting from 1. If omitted, the server default is used unless ``limit`` or ``all_pages`` is set.
    page_size: Rows per page. The SDK validates this against the endpoint-specific maximum.
    limit: Maximum number of rows to return. The SDK may fetch multiple pages to satisfy this limit.
    all_pages: Fetch and combine pages until the server reports the last page.
    max_pages: Optional safety cap for ``all_pages``.
    raw: Return the decoded JSON payload without tabular extraction.
    fields: Optional field list or comma-separated field string applied after extraction.
    as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
    **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

Returns:
    A pandas ``DataFrame`` by default, Python rows when
    ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
    payloads when multi-page fetching is used with ``raw=True``.
```

<h4 id="api-stock-adjust-factor"><code>stock_adjust_factor</code></h4>

- 接口名称：股票复权因子
- HTTP：`GET`
- Path：`api/v1/market/data/stock-adjust-factor`
- 参数：`symbol`, `trade_date`, `start_date`, `end_date`, `offset`, `limit`
- 来源文档：`股票复权因子.md`
- 原始接口：`stock_adjust_factor`

```text
股票复权因子.

Endpoint: ``api/v1/market/data/stock-adjust-factor``.
Method: ``GET``.
Documented endpoint: ``stock_adjust_factor``.

Args:
    symbol: 股票代码，支持纯数字或带后缀格式；区间扫描必填 (type: string; required: N).
    trade_date: 交易日期 YYYYMMDD；空则默认当天，非交易日回退前一交易日 (type: string; required: N).
    start_date: 区间起始日期 YYYYMMDD；区间扫描必填且需配 symbol (type: string; required: N).
    end_date: 区间结束日期 YYYYMMDD；区间扫描必填且需配 symbol (type: string; required: N).
    offset: 返回结果起始偏移 (type: int; required: N).
    limit: 返回结果最大条数 (type: int; required: N).
    raw: Return the decoded JSON payload without tabular extraction.
    fields: Optional field list or comma-separated field string applied after extraction.
    as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
    **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

Returns:
    A pandas ``DataFrame`` by default, Python rows when
    ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
    payloads when multi-page fetching is used with ``raw=True``.
```

<h4 id="api-stock-candlesticks"><code>stock_candlesticks</code></h4>

- 接口名称：股票K线
- HTTP：`POST`
- Path：`api/v1/market/data/stock-candlesticks`
- 参数：`symbol`, `interval_unit`, `interval_value`, `adjust_kind`, `since_ts_millis`, `until_ts_millis`, `limit`
- 来源文档：`股票K线.md`
- 原始接口：`stock_candlesticks`

```text
股票K线.

Endpoint: ``api/v1/market/data/stock-candlesticks``.
Method: ``POST``.
Documented endpoint: ``stock_candlesticks``.

Args:
    symbol: 标的代码，如 000001.SZ (type: SymbolKey; required: Y).
    interval_unit: 周期单位：Minute/Day/Week/Month/Year (type: enum; required: Y).
    interval_value: 间隔数值（默认1，如 Day+1=日K，Minute+5=5分钟） (type: int; required: N).
    adjust_kind: 复权：None(默认,除权)/Forward(前复权)/Backward(后复权) (type: enum; required: N).
    since_ts_millis: 开始时间戳（毫秒）；与 until 跨度 ≤3 天 (type: DateTime(ms); required: N).
    until_ts_millis: 结束时间戳（毫秒） (type: DateTime(ms); required: Y).
    limit: 返回条数上限 (type: int; required: N).
    raw: Return the decoded JSON payload without tabular extraction.
    fields: Optional field list or comma-separated field string applied after extraction.
    as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
    **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

Returns:
    A pandas ``DataFrame`` by default, Python rows when
    ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
    payloads when multi-page fetching is used with ``raw=True``.
```

<h4 id="api-stock-candlesticks-batch"><code>stock_candlesticks_batch</code></h4>

- 接口名称：批量股票K线
- HTTP：`POST`
- Path：`api/v1/market/data/stock-candlesticks/batch`
- 参数：`symbols`, `interval_unit`, `interval_value`, `adjust_kind`, `since_ts_millis`, `until_ts_millis`, `limit`
- 来源文档：`批量股票K线.md`
- 原始接口：`stock_candlesticks_batch`

```text
批量股票K线.

Endpoint: ``api/v1/market/data/stock-candlesticks/batch``.
Method: ``POST``.
Documented endpoint: ``stock_candlesticks_batch``.

Args:
    symbols: 标的代码列表，如 ["000001.SZ","600000.SH"] (type: array[SymbolKey]; required: Y).
    interval_unit: 周期单位：Minute/Day/Week/Month/Year (type: enum; required: Y).
    interval_value: 间隔数值（默认1） (type: int; required: N).
    adjust_kind: 复权：None(默认)/Forward(前复权)/Backward(后复权) (type: enum; required: N).
    since_ts_millis: 开始时间戳（毫秒）；与 until 跨度 ≤3 天 (type: DateTime(ms); required: N).
    until_ts_millis: 结束时间戳（毫秒） (type: DateTime(ms); required: Y).
    limit: 每标的返回条数上限 (type: int; required: N).
    raw: Return the decoded JSON payload without tabular extraction.
    fields: Optional field list or comma-separated field string applied after extraction.
    as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
    **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

Returns:
    A pandas ``DataFrame`` by default, Python rows when
    ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
    payloads when multi-page fetching is used with ``raw=True``.
```

<h4 id="api-stock-capital-flows-paginated"><code>stock_capital_flows_paginated</code></h4>

- 接口名称：股票资金流向
- HTTP：`GET`
- Path：`api/v1/market/data/stock-capital-flows`
- 参数：`date`, `page`, `page_size`
- 来源文档：`股票资金流向.md`
- 原始接口：`stock_capital_flows_paginated`

```text
股票资金流向.

Endpoint: ``api/v1/market/data/stock-capital-flows``.
Method: ``GET``.
Documented endpoint: ``stock_capital_flows_paginated``.

Args:
    date: 查询日期 YYYYMMDD；传入时查询该日 15:30 快照 (type: string; required: N).
    page: Page number, starting from 1. If omitted, the server default is used unless ``limit`` or ``all_pages`` is set.
    page_size: Rows per page. The SDK validates this against the endpoint-specific maximum.
    limit: Maximum number of rows to return. The SDK may fetch multiple pages to satisfy this limit.
    all_pages: Fetch and combine pages until the server reports the last page.
    max_pages: Optional safety cap for ``all_pages``.
    raw: Return the decoded JSON payload without tabular extraction.
    fields: Optional field list or comma-separated field string applied after extraction.
    as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
    **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

Returns:
    A pandas ``DataFrame`` by default, Python rows when
    ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
    payloads when multi-page fetching is used with ``raw=True``.
```

<h4 id="api-stock-comment-desire-em"><code>stock_comment_desire_em</code></h4>

- 接口名称：千股千评意愿度
- HTTP：`GET`
- Path：`api/v1/market/data/stock-comment/desire`
- 参数：`symbol`
- 来源文档：`千股千评意愿度.md`
- 原始接口：`stock_comment_desire_em`

```text
千股千评意愿度.

Endpoint: ``api/v1/market/data/stock-comment/desire``.
Method: ``GET``.
Documented endpoint: ``stock_comment_desire_em``.

Args:
    symbol: 证券代码（纯数字，如 600000） (type: string; required: Y).
    raw: Return the decoded JSON payload without tabular extraction.
    fields: Optional field list or comma-separated field string applied after extraction.
    as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
    **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

Returns:
    A pandas ``DataFrame`` by default, Python rows when
    ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
    payloads when multi-page fetching is used with ``raw=True``.
```

<h4 id="api-stock-comment-em"><code>stock_comment_em</code></h4>

- 接口名称：千股千评
- HTTP：`GET`
- Path：`api/v1/market/data/stock-comment/index`
- 参数：`page`, `page_size`
- 来源文档：`千股千评.md`
- 原始接口：`stock_comment_em`

```text
千股千评.

Endpoint: ``api/v1/market/data/stock-comment/index``.
Method: ``GET``.
Documented endpoint: ``stock_comment_em``.

Args:
    page: Page number, starting from 1. If omitted, the server default is used unless ``limit`` or ``all_pages`` is set.
    page_size: Rows per page. The SDK validates this against the endpoint-specific maximum.
    limit: Maximum number of rows to return. The SDK may fetch multiple pages to satisfy this limit.
    all_pages: Fetch and combine pages until the server reports the last page.
    max_pages: Optional safety cap for ``all_pages``.
    raw: Return the decoded JSON payload without tabular extraction.
    fields: Optional field list or comma-separated field string applied after extraction.
    as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
    **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

Returns:
    A pandas ``DataFrame`` by default, Python rows when
    ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
    payloads when multi-page fetching is used with ``raw=True``.
```

<h4 id="api-stock-comment-focus-em"><code>stock_comment_focus_em</code></h4>

- 接口名称：千股千评关注度
- HTTP：`GET`
- Path：`api/v1/market/data/stock-comment/focus`
- 参数：`symbol`
- 来源文档：`千股千评关注度.md`
- 原始接口：`stock_comment_focus_em`

```text
千股千评关注度.

Endpoint: ``api/v1/market/data/stock-comment/focus``.
Method: ``GET``.
Documented endpoint: ``stock_comment_focus_em``.

Args:
    symbol: 证券代码（纯数字，如 600000） (type: string; required: Y).
    raw: Return the decoded JSON payload without tabular extraction.
    fields: Optional field list or comma-separated field string applied after extraction.
    as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
    **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

Returns:
    A pandas ``DataFrame`` by default, Python rows when
    ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
    payloads when multi-page fetching is used with ``raw=True``.
```

<h4 id="api-stock-comment-org-participate-em"><code>stock_comment_org_participate_em</code></h4>

- 接口名称：机构参与度
- HTTP：`GET`
- Path：`api/v1/market/data/stock-comment/org-participate`
- 参数：`symbol`
- 来源文档：`机构参与度.md`
- 原始接口：`stock_comment_org_participate_em`

```text
机构参与度.

Endpoint: ``api/v1/market/data/stock-comment/org-participate``.
Method: ``GET``.
Documented endpoint: ``stock_comment_org_participate_em``.

Args:
    symbol: 证券代码（纯数字，如 600000） (type: string; required: Y).
    raw: Return the decoded JSON payload without tabular extraction.
    fields: Optional field list or comma-separated field string applied after extraction.
    as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
    **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

Returns:
    A pandas ``DataFrame`` by default, Python rows when
    ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
    payloads when multi-page fetching is used with ``raw=True``.
```

<h4 id="api-stock-comment-score-em"><code>stock_comment_score_em</code></h4>

- 接口名称：千股千评评分
- HTTP：`GET`
- Path：`api/v1/market/data/stock-comment/score`
- 参数：`symbol`
- 来源文档：`千股千评评分.md`
- 原始接口：`stock_comment_score_em`

```text
千股千评评分.

Endpoint: ``api/v1/market/data/stock-comment/score``.
Method: ``GET``.
Documented endpoint: ``stock_comment_score_em``.

Args:
    symbol: 证券代码（纯数字，如 600000） (type: string; required: Y).
    raw: Return the decoded JSON payload without tabular extraction.
    fields: Optional field list or comma-separated field string applied after extraction.
    as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
    **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

Returns:
    A pandas ``DataFrame`` by default, Python rows when
    ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
    payloads when multi-page fetching is used with ``raw=True``.
```

<h4 id="api-stock-filter"><code>stock_filter</code></h4>

- 接口名称：股票筛选
- HTTP：`GET`
- Path：`api/v1/market/data/stock-list/filter`
- 参数：`board`, `listing_date_since`, `page`, `page_size`
- 来源文档：`股票筛选.md`
- 原始接口：`stock_filter`

```text
股票筛选.

Endpoint: ``api/v1/market/data/stock-list/filter``.
Method: ``GET``.
Documented endpoint: ``stock_filter``.

Args:
    board: 板块/交易所筛选：`star` / `chi_next` / `bjse` / `xshg` / `xshe` / `main` (type: string; required: N).
    listing_date_since: 上市日期起点 YYYYMMDD，筛选此后上市的股票 (type: string; required: N).
    page: Page number, starting from 1. If omitted, the server default is used unless ``limit`` or ``all_pages`` is set.
    page_size: Rows per page. The SDK validates this against the endpoint-specific maximum.
    limit: Maximum number of rows to return. The SDK may fetch multiple pages to satisfy this limit.
    all_pages: Fetch and combine pages until the server reports the last page.
    max_pages: Optional safety cap for ``all_pages``.
    raw: Return the decoded JSON payload without tabular extraction.
    fields: Optional field list or comma-separated field string applied after extraction.
    as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
    **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

Returns:
    A pandas ``DataFrame`` by default, Python rows when
    ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
    payloads when multi-page fetching is used with ``raw=True``.
```

<h4 id="api-stock-float-holders"><code>stock_float_holders</code></h4>

- 接口名称：十大流通股东
- HTTP：`GET`
- Path：`api/v1/market/data/holder/stock-holder-ften`
- 参数：`stock_code`, `is_last`, `page`, `page_size`
- 来源文档：`十大流通股东.md`
- 原始接口：`stock_float_holders`

```text
十大流通股东.

Endpoint: ``api/v1/market/data/holder/stock-holder-ften``.
Method: ``GET``.
Documented endpoint: ``stock_float_holders``.

Args:
    stock_code: 标的代码，指定时返回该标的全部历史数据 (type: string; required: N).
    is_last: 是否取所有标的最新一期，true 时按 page/page_size 分页 (type: bool; required: N).
    page: Page number, starting from 1. If omitted, the server default is used unless ``limit`` or ``all_pages`` is set.
    page_size: Rows per page. The SDK validates this against the endpoint-specific maximum.
    limit: Maximum number of rows to return. The SDK may fetch multiple pages to satisfy this limit.
    all_pages: Fetch and combine pages until the server reports the last page.
    max_pages: Optional safety cap for ``all_pages``.
    raw: Return the decoded JSON payload without tabular extraction.
    fields: Optional field list or comma-separated field string applied after extraction.
    as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
    **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

Returns:
    A pandas ``DataFrame`` by default, Python rows when
    ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
    payloads when multi-page fetching is used with ``raw=True``.
```

<h4 id="api-stock-ggcg-em"><code>stock_ggcg_em</code></h4>

- 接口名称：东方财富股东增减持
- HTTP：`GET`
- Path：`api/v1/market/data/holder/stock-ggcg-em`
- 参数：`symbol`, `page`, `page_size`
- 来源文档：`东方财富股东增减持.md`
- 原始接口：`stock_ggcg_em_handler`

```text
东方财富股东增减持.

Endpoint: ``api/v1/market/data/holder/stock-ggcg-em``.
Method: ``GET``.
Documented endpoint: ``stock_ggcg_em_handler``.

Args:
    symbol: 数据类型：全部 / 股东增持 / 股东减持，默认全部 (type: string; required: N).
    page: Page number, starting from 1. If omitted, the server default is used unless ``limit`` or ``all_pages`` is set.
    page_size: Rows per page. The SDK validates this against the endpoint-specific maximum.
    limit: Maximum number of rows to return. The SDK may fetch multiple pages to satisfy this limit.
    all_pages: Fetch and combine pages until the server reports the last page.
    max_pages: Optional safety cap for ``all_pages``.
    raw: Return the decoded JSON payload without tabular extraction.
    fields: Optional field list or comma-separated field string applied after extraction.
    as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
    **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

Returns:
    A pandas ``DataFrame`` by default, Python rows when
    ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
    payloads when multi-page fetching is used with ``raw=True``.
```

<h4 id="api-stock-ggmx"><code>stock_ggmx</code></h4>

- 接口名称：董监高持股变动
- HTTP：`GET`
- Path：`api/v1/market/data/holder/stock-ggmx`
- 参数：`stock_code`, `change_direction`, `start_date`, `end_date`, `page`, `page_size`
- 来源文档：`董监高持股变动.md`
- 原始接口：`stock_ggmx_handler`

```text
董监高持股变动.

Endpoint: ``api/v1/market/data/holder/stock-ggmx``.
Method: ``GET``.
Documented endpoint: ``stock_ggmx_handler``.

Args:
    stock_code: 股票代码（如 600001），别名 stockCode (type: string; required: N).
    change_direction: 变动方向：增持 / 减持，别名 changeDirection (type: string; required: N).
    start_date: 变动日期起始 YYYY-MM-DD，别名 startDate (type: string; required: N).
    end_date: 变动日期截止 YYYY-MM-DD，别名 endDate (type: string; required: N).
    page: Page number, starting from 1. If omitted, the server default is used unless ``limit`` or ``all_pages`` is set.
    page_size: Rows per page. The SDK validates this against the endpoint-specific maximum.
    limit: Maximum number of rows to return. The SDK may fetch multiple pages to satisfy this limit.
    all_pages: Fetch and combine pages until the server reports the last page.
    max_pages: Optional safety cap for ``all_pages``.
    raw: Return the decoded JSON payload without tabular extraction.
    fields: Optional field list or comma-separated field string applied after extraction.
    as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
    **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

Returns:
    A pandas ``DataFrame`` by default, Python rows when
    ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
    payloads when multi-page fetching is used with ``raw=True``.
```

<h4 id="api-stock-ggmx-buy-ranking"><code>stock_ggmx_buy_ranking</code></h4>

- 接口名称：董监高增持排名
- HTTP：`GET`
- Path：`api/v1/market/data/holder/stock-ggmx-buy-ranking`
- 参数：`time_range`, `page`, `page_size`
- 来源文档：`董监高增持排名.md`
- 原始接口：`stock_ggmx_buy_ranking_handler`

```text
董监高增持排名.

Endpoint: ``api/v1/market/data/holder/stock-ggmx-buy-ranking``.
Method: ``GET``.
Documented endpoint: ``stock_ggmx_buy_ranking_handler``.

Args:
    time_range: 时间范围：1m / 3m / 6m / 1y / 2y，默认 1m，别名 timeRange (type: string; required: N).
    page: Page number, starting from 1. If omitted, the server default is used unless ``limit`` or ``all_pages`` is set.
    page_size: Rows per page. The SDK validates this against the endpoint-specific maximum.
    limit: Maximum number of rows to return. The SDK may fetch multiple pages to satisfy this limit.
    all_pages: Fetch and combine pages until the server reports the last page.
    max_pages: Optional safety cap for ``all_pages``.
    raw: Return the decoded JSON payload without tabular extraction.
    fields: Optional field list or comma-separated field string applied after extraction.
    as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
    **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

Returns:
    A pandas ``DataFrame`` by default, Python rows when
    ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
    payloads when multi-page fetching is used with ``raw=True``.
```

<h4 id="api-stock-ggmx-sell-ranking"><code>stock_ggmx_sell_ranking</code></h4>

- 接口名称：董监高减持排名
- HTTP：`GET`
- Path：`api/v1/market/data/holder/stock-ggmx-sell-ranking`
- 参数：`time_range`, `page`, `page_size`
- 来源文档：`董监高减持排名.md`
- 原始接口：`stock_ggmx_sell_ranking_handler`

```text
董监高减持排名.

Endpoint: ``api/v1/market/data/holder/stock-ggmx-sell-ranking``.
Method: ``GET``.
Documented endpoint: ``stock_ggmx_sell_ranking_handler``.

Args:
    time_range: 时间范围：1m / 3m / 6m / 1y / 2y，默认 1m，别名 timeRange (type: string; required: N).
    page: Page number, starting from 1. If omitted, the server default is used unless ``limit`` or ``all_pages`` is set.
    page_size: Rows per page. The SDK validates this against the endpoint-specific maximum.
    limit: Maximum number of rows to return. The SDK may fetch multiple pages to satisfy this limit.
    all_pages: Fetch and combine pages until the server reports the last page.
    max_pages: Optional safety cap for ``all_pages``.
    raw: Return the decoded JSON payload without tabular extraction.
    fields: Optional field list or comma-separated field string applied after extraction.
    as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
    **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

Returns:
    A pandas ``DataFrame`` by default, Python rows when
    ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
    payloads when multi-page fetching is used with ``raw=True``.
```

<h4 id="api-stock-holders"><code>stock_holders</code></h4>

- 接口名称：十大股东
- HTTP：`GET`
- Path：`api/v1/market/data/holder/stock-holder-ten`
- 参数：`stock_code`, `is_last`, `page`, `page_size`
- 来源文档：`十大股东.md`
- 原始接口：`stock_holders`

```text
十大股东.

Endpoint: ``api/v1/market/data/holder/stock-holder-ten``.
Method: ``GET``.
Documented endpoint: ``stock_holders``.

Args:
    stock_code: 标的代码，指定时返回该标的全部历史数据 (type: string; required: N).
    is_last: 是否取所有标的最新一期，true 时按 page/page_size 分页 (type: bool; required: N).
    page: Page number, starting from 1. If omitted, the server default is used unless ``limit`` or ``all_pages`` is set.
    page_size: Rows per page. The SDK validates this against the endpoint-specific maximum.
    limit: Maximum number of rows to return. The SDK may fetch multiple pages to satisfy this limit.
    all_pages: Fetch and combine pages until the server reports the last page.
    max_pages: Optional safety cap for ``all_pages``.
    raw: Return the decoded JSON payload without tabular extraction.
    fields: Optional field list or comma-separated field string applied after extraction.
    as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
    **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

Returns:
    A pandas ``DataFrame`` by default, Python rows when
    ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
    payloads when multi-page fetching is used with ``raw=True``.
```

<h4 id="api-stock-holders-number"><code>stock_holders_number</code></h4>

- 接口名称：股东人数
- HTTP：`GET`
- Path：`api/v1/market/data/holder/stock-holder-nums`
- 参数：`stock_code`, `is_last`, `page`, `page_size`
- 来源文档：`股东人数.md`
- 原始接口：`stock_holders_number`

```text
股东人数.

Endpoint: ``api/v1/market/data/holder/stock-holder-nums``.
Method: ``GET``.
Documented endpoint: ``stock_holders_number``.

Args:
    stock_code: 标的代码，指定时返回该标的全部历史数据 (type: string; required: N).
    is_last: 是否取所有标的最新一期，true 时按 page/page_size 分页 (type: bool; required: N).
    page: Page number, starting from 1. If omitted, the server default is used unless ``limit`` or ``all_pages`` is set.
    page_size: Rows per page. The SDK validates this against the endpoint-specific maximum.
    limit: Maximum number of rows to return. The SDK may fetch multiple pages to satisfy this limit.
    all_pages: Fetch and combine pages until the server reports the last page.
    max_pages: Optional safety cap for ``all_pages``.
    raw: Return the decoded JSON payload without tabular extraction.
    fields: Optional field list or comma-separated field string applied after extraction.
    as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
    **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

Returns:
    A pandas ``DataFrame`` by default, Python rows when
    ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
    payloads when multi-page fetching is used with ``raw=True``.
```

<h4 id="api-stock-institution-holdings"><code>stock_institution_holdings</code></h4>

- 接口名称：机构持股
- HTTP：`GET`
- Path：`api/v1/market/data/share/stock-institution-holdings`
- 参数：`year`, `report_type`, `inst_type`, `page`, `page_size`
- 来源文档：`机构持股.md`
- 原始接口：`get_stock_institution_holdings`

```text
机构持股.

Endpoint: ``api/v1/market/data/share/stock-institution-holdings``.
Method: ``GET``.
Documented endpoint: ``get_stock_institution_holdings``.

Args:
    year: 年份 (type: int; required: Y).
    report_type: 报告类型：q1 / q2 / q3 / annual / announcement (type: ReportType; required: Y).
    inst_type: 机构类型：all_inst / fund / qfii / insurance / social_security / securities / trust / other (type: InstitutionType; required: Y).
    page: Page number, starting from 1. If omitted, the server default is used unless ``limit`` or ``all_pages`` is set.
    page_size: Rows per page. The SDK validates this against the endpoint-specific maximum.
    limit: Maximum number of rows to return. The SDK may fetch multiple pages to satisfy this limit.
    all_pages: Fetch and combine pages until the server reports the last page.
    max_pages: Optional safety cap for ``all_pages``.
    raw: Return the decoded JSON payload without tabular extraction.
    fields: Optional field list or comma-separated field string applied after extraction.
    as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
    **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

Returns:
    A pandas ``DataFrame`` by default, Python rows when
    ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
    payloads when multi-page fetching is used with ``raw=True``.
```

<h4 id="api-stock-institution-holdings-detail"><code>stock_institution_holdings_detail</code></h4>

- 接口名称：机构持股明细
- HTTP：`GET`
- Path：`api/v1/market/data/share/stock-institution-holdings-detail`
- 参数：`stock_code`, `year`, `report_type`, `inst_type`, `page`, `page_size`
- 来源文档：`机构持股明细.md`
- 原始接口：`get_stock_institution_holdings_detail`

```text
机构持股明细.

Endpoint: ``api/v1/market/data/share/stock-institution-holdings-detail``.
Method: ``GET``.
Documented endpoint: ``get_stock_institution_holdings_detail``.

Args:
    stock_code: 股票代码 (type: string; required: Y).
    year: 年份 (type: int; required: Y).
    report_type: 报告类型：q1 / q2 / q3 / annual / announcement (type: ReportType; required: Y).
    inst_type: 机构类型：all_inst / fund / qfii / insurance / social_security / securities / trust / other (type: InstitutionType; required: Y).
    page: Page number, starting from 1. If omitted, the server default is used unless ``limit`` or ``all_pages`` is set.
    page_size: Rows per page. The SDK validates this against the endpoint-specific maximum.
    limit: Maximum number of rows to return. The SDK may fetch multiple pages to satisfy this limit.
    all_pages: Fetch and combine pages until the server reports the last page.
    max_pages: Optional safety cap for ``all_pages``.
    raw: Return the decoded JSON payload without tabular extraction.
    fields: Optional field list or comma-separated field string applied after extraction.
    as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
    **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

Returns:
    A pandas ``DataFrame`` by default, Python rows when
    ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
    payloads when multi-page fetching is used with ``raw=True``.
```

<h4 id="api-stock-institution-share-holdings"><code>stock_institution_share_holdings</code></h4>

- 接口名称：机构股本持股
- HTTP：`GET`
- Path：`api/v1/market/data/institution/institution-share-holdings`
- 参数：`institution_id`, `year`, `report_type`, `invest_type`
- 来源文档：`机构股本持股.md`
- 原始接口：`get_stock_institution_share_holdings`

```text
机构股本持股.

Endpoint: ``api/v1/market/data/institution/institution-share-holdings``.
Method: ``GET``.
Documented endpoint: ``get_stock_institution_share_holdings``.

Args:
    institution_id: 机构 ID (type: string; required: Y).
    year: 年份 (type: int; required: Y).
    report_type: 报告类型：q1 / q2 / q3 / annual / announcement (type: ReportType; required: Y).
    invest_type: 持仓类型：all / stock / fund / bond / other (type: InvestType; required: Y).
    raw: Return the decoded JSON payload without tabular extraction.
    fields: Optional field list or comma-separated field string applied after extraction.
    as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
    **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

Returns:
    A pandas ``DataFrame`` by default, Python rows when
    ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
    payloads when multi-page fetching is used with ``raw=True``.
```

<h4 id="api-stock-intraday-auction-volume"><code>stock_intraday_auction_volume</code></h4>

- 接口名称：集合竞价成交量
- HTTP：`GET`
- Path：`api/v1/market/data/intraday-auction-volume`
- 参数：`trade_date`, `page`, `page_size`
- 来源文档：`集合竞价成交量.md`
- 原始接口：`stock_intraday_auction_volume`

```text
集合竞价成交量.

Endpoint: ``api/v1/market/data/intraday-auction-volume``.
Method: ``GET``.
Documented endpoint: ``stock_intraday_auction_volume``.

Args:
    trade_date: 交易日期 YYYYMMDD；不传返回当日实时数据 (type: string; required: N).
    page: Page number, starting from 1. If omitted, the server default is used unless ``limit`` or ``all_pages`` is set.
    page_size: Rows per page. The SDK validates this against the endpoint-specific maximum.
    limit: Maximum number of rows to return. The SDK may fetch multiple pages to satisfy this limit.
    all_pages: Fetch and combine pages until the server reports the last page.
    max_pages: Optional safety cap for ``all_pages``.
    raw: Return the decoded JSON payload without tabular extraction.
    fields: Optional field list or comma-separated field string applied after extraction.
    as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
    **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

Returns:
    A pandas ``DataFrame`` by default, Python rows when
    ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
    payloads when multi-page fetching is used with ``raw=True``.
```

<h4 id="api-stock-intraday-auction-volume-symbol"><code>stock_intraday_auction_volume_symbol</code></h4>

- 接口名称：单标的集合竞价成交量
- HTTP：`GET`
- Path：`api/v1/market/data/intraday-auction-volume/symbol`
- 参数：`symbol`, `trade_date`, `page`, `page_size`
- 来源文档：`单标的集合竞价成交量.md`
- 原始接口：`stock_intraday_auction_volume_symbol`

```text
单标的集合竞价成交量.

Endpoint: ``api/v1/market/data/intraday-auction-volume/symbol``.
Method: ``GET``.
Documented endpoint: ``stock_intraday_auction_volume_symbol``.

Args:
    symbol: 标的代码，格式 code.suffix（XSHG/SH、XSHE/SZ、BJSE/BJ） (type: string; required: Y).
    trade_date: 交易日期 YYYYMMDD；不传返回当日实时数据 (type: string; required: N).
    page: Page number, starting from 1. If omitted, the server default is used unless ``limit`` or ``all_pages`` is set.
    page_size: Rows per page. The SDK validates this against the endpoint-specific maximum.
    limit: Maximum number of rows to return. The SDK may fetch multiple pages to satisfy this limit.
    all_pages: Fetch and combine pages until the server reports the last page.
    max_pages: Optional safety cap for ``all_pages``.
    raw: Return the decoded JSON payload without tabular extraction.
    fields: Optional field list or comma-separated field string applied after extraction.
    as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
    **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

Returns:
    A pandas ``DataFrame`` by default, Python rows when
    ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
    payloads when multi-page fetching is used with ``raw=True``.
```

<h4 id="api-stock-ipos"><code>stock_ipos</code></h4>

- 接口名称：股票IPO
- HTTP：`GET`
- Path：`api/v1/market/data/stock-ipos`
- 参数：`page`, `page_size`
- 来源文档：`股票IPO.md`
- 原始接口：`stock_ipos`

```text
股票IPO.

Endpoint: ``api/v1/market/data/stock-ipos``.
Method: ``GET``.
Documented endpoint: ``stock_ipos``.

Args:
    page: Page number, starting from 1. If omitted, the server default is used unless ``limit`` or ``all_pages`` is set.
    page_size: Rows per page. The SDK validates this against the endpoint-specific maximum.
    limit: Maximum number of rows to return. The SDK may fetch multiple pages to satisfy this limit.
    all_pages: Fetch and combine pages until the server reports the last page.
    max_pages: Optional safety cap for ``all_pages``.
    raw: Return the decoded JSON payload without tabular extraction.
    fields: Optional field list or comma-separated field string applied after extraction.
    as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
    **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

Returns:
    A pandas ``DataFrame`` by default, Python rows when
    ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
    payloads when multi-page fetching is used with ``raw=True``.
```

<h4 id="api-stock-list"><code>stock_list</code></h4>

- 接口名称：股票列表
- HTTP：`GET`
- Path：`api/v1/market/data/stock-list`
- 参数：-
- 来源文档：`股票列表.md`
- 原始接口：`get_stock_list`

```text
股票列表.

Endpoint: ``api/v1/market/data/stock-list``.
Method: ``GET``.
Documented endpoint: ``get_stock_list``.

Args:
    raw: Return the decoded JSON payload without tabular extraction.
    fields: Optional field list or comma-separated field string applied after extraction.
    as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
    **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

Returns:
    A pandas ``DataFrame`` by default, Python rows when
    ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
    payloads when multi-page fetching is used with ``raw=True``.
```

<h4 id="api-stock-market"><code>stock_market</code></h4>

- 接口名称：市场行情快照
- HTTP：`GET`
- Path：`api/v1/market/data/daec/market/snapshot`
- 参数：`scope`
- 来源文档：`市场行情快照.md`
- 原始接口：`stock_market`

```text
股票市场行情.

Endpoint: ``api/v1/market/data/daec/market/snapshot``.
Method: ``GET``.
Documented endpoint: ``stock_market``.

Args:
    scope: 市场范围：ChinaStock(默认) / Xshg / Xshe / Bjse (type: string; required: N).
    raw: Return the decoded JSON payload without tabular extraction.
    fields: Optional field list or comma-separated field string applied after extraction.
    as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
    **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

Returns:
    A pandas ``DataFrame`` by default, Python rows when
    ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
    payloads when multi-page fetching is used with ``raw=True``.
```

<h4 id="api-stock-market-distribution-intraday"><code>stock_market_distribution_intraday</code></h4>

- 接口名称：日内涨跌停分布历史
- HTTP：`GET`
- Path：`api/v1/market/data/daec/market/distribution-history`
- 参数：`scope`
- 来源文档：`日内涨跌停分布历史.md`
- 原始接口：`stock_market_distribution_intraday`

```text
市场涨跌分布分时.

Endpoint: ``api/v1/market/data/daec/market/distribution-history``.
Method: ``GET``.
Documented endpoint: ``stock_market_distribution_intraday``.

Args:
    scope: 市场范围：ChinaStock(默认) / Xshg / Xshe / Bjse (type: string; required: N).
    raw: Return the decoded JSON payload without tabular extraction.
    fields: Optional field list or comma-separated field string applied after extraction.
    as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
    **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

Returns:
    A pandas ``DataFrame`` by default, Python rows when
    ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
    payloads when multi-page fetching is used with ``raw=True``.
```

<h4 id="api-stock-daec-stocks"><code>stock_daec_stocks</code></h4>

- 接口名称：A股行情列表
- HTTP：`GET`
- Path：`api/v1/market/data/daec/stocks/{board}`
- 参数：`board`, `page`, `page_size`, `filter`, `order_by`
- 来源文档：`A股行情列表.md`
- 原始接口：`stock_daec_stocks`

```text
A股行情列表（DAEC 全字段族）.

Endpoint: ``api/v1/market/data/daec/stocks/{board}``.
Method: ``GET``.
Documented endpoint: ``stock_daec_stocks``.

Args:
    board: 板块路径参数，如 all / xshg / xshe / bjse (type: string; required: Y).
    page: Page number, starting from 1. If omitted, the server default is used unless ``limit`` or ``all_pages`` is set.
    page_size: Rows per page. The SDK validates this against the endpoint-specific maximum.
    limit: Maximum number of rows to return. The SDK may fetch multiple pages to satisfy this limit.
    all_pages: Fetch and combine pages until the server reports the last page.
    max_pages: Optional safety cap for ``all_pages``.
    filter: 筛选表达式，如 ``close > 10`` 或 ``name.contains("银行")`` (type: string; required: N).
    order_by: 排序表达式，如 ``change_rate desc`` (type: string; required: N).
    raw: Return the decoded JSON payload without tabular extraction.
    fields: Optional field list or comma-separated field string applied after extraction.
    as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
    **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

Returns:
    A pandas ``DataFrame`` by default, Python rows when
    ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
    payloads when multi-page fetching is used with ``raw=True``.
```

<h4 id="api-stock-realtime-list"><code>stock_realtime_list</code></h4>

- 接口名称：A股行情列表
- HTTP：`GET`
- Path：`api/v1/market/data/stock-list/{board}`
- 参数：`board`, `page`, `page_size`
- 来源文档：`A股行情列表.md`
- 原始接口：`stock_realtime_list`

```text
A股行情列表（stock-list 实时行情族）.

Endpoint: ``api/v1/market/data/stock-list/{board}``.
Method: ``GET``.
Documented endpoint: ``stock_realtime_list``.

Args:
    board: 板块路径参数，如 chi-next / star / new (type: string; required: Y).
    page: Page number, starting from 1. If omitted, the server default is used unless ``limit`` or ``all_pages`` is set.
    page_size: Rows per page. The SDK validates this against the endpoint-specific maximum.
    limit: Maximum number of rows to return. The SDK may fetch multiple pages to satisfy this limit.
    all_pages: Fetch and combine pages until the server reports the last page.
    max_pages: Optional safety cap for ``all_pages``.
    raw: Return the decoded JSON payload without tabular extraction.
    fields: Optional field list or comma-separated field string applied after extraction.
    as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
    **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

Returns:
    A pandas ``DataFrame`` by default, Python rows when
    ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
    payloads when multi-page fetching is used with ``raw=True``.
```

<h4 id="api-stock-pledge-detail"><code>stock_pledge_detail</code></h4>

- 接口名称：股权质押明细
- HTTP：`GET`
- Path：`api/v1/market/data/pledge/pledge-detail`
- 参数：`stock_code`, `is_last`, `page`, `page_size`
- 来源文档：`股权质押明细.md`
- 原始接口：`stock_pledge_detail`

```text
股权质押明细.

Endpoint: ``api/v1/market/data/pledge/pledge-detail``.
Method: ``GET``.
Documented endpoint: ``stock_pledge_detail``.

Args:
    stock_code: 股票代码（symbol.suffix 格式或纯代码）；不传时需配合 `is_last=true` (type: string; required: N).
    is_last: 是否仅获取最新一期（无 `stock_code` 时必填为 true） (type: bool; required: N).
    page: Page number, starting from 1. If omitted, the server default is used unless ``limit`` or ``all_pages`` is set.
    page_size: Rows per page. The SDK validates this against the endpoint-specific maximum.
    limit: Maximum number of rows to return. The SDK may fetch multiple pages to satisfy this limit.
    all_pages: Fetch and combine pages until the server reports the last page.
    max_pages: Optional safety cap for ``all_pages``.
    raw: Return the decoded JSON payload without tabular extraction.
    fields: Optional field list or comma-separated field string applied after extraction.
    as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
    **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

Returns:
    A pandas ``DataFrame`` by default, Python rows when
    ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
    payloads when multi-page fetching is used with ``raw=True``.
```

<h4 id="api-stock-pledge-summary"><code>stock_pledge_summary</code></h4>

- 接口名称：股权质押汇总
- HTTP：`GET`
- Path：`api/v1/market/data/pledge/pledge-summary`
- 参数：`page`, `page_size`
- 来源文档：`股权质押汇总.md`
- 原始接口：`stock_pledge_summary`

```text
股权质押汇总.

Endpoint: ``api/v1/market/data/pledge/pledge-summary``.
Method: ``GET``.
Documented endpoint: ``stock_pledge_summary``.

Args:
    page: Page number, starting from 1. If omitted, the server default is used unless ``limit`` or ``all_pages`` is set.
    page_size: Rows per page. The SDK validates this against the endpoint-specific maximum.
    limit: Maximum number of rows to return. The SDK may fetch multiple pages to satisfy this limit.
    all_pages: Fetch and combine pages until the server reports the last page.
    max_pages: Optional safety cap for ``all_pages``.
    raw: Return the decoded JSON payload without tabular extraction.
    fields: Optional field list or comma-separated field string applied after extraction.
    as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
    **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

Returns:
    A pandas ``DataFrame`` by default, Python rows when
    ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
    payloads when multi-page fetching is used with ``raw=True``.
```

<h4 id="api-stock-prev-close"><code>stock_prev_close</code></h4>

- 接口名称：标的昨收价
- HTTP：`GET`
- Path：`api/v1/market/data/daec/history/prev-closes`
- 参数：`symbol`, `since`, `until`
- 来源文档：`标的昨收价.md`
- 原始接口：`stock_prev_close`

```text
股票前收盘价.

Endpoint: ``api/v1/market/data/daec/history/prev-closes``.
Method: ``GET``.
Documented endpoint: ``stock_prev_close``.

Args:
    symbol: 标的代码 (type: SymbolKey; required: Y).
    since: 开始日期，格式 YYYYMMDD (type: date; required: Y).
    until: 结束日期，格式 YYYYMMDD (type: date; required: Y).
    raw: Return the decoded JSON payload without tabular extraction.
    fields: Optional field list or comma-separated field string applied after extraction.
    as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
    **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

Returns:
    A pandas ``DataFrame`` by default, Python rows when
    ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
    payloads when multi-page fetching is used with ``raw=True``.
```

<h4 id="api-stock-intraday-prices"><code>stock_intraday_prices</code></h4>

- 接口名称：标的分时数据
- HTTP：`GET`
- Path：`api/v1/market/data/daec/history/prices`
- 参数：`symbol`, `range`, `days`, `ts_ms`
- 来源文档：`标得分时数据.md`
- 原始接口：`stock_intraday_prices`

```text
标的分时数据.

Endpoint: ``api/v1/market/data/daec/history/prices``.
Method: ``GET``.
Documented endpoint: ``stock_intraday_prices``.

Args:
    symbol: 标的代码，如 600000.XSHG (type: string; required: Y).
    range: 预置时间区间：Today / FiveDays (type: string; required: N).
    days: 近 N 个交易日至今 (type: uint32; required: N).
    ts_ms: 起始毫秒时间戳 (type: int64; required: N).
    raw: Return the decoded JSON payload without tabular extraction.
    fields: Optional field list or comma-separated field string applied after extraction.
    as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
    **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

Returns:
    A pandas ``DataFrame`` by default, Python rows when
    ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
    payloads when multi-page fetching is used with ``raw=True``.
```

<h4 id="api-stock-rating-top5"><code>stock_rating_top5</code></h4>

- 接口名称：飞兔股票评级Top5
- HTTP：`GET`
- Path：`api/v1/market/data/feitu/stock-rating-top5`
- 参数：`date`, `variant`, `type`
- 来源文档：`飞兔股票评级Top5.md`
- 原始接口：`stock_rating_top5`

```text
飞兔股票评级Top5.

Endpoint: ``api/v1/market/data/feitu/stock-rating-top5``.
Method: ``GET``.
Documented endpoint: ``stock_rating_top5``.

Args:
    date: 日期 YYYYMMDD (type: string; required: Y).
    variant: 档位，如 300001（30w01）、300000（30w），默认 300001 (type: string; required: N).
    type: 市场：all / xshg / xshe / bjse，默认 all (type: StockRatingMarketFilter; required: N).
    raw: Return the decoded JSON payload without tabular extraction.
    fields: Optional field list or comma-separated field string applied after extraction.
    as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
    **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

Returns:
    A pandas ``DataFrame`` by default, Python rows when
    ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
    payloads when multi-page fetching is used with ``raw=True``.
```

<h4 id="api-stock-share"><code>stock_share</code></h4>

- 接口名称：股本
- HTTP：`GET`
- Path：`api/v1/market/data/share/get-stock-share`
- 参数：`stock_code`, `date`
- 来源文档：`股本.md`
- 原始接口：`get_stock_share_handler`

```text
股本.

Endpoint: ``api/v1/market/data/share/get-stock-share``.
Method: ``GET``.
Documented endpoint: ``get_stock_share_handler``.

Args:
    stock_code: 股票代码 (type: string; required: Y).
    date: 日期 YYYYMMDD (type: string; required: Y).
    raw: Return the decoded JSON payload without tabular extraction.
    fields: Optional field list or comma-separated field string applied after extraction.
    as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
    **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

Returns:
    A pandas ``DataFrame`` by default, Python rows when
    ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
    payloads when multi-page fetching is used with ``raw=True``.
```

<h4 id="api-stock-share-chg"><code>stock_share_chg</code></h4>

- 接口名称：股东增减持
- HTTP：`GET`
- Path：`api/v1/market/data/holder/stock-share-chg`
- 参数：`stock_code`, `is_last`, `page`, `page_size`
- 来源文档：`股东增减持.md`
- 原始接口：`stock_share_chg`

```text
股东增减持.

Endpoint: ``api/v1/market/data/holder/stock-share-chg``.
Method: ``GET``.
Documented endpoint: ``stock_share_chg``.

Args:
    stock_code: 标的代码，指定时返回该标的分页历史数据 (type: string; required: N).
    is_last: 是否取所有标的最新一期，true 时按 page/page_size 分页 (type: bool; required: N).
    page: Page number, starting from 1. If omitted, the server default is used unless ``limit`` or ``all_pages`` is set.
    page_size: Rows per page. The SDK validates this against the endpoint-specific maximum.
    limit: Maximum number of rows to return. The SDK may fetch multiple pages to satisfy this limit.
    all_pages: Fetch and combine pages until the server reports the last page.
    max_pages: Optional safety cap for ``all_pages``.
    raw: Return the decoded JSON payload without tabular extraction.
    fields: Optional field list or comma-separated field string applied after extraction.
    as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
    **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

Returns:
    A pandas ``DataFrame`` by default, Python rows when
    ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
    payloads when multi-page fetching is used with ``raw=True``.
```

<h4 id="api-stock-signal-latest-snapshot"><code>stock_signal_latest_snapshot</code></h4>

- 接口名称：信号最新快照
- HTTP：`GET`
- Path：`api/v1/market/data/stock-signal-latest-snapshot`
- 参数：`signal_type`, `page`, `page_size`
- 来源文档：`信号最新快照.md`
- 原始接口：`stock_signal_latest_snapshot`

```text
信号最新快照.

Endpoint: ``api/v1/market/data/stock-signal-latest-snapshot``.
Method: ``GET``.
Documented endpoint: ``stock_signal_latest_snapshot``.

Args:
    signal_type: 信号类型过滤，不传返回全部。可选值：`new_high_month`、`new_high_60d`、`new_high_120d`、`new_high_250d`、`new_low_month`、`new_low_60d`、`new_low_120d`、`new_low_250d`、`consecutive_up`、`consecutive_down`、`consecutive_vol_up`、`consecutive_vol_down`、`break_up_ma5`、`break_up_ma10`、`break_up_ma20`、`break_down_ma5`、`break_down_ma10`、`break_down_ma20`、`vol_price_rise`、`vol_price_fall` (type: string; required: N).
    page: Page number, starting from 1. If omitted, the server default is used unless ``limit`` or ``all_pages`` is set.
    page_size: Rows per page. The SDK validates this against the endpoint-specific maximum.
    limit: Maximum number of rows to return. The SDK may fetch multiple pages to satisfy this limit.
    all_pages: Fetch and combine pages until the server reports the last page.
    max_pages: Optional safety cap for ``all_pages``.
    raw: Return the decoded JSON payload without tabular extraction.
    fields: Optional field list or comma-separated field string applied after extraction.
    as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
    **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

Returns:
    A pandas ``DataFrame`` by default, Python rows when
    ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
    payloads when multi-page fetching is used with ``raw=True``.
```

<h4 id="api-stock-trade"><code>stock_trade</code></h4>

- 接口名称：标的逐笔成交
- HTTP：`GET`
- Path：`api/v1/market/data/daec/history/trades`
- 参数：`symbol`
- 来源文档：`标的逐笔成交.md`
- 原始接口：`stock_trade`

```text
股票分时成交.

Endpoint: ``api/v1/market/data/daec/history/trades``.
Method: ``GET``.
Documented endpoint: ``stock_trade``.

Args:
    symbol: 标的代码 (type: SymbolKey; required: Y).
    raw: Return the decoded JSON payload without tabular extraction.
    fields: Optional field list or comma-separated field string applied after extraction.
    as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
    **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

Returns:
    A pandas ``DataFrame`` by default, Python rows when
    ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
    payloads when multi-page fetching is used with ``raw=True``.
```

<h4 id="api-stock-unlock"><code>stock_unlock</code></h4>

- 接口名称：限售解禁
- HTTP：`GET`
- Path：`api/v1/market/data/unlock/stock-unlock`
- 参数：`stock_code`, `page`, `page_size`
- 来源文档：`限售解禁.md`
- 原始接口：`stock_unlock_handler`

```text
限售解禁.

Endpoint: ``api/v1/market/data/unlock/stock-unlock``.
Method: ``GET``.
Documented endpoint: ``stock_unlock_handler``.

Args:
    stock_code: 证券代码 (type: string; required: Y).
    page: Page number, starting from 1. If omitted, the server default is used unless ``limit`` or ``all_pages`` is set.
    page_size: Rows per page. The SDK validates this against the endpoint-specific maximum.
    limit: Maximum number of rows to return. The SDK may fetch multiple pages to satisfy this limit.
    all_pages: Fetch and combine pages until the server reports the last page.
    max_pages: Optional safety cap for ``all_pages``.
    raw: Return the decoded JSON payload without tabular extraction.
    fields: Optional field list or comma-separated field string applied after extraction.
    as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
    **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

Returns:
    A pandas ``DataFrame`` by default, Python rows when
    ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
    payloads when multi-page fetching is used with ``raw=True``.
```

<h4 id="api-stock-unlock-by-date"><code>stock_unlock_by_date</code></h4>

- 接口名称：限售解禁按日期
- HTTP：`GET`
- Path：`api/v1/market/data/unlock/stock-unlock-by-date`
- 参数：`start_date`, `end_date`, `page`, `page_size`
- 来源文档：`限售解禁按日期.md`
- 原始接口：`stock_unlock_by_date_handler`

```text
限售解禁按日期.

Endpoint: ``api/v1/market/data/unlock/stock-unlock-by-date``.
Method: ``GET``.
Documented endpoint: ``stock_unlock_by_date_handler``.

Args:
    start_date: 起始日期（YYYY-MM-DD） (type: string; required: Y).
    end_date: 结束日期（YYYY-MM-DD） (type: string; required: Y).
    page: Page number, starting from 1. If omitted, the server default is used unless ``limit`` or ``all_pages`` is set.
    page_size: Rows per page. The SDK validates this against the endpoint-specific maximum.
    limit: Maximum number of rows to return. The SDK may fetch multiple pages to satisfy this limit.
    all_pages: Fetch and combine pages until the server reports the last page.
    max_pages: Optional safety cap for ``all_pages``.
    raw: Return the decoded JSON payload without tabular extraction.
    fields: Optional field list or comma-separated field string applied after extraction.
    as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
    **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

Returns:
    A pandas ``DataFrame`` by default, Python rows when
    ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
    payloads when multi-page fetching is used with ``raw=True``.
```

<h4 id="api-suspension-list"><code>suspension_list</code></h4>

- 接口名称：停牌列表
- HTTP：`GET`
- Path：`api/v1/market/data/suspension-list`
- 参数：`trade_date`, `page`, `page_size`
- 来源文档：`停牌列表.md`
- 原始接口：`suspension_list`

```text
停牌列表.

Endpoint: ``api/v1/market/data/suspension-list``.
Method: ``GET``.
Documented endpoint: ``suspension_list``.

Args:
    trade_date: 交易日，格式 YYYYMMDD，默认当天 (type: string; required: N).
    page: Page number, starting from 1. If omitted, the server default is used unless ``limit`` or ``all_pages`` is set.
    page_size: Rows per page. The SDK validates this against the endpoint-specific maximum.
    limit: Maximum number of rows to return. The SDK may fetch multiple pages to satisfy this limit.
    all_pages: Fetch and combine pages until the server reports the last page.
    max_pages: Optional safety cap for ``all_pages``.
    raw: Return the decoded JSON payload without tabular extraction.
    fields: Optional field list or comma-separated field string applied after extraction.
    as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
    **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

Returns:
    A pandas ``DataFrame`` by default, Python rows when
    ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
    payloads when multi-page fetching is used with ``raw=True``.
```

<h4 id="api-sz-hk-stock-connect-members"><code>sz_hk_stock_connect_members</code></h4>

- 接口名称：深股通成份
- HTTP：`GET`
- Path：`api/v1/market/data/sz-hk-stock-connect-members`
- 参数：-
- 来源文档：`深股通成份.md`
- 原始接口：`sz_hk_stock_connect_members`

```text
深股通成份.

Endpoint: ``api/v1/market/data/sz-hk-stock-connect-members``.
Method: ``GET``.
Documented endpoint: ``sz_hk_stock_connect_members``.

Args:
    raw: Return the decoded JSON payload without tabular extraction.
    fields: Optional field list or comma-separated field string applied after extraction.
    as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
    **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

Returns:
    A pandas ``DataFrame`` by default, Python rows when
    ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
    payloads when multi-page fetching is used with ``raw=True``.
```

<h4 id="api-ths-all-board-kline"><code>ths_all_board_kline</code></h4>

- 接口名称：同花顺全板块K线
- HTTP：`GET`
- Path：`api/v1/market/data/ths-all-board-kline`
- 参数：`start_date`, `end_date`, `page`, `page_size`
- 来源文档：`同花顺全板块K线.md`
- 原始接口：`ths_all_board_kline`

```text
同花顺全板块K线.

Endpoint: ``api/v1/market/data/ths-all-board-kline``.
Method: ``GET``.
Documented endpoint: ``ths_all_board_kline``.

Args:
    start_date: 起始日期（含），YYYY-MM-DD 或 YYYYMMDD (type: string; required: N).
    end_date: 截止日期（含），YYYY-MM-DD 或 YYYYMMDD (type: string; required: N).
    page: Page number, starting from 1. If omitted, the server default is used unless ``limit`` or ``all_pages`` is set.
    page_size: Rows per page. The SDK validates this against the endpoint-specific maximum.
    limit: Maximum number of rows to return. The SDK may fetch multiple pages to satisfy this limit.
    all_pages: Fetch and combine pages until the server reports the last page.
    max_pages: Optional safety cap for ``all_pages``.
    raw: Return the decoded JSON payload without tabular extraction.
    fields: Optional field list or comma-separated field string applied after extraction.
    as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
    **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

Returns:
    A pandas ``DataFrame`` by default, Python rows when
    ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
    payloads when multi-page fetching is used with ``raw=True``.
```

<h4 id="api-ths-board-kline"><code>ths_board_kline</code></h4>

- 接口名称：同花顺板块K线
- HTTP：`GET`
- Path：`api/v1/market/data/ths-board-kline`
- 参数：`board_code`, `page`, `page_size`
- 来源文档：`同花顺板块K线.md`
- 原始接口：`ths_board_kline`

```text
同花顺板块K线.

Endpoint: ``api/v1/market/data/ths-board-kline``.
Method: ``GET``.
Documented endpoint: ``ths_board_kline``.

Args:
    board_code: 板块代码，如 886056 (type: string; required: Y).
    page: Page number, starting from 1. If omitted, the server default is used unless ``limit`` or ``all_pages`` is set.
    page_size: Rows per page. The SDK validates this against the endpoint-specific maximum.
    limit: Maximum number of rows to return. The SDK may fetch multiple pages to satisfy this limit.
    all_pages: Fetch and combine pages until the server reports the last page.
    max_pages: Optional safety cap for ``all_pages``.
    raw: Return the decoded JSON payload without tabular extraction.
    fields: Optional field list or comma-separated field string applied after extraction.
    as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
    **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

Returns:
    A pandas ``DataFrame`` by default, Python rows when
    ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
    payloads when multi-page fetching is used with ``raw=True``.
```

<h4 id="api-ths-board-list"><code>ths_board_list</code></h4>

- 接口名称：同花顺板块列表
- HTTP：`GET`
- Path：`api/v1/market/data/ths-board-list`
- 参数：-
- 来源文档：`同花顺板块列表.md`
- 原始接口：`ths_board_list`

```text
同花顺板块列表.

Endpoint: ``api/v1/market/data/ths-board-list``.
Method: ``GET``.
Documented endpoint: ``ths_board_list``.

Args:
    raw: Return the decoded JSON payload without tabular extraction.
    fields: Optional field list or comma-separated field string applied after extraction.
    as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
    **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

Returns:
    A pandas ``DataFrame`` by default, Python rows when
    ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
    payloads when multi-page fetching is used with ``raw=True``.
```

<h4 id="api-xueqiu-rank"><code>xueqiu_rank</code></h4>

- 接口名称：雪球股票排名
- HTTP：`GET`
- Path：`api/v1/market/data/xueqiu-rank`
- 参数：`rank_group`, `period`, `trade_date`, `page`, `page_size`
- 来源文档：`雪球股票排名.md`
- 原始接口：`xueqiu_rank`

```text
雪球股票排名.

Endpoint: ``api/v1/market/data/xueqiu-rank``.
Method: ``GET``.
Documented endpoint: ``xueqiu_rank``.

Args:
    rank_group: 榜单组：`follow`（关注）/ `tweet`（讨论）/ `deal`（交易） (type: string; required: N).
    period: 周期：`7d`（本周新增）/ `total`（最热门） (type: string; required: N).
    trade_date: 交易日期，格式 `YYYY-MM-DD`，不传默认取最新 (type: string; required: N).
    page: Page number, starting from 1. If omitted, the server default is used unless ``limit`` or ``all_pages`` is set.
    page_size: Rows per page. The SDK validates this against the endpoint-specific maximum.
    limit: Maximum number of rows to return. The SDK may fetch multiple pages to satisfy this limit.
    all_pages: Fetch and combine pages until the server reports the last page.
    max_pages: Optional safety cap for ``all_pages``.
    raw: Return the decoded JSON payload without tabular extraction.
    fields: Optional field list or comma-separated field string applied after extraction.
    as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
    **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

Returns:
    A pandas ``DataFrame`` by default, Python rows when
    ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
    payloads when multi-page fetching is used with ``raw=True``.
```

<h4 id="api-yzxdr-detail"><code>yzxdr_detail</code></h4>

- 接口名称：除权除息明细
- HTTP：`GET`
- Path：`api/v1/market/data/yzxdr-detail`
- 参数：`year`, `quarter`, `stock_code`, `page`, `page_size`
- 来源文档：`除权除息明细.md`
- 原始接口：`get_yzxdr_detail`

```text
除权除息明细.

Endpoint: ``api/v1/market/data/yzxdr-detail``.
Method: ``GET``.
Documented endpoint: ``get_yzxdr_detail``.

Args:
    year: 年份（如 2026） (type: uint32; required: Y).
    quarter: 季度，1-4 (type: uint32; required: Y).
    stock_code: 股票代码，6 位数字 (type: string; required: N).
    page: Page number, starting from 1. If omitted, the server default is used unless ``limit`` or ``all_pages`` is set.
    page_size: Rows per page. The SDK validates this against the endpoint-specific maximum.
    limit: Maximum number of rows to return. The SDK may fetch multiple pages to satisfy this limit.
    all_pages: Fetch and combine pages until the server reports the last page.
    max_pages: Optional safety cap for ``all_pages``.
    raw: Return the decoded JSON payload without tabular extraction.
    fields: Optional field list or comma-separated field string applied after extraction.
    as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
    **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

Returns:
    A pandas ``DataFrame`` by default, Python rows when
    ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
    payloads when multi-page fetching is used with ``raw=True``.
```

<h4 id="api-pledge-summary"><code>pledge_summary</code></h4>

- 接口名称：股权质押汇总
- HTTP：`GET`
- Path：`api/v1/market/data/pledge/pledge-summary`
- 参数：`page`, `page_size`
- 来源文档：`股权质押汇总.md`
- 原始接口：`stock_pledge_summary`

```text
股权质押汇总.

Endpoint: ``api/v1/market/data/pledge/pledge-summary``.
Method: ``GET``.
Documented endpoint: ``stock_pledge_summary``.

Args:
    page: Page number, starting from 1. If omitted, the server default is used unless ``limit`` or ``all_pages`` is set.
    page_size: Rows per page. The SDK validates this against the endpoint-specific maximum.
    limit: Maximum number of rows to return. The SDK may fetch multiple pages to satisfy this limit.
    all_pages: Fetch and combine pages until the server reports the last page.
    max_pages: Optional safety cap for ``all_pages``.
    raw: Return the decoded JSON payload without tabular extraction.
    fields: Optional field list or comma-separated field string applied after extraction.
    as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
    **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

Returns:
    A pandas ``DataFrame`` by default, Python rows when
    ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
    payloads when multi-page fetching is used with ``raw=True``.
```

<h4 id="api-stock-capital-flows"><code>stock_capital_flows</code></h4>

- 接口名称：股票资金流向
- HTTP：`GET`
- Path：`api/v1/market/data/stock-capital-flows`
- 参数：`date`, `page`, `page_size`
- 来源文档：`股票资金流向.md`
- 原始接口：`stock_capital_flows_paginated`

```text
股票资金流向.

Endpoint: ``api/v1/market/data/stock-capital-flows``.
Method: ``GET``.
Documented endpoint: ``stock_capital_flows_paginated``.

Args:
    date: 查询日期 YYYYMMDD；传入时查询该日 15:30 快照 (type: string; required: N).
    page: Page number, starting from 1. If omitted, the server default is used unless ``limit`` or ``all_pages`` is set.
    page_size: Rows per page. The SDK validates this against the endpoint-specific maximum.
    limit: Maximum number of rows to return. The SDK may fetch multiple pages to satisfy this limit.
    all_pages: Fetch and combine pages until the server reports the last page.
    max_pages: Optional safety cap for ``all_pages``.
    raw: Return the decoded JSON payload without tabular extraction.
    fields: Optional field list or comma-separated field string applied after extraction.
    as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
    **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

Returns:
    A pandas ``DataFrame`` by default, Python rows when
    ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
    payloads when multi-page fetching is used with ``raw=True``.
```

### 港股数据

<h4 id="api-company-hk"><code>company_hk</code></h4>

- 接口名称：港股公司信息
- HTTP：`GET`
- Path：`api/v1/market/data/hk/company-hk`
- 参数：`trade_code`
- 来源文档：`港股公司信息.md`
- 原始接口：`get_company_hk`

```text
港股公司信息.

Endpoint: ``api/v1/market/data/hk/company-hk``.
Method: ``GET``.
Documented endpoint: ``get_company_hk``.

Args:
    trade_code: 港股交易代码 (type: string; required: Y).
    raw: Return the decoded JSON payload without tabular extraction.
    fields: Optional field list or comma-separated field string applied after extraction.
    as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
    **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

Returns:
    A pandas ``DataFrame`` by default, Python rows when
    ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
    payloads when multi-page fetching is used with ``raw=True``.
```

<h4 id="api-eastmoney-hk-index-daily-kline"><code>eastmoney_hk_index_daily_kline</code></h4>

- 接口名称：东方财富港股指数日K
- HTTP：`GET`
- Path：`api/v1/market/data/eastmoney-hk-index-daily-kline`
- 参数：`index_code`, `trade_date`, `start_date`, `end_date`, `page`, `page_size`
- 来源文档：`东方财富港股指数日K.md`
- 原始接口：`get_eastmoney_hk_index_daily_kline`

```text
东方财富港股指数日K.

Endpoint: ``api/v1/market/data/eastmoney-hk-index-daily-kline``.
Method: ``GET``.
Documented endpoint: ``get_eastmoney_hk_index_daily_kline``.

Args:
    index_code: 指数代码，如 HSI / HSCEI / HSTECH；不传返回全部指数 (type: string; required: N).
    trade_date: 交易日 YYYY-MM-DD；与 start_date/end_date 互斥 (type: string; required: N).
    start_date: 区间起始日 YYYY-MM-DD；需与 end_date 同时提供 (type: string; required: N).
    end_date: 区间结束日 YYYY-MM-DD；需与 start_date 同时提供 (type: string; required: N).
    page: Page number, starting from 1. If omitted, the server default is used unless ``limit`` or ``all_pages`` is set.
    page_size: Rows per page. The SDK validates this against the endpoint-specific maximum.
    limit: Maximum number of rows to return. The SDK may fetch multiple pages to satisfy this limit.
    all_pages: Fetch and combine pages until the server reports the last page.
    max_pages: Optional safety cap for ``all_pages``.
    raw: Return the decoded JSON payload without tabular extraction.
    fields: Optional field list or comma-separated field string applied after extraction.
    as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
    **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

Returns:
    A pandas ``DataFrame`` by default, Python rows when
    ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
    payloads when multi-page fetching is used with ``raw=True``.
```

<h4 id="api-hk-balance-bank"><code>hk_balance_bank</code></h4>

- 接口名称：港股资产负债表
- HTTP：`GET`
- Path：`api/v1/market/data/hk/hk-balance-bank`
- 参数：`trade_code`, `year`, `report_type`, `start_date`, `end_date`, `page`, `page_size`
- 来源文档：`港股资产负债表.md`
- 原始接口：`hk_balance_bank`

```text
港股资产负债表.

Endpoint: ``api/v1/market/data/hk/hk-balance-bank``.
Method: ``GET``.
Documented endpoint: ``hk_balance_bank``.

Args:
    trade_code: 港股代码（支持 `700` / `00700.HK`） (type: string; required: N).
    year: 报告期年份（如 2024），按 `end_date` 日历年过滤，需配 `report_type` (type: int32; required: N).
    report_type: 报告类型：annual（年报）/ semi（半年报），需配 `year` (type: string; required: N).
    start_date: 起始截止日期 YYYYMMDD，筛选 `end_date >= 此值` (type: int32; required: N).
    end_date: 结束截止日期 YYYYMMDD，筛选 `end_date <= 此值` (type: int32; required: N).
    page: Page number, starting from 1. If omitted, the server default is used unless ``limit`` or ``all_pages`` is set.
    page_size: Rows per page. The SDK validates this against the endpoint-specific maximum.
    limit: Maximum number of rows to return. The SDK may fetch multiple pages to satisfy this limit.
    all_pages: Fetch and combine pages until the server reports the last page.
    max_pages: Optional safety cap for ``all_pages``.
    raw: Return the decoded JSON payload without tabular extraction.
    fields: Optional field list or comma-separated field string applied after extraction.
    as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
    **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

Returns:
    A pandas ``DataFrame`` by default, Python rows when
    ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
    payloads when multi-page fetching is used with ``raw=True``.
```

<h4 id="api-hk-balance-gene"><code>hk_balance_gene</code></h4>

- 接口名称：港股资产负债表
- HTTP：`GET`
- Path：`api/v1/market/data/hk/hk-balance-gene`
- 参数：`trade_code`, `year`, `report_type`, `start_date`, `end_date`, `page`, `page_size`
- 来源文档：`港股资产负债表.md`
- 原始接口：`hk_balance_gene`

```text
港股资产负债表.

Endpoint: ``api/v1/market/data/hk/hk-balance-gene``.
Method: ``GET``.
Documented endpoint: ``hk_balance_gene``.

Args:
    trade_code: 港股代码（支持 `700` / `00700.HK`） (type: string; required: N).
    year: 报告期年份（如 2024），按 `end_date` 日历年过滤，需配 `report_type` (type: int32; required: N).
    report_type: 报告类型：annual（年报）/ semi（半年报），需配 `year` (type: string; required: N).
    start_date: 起始截止日期 YYYYMMDD，筛选 `end_date >= 此值` (type: int32; required: N).
    end_date: 结束截止日期 YYYYMMDD，筛选 `end_date <= 此值` (type: int32; required: N).
    page: Page number, starting from 1. If omitted, the server default is used unless ``limit`` or ``all_pages`` is set.
    page_size: Rows per page. The SDK validates this against the endpoint-specific maximum.
    limit: Maximum number of rows to return. The SDK may fetch multiple pages to satisfy this limit.
    all_pages: Fetch and combine pages until the server reports the last page.
    max_pages: Optional safety cap for ``all_pages``.
    raw: Return the decoded JSON payload without tabular extraction.
    fields: Optional field list or comma-separated field string applied after extraction.
    as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
    **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

Returns:
    A pandas ``DataFrame`` by default, Python rows when
    ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
    payloads when multi-page fetching is used with ``raw=True``.
```

<h4 id="api-hk-balance-insur"><code>hk_balance_insur</code></h4>

- 接口名称：港股资产负债表
- HTTP：`GET`
- Path：`api/v1/market/data/hk/hk-balance-insur`
- 参数：`trade_code`, `year`, `report_type`, `start_date`, `end_date`, `page`, `page_size`
- 来源文档：`港股资产负债表.md`
- 原始接口：`hk_balance_insur`

```text
港股资产负债表.

Endpoint: ``api/v1/market/data/hk/hk-balance-insur``.
Method: ``GET``.
Documented endpoint: ``hk_balance_insur``.

Args:
    trade_code: 港股代码（支持 `700` / `00700.HK`） (type: string; required: N).
    year: 报告期年份（如 2024），按 `end_date` 日历年过滤，需配 `report_type` (type: int32; required: N).
    report_type: 报告类型：annual（年报）/ semi（半年报），需配 `year` (type: string; required: N).
    start_date: 起始截止日期 YYYYMMDD，筛选 `end_date >= 此值` (type: int32; required: N).
    end_date: 结束截止日期 YYYYMMDD，筛选 `end_date <= 此值` (type: int32; required: N).
    page: Page number, starting from 1. If omitted, the server default is used unless ``limit`` or ``all_pages`` is set.
    page_size: Rows per page. The SDK validates this against the endpoint-specific maximum.
    limit: Maximum number of rows to return. The SDK may fetch multiple pages to satisfy this limit.
    all_pages: Fetch and combine pages until the server reports the last page.
    max_pages: Optional safety cap for ``all_pages``.
    raw: Return the decoded JSON payload without tabular extraction.
    fields: Optional field list or comma-separated field string applied after extraction.
    as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
    **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

Returns:
    A pandas ``DataFrame`` by default, Python rows when
    ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
    payloads when multi-page fetching is used with ``raw=True``.
```

<h4 id="api-hk-basinfo-get"><code>hk_basinfo_get</code></h4>

- 接口名称：港股个股信息
- HTTP：`GET`
- Path：`api/v1/market/data/hk/hk-view`
- 参数：`hk_code`
- 来源文档：`港股个股信息.md`
- 原始接口：`get_hk_basinfo_get`

```text
港股个股信息.

Endpoint: ``api/v1/market/data/hk/hk-view``.
Method: ``GET``.
Documented endpoint: ``get_hk_basinfo_get``.

Args:
    hk_code: 港股代码，如 `00700.HK` (type: string; required: Y).
    raw: Return the decoded JSON payload without tabular extraction.
    fields: Optional field list or comma-separated field string applied after extraction.
    as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
    **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

Returns:
    A pandas ``DataFrame`` by default, Python rows when
    ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
    payloads when multi-page fetching is used with ``raw=True``.
```

<h4 id="api-hk-basinfo-post"><code>hk_basinfo_post</code></h4>

- 接口名称：港股个股信息
- HTTP：`GET`
- Path：`api/v1/market/data/hk/hk-view`
- 参数：`hk_code`
- 来源文档：`港股个股信息.md`
- 原始接口：`get_hk_basinfo_post`

```text
港股个股信息.

Endpoint: ``api/v1/market/data/hk/hk-view``.
Method: ``GET``.
Documented endpoint: ``get_hk_basinfo_post``.

Args:
    hk_code: 港股代码，如 `00700.HK` (type: string; required: Y).
    raw: Return the decoded JSON payload without tabular extraction.
    fields: Optional field list or comma-separated field string applied after extraction.
    as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
    **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

Returns:
    A pandas ``DataFrame`` by default, Python rows when
    ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
    payloads when multi-page fetching is used with ``raw=True``.
```

<h4 id="api-hk-candlesticks"><code>hk_candlesticks</code></h4>

- 接口名称：港股K线
- HTTP：`GET`
- Path：`api/v1/market/data/hk/hk-candlesticks`
- 参数：`trade_code`, `interval_unit`, `until_date`, `since_date`, `interval_value`, `limit`, `adjust_kind`
- 来源文档：`港股K线.md`
- 原始接口：`get_hk_candlesticks`

```text
港股K线.

Endpoint: ``api/v1/market/data/hk/hk-candlesticks``.
Method: ``GET``.
Documented endpoint: ``get_hk_candlesticks``.

Args:
    trade_code: 港股代码，如 `00700.HK` 或 `700` (type: string; required: Y).
    interval_unit: 间隔单位：day / month / quarter / year (type: string; required: Y).
    until_date: 结束日期（YYYY-MM-DD） (type: date; required: Y).
    since_date: 开始日期（YYYY-MM-DD） (type: date; required: N).
    interval_value: 间隔数值（当前仅支持 1） (type: int; required: N).
    limit: 数量限制（保留最近 N 根） (type: int; required: N).
    adjust_kind: 复权类型：forward(默认/前复权) / none(不复权) (type: string; required: N).
    raw: Return the decoded JSON payload without tabular extraction.
    fields: Optional field list or comma-separated field string applied after extraction.
    as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
    **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

Returns:
    A pandas ``DataFrame`` by default, Python rows when
    ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
    payloads when multi-page fetching is used with ``raw=True``.
```

<h4 id="api-hk-cashflow"><code>hk_cashflow</code></h4>

- 接口名称：港股现金流量表
- HTTP：`GET`
- Path：`api/v1/market/data/hk/hk-cashflow`
- 参数：`stock_code`, `year`, `report_type`, `start_date`, `end_date`, `page`, `page_size`
- 来源文档：`港股现金流量表.md`
- 原始接口：`hk_cashflow`

```text
港股现金流量表.

Endpoint: ``api/v1/market/data/hk/hk-cashflow``.
Method: ``GET``.
Documented endpoint: ``hk_cashflow``.

Args:
    stock_code: 港股代码（如 `00700.HK`） (type: string; required: N).
    year: 报告期年份（如 2024），按 `end_date` 日历年过滤，需配 `report_type` (type: int32; required: N).
    report_type: 报告类型：annual（年报）/ semi（半年报），需配 `year` (type: string; required: N).
    start_date: 报告期范围下界 YYYYMMDD（含），过滤 `end_date >= 此值` (type: int32; required: N).
    end_date: 报告期范围上界 YYYYMMDD（含），过滤 `end_date <= 此值` (type: int32; required: N).
    page: Page number, starting from 1. If omitted, the server default is used unless ``limit`` or ``all_pages`` is set.
    page_size: Rows per page. The SDK validates this against the endpoint-specific maximum.
    limit: Maximum number of rows to return. The SDK may fetch multiple pages to satisfy this limit.
    all_pages: Fetch and combine pages until the server reports the last page.
    max_pages: Optional safety cap for ``all_pages``.
    raw: Return the decoded JSON payload without tabular extraction.
    fields: Optional field list or comma-separated field string applied after extraction.
    as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
    **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

Returns:
    A pandas ``DataFrame`` by default, Python rows when
    ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
    payloads when multi-page fetching is used with ``raw=True``.
```

<h4 id="api-hk-income-bank"><code>hk_income_bank</code></h4>

- 接口名称：港股利润表
- HTTP：`GET`
- Path：`api/v1/market/data/hk/hk-income-bank`
- 参数：`trade_code`, `year`, `report_type`, `start_date`, `end_date`, `page`, `page_size`
- 来源文档：`港股利润表.md`
- 原始接口：`hk_income_bank`

```text
港股利润表.

Endpoint: ``api/v1/market/data/hk/hk-income-bank``.
Method: ``GET``.
Documented endpoint: ``hk_income_bank``.

Args:
    trade_code: 港股代码（支持 `700` / `00700.HK`） (type: string; required: N).
    year: 报告期年份（如 2024），按 `end_date` 日历年过滤，需配 `report_type` (type: int32; required: N).
    report_type: 报告类型：annual（年报）/ semi（半年报），需配 `year` (type: string; required: N).
    start_date: 起始截止日期 YYYYMMDD，筛选 `end_date >= 此值` (type: int32; required: N).
    end_date: 结束截止日期 YYYYMMDD，筛选 `end_date <= 此值` (type: int32; required: N).
    page: Page number, starting from 1. If omitted, the server default is used unless ``limit`` or ``all_pages`` is set.
    page_size: Rows per page. The SDK validates this against the endpoint-specific maximum.
    limit: Maximum number of rows to return. The SDK may fetch multiple pages to satisfy this limit.
    all_pages: Fetch and combine pages until the server reports the last page.
    max_pages: Optional safety cap for ``all_pages``.
    raw: Return the decoded JSON payload without tabular extraction.
    fields: Optional field list or comma-separated field string applied after extraction.
    as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
    **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

Returns:
    A pandas ``DataFrame`` by default, Python rows when
    ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
    payloads when multi-page fetching is used with ``raw=True``.
```

<h4 id="api-hk-income-gene"><code>hk_income_gene</code></h4>

- 接口名称：港股利润表
- HTTP：`GET`
- Path：`api/v1/market/data/hk/hk-income-gene`
- 参数：`trade_code`, `year`, `report_type`, `start_date`, `end_date`, `page`, `page_size`
- 来源文档：`港股利润表.md`
- 原始接口：`hk_income_gene`

```text
港股利润表.

Endpoint: ``api/v1/market/data/hk/hk-income-gene``.
Method: ``GET``.
Documented endpoint: ``hk_income_gene``.

Args:
    trade_code: 港股代码（支持 `700` / `00700.HK`） (type: string; required: N).
    year: 报告期年份（如 2024），按 `end_date` 日历年过滤，需配 `report_type` (type: int32; required: N).
    report_type: 报告类型：annual（年报）/ semi（半年报），需配 `year` (type: string; required: N).
    start_date: 起始截止日期 YYYYMMDD，筛选 `end_date >= 此值` (type: int32; required: N).
    end_date: 结束截止日期 YYYYMMDD，筛选 `end_date <= 此值` (type: int32; required: N).
    page: Page number, starting from 1. If omitted, the server default is used unless ``limit`` or ``all_pages`` is set.
    page_size: Rows per page. The SDK validates this against the endpoint-specific maximum.
    limit: Maximum number of rows to return. The SDK may fetch multiple pages to satisfy this limit.
    all_pages: Fetch and combine pages until the server reports the last page.
    max_pages: Optional safety cap for ``all_pages``.
    raw: Return the decoded JSON payload without tabular extraction.
    fields: Optional field list or comma-separated field string applied after extraction.
    as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
    **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

Returns:
    A pandas ``DataFrame`` by default, Python rows when
    ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
    payloads when multi-page fetching is used with ``raw=True``.
```

<h4 id="api-hk-income-insur"><code>hk_income_insur</code></h4>

- 接口名称：港股利润表
- HTTP：`GET`
- Path：`api/v1/market/data/hk/hk-income-insur`
- 参数：`trade_code`, `year`, `report_type`, `start_date`, `end_date`, `page`, `page_size`
- 来源文档：`港股利润表.md`
- 原始接口：`hk_income_insur`

```text
港股利润表.

Endpoint: ``api/v1/market/data/hk/hk-income-insur``.
Method: ``GET``.
Documented endpoint: ``hk_income_insur``.

Args:
    trade_code: 港股代码（支持 `700` / `00700.HK`） (type: string; required: N).
    year: 报告期年份（如 2024），按 `end_date` 日历年过滤，需配 `report_type` (type: int32; required: N).
    report_type: 报告类型：annual（年报）/ semi（半年报），需配 `year` (type: string; required: N).
    start_date: 起始截止日期 YYYYMMDD，筛选 `end_date >= 此值` (type: int32; required: N).
    end_date: 结束截止日期 YYYYMMDD，筛选 `end_date <= 此值` (type: int32; required: N).
    page: Page number, starting from 1. If omitted, the server default is used unless ``limit`` or ``all_pages`` is set.
    page_size: Rows per page. The SDK validates this against the endpoint-specific maximum.
    limit: Maximum number of rows to return. The SDK may fetch multiple pages to satisfy this limit.
    all_pages: Fetch and combine pages until the server reports the last page.
    max_pages: Optional safety cap for ``all_pages``.
    raw: Return the decoded JSON payload without tabular extraction.
    fields: Optional field list or comma-separated field string applied after extraction.
    as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
    **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

Returns:
    A pandas ``DataFrame`` by default, Python rows when
    ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
    payloads when multi-page fetching is used with ``raw=True``.
```

<h4 id="api-hk-valuatnanalyd"><code>hk_valuatnanalyd</code></h4>

- 接口名称：港股估值分析
- HTTP：`GET`
- Path：`api/v1/market/data/hk/hk-valuatnanalyd`
- 参数：`trade_code`, `page`, `page_size`
- 来源文档：`港股估值分析.md`
- 原始接口：`get_hk_valuatnanalyd`

```text
港股估值分析.

Endpoint: ``api/v1/market/data/hk/hk-valuatnanalyd``.
Method: ``GET``.
Documented endpoint: ``get_hk_valuatnanalyd``.

Args:
    trade_code: 港股代码（支持 `700` / `00700.HK`）；留空查全市场 (type: string; required: N).
    page: Page number, starting from 1. If omitted, the server default is used unless ``limit`` or ``all_pages`` is set.
    page_size: Rows per page. The SDK validates this against the endpoint-specific maximum.
    limit: Maximum number of rows to return. The SDK may fetch multiple pages to satisfy this limit.
    all_pages: Fetch and combine pages until the server reports the last page.
    max_pages: Optional safety cap for ``all_pages``.
    raw: Return the decoded JSON payload without tabular extraction.
    fields: Optional field list or comma-separated field string applied after extraction.
    as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
    **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

Returns:
    A pandas ``DataFrame`` by default, Python rows when
    ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
    payloads when multi-page fetching is used with ``raw=True``.
```

<h4 id="api-market-cap-hk"><code>market_cap_hk</code></h4>

- 接口名称：港股市值
- HTTP：`GET`
- Path：`api/v1/market/data/hk/market-cap-hk`
- 参数：`trade_code`
- 来源文档：`港股市值.md`
- 原始接口：`get_market_cap_hk`

```text
港股市值.

Endpoint: ``api/v1/market/data/hk/market-cap-hk``.
Method: ``GET``.
Documented endpoint: ``get_market_cap_hk``.

Args:
    trade_code: 港股交易代码 (type: string; required: Y).
    raw: Return the decoded JSON payload without tabular extraction.
    fields: Optional field list or comma-separated field string applied after extraction.
    as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
    **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

Returns:
    A pandas ``DataFrame`` by default, Python rows when
    ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
    payloads when multi-page fetching is used with ``raw=True``.
```

### 美股数据

<h4 id="api-eastmoney-us-stock-daily-kline"><code>eastmoney_us_stock_daily_kline</code></h4>

- 接口名称：东方财富美股日OHLC
- HTTP：`GET`
- Path：`api/v1/market/data/eastmoney-us-stock-daily-ohlc`
- 参数：`stock_code`, `start_date`, `end_date`, `page`, `page_size`
- 来源文档：`东方财富美股日OHLC.md`
- 原始接口：`eastmoney_us_stock_daily_kline`

```text
东方财富美股日OHLC.

Endpoint: ``api/v1/market/data/eastmoney-us-stock-daily-ohlc``.
Method: ``GET``.
Documented endpoint: ``eastmoney_us_stock_daily_kline``.

Args:
    stock_code: 股票代码，如 AAPL (type: string; required: Y).
    start_date: 起始日期（含），YYYY-MM-DD 或 YYYYMMDD；不传从最早开始 (type: string; required: N).
    end_date: 截止日期（含），YYYY-MM-DD 或 YYYYMMDD；不传到最晚 (type: string; required: N).
    page: Page number, starting from 1. If omitted, the server default is used unless ``limit`` or ``all_pages`` is set.
    page_size: Rows per page. The SDK validates this against the endpoint-specific maximum.
    limit: Maximum number of rows to return. The SDK may fetch multiple pages to satisfy this limit.
    all_pages: Fetch and combine pages until the server reports the last page.
    max_pages: Optional safety cap for ``all_pages``.
    raw: Return the decoded JSON payload without tabular extraction.
    fields: Optional field list or comma-separated field string applied after extraction.
    as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
    **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

Returns:
    A pandas ``DataFrame`` by default, Python rows when
    ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
    payloads when multi-page fetching is used with ``raw=True``.
```

<h4 id="api-eastmoney-us-stock-latest-kline"><code>eastmoney_us_stock_latest_kline</code></h4>

- 接口名称：东方财富美股最新OHLC
- HTTP：`GET`
- Path：`api/v1/market/data/eastmoney-us-stock-latest-ohlc`
- 参数：`stock_code`, `page`, `page_size`
- 来源文档：`东方财富美股最新OHLC.md`
- 原始接口：`eastmoney_us_stock_latest_kline`

```text
东方财富美股最新OHLC.

Endpoint: ``api/v1/market/data/eastmoney-us-stock-latest-ohlc``.
Method: ``GET``.
Documented endpoint: ``eastmoney_us_stock_latest_kline``.

Args:
    stock_code: 股票代码，如 ADV；不传返回全部美股最新 K 线 (type: string; required: N).
    page: Page number, starting from 1. If omitted, the server default is used unless ``limit`` or ``all_pages`` is set.
    page_size: Rows per page. The SDK validates this against the endpoint-specific maximum.
    limit: Maximum number of rows to return. The SDK may fetch multiple pages to satisfy this limit.
    all_pages: Fetch and combine pages until the server reports the last page.
    max_pages: Optional safety cap for ``all_pages``.
    raw: Return the decoded JSON payload without tabular extraction.
    fields: Optional field list or comma-separated field string applied after extraction.
    as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
    **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

Returns:
    A pandas ``DataFrame`` by default, Python rows when
    ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
    payloads when multi-page fetching is used with ``raw=True``.
```

<h4 id="api-eastmoney-us-stock-list"><code>eastmoney_us_stock_list</code></h4>

- 接口名称：东方财富美股列表
- HTTP：`GET`
- Path：`api/v1/market/data/eastmoney-us-stock-list`
- 参数：`refresh`, `page`, `page_size`
- 来源文档：`东方财富美股列表.md`
- 原始接口：`eastmoney_us_stock_list`

```text
东方财富美股列表.

Endpoint: ``api/v1/market/data/eastmoney-us-stock-list``.
Method: ``GET``.
Documented endpoint: ``eastmoney_us_stock_list``.

Args:
    refresh: 为 true 时强制从 CSV 重新加载列表缓存 (type: bool; required: N).
    page: Page number, starting from 1. If omitted, the server default is used unless ``limit`` or ``all_pages`` is set.
    page_size: Rows per page. The SDK validates this against the endpoint-specific maximum.
    limit: Maximum number of rows to return. The SDK may fetch multiple pages to satisfy this limit.
    all_pages: Fetch and combine pages until the server reports the last page.
    max_pages: Optional safety cap for ``all_pages``.
    raw: Return the decoded JSON payload without tabular extraction.
    fields: Optional field list or comma-separated field string applied after extraction.
    as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
    **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

Returns:
    A pandas ``DataFrame`` by default, Python rows when
    ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
    payloads when multi-page fetching is used with ``raw=True``.
```

<h4 id="api-us-balance"><code>us_balance</code></h4>

- 接口名称：美股资产负债表
- HTTP：`GET`
- Path：`api/v1/market/data/us/us-balance`
- 参数：`stock_code`, `period`, `report_type`, `start_date`, `end_date`, `page`, `page_size`
- 来源文档：`美股资产负债表.md`
- 原始接口：`us_balance`

```text
美股资产负债表.

Endpoint: ``api/v1/market/data/us/us-balance``.
Method: ``GET``.
Documented endpoint: ``us_balance``.

Args:
    stock_code: 美股代码，纯代码不带后缀，如 NVDA (type: string; required: Y).
    period: 财年（如 2024），匹配 stmt_year，非自然年 (type: int; required: N).
    report_type: 报告期类型：Q1 / Q2 / Q3 / Q4 / H1 (type: string; required: N).
    start_date: 报告期下界 YYYYMMDD（含），过滤 end_date (type: int; required: N).
    end_date: 报告期上界 YYYYMMDD（含），过滤 end_date (type: int; required: N).
    page: Page number, starting from 1. If omitted, the server default is used unless ``limit`` or ``all_pages`` is set.
    page_size: Rows per page. The SDK validates this against the endpoint-specific maximum.
    limit: Maximum number of rows to return. The SDK may fetch multiple pages to satisfy this limit.
    all_pages: Fetch and combine pages until the server reports the last page.
    max_pages: Optional safety cap for ``all_pages``.
    raw: Return the decoded JSON payload without tabular extraction.
    fields: Optional field list or comma-separated field string applied after extraction.
    as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
    **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

Returns:
    A pandas ``DataFrame`` by default, Python rows when
    ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
    payloads when multi-page fetching is used with ``raw=True``.
```

<h4 id="api-us-basic"><code>us_basic</code></h4>

- 接口名称：美股基础信息
- HTTP：`GET`
- Path：`api/v1/market/data/us/us-basic`
- 参数：`stock_code`, `page`, `page_size`
- 来源文档：`美股基础信息.md`
- 原始接口：`us_basic`

```text
美股基础信息.

Endpoint: ``api/v1/market/data/us/us-basic``.
Method: ``GET``.
Documented endpoint: ``us_basic``.

Args:
    stock_code: 美股代码（可选），纯代码如 NVDA；不传则分页返回全部 (type: string; required: N).
    page: Page number, starting from 1. If omitted, the server default is used unless ``limit`` or ``all_pages`` is set.
    page_size: Rows per page. The SDK validates this against the endpoint-specific maximum.
    limit: Maximum number of rows to return. The SDK may fetch multiple pages to satisfy this limit.
    all_pages: Fetch and combine pages until the server reports the last page.
    max_pages: Optional safety cap for ``all_pages``.
    raw: Return the decoded JSON payload without tabular extraction.
    fields: Optional field list or comma-separated field string applied after extraction.
    as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
    **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

Returns:
    A pandas ``DataFrame`` by default, Python rows when
    ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
    payloads when multi-page fetching is used with ``raw=True``.
```

<h4 id="api-us-cashflow"><code>us_cashflow</code></h4>

- 接口名称：美股现金流
- HTTP：`GET`
- Path：`api/v1/market/data/us/us-cashflow`
- 参数：`stock_code`, `period`, `report_type`, `start_date`, `end_date`, `page`, `page_size`
- 来源文档：`美股现金流.md`
- 原始接口：`us_cashflow`

```text
美股现金流.

Endpoint: ``api/v1/market/data/us/us-cashflow``.
Method: ``GET``.
Documented endpoint: ``us_cashflow``.

Args:
    stock_code: 美股代码，纯代码不带后缀，如 NVDA (type: string; required: Y).
    period: 财年（如 2024），匹配 stmt_year，非自然年 (type: int; required: N).
    report_type: 报告期类型：Q1 / Q2 / Q3 / Q4 / H1 (type: string; required: N).
    start_date: 报告期下界 YYYYMMDD（含），过滤 end_date (type: int; required: N).
    end_date: 报告期上界 YYYYMMDD（含），过滤 end_date (type: int; required: N).
    page: Page number, starting from 1. If omitted, the server default is used unless ``limit`` or ``all_pages`` is set.
    page_size: Rows per page. The SDK validates this against the endpoint-specific maximum.
    limit: Maximum number of rows to return. The SDK may fetch multiple pages to satisfy this limit.
    all_pages: Fetch and combine pages until the server reports the last page.
    max_pages: Optional safety cap for ``all_pages``.
    raw: Return the decoded JSON payload without tabular extraction.
    fields: Optional field list or comma-separated field string applied after extraction.
    as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
    **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

Returns:
    A pandas ``DataFrame`` by default, Python rows when
    ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
    payloads when multi-page fetching is used with ``raw=True``.
```

<h4 id="api-us-income"><code>us_income</code></h4>

- 接口名称：美股利润表
- HTTP：`GET`
- Path：`api/v1/market/data/us/us-income`
- 参数：`stock_code`, `period`, `report_type`, `start_date`, `end_date`, `page`, `page_size`
- 来源文档：`美股利润表.md`
- 原始接口：`us_income`

```text
美股利润表.

Endpoint: ``api/v1/market/data/us/us-income``.
Method: ``GET``.
Documented endpoint: ``us_income``.

Args:
    stock_code: 美股代码，纯代码不带后缀，如 NVDA (type: string; required: Y).
    period: 财年（如 2024），匹配 stmt_year，非自然年 (type: int; required: N).
    report_type: 报告期类型：Q1 / Q2 / Q3 / Q4 / H1 (type: string; required: N).
    start_date: 报告期下界 YYYYMMDD（含），过滤 end_date (type: int; required: N).
    end_date: 报告期上界 YYYYMMDD（含），过滤 end_date (type: int; required: N).
    page: Page number, starting from 1. If omitted, the server default is used unless ``limit`` or ``all_pages`` is set.
    page_size: Rows per page. The SDK validates this against the endpoint-specific maximum.
    limit: Maximum number of rows to return. The SDK may fetch multiple pages to satisfy this limit.
    all_pages: Fetch and combine pages until the server reports the last page.
    max_pages: Optional safety cap for ``all_pages``.
    raw: Return the decoded JSON payload without tabular extraction.
    fields: Optional field list or comma-separated field string applied after extraction.
    as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
    **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

Returns:
    A pandas ``DataFrame`` by default, Python rows when
    ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
    payloads when multi-page fetching is used with ``raw=True``.
```

<h4 id="api-eastmoney-us-stock-daily-ohlc"><code>eastmoney_us_stock_daily_ohlc</code></h4>

- 接口名称：东方财富美股日OHLC
- HTTP：`GET`
- Path：`api/v1/market/data/eastmoney-us-stock-daily-ohlc`
- 参数：`stock_code`, `start_date`, `end_date`, `page`, `page_size`
- 来源文档：`东方财富美股日OHLC.md`
- 原始接口：`eastmoney_us_stock_daily_kline`

```text
东方财富美股日OHLC.

Endpoint: ``api/v1/market/data/eastmoney-us-stock-daily-ohlc``.
Method: ``GET``.
Documented endpoint: ``eastmoney_us_stock_daily_kline``.

Args:
    stock_code: 股票代码，如 AAPL (type: string; required: Y).
    start_date: 起始日期（含），YYYY-MM-DD 或 YYYYMMDD；不传从最早开始 (type: string; required: N).
    end_date: 截止日期（含），YYYY-MM-DD 或 YYYYMMDD；不传到最晚 (type: string; required: N).
    page: Page number, starting from 1. If omitted, the server default is used unless ``limit`` or ``all_pages`` is set.
    page_size: Rows per page. The SDK validates this against the endpoint-specific maximum.
    limit: Maximum number of rows to return. The SDK may fetch multiple pages to satisfy this limit.
    all_pages: Fetch and combine pages until the server reports the last page.
    max_pages: Optional safety cap for ``all_pages``.
    raw: Return the decoded JSON payload without tabular extraction.
    fields: Optional field list or comma-separated field string applied after extraction.
    as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
    **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

Returns:
    A pandas ``DataFrame`` by default, Python rows when
    ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
    payloads when multi-page fetching is used with ``raw=True``.
```

<h4 id="api-eastmoney-us-stock-latest-ohlc"><code>eastmoney_us_stock_latest_ohlc</code></h4>

- 接口名称：东方财富美股最新OHLC
- HTTP：`GET`
- Path：`api/v1/market/data/eastmoney-us-stock-latest-ohlc`
- 参数：`stock_code`, `page`, `page_size`
- 来源文档：`东方财富美股最新OHLC.md`
- 原始接口：`eastmoney_us_stock_latest_kline`

```text
东方财富美股最新OHLC.

Endpoint: ``api/v1/market/data/eastmoney-us-stock-latest-ohlc``.
Method: ``GET``.
Documented endpoint: ``eastmoney_us_stock_latest_kline``.

Args:
    stock_code: 股票代码，如 ADV；不传返回全部美股最新 K 线 (type: string; required: N).
    page: Page number, starting from 1. If omitted, the server default is used unless ``limit`` or ``all_pages`` is set.
    page_size: Rows per page. The SDK validates this against the endpoint-specific maximum.
    limit: Maximum number of rows to return. The SDK may fetch multiple pages to satisfy this limit.
    all_pages: Fetch and combine pages until the server reports the last page.
    max_pages: Optional safety cap for ``all_pages``.
    raw: Return the decoded JSON payload without tabular extraction.
    fields: Optional field list or comma-separated field string applied after extraction.
    as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
    **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

Returns:
    A pandas ``DataFrame`` by default, Python rows when
    ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
    payloads when multi-page fetching is used with ``raw=True``.
```

### 指数专题

<h4 id="api-global-index-daily-kline"><code>global_index_daily_kline</code></h4>

- 接口名称：全球指数日K线
- HTTP：`GET`
- Path：`api/v1/market/data/global-index/daily-kline`
- 参数：`secid`, `start_date`, `end_date`
- 来源文档：`全球指数日K线.md`
- 原始接口：`global_index_daily_kline`

```text
全球指数日K线.

Endpoint: ``api/v1/market/data/global-index/daily-kline``.
Method: ``GET``.
Documented endpoint: ``global_index_daily_kline``.

Args:
    secid: 东方财富全球指数编码，如 100.NDX、100.DJIA、100.SPX、100.HSI、100.N225 (type: string; required: Y).
    start_date: 开始日期 YYYY-MM-DD（含） (type: string; required: N).
    end_date: 结束日期 YYYY-MM-DD（含） (type: string; required: N).
    raw: Return the decoded JSON payload without tabular extraction.
    fields: Optional field list or comma-separated field string applied after extraction.
    as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
    **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

Returns:
    A pandas ``DataFrame`` by default, Python rows when
    ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
    payloads when multi-page fetching is used with ``raw=True``.
```

<h4 id="api-index-description-all"><code>index_description_all</code></h4>

- 接口名称：指数基础信息
- HTTP：`GET`
- Path：`api/v1/market/data/index-description-all`
- 参数：-
- 来源文档：`指数基础信息.md`
- 原始接口：`index_description_all`

```text
指数基础信息.

Endpoint: ``api/v1/market/data/index-description-all``.
Method: ``GET``.
Documented endpoint: ``index_description_all``.

Args:
    raw: Return the decoded JSON payload without tabular extraction.
    fields: Optional field list or comma-separated field string applied after extraction.
    as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
    **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

Returns:
    A pandas ``DataFrame`` by default, Python rows when
    ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
    payloads when multi-page fetching is used with ``raw=True``.
```

<h4 id="api-index-description-list"><code>index_description_list</code></h4>

- 接口名称：中证指数描述列表
- HTTP：`GET`
- Path：`api/v1/market/data/index/index_description`
- 参数：`page`, `page_size`
- 来源文档：`中证指数描述列表.md`
- 原始接口：`index_description_list_handler`

```text
中证指数描述列表.

Endpoint: ``api/v1/market/data/index/index_description``.
Method: ``GET``.
Documented endpoint: ``index_description_list_handler``.

Args:
    page: Page number, starting from 1. If omitted, the server default is used unless ``limit`` or ``all_pages`` is set.
    page_size: Rows per page. The SDK validates this against the endpoint-specific maximum.
    limit: Maximum number of rows to return. The SDK may fetch multiple pages to satisfy this limit.
    all_pages: Fetch and combine pages until the server reports the last page.
    max_pages: Optional safety cap for ``all_pages``.
    raw: Return the decoded JSON payload without tabular extraction.
    fields: Optional field list or comma-separated field string applied after extraction.
    as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
    **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

Returns:
    A pandas ``DataFrame`` by default, Python rows when
    ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
    payloads when multi-page fetching is used with ``raw=True``.
```

<h4 id="api-index-weight-list"><code>index_weight_list</code></h4>

- 接口名称：指数权重列表
- HTTP：`GET`
- Path：`api/v1/market/data/index/index_weight`
- 参数：`index_code`, `date`, `page`, `page_size`
- 来源文档：`指数权重列表.md`
- 原始接口：`index_weight_list_handler`

```text
指数权重列表.

Endpoint: ``api/v1/market/data/index/index_weight``.
Method: ``GET``.
Documented endpoint: ``index_weight_list_handler``.

Args:
    index_code: 指数代码，如 000300（沪深300），为空会被拒 (type: string; required: Y).
    date: 权重采集日期 YYYYMMDD（如 20260529），不传取最新期 (type: string; required: N).
    page: Page number, starting from 1. If omitted, the server default is used unless ``limit`` or ``all_pages`` is set.
    page_size: Rows per page. The SDK validates this against the endpoint-specific maximum.
    limit: Maximum number of rows to return. The SDK may fetch multiple pages to satisfy this limit.
    all_pages: Fetch and combine pages until the server reports the last page.
    max_pages: Optional safety cap for ``all_pages``.
    raw: Return the decoded JSON payload without tabular extraction.
    fields: Optional field list or comma-separated field string applied after extraction.
    as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
    **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

Returns:
    A pandas ``DataFrame`` by default, Python rows when
    ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
    payloads when multi-page fetching is used with ``raw=True``.
```

<h4 id="api-index-weight-summary"><code>index_weight_summary</code></h4>

- 接口名称：指数权重汇总
- HTTP：`GET`
- Path：`api/v1/market/data/index/index_weight_summary`
- 参数：`page`, `page_size`
- 来源文档：`指数权重汇总.md`
- 原始接口：`index_weight_summary_handler`

```text
指数权重汇总.

Endpoint: ``api/v1/market/data/index/index_weight_summary``.
Method: ``GET``.
Documented endpoint: ``index_weight_summary_handler``.

Args:
    page: Page number, starting from 1. If omitted, the server default is used unless ``limit`` or ``all_pages`` is set.
    page_size: Rows per page. The SDK validates this against the endpoint-specific maximum.
    limit: Maximum number of rows to return. The SDK may fetch multiple pages to satisfy this limit.
    all_pages: Fetch and combine pages until the server reports the last page.
    max_pages: Optional safety cap for ``all_pages``.
    raw: Return the decoded JSON payload without tabular extraction.
    fields: Optional field list or comma-separated field string applied after extraction.
    as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
    **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

Returns:
    A pandas ``DataFrame`` by default, Python rows when
    ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
    payloads when multi-page fetching is used with ``raw=True``.
```

<h4 id="api-sw-industry-constituent-history"><code>sw_industry_constituent_history</code></h4>

- 接口名称：申万行业成份股历史
- HTTP：`GET`
- Path：`api/v1/market/data/sw-industry/constituent-history`
- 参数：`industry_code`
- 来源文档：`申万行业成份股历史.md`
- 原始接口：`sw_industry_constituent_history`

```text
申万行业成份股历史.

Endpoint: ``api/v1/market/data/sw-industry/constituent-history``.
Method: ``GET``.
Documented endpoint: ``sw_industry_constituent_history``.

Args:
    industry_code: 行业代码，带 .SI 后缀，如 801010.SI (type: string; required: Y).
    raw: Return the decoded JSON payload without tabular extraction.
    fields: Optional field list or comma-separated field string applied after extraction.
    as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
    **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

Returns:
    A pandas ``DataFrame`` by default, Python rows when
    ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
    payloads when multi-page fetching is used with ``raw=True``.
```

<h4 id="api-sw-industry-daily-metrics"><code>sw_industry_daily_metrics</code></h4>

- 接口名称：申万行业日度指标
- HTTP：`GET`
- Path：`api/v1/market/data/sw-industry/daily-metrics`
- 参数：`level`, `start_date`, `end_date`, `industry_code`, `page`, `page_size`
- 来源文档：`申万行业日度指标.md`
- 原始接口：`sw_industry_daily_metrics`

```text
申万行业日度指标.

Endpoint: ``api/v1/market/data/sw-industry/daily-metrics``.
Method: ``GET``.
Documented endpoint: ``sw_industry_daily_metrics``.

Args:
    level: 行业层级：1/2/3 (type: int; required: Y).
    start_date: 起始日期，YYYYMMDD (type: string; required: Y).
    end_date: 截止日期，YYYYMMDD (type: string; required: Y).
    industry_code: 行业代码，带 .SI 后缀，如 801010.SI (type: string; required: Y).
    page: Page number, starting from 1. If omitted, the server default is used unless ``limit`` or ``all_pages`` is set.
    page_size: Rows per page. The SDK validates this against the endpoint-specific maximum.
    limit: Maximum number of rows to return. The SDK may fetch multiple pages to satisfy this limit.
    all_pages: Fetch and combine pages until the server reports the last page.
    max_pages: Optional safety cap for ``all_pages``.
    raw: Return the decoded JSON payload without tabular extraction.
    fields: Optional field list or comma-separated field string applied after extraction.
    as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
    **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

Returns:
    A pandas ``DataFrame`` by default, Python rows when
    ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
    payloads when multi-page fetching is used with ``raw=True``.
```

<h4 id="api-sw-industry-overview"><code>sw_industry_overview</code></h4>

- 接口名称：申万行业总览
- HTTP：`GET`
- Path：`api/v1/market/data/sw-industry/overview`
- 参数：`date`, `level`, `page`, `page_size`
- 来源文档：`申万行业总览.md`
- 原始接口：`sw_industry_overview`

```text
申万行业总览.

Endpoint: ``api/v1/market/data/sw-industry/overview``.
Method: ``GET``.
Documented endpoint: ``sw_industry_overview``.

Args:
    date: 交易日，格式 YYYYMMDD (type: string; required: Y).
    level: 行业层级：1/2/3，不传返回全部 (type: int; required: N).
    page: Page number, starting from 1. If omitted, the server default is used unless ``limit`` or ``all_pages`` is set.
    page_size: Rows per page. The SDK validates this against the endpoint-specific maximum.
    limit: Maximum number of rows to return. The SDK may fetch multiple pages to satisfy this limit.
    all_pages: Fetch and combine pages until the server reports the last page.
    max_pages: Optional safety cap for ``all_pages``.
    raw: Return the decoded JSON payload without tabular extraction.
    fields: Optional field list or comma-separated field string applied after extraction.
    as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
    **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

Returns:
    A pandas ``DataFrame`` by default, Python rows when
    ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
    payloads when multi-page fetching is used with ``raw=True``.
```

### ETF专题

<h4 id="api-etf-adjust-factor"><code>etf_adjust_factor</code></h4>

- 接口名称：ETF复权因子
- HTTP：`GET`
- Path：`api/v1/market/data/etf-adjust-factor`
- 参数：`symbol`, `trade_date`, `start_date`, `end_date`, `offset`, `limit`
- 来源文档：`ETF复权因子.md`
- 原始接口：`etf_adjust_factor`

```text
ETF复权因子.

Endpoint: ``api/v1/market/data/etf-adjust-factor``.
Method: ``GET``.
Documented endpoint: ``etf_adjust_factor``.

Args:
    symbol: ETF 代码，支持纯数字或带后缀格式；区间扫描必填 (type: string; required: N).
    trade_date: 交易日期 YYYYMMDD；空则默认当天，非交易日回退前一交易日 (type: string; required: N).
    start_date: 区间起始日期 YYYYMMDD；区间扫描必填且需配 symbol (type: string; required: N).
    end_date: 区间结束日期 YYYYMMDD；区间扫描必填且需配 symbol (type: string; required: N).
    offset: 返回结果起始偏移 (type: int; required: N).
    limit: 返回结果最大条数 (type: int; required: N).
    raw: Return the decoded JSON payload without tabular extraction.
    fields: Optional field list or comma-separated field string applied after extraction.
    as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
    **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

Returns:
    A pandas ``DataFrame`` by default, Python rows when
    ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
    payloads when multi-page fetching is used with ``raw=True``.
```

<h4 id="api-etf-components"><code>etf_components</code></h4>

- 接口名称：ETF成份股
- HTTP：`GET`
- Path：`api/v1/market/data/etf-component`
- 参数：`symbol`
- 来源文档：`ETF成份股.md`
- 原始接口：`get_etf_components_handler`

```text
ETF成份股.

Endpoint: ``api/v1/market/data/etf-component``.
Method: ``GET``.
Documented endpoint: ``get_etf_components_handler``.

Args:
    symbol: ETF 标的代码，带交易所后缀，如 510300.XSHG、159915.XSHE (type: string; required: Y).
    raw: Return the decoded JSON payload without tabular extraction.
    fields: Optional field list or comma-separated field string applied after extraction.
    as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
    **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

Returns:
    A pandas ``DataFrame`` by default, Python rows when
    ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
    payloads when multi-page fetching is used with ``raw=True``.
```

<h4 id="api-etf-components-all"><code>etf_components_all</code></h4>

- 接口名称：ETF成份列表
- HTTP：`GET`
- Path：`api/v1/market/data/etf-components-all`
- 参数：-
- 来源文档：`ETF成份列表.md`
- 原始接口：`etf_components_all`

```text
ETF成份列表.

Endpoint: ``api/v1/market/data/etf-components-all``.
Method: ``GET``.
Documented endpoint: ``etf_components_all``.

Args:
    raw: Return the decoded JSON payload without tabular extraction.
    fields: Optional field list or comma-separated field string applied after extraction.
    as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
    **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

Returns:
    A pandas ``DataFrame`` by default, Python rows when
    ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
    payloads when multi-page fetching is used with ``raw=True``.
```

<h4 id="api-etf-description-all"><code>etf_description_all</code></h4>

- 接口名称：ETF基础信息
- HTTP：`GET`
- Path：`api/v1/market/data/etf-description-all`
- 参数：-
- 来源文档：`ETF基础信息.md`
- 原始接口：`etf_description_all`

```text
ETF基础信息.

Endpoint: ``api/v1/market/data/etf-description-all``.
Method: ``GET``.
Documented endpoint: ``etf_description_all``.

Args:
    raw: Return the decoded JSON payload without tabular extraction.
    fields: Optional field list or comma-separated field string applied after extraction.
    as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
    **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

Returns:
    A pandas ``DataFrame`` by default, Python rows when
    ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
    payloads when multi-page fetching is used with ``raw=True``.
```

<h4 id="api-etf-fund-export"><code>etf_fund_export</code></h4>

- 接口名称：指数ETF基金导出
- HTTP：`GET`
- Path：`api/v1/market/data/etf/zhitou-etf`
- 参数：`request_id`, `page`, `page_size`
- 来源文档：`指数ETF基金导出.md`
- 原始接口：`etf_fund_export`

```text
指数ETF基金导出.

Endpoint: ``api/v1/market/data/etf/zhitou-etf``.
Method: ``GET``.
Documented endpoint: ``etf_fund_export``.

Args:
    request_id: 请求唯一标识，由调用方生成，原样写入响应 (type: string; required: Y).
    page: Page number, starting from 1. If omitted, the server default is used unless ``limit`` or ``all_pages`` is set.
    page_size: Rows per page. The SDK validates this against the endpoint-specific maximum.
    limit: Maximum number of rows to return. The SDK may fetch multiple pages to satisfy this limit.
    all_pages: Fetch and combine pages until the server reports the last page.
    max_pages: Optional safety cap for ``all_pages``.
    raw: Return the decoded JSON payload without tabular extraction.
    fields: Optional field list or comma-separated field string applied after extraction.
    as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
    **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

Returns:
    A pandas ``DataFrame`` by default, Python rows when
    ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
    payloads when multi-page fetching is used with ``raw=True``.
```

<h4 id="api-etf-pcf-list"><code>etf_pcf_list</code></h4>

- 接口名称：ETF-PCF清单列表
- HTTP：`GET`
- Path：`api/v1/market/data/etf-pcf/etf-pcfs`
- 参数：`date`, `page`, `page_size`
- 来源文档：`ETF-PCF清单列表.md`
- 原始接口：`etf_pcf_list_handler`

```text
ETF-PCF清单列表.

Endpoint: ``api/v1/market/data/etf-pcf/etf-pcfs``.
Method: ``GET``.
Documented endpoint: ``etf_pcf_list_handler``.

Args:
    date: 日期 YYYYMMDD，必填 (type: int; required: Y).
    page: Page number, starting from 1. If omitted, the server default is used unless ``limit`` or ``all_pages`` is set.
    page_size: Rows per page. The SDK validates this against the endpoint-specific maximum.
    limit: Maximum number of rows to return. The SDK may fetch multiple pages to satisfy this limit.
    all_pages: Fetch and combine pages until the server reports the last page.
    max_pages: Optional safety cap for ``all_pages``.
    raw: Return the decoded JSON payload without tabular extraction.
    fields: Optional field list or comma-separated field string applied after extraction.
    as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
    **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

Returns:
    A pandas ``DataFrame`` by default, Python rows when
    ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
    payloads when multi-page fetching is used with ``raw=True``.
```

<h4 id="api-etf-pre"><code>etf_pre</code></h4>

- 接口名称：ETF盘前数据
- HTTP：`GET`
- Path：`api/v1/market/data/etf-pre-data`
- 参数：`date`
- 来源文档：`ETF盘前数据.md`
- 原始接口：`get_etf_pre`

```text
ETF盘前数据.

Endpoint: ``api/v1/market/data/etf-pre-data``.
Method: ``GET``.
Documented endpoint: ``get_etf_pre``.

Args:
    date: 交易日 YYYYMMDD；不传则使用当日（CST） (type: int; required: N).
    raw: Return the decoded JSON payload without tabular extraction.
    fields: Optional field list or comma-separated field string applied after extraction.
    as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
    **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

Returns:
    A pandas ``DataFrame`` by default, Python rows when
    ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
    payloads when multi-page fetching is used with ``raw=True``.
```

<h4 id="api-etf-pre-single"><code>etf_pre_single</code></h4>

- 接口名称：单只ETF盘前数据
- HTTP：`GET`
- Path：`api/v1/market/data/etf-pre-single`
- 参数：`symbol`, `date`
- 来源文档：`单只ETF盘前数据.md`
- 原始接口：`get_etf_pre_single_handler`

```text
单只ETF盘前数据.

Endpoint: ``api/v1/market/data/etf-pre-single``.
Method: ``GET``.
Documented endpoint: ``get_etf_pre_single_handler``.

Args:
    symbol: ETF 标的代码，带交易所后缀，如 510300.XSHG、159915.XSHE (type: string; required: Y).
    date: 交易日 YYYYMMDD；不传则使用当日（CST） (type: int; required: N).
    raw: Return the decoded JSON payload without tabular extraction.
    fields: Optional field list or comma-separated field string applied after extraction.
    as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
    **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

Returns:
    A pandas ``DataFrame`` by default, Python rows when
    ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
    payloads when multi-page fetching is used with ``raw=True``.
```

### 公募基金

<h4 id="api-fund-basicinfo"><code>fund_basicinfo</code></h4>

- 接口名称：基金基础信息
- HTTP：`GET`
- Path：`api/v1/market/data/fund/fund-basicinfo`
- 参数：`institution_code`, `page`, `page_size`
- 来源文档：`基金基础信息.md`
- 原始接口：`get_fund_basicinfo`

```text
基金基础信息.

Endpoint: ``api/v1/market/data/fund/fund-basicinfo``.
Method: ``GET``.
Documented endpoint: ``get_fund_basicinfo``.

Args:
    institution_code: 基金代码 (type: string; required: Y).
    page: Page number, starting from 1. If omitted, the server default is used unless ``limit`` or ``all_pages`` is set.
    page_size: Rows per page. The SDK validates this against the endpoint-specific maximum.
    limit: Maximum number of rows to return. The SDK may fetch multiple pages to satisfy this limit.
    all_pages: Fetch and combine pages until the server reports the last page.
    max_pages: Optional safety cap for ``all_pages``.
    raw: Return the decoded JSON payload without tabular extraction.
    fields: Optional field list or comma-separated field string applied after extraction.
    as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
    **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

Returns:
    A pandas ``DataFrame`` by default, Python rows when
    ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
    payloads when multi-page fetching is used with ``raw=True``.
```

<h4 id="api-fund-cal-return"><code>fund_cal_return</code></h4>

- 接口名称：基金收益
- HTTP：`GET`
- Path：`api/v1/market/data/fund/fund-cal-return`
- 参数：`institution_code`, `cal-type`
- 来源文档：`基金收益.md`
- 原始接口：`get_fund_cal_return`

```text
基金收益.

Endpoint: ``api/v1/market/data/fund/fund-cal-return``.
Method: ``GET``.
Documented endpoint: ``get_fund_cal_return``.

Args:
    institution_code: 基金代码（6位数字） (type: string; required: Y).
    cal_type: 查询区间：1M / 3M / 6M / 1Y / 3Y / 5Y / YTD（请求字段名为 `cal-type`） (type: string; required: Y). Request key: ``cal-type``.
    raw: Return the decoded JSON payload without tabular extraction.
    fields: Optional field list or comma-separated field string applied after extraction.
    as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
    **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

Returns:
    A pandas ``DataFrame`` by default, Python rows when
    ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
    payloads when multi-page fetching is used with ``raw=True``.
```

<h4 id="api-fund-nav"><code>fund_nav</code></h4>

- 接口名称：基金净值
- HTTP：`GET`
- Path：`api/v1/market/data/fund/fund-nav`
- 参数：`institution_code`, `page`, `page_size`
- 来源文档：`基金净值.md`
- 原始接口：`get_fund_nav`

```text
基金净值.

Endpoint: ``api/v1/market/data/fund/fund-nav``.
Method: ``GET``.
Documented endpoint: ``get_fund_nav``.

Args:
    institution_code: 基金代码 (type: string; required: Y).
    page: Page number, starting from 1. If omitted, the server default is used unless ``limit`` or ``all_pages`` is set.
    page_size: Rows per page. The SDK validates this against the endpoint-specific maximum.
    limit: Maximum number of rows to return. The SDK may fetch multiple pages to satisfy this limit.
    all_pages: Fetch and combine pages until the server reports the last page.
    max_pages: Optional safety cap for ``all_pages``.
    raw: Return the decoded JSON payload without tabular extraction.
    fields: Optional field list or comma-separated field string applied after extraction.
    as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
    **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

Returns:
    A pandas ``DataFrame`` by default, Python rows when
    ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
    payloads when multi-page fetching is used with ``raw=True``.
```

<h4 id="api-fund-overview"><code>fund_overview</code></h4>

- 接口名称：基金总览
- HTTP：`GET`
- Path：`api/v1/market/data/fund/fund-overview`
- 参数：`page`, `page_size`
- 来源文档：`基金总览.md`
- 原始接口：`get_fund_overview`

```text
基金总览.

Endpoint: ``api/v1/market/data/fund/fund-overview``.
Method: ``GET``.
Documented endpoint: ``get_fund_overview``.

Args:
    page: Page number, starting from 1. If omitted, the server default is used unless ``limit`` or ``all_pages`` is set.
    page_size: Rows per page. The SDK validates this against the endpoint-specific maximum.
    limit: Maximum number of rows to return. The SDK may fetch multiple pages to satisfy this limit.
    all_pages: Fetch and combine pages until the server reports the last page.
    max_pages: Optional safety cap for ``all_pages``.
    raw: Return the decoded JSON payload without tabular extraction.
    fields: Optional field list or comma-separated field string applied after extraction.
    as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
    **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

Returns:
    A pandas ``DataFrame`` by default, Python rows when
    ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
    payloads when multi-page fetching is used with ``raw=True``.
```

<h4 id="api-fund-support-symbols"><code>fund_support_symbols</code></h4>

- 接口名称：基金支持标的
- HTTP：`GET`
- Path：`api/v1/market/data/fund/fund-support-symbols`
- 参数：`page`, `page_size`
- 来源文档：`基金支持标的.md`
- 原始接口：`get_fund_support_symbols`

```text
基金支持标的.

Endpoint: ``api/v1/market/data/fund/fund-support-symbols``.
Method: ``GET``.
Documented endpoint: ``get_fund_support_symbols``.

Args:
    page: Page number, starting from 1. If omitted, the server default is used unless ``limit`` or ``all_pages`` is set.
    page_size: Rows per page. The SDK validates this against the endpoint-specific maximum.
    limit: Maximum number of rows to return. The SDK may fetch multiple pages to satisfy this limit.
    all_pages: Fetch and combine pages until the server reports the last page.
    max_pages: Optional safety cap for ``all_pages``.
    raw: Return the decoded JSON payload without tabular extraction.
    fields: Optional field list or comma-separated field string applied after extraction.
    as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
    **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

Returns:
    A pandas ``DataFrame`` by default, Python rows when
    ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
    payloads when multi-page fetching is used with ``raw=True``.
```

### 期货数据

<h4 id="api-china-futures-base-data"><code>china_futures_base_data</code></h4>

- 接口名称：中国期货基础数据
- HTTP：`GET`
- Path：`api/v1/market/data/futures/futures-base-data`
- 参数：`trade_date`, `symbol`
- 来源文档：`中国期货基础数据.md`
- 原始接口：`get_china_futures_base_data_handler`

```text
中国期货基础数据.

Endpoint: ``api/v1/market/data/futures/futures-base-data``.
Method: ``GET``.
Documented endpoint: ``get_china_futures_base_data_handler``.

Args:
    trade_date: 交易日 YYYYMMDD；不传则使用前一交易日（CST） (type: int; required: N).
    symbol: WIND 合约全码如 A2605.DCE；大小写不敏感；不传或空表示该日全部 (type: string; required: N).
    raw: Return the decoded JSON payload without tabular extraction.
    fields: Optional field list or comma-separated field string applied after extraction.
    as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
    **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

Returns:
    A pandas ``DataFrame`` by default, Python rows when
    ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
    payloads when multi-page fetching is used with ``raw=True``.
```

<h4 id="api-china-futures-lists"><code>china_futures_lists</code></h4>

- 接口名称：中国期货列表
- HTTP：`GET`
- Path：`api/v1/market/data/futures/futures-lists`
- 参数：`trade_date`
- 来源文档：`中国期货列表.md`
- 原始接口：`get_china_futures_lists_handler`

```text
中国期货列表.

Endpoint: ``api/v1/market/data/futures/futures-lists``.
Method: ``GET``.
Documented endpoint: ``get_china_futures_lists_handler``.

Args:
    trade_date: 交易日 YYYYMMDD；不传则使用前一交易日（CST） (type: int; required: N).
    raw: Return the decoded JSON payload without tabular extraction.
    fields: Optional field list or comma-separated field string applied after extraction.
    as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
    **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

Returns:
    A pandas ``DataFrame`` by default, Python rows when
    ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
    payloads when multi-page fetching is used with ``raw=True``.
```

<h4 id="api-eastmoney-futures-position"><code>eastmoney_futures_position</code></h4>

- 接口名称：东方财富期货持仓
- HTTP：`GET`
- Path：`api/v1/market/data/eastmoney-futures-position`
- 参数：`exchange`, `variety_code`, `contract_code`, `trade_date`, `start_date`, `end_date`, `member_name_abbr`, `page`, `page_size`
- 来源文档：`东方财富期货持仓.md`
- 原始接口：`get_eastmoney_futures_position`

```text
东方财富期货持仓.

Endpoint: ``api/v1/market/data/eastmoney-futures-position``.
Method: ``GET``.
Documented endpoint: ``get_eastmoney_futures_position``.

Args:
    exchange: 交易所代码：shfe / dce / czce / cffex / ine / gfe (type: string; required: N).
    variety_code: 品种代码，如 cu / au / al / IF (type: string; required: N).
    contract_code: 合约代码，如 CU2607 / AU2608 (type: string; required: N).
    trade_date: 交易日 YYYYMMDD；与 start_date/end_date 互斥 (type: string; required: N).
    start_date: 区间起始日 YYYYMMDD；需与 end_date 同时提供 (type: string; required: N).
    end_date: 区间结束日 YYYYMMDD；需与 start_date 同时提供 (type: string; required: N).
    member_name_abbr: 会员简称 (type: string; required: N).
    page: Page number, starting from 1. If omitted, the server default is used unless ``limit`` or ``all_pages`` is set.
    page_size: Rows per page. The SDK validates this against the endpoint-specific maximum.
    limit: Maximum number of rows to return. The SDK may fetch multiple pages to satisfy this limit.
    all_pages: Fetch and combine pages until the server reports the last page.
    max_pages: Optional safety cap for ``all_pages``.
    raw: Return the decoded JSON payload without tabular extraction.
    fields: Optional field list or comma-separated field string applied after extraction.
    as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
    **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

Returns:
    A pandas ``DataFrame`` by default, Python rows when
    ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
    payloads when multi-page fetching is used with ``raw=True``.
```

<h4 id="api-futures-contract-kline"><code>futures_contract_kline</code></h4>

- 接口名称：期货合约K线
- HTTP：`GET`
- Path：`api/v1/market/data/futures/kline`
- 参数：`symbol`, `interval`, `start`, `end`, `limit`
- 来源文档：`期货合约K线.md`
- 原始接口：`futures_contract_kline`

```text
期货合约K线.

Endpoint: ``api/v1/market/data/futures/kline``.
Method: ``GET``.
Documented endpoint: ``futures_contract_kline``.

Args:
    symbol: WIND 合约全码，如 A2605.DCE (type: string; required: Y).
    interval: 周期，默认 1min；可选 1min/5min/15min/30min/60min/daily/weekly/monthly/quarterly/yearly (type: string; required: N).
    start: 开始时间戳（毫秒）；与 end 跨度 ≤3 天；仅 start 表示 [start,+∞) (type: int64; required: N).
    end: 结束时间戳（毫秒，闭区间）；须与 start 同时传入，禁止只传 end (type: int64; required: N).
    limit: 最大返回条数，默认 500 (type: int; required: N).
    raw: Return the decoded JSON payload without tabular extraction.
    fields: Optional field list or comma-separated field string applied after extraction.
    as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
    **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

Returns:
    A pandas ``DataFrame`` by default, Python rows when
    ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
    payloads when multi-page fetching is used with ``raw=True``.
```

<h4 id="api-major-contract"><code>major_contract</code></h4>

- 接口名称：重大合同
- HTTP：`GET`
- Path：`api/v1/market/data/corporate/contract`
- 参数：`start_date`, `end_date`
- 来源文档：`重大合同.md`
- 原始接口：`major_contract`

```text
重大合同.

Endpoint: ``api/v1/market/data/corporate/contract``.
Method: ``GET``.
Documented endpoint: ``major_contract``.

Args:
    start_date: 起始日期（YYYYMMDD），区间跨度 ≤ 3 天 (type: string; required: Y).
    end_date: 结束日期（YYYYMMDD），区间跨度 ≤ 3 天 (type: string; required: Y).
    raw: Return the decoded JSON payload without tabular extraction.
    fields: Optional field list or comma-separated field string applied after extraction.
    as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
    **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

Returns:
    A pandas ``DataFrame`` by default, Python rows when
    ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
    payloads when multi-page fetching is used with ``raw=True``.
```

<h4 id="api-major-contract-by-symbol"><code>major_contract_by_symbol</code></h4>

- 接口名称：重大合同按标的
- HTTP：`GET`
- Path：`api/v1/market/data/corporate/contract/by-symbol`
- 参数：`symbol`, `page`, `page_size`
- 来源文档：`重大合同按标的.md`
- 原始接口：`major_contract_by_symbol`

```text
重大合同按标的.

Endpoint: ``api/v1/market/data/corporate/contract/by-symbol``.
Method: ``GET``.
Documented endpoint: ``major_contract_by_symbol``.

Args:
    symbol: 证券代码（标的） (type: string; required: Y).
    page: Page number, starting from 1. If omitted, the server default is used unless ``limit`` or ``all_pages`` is set.
    page_size: Rows per page. The SDK validates this against the endpoint-specific maximum.
    limit: Maximum number of rows to return. The SDK may fetch multiple pages to satisfy this limit.
    all_pages: Fetch and combine pages until the server reports the last page.
    max_pages: Optional safety cap for ``all_pages``.
    raw: Return the decoded JSON payload without tabular extraction.
    fields: Optional field list or comma-separated field string applied after extraction.
    as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
    **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

Returns:
    A pandas ``DataFrame`` by default, Python rows when
    ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
    payloads when multi-page fetching is used with ``raw=True``.
```

<h4 id="api-major-contract-summary"><code>major_contract_summary</code></h4>

- 接口名称：重大合同汇总
- HTTP：`GET`
- Path：`api/v1/market/data/corporate/contract/summary`
- 参数：`page`, `page_size`
- 来源文档：`重大合同汇总.md`
- 原始接口：`major_contract_summary`

```text
重大合同汇总.

Endpoint: ``api/v1/market/data/corporate/contract/summary``.
Method: ``GET``.
Documented endpoint: ``major_contract_summary``.

Args:
    page: Page number, starting from 1. If omitted, the server default is used unless ``limit`` or ``all_pages`` is set.
    page_size: Rows per page. The SDK validates this against the endpoint-specific maximum.
    limit: Maximum number of rows to return. The SDK may fetch multiple pages to satisfy this limit.
    all_pages: Fetch and combine pages until the server reports the last page.
    max_pages: Optional safety cap for ``all_pages``.
    raw: Return the decoded JSON payload without tabular extraction.
    fields: Optional field list or comma-separated field string applied after extraction.
    as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
    **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

Returns:
    A pandas ``DataFrame`` by default, Python rows when
    ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
    payloads when multi-page fetching is used with ``raw=True``.
```

<h4 id="api-eastmoney-futures-strange"><code>eastmoney_futures_strange</code></h4>

- 接口名称：东方财富期货持仓
- HTTP：`GET`
- Path：`api/v1/market/data/eastmoney-futures-position`
- 参数：`exchange`, `variety_code`, `contract_code`, `trade_date`, `start_date`, `end_date`, `member_name_abbr`, `page`, `page_size`
- 来源文档：`东方财富期货持仓.md`
- 原始接口：`get_eastmoney_futures_position`

```text
东方财富期货持仓.

Endpoint: ``api/v1/market/data/eastmoney-futures-position``.
Method: ``GET``.
Documented endpoint: ``get_eastmoney_futures_position``.

Args:
    exchange: 交易所代码：shfe / dce / czce / cffex / ine / gfe (type: string; required: N).
    variety_code: 品种代码，如 cu / au / al / IF (type: string; required: N).
    contract_code: 合约代码，如 CU2607 / AU2608 (type: string; required: N).
    trade_date: 交易日 YYYYMMDD；与 start_date/end_date 互斥 (type: string; required: N).
    start_date: 区间起始日 YYYYMMDD；需与 end_date 同时提供 (type: string; required: N).
    end_date: 区间结束日 YYYYMMDD；需与 start_date 同时提供 (type: string; required: N).
    member_name_abbr: 会员简称 (type: string; required: N).
    page: Page number, starting from 1. If omitted, the server default is used unless ``limit`` or ``all_pages`` is set.
    page_size: Rows per page. The SDK validates this against the endpoint-specific maximum.
    limit: Maximum number of rows to return. The SDK may fetch multiple pages to satisfy this limit.
    all_pages: Fetch and combine pages until the server reports the last page.
    max_pages: Optional safety cap for ``all_pages``.
    raw: Return the decoded JSON payload without tabular extraction.
    fields: Optional field list or comma-separated field string applied after extraction.
    as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
    **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

Returns:
    A pandas ``DataFrame`` by default, Python rows when
    ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
    payloads when multi-page fetching is used with ``raw=True``.
```

<h4 id="api-futures-kline"><code>futures_kline</code></h4>

- 接口名称：期货合约K线
- HTTP：`GET`
- Path：`api/v1/market/data/futures/kline`
- 参数：`symbol`, `interval`, `start`, `end`, `limit`
- 来源文档：`期货合约K线.md`
- 原始接口：`futures_contract_kline`

```text
期货合约K线.

Endpoint: ``api/v1/market/data/futures/kline``.
Method: ``GET``.
Documented endpoint: ``futures_contract_kline``.

Args:
    symbol: WIND 合约全码，如 A2605.DCE (type: string; required: Y).
    interval: 周期，默认 1min；可选 1min/5min/15min/30min/60min/daily/weekly/monthly/quarterly/yearly (type: string; required: N).
    start: 开始时间戳（毫秒）；与 end 跨度 ≤3 天；仅 start 表示 [start,+∞) (type: int64; required: N).
    end: 结束时间戳（毫秒，闭区间）；须与 start 同时传入，禁止只传 end (type: int64; required: N).
    limit: 最大返回条数，默认 500 (type: int; required: N).
    raw: Return the decoded JSON payload without tabular extraction.
    fields: Optional field list or comma-separated field string applied after extraction.
    as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
    **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

Returns:
    A pandas ``DataFrame`` by default, Python rows when
    ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
    payloads when multi-page fetching is used with ``raw=True``.
```

### 债券专题

<h4 id="api-cb-base-data"><code>cb_base_data</code></h4>

- 接口名称：可转债基础数据
- HTTP：`GET`
- Path：`api/v1/market/data/cb/cb-base-data`
- 参数：`symbol_code`
- 来源文档：`可转债基础数据.md`
- 原始接口：`get_cb_base_data_handler`

```text
可转债基础数据.

Endpoint: ``api/v1/market/data/cb/cb-base-data``.
Method: ``GET``.
Documented endpoint: ``get_cb_base_data_handler``.

Args:
    symbol_code: 转债代码 (type: string; required: Y).
    raw: Return the decoded JSON payload without tabular extraction.
    fields: Optional field list or comma-separated field string applied after extraction.
    as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
    **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

Returns:
    A pandas ``DataFrame`` by default, Python rows when
    ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
    payloads when multi-page fetching is used with ``raw=True``.
```

<h4 id="api-cb-lists"><code>cb_lists</code></h4>

- 接口名称：可转债列表
- HTTP：`GET`
- Path：`api/v1/market/data/cb/cb-lists`
- 参数：-
- 来源文档：`可转债列表.md`
- 原始接口：`get_cb_lists_handler`

```text
可转债列表.

Endpoint: ``api/v1/market/data/cb/cb-lists``.
Method: ``GET``.
Documented endpoint: ``get_cb_lists_handler``.

Args:
    raw: Return the decoded JSON payload without tabular extraction.
    fields: Optional field list or comma-separated field string applied after extraction.
    as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
    **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

Returns:
    A pandas ``DataFrame`` by default, Python rows when
    ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
    payloads when multi-page fetching is used with ``raw=True``.
```

### 宏观经济

<h4 id="api-baidu-financial-calendar"><code>baidu_financial_calendar</code></h4>

- 接口名称：百度财经日历
- HTTP：`GET`
- Path：`api/v1/market/data/finance/financial-calendar/baidu`
- 参数：`start_date`, `end_date`, `category`, `page`, `page_size`
- 来源文档：`百度财经日历.md`
- 原始接口：`baidu_financial_calendar`

```text
百度财经日历.

Endpoint: ``api/v1/market/data/finance/financial-calendar/baidu``.
Method: ``GET``.
Documented endpoint: ``baidu_financial_calendar``.

Args:
    start_date: 起始日期 (type: string; required: Y).
    end_date: 结束日期（与 start_date 间隔 ≤ 3 天） (type: string; required: Y).
    category: 筛选大类：`economic` / `ipo` / `report_time` / `trade_reminder`；不传返回全部 (type: string; required: N).
    page: Page number, starting from 1. If omitted, the server default is used unless ``limit`` or ``all_pages`` is set.
    page_size: Rows per page. The SDK validates this against the endpoint-specific maximum.
    limit: Maximum number of rows to return. The SDK may fetch multiple pages to satisfy this limit.
    all_pages: Fetch and combine pages until the server reports the last page.
    max_pages: Optional safety cap for ``all_pages``.
    raw: Return the decoded JSON payload without tabular extraction.
    fields: Optional field list or comma-separated field string applied after extraction.
    as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
    **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

Returns:
    A pandas ``DataFrame`` by default, Python rows when
    ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
    payloads when multi-page fetching is used with ``raw=True``.
```

<h4 id="api-consumer-credit-monthly"><code>consumer_credit_monthly</code></h4>

- 接口名称：社融信贷
- HTTP：`GET`
- Path：`api/v1/market/data/economic/china-credit-loans`
- 参数：-
- 来源文档：`社融信贷.md`
- 原始接口：`consumer_credit_monthly`

```text
社融信贷.

Endpoint: ``api/v1/market/data/economic/china-credit-loans``.
Method: ``GET``.
Documented endpoint: ``consumer_credit_monthly``.

Args:
    raw: Return the decoded JSON payload without tabular extraction.
    fields: Optional field list or comma-separated field string applied after extraction.
    as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
    **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

Returns:
    A pandas ``DataFrame`` by default, Python rows when
    ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
    payloads when multi-page fetching is used with ``raw=True``.
```

<h4 id="api-consumer-customs-trade-monthly"><code>consumer_customs_trade_monthly</code></h4>

- 接口名称：进出口
- HTTP：`GET`
- Path：`api/v1/market/data/economic/china-customs-trade`
- 参数：-
- 来源文档：`进出口.md`
- 原始接口：`consumer_customs_trade_monthly`

```text
进出口.

Endpoint: ``api/v1/market/data/economic/china-customs-trade``.
Method: ``GET``.
Documented endpoint: ``consumer_customs_trade_monthly``.

Args:
    raw: Return the decoded JSON payload without tabular extraction.
    fields: Optional field list or comma-separated field string applied after extraction.
    as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
    **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

Returns:
    A pandas ``DataFrame`` by default, Python rows when
    ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
    payloads when multi-page fetching is used with ``raw=True``.
```

<h4 id="api-consumer-fiscal-revenue-monthly"><code>consumer_fiscal_revenue_monthly</code></h4>

- 接口名称：财政收入
- HTTP：`GET`
- Path：`api/v1/market/data/economic/china-fiscal-revenue`
- 参数：-
- 来源文档：`财政收入.md`
- 原始接口：`consumer_fiscal_revenue_monthly`

```text
财政收入.

Endpoint: ``api/v1/market/data/economic/china-fiscal-revenue``.
Method: ``GET``.
Documented endpoint: ``consumer_fiscal_revenue_monthly``.

Args:
    raw: Return the decoded JSON payload without tabular extraction.
    fields: Optional field list or comma-separated field string applied after extraction.
    as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
    **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

Returns:
    A pandas ``DataFrame`` by default, Python rows when
    ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
    payloads when multi-page fetching is used with ``raw=True``.
```

<h4 id="api-consumer-fixed-asset-monthly"><code>consumer_fixed_asset_monthly</code></h4>

- 接口名称：固定资产投资
- HTTP：`GET`
- Path：`api/v1/market/data/economic/china-fixed-asset-investment`
- 参数：-
- 来源文档：`固定资产投资.md`
- 原始接口：`consumer_fixed_asset_monthly`

```text
固定资产投资.

Endpoint: ``api/v1/market/data/economic/china-fixed-asset-investment``.
Method: ``GET``.
Documented endpoint: ``consumer_fixed_asset_monthly``.

Args:
    raw: Return the decoded JSON payload without tabular extraction.
    fields: Optional field list or comma-separated field string applied after extraction.
    as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
    **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

Returns:
    A pandas ``DataFrame`` by default, Python rows when
    ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
    payloads when multi-page fetching is used with ``raw=True``.
```

<h4 id="api-consumer-gdp-quarterly"><code>consumer_gdp_quarterly</code></h4>

- 接口名称：GDP
- HTTP：`GET`
- Path：`api/v1/market/data/economic/china-gdp`
- 参数：-
- 来源文档：`GDP.md`
- 原始接口：`consumer_gdp_quarterly`

```text
GDP.

Endpoint: ``api/v1/market/data/economic/china-gdp``.
Method: ``GET``.
Documented endpoint: ``consumer_gdp_quarterly``.

Args:
    raw: Return the decoded JSON payload without tabular extraction.
    fields: Optional field list or comma-separated field string applied after extraction.
    as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
    **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

Returns:
    A pandas ``DataFrame`` by default, Python rows when
    ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
    payloads when multi-page fetching is used with ``raw=True``.
```

<h4 id="api-consumer-industrial-added-value-monthly"><code>consumer_industrial_added_value_monthly</code></h4>

- 接口名称：工业增加值
- HTTP：`GET`
- Path：`api/v1/market/data/economic/china-industrial-added-value`
- 参数：-
- 来源文档：`工业增加值.md`
- 原始接口：`consumer_industrial_added_value_monthly`

```text
工业增加值.

Endpoint: ``api/v1/market/data/economic/china-industrial-added-value``.
Method: ``GET``.
Documented endpoint: ``consumer_industrial_added_value_monthly``.

Args:
    raw: Return the decoded JSON payload without tabular extraction.
    fields: Optional field list or comma-separated field string applied after extraction.
    as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
    **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

Returns:
    A pandas ``DataFrame`` by default, Python rows when
    ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
    payloads when multi-page fetching is used with ``raw=True``.
```

<h4 id="api-consumer-money-supply-monthly"><code>consumer_money_supply_monthly</code></h4>

- 接口名称：货币供应
- HTTP：`GET`
- Path：`api/v1/market/data/economic/china-money-supply`
- 参数：-
- 来源文档：`货币供应.md`
- 原始接口：`consumer_money_supply_monthly`

```text
货币供应.

Endpoint: ``api/v1/market/data/economic/china-money-supply``.
Method: ``GET``.
Documented endpoint: ``consumer_money_supply_monthly``.

Args:
    raw: Return the decoded JSON payload without tabular extraction.
    fields: Optional field list or comma-separated field string applied after extraction.
    as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
    **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

Returns:
    A pandas ``DataFrame`` by default, Python rows when
    ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
    payloads when multi-page fetching is used with ``raw=True``.
```

<h4 id="api-consumer-pmi-monthly"><code>consumer_pmi_monthly</code></h4>

- 接口名称：PMI
- HTTP：`GET`
- Path：`api/v1/market/data/economic/china-pmi`
- 参数：-
- 来源文档：`PMI.md`
- 原始接口：`consumer_pmi_monthly`

```text
PMI.

Endpoint: ``api/v1/market/data/economic/china-pmi``.
Method: ``GET``.
Documented endpoint: ``consumer_pmi_monthly``.

Args:
    raw: Return the decoded JSON payload without tabular extraction.
    fields: Optional field list or comma-separated field string applied after extraction.
    as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
    **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

Returns:
    A pandas ``DataFrame`` by default, Python rows when
    ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
    payloads when multi-page fetching is used with ``raw=True``.
```

<h4 id="api-consumer-ppi-monthly"><code>consumer_ppi_monthly</code></h4>

- 接口名称：PPI
- HTTP：`GET`
- Path：`api/v1/market/data/economic/china-ppi`
- 参数：-
- 来源文档：`PPI.md`
- 原始接口：`consumer_ppi_monthly`

```text
PPI.

Endpoint: ``api/v1/market/data/economic/china-ppi``.
Method: ``GET``.
Documented endpoint: ``consumer_ppi_monthly``.

Args:
    raw: Return the decoded JSON payload without tabular extraction.
    fields: Optional field list or comma-separated field string applied after extraction.
    as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
    **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

Returns:
    A pandas ``DataFrame`` by default, Python rows when
    ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
    payloads when multi-page fetching is used with ``raw=True``.
```

<h4 id="api-consumer-price-index-monthly"><code>consumer_price_index_monthly</code></h4>

- 接口名称：CPI
- HTTP：`GET`
- Path：`api/v1/market/data/economic/china-cpi`
- 参数：-
- 来源文档：`CPI.md`
- 原始接口：`consumer_price_index_monthly`

```text
CPI.

Endpoint: ``api/v1/market/data/economic/china-cpi``.
Method: ``GET``.
Documented endpoint: ``consumer_price_index_monthly``.

Args:
    raw: Return the decoded JSON payload without tabular extraction.
    fields: Optional field list or comma-separated field string applied after extraction.
    as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
    **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

Returns:
    A pandas ``DataFrame`` by default, Python rows when
    ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
    payloads when multi-page fetching is used with ``raw=True``.
```

<h4 id="api-consumer-retail-sales-monthly"><code>consumer_retail_sales_monthly</code></h4>

- 接口名称：社零
- HTTP：`GET`
- Path：`api/v1/market/data/economic/china-retail-sales`
- 参数：-
- 来源文档：`社零.md`
- 原始接口：`consumer_retail_sales_monthly`

```text
社零.

Endpoint: ``api/v1/market/data/economic/china-retail-sales``.
Method: ``GET``.
Documented endpoint: ``consumer_retail_sales_monthly``.

Args:
    raw: Return the decoded JSON payload without tabular extraction.
    fields: Optional field list or comma-separated field string applied after extraction.
    as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
    **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

Returns:
    A pandas ``DataFrame`` by default, Python rows when
    ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
    payloads when multi-page fetching is used with ``raw=True``.
```

<h4 id="api-lpr-monthly"><code>lpr_monthly</code></h4>

- 接口名称：LPR
- HTTP：`GET`
- Path：`api/v1/market/data/economic/china-lpr`
- 参数：-
- 来源文档：`LPR.md`
- 原始接口：`lpr_monthly`

```text
LPR.

Endpoint: ``api/v1/market/data/economic/china-lpr``.
Method: ``GET``.
Documented endpoint: ``lpr_monthly``.

Args:
    raw: Return the decoded JSON payload without tabular extraction.
    fields: Optional field list or comma-separated field string applied after extraction.
    as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
    **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

Returns:
    A pandas ``DataFrame`` by default, Python rows when
    ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
    payloads when multi-page fetching is used with ``raw=True``.
```

<h4 id="api-reserve-ratio-monthly"><code>reserve_ratio_monthly</code></h4>

- 接口名称：存款准备金率
- HTTP：`GET`
- Path：`api/v1/market/data/economic/china-reserve-ratio`
- 参数：-
- 来源文档：`存款准备金率.md`
- 原始接口：`reserve_ratio_monthly`

```text
存款准备金率.

Endpoint: ``api/v1/market/data/economic/china-reserve-ratio``.
Method: ``GET``.
Documented endpoint: ``reserve_ratio_monthly``.

Args:
    raw: Return the decoded JSON payload without tabular extraction.
    fields: Optional field list or comma-separated field string applied after extraction.
    as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
    **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

Returns:
    A pandas ``DataFrame`` by default, Python rows when
    ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
    payloads when multi-page fetching is used with ``raw=True``.
```

<h4 id="api-tax-revenue-monthly"><code>tax_revenue_monthly</code></h4>

- 接口名称：税收
- HTTP：`GET`
- Path：`api/v1/market/data/economic/china-tax-revenue`
- 参数：-
- 来源文档：`税收.md`
- 原始接口：`tax_revenue_monthly`

```text
税收.

Endpoint: ``api/v1/market/data/economic/china-tax-revenue``.
Method: ``GET``.
Documented endpoint: ``tax_revenue_monthly``.

Args:
    raw: Return the decoded JSON payload without tabular extraction.
    fields: Optional field list or comma-separated field string applied after extraction.
    as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
    **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

Returns:
    A pandas ``DataFrame`` by default, Python rows when
    ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
    payloads when multi-page fetching is used with ``raw=True``.
```

<h4 id="api-us-economic"><code>us_economic</code></h4>

- 接口名称：美国经济指标
- HTTP：`GET`
- Path：`api/v1/market/data/economic/us-economic`
- 参数：`type`
- 来源文档：`美国经济指标.md`
- 原始接口：`us_economic`

```text
美国经济指标.

Endpoint: ``api/v1/market/data/economic/us-economic``.
Method: ``GET``.
Documented endpoint: ``us_economic``.

Args:
    type: 指标类型，枚举值见下表 (type: string; required: Y).
    raw: Return the decoded JSON payload without tabular extraction.
    fields: Optional field list or comma-separated field string applied after extraction.
    as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
    **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

Returns:
    A pandas ``DataFrame`` by default, Python rows when
    ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
    payloads when multi-page fetching is used with ``raw=True``.
```

<h4 id="api-wallstreetcn-financial-calendar"><code>wallstreetcn_financial_calendar</code></h4>

- 接口名称：华尔街见闻财经日历
- HTTP：`GET`
- Path：`api/v1/market/data/finance/financial-calendar/wallstreetcn`
- 参数：`start_date`, `end_date`, `page`, `page_size`
- 来源文档：`华尔街见闻财经日历.md`
- 原始接口：`wallstreetcn_financial_calendar`

```text
华尔街见闻财经日历.

Endpoint: ``api/v1/market/data/finance/financial-calendar/wallstreetcn``.
Method: ``GET``.
Documented endpoint: ``wallstreetcn_financial_calendar``.

Args:
    start_date: 起始日期 (type: string; required: Y).
    end_date: 结束日期（与 start_date 间隔 ≤ 3 天） (type: string; required: Y).
    page: Page number, starting from 1. If omitted, the server default is used unless ``limit`` or ``all_pages`` is set.
    page_size: Rows per page. The SDK validates this against the endpoint-specific maximum.
    limit: Maximum number of rows to return. The SDK may fetch multiple pages to satisfy this limit.
    all_pages: Fetch and combine pages until the server reports the last page.
    max_pages: Optional safety cap for ``all_pages``.
    raw: Return the decoded JSON payload without tabular extraction.
    fields: Optional field list or comma-separated field string applied after extraction.
    as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
    **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

Returns:
    A pandas ``DataFrame`` by default, Python rows when
    ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
    payloads when multi-page fetching is used with ``raw=True``.
```

### 大模型语料

<h4 id="api-semantic-search-news"><code>semantic_search_news</code></h4>

- 接口名称：新闻语义搜索
- HTTP：`GET`
- Path：`api/v1/market/data/semantic-search-news`
- 参数：`query`, `limit`, `year`, `start_time`, `end_time`
- 来源文档：`新闻语义搜索.md`
- 原始接口：`semantic_search_news_handler`

```text
新闻语义搜索.

Endpoint: ``api/v1/market/data/semantic-search-news``.
Method: ``GET``.
Documented endpoint: ``semantic_search_news_handler``.

Args:
    query: 搜索文字 (type: string; required: Y).
    limit: 返回条数，默认由服务端决定 (type: int; required: N).
    year: 年份，限定搜索范围 (type: int; required: N).
    start_time: 起始时间（带时区），与 end_time 同传时区间不超过 3 天 (type: datetime; required: N).
    end_time: 结束时间（带时区），与 start_time 同传时区间不超过 3 天 (type: datetime; required: N).
    raw: Return the decoded JSON payload without tabular extraction.
    fields: Optional field list or comma-separated field string applied after extraction.
    as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
    **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

Returns:
    A pandas ``DataFrame`` by default, Python rows when
    ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
    payloads when multi-page fetching is used with ``raw=True``.
```

<h4 id="api-shareholders-meeting"><code>shareholders_meeting</code></h4>

- 接口名称：股东大会
- HTTP：`GET`
- Path：`api/v1/market/data/corporate/meeting`
- 参数：`page`, `page_size`
- 来源文档：`股东大会.md`
- 原始接口：`shareholders_meeting`

```text
股东大会.

Endpoint: ``api/v1/market/data/corporate/meeting``.
Method: ``GET``.
Documented endpoint: ``shareholders_meeting``.

Args:
    page: Page number, starting from 1. If omitted, the server default is used unless ``limit`` or ``all_pages`` is set.
    page_size: Rows per page. The SDK validates this against the endpoint-specific maximum.
    limit: Maximum number of rows to return. The SDK may fetch multiple pages to satisfy this limit.
    all_pages: Fetch and combine pages until the server reports the last page.
    max_pages: Optional safety cap for ``all_pages``.
    raw: Return the decoded JSON payload without tabular extraction.
    fields: Optional field list or comma-separated field string applied after extraction.
    as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
    **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

Returns:
    A pandas ``DataFrame`` by default, Python rows when
    ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
    payloads when multi-page fetching is used with ``raw=True``.
```

<h4 id="api-stock-announcements"><code>stock_announcements</code></h4>

- 接口名称：公告列表
- HTTP：`GET`
- Path：`api/v1/market/data/announcements/stock-announcements`
- 参数：`stock_code`, `start_date`, `end_date`, `type`, `page`, `page_size`
- 来源文档：`公告列表.md`
- 原始接口：`stock_announcements`

```text
公告列表.

Endpoint: ``api/v1/market/data/announcements/stock-announcements``.
Method: ``GET``.
Documented endpoint: ``stock_announcements``.

Args:
    stock_code: 证券代码（按标的查询时必填） (type: string; required: N).
    start_date: 开始日期 YYYYMMDD（按日期范围查询时必填） (type: string; required: N).
    end_date: 结束日期 YYYYMMDD，不填默认当前时间 (type: string; required: N).
    type: 查询类型，当前只支持 `stock` (type: string; required: Y).
    page: Page number, starting from 1. If omitted, the server default is used unless ``limit`` or ``all_pages`` is set.
    page_size: Rows per page. The SDK validates this against the endpoint-specific maximum.
    limit: Maximum number of rows to return. The SDK may fetch multiple pages to satisfy this limit.
    all_pages: Fetch and combine pages until the server reports the last page.
    max_pages: Optional safety cap for ``all_pages``.
    raw: Return the decoded JSON payload without tabular extraction.
    fields: Optional field list or comma-separated field string applied after extraction.
    as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
    **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

Returns:
    A pandas ``DataFrame`` by default, Python rows when
    ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
    payloads when multi-page fetching is used with ``raw=True``.
```

<h4 id="api-stock-reports"><code>stock_reports</code></h4>

- 接口名称：研报列表
- HTTP：`GET`
- Path：`api/v1/market/data/report/stock-reports`
- 参数：`stock_code`, `start_date`, `end_date`, `type`, `page`, `page_size`
- 来源文档：`研报列表.md`
- 原始接口：`stock_reports`

```text
研报列表.

Endpoint: ``api/v1/market/data/report/stock-reports``.
Method: ``GET``.
Documented endpoint: ``stock_reports``.

Args:
    stock_code: 证券代码（按标的查询时必填） (type: string; required: N).
    start_date: 开始日期 YYYYMMDD（按日期范围查询时必填） (type: string; required: N).
    end_date: 结束日期 YYYYMMDD，不填默认当前时间 (type: string; required: N).
    type: 查询类型，当前只支持 `stock` (type: string; required: Y).
    page: Page number, starting from 1. If omitted, the server default is used unless ``limit`` or ``all_pages`` is set.
    page_size: Rows per page. The SDK validates this against the endpoint-specific maximum.
    limit: Maximum number of rows to return. The SDK may fetch multiple pages to satisfy this limit.
    all_pages: Fetch and combine pages until the server reports the last page.
    max_pages: Optional safety cap for ``all_pages``.
    raw: Return the decoded JSON payload without tabular extraction.
    fields: Optional field list or comma-separated field string applied after extraction.
    as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
    **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

Returns:
    A pandas ``DataFrame`` by default, Python rows when
    ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
    payloads when multi-page fetching is used with ``raw=True``.
```

<h4 id="api-type-reports"><code>type_reports</code></h4>

- 接口名称：研报分类
- HTTP：`GET`
- Path：`api/v1/market/data/report/type-reports`
- 参数：`rept_type`, `start_date`, `end_date`, `page`, `page_size`
- 来源文档：`研报分类.md`
- 原始接口：`type_reports`

```text
研报分类.

Endpoint: ``api/v1/market/data/report/type-reports``.
Method: ``GET``.
Documented endpoint: ``type_reports``.

Args:
    rept_type: 研报类型：MacroReport / IndustryReport / BrokerMorningReport / StrategyReport / NewStockReport (type: string; required: Y).
    start_date: 开始日期 YYYYMMDD (type: string; required: Y).
    end_date: 结束日期 YYYYMMDD，不填默认与 `start_date` 相同 (type: string; required: N).
    page: Page number, starting from 1. If omitted, the server default is used unless ``limit`` or ``all_pages`` is set.
    page_size: Rows per page. The SDK validates this against the endpoint-specific maximum.
    limit: Maximum number of rows to return. The SDK may fetch multiple pages to satisfy this limit.
    all_pages: Fetch and combine pages until the server reports the last page.
    max_pages: Optional safety cap for ``all_pages``.
    raw: Return the decoded JSON payload without tabular extraction.
    fields: Optional field list or comma-separated field string applied after extraction.
    as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
    **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

Returns:
    A pandas ``DataFrame`` by default, Python rows when
    ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
    payloads when multi-page fetching is used with ``raw=True``.
```

### 现货数据

<h4 id="api-bullion-price"><code>bullion_price</code></h4>

- 接口名称：贵金属价格
- HTTP：`GET`
- Path：`api/v1/market/data/bullion/price`
- 参数：`symbol`, `start_date`, `end_date`, `page`, `page_size`
- 来源文档：`贵金属价格.md`
- 原始接口：`get_bullion_price`

```text
贵金属价格.

Endpoint: ``api/v1/market/data/bullion/price``.
Method: ``GET``.
Documented endpoint: ``get_bullion_price``.

Args:
    symbol: 标的代码，如 XAUUSD、AU9999 (type: string; required: Y).
    start_date: 查询起始日期 YYYYMMDD (type: int; required: Y).
    end_date: 查询结束日期 YYYYMMDD；与 start_date 跨度 ≤3 天 (type: int; required: Y).
    page: Page number, starting from 1. If omitted, the server default is used unless ``limit`` or ``all_pages`` is set.
    page_size: Rows per page. The SDK validates this against the endpoint-specific maximum.
    limit: Maximum number of rows to return. The SDK may fetch multiple pages to satisfy this limit.
    all_pages: Fetch and combine pages until the server reports the last page.
    max_pages: Optional safety cap for ``all_pages``.
    raw: Return the decoded JSON payload without tabular extraction.
    fields: Optional field list or comma-separated field string applied after extraction.
    as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
    **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

Returns:
    A pandas ``DataFrame`` by default, Python rows when
    ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
    payloads when multi-page fetching is used with ``raw=True``.
```

<h4 id="api-bullion-support-symbol"><code>bullion_support_symbol</code></h4>

- 接口名称：贵金属支持标的
- HTTP：`GET`
- Path：`api/v1/market/data/bullion/support-symbol`
- 参数：-
- 来源文档：`贵金属支持标的.md`
- 原始接口：`get_bullion_support_symbol`

```text
贵金属支持标的.

Endpoint: ``api/v1/market/data/bullion/support-symbol``.
Method: ``GET``.
Documented endpoint: ``get_bullion_support_symbol``.

Args:
    raw: Return the decoded JSON payload without tabular extraction.
    fields: Optional field list or comma-separated field string applied after extraction.
    as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
    **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

Returns:
    A pandas ``DataFrame`` by default, Python rows when
    ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
    payloads when multi-page fetching is used with ``raw=True``.
```

### 外汇数据

<h4 id="api-consumer-forex-gold-monthly"><code>consumer_forex_gold_monthly</code></h4>

- 接口名称：外汇黄金
- HTTP：`GET`
- Path：`api/v1/market/data/economic/china-forex-gold`
- 参数：-
- 来源文档：`外汇黄金.md`
- 原始接口：`consumer_forex_gold_monthly`

```text
外汇黄金.

Endpoint: ``api/v1/market/data/economic/china-forex-gold``.
Method: ``GET``.
Documented endpoint: ``consumer_forex_gold_monthly``.

Args:
    raw: Return the decoded JSON payload without tabular extraction.
    fields: Optional field list or comma-separated field string applied after extraction.
    as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
    **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

Returns:
    A pandas ``DataFrame`` by default, Python rows when
    ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
    payloads when multi-page fetching is used with ``raw=True``.
```

### 未发布

<h4 id="api-stock-dividends-paginated"><code>stock_dividends_paginated</code></h4>

- 接口名称：股票分红记录分页
- HTTP：`GET`
- Path：`api/v1/market/data/dividends`
- 参数：`page`, `page_size`
- 来源文档：`股票分红记录分页.md`
- 原始接口：`stock_dividends_paginated`

```text
股票分红记录分页.

Endpoint: ``api/v1/market/data/dividends``.
Method: ``GET``.
Documented endpoint: ``stock_dividends_paginated``.

Args:
    page: Page number, starting from 1. If omitted, the server default is used unless ``limit`` or ``all_pages`` is set.
    page_size: Rows per page. The SDK validates this against the endpoint-specific maximum.
    limit: Maximum number of rows to return. The SDK may fetch multiple pages to satisfy this limit.
    all_pages: Fetch and combine pages until the server reports the last page.
    max_pages: Optional safety cap for ``all_pages``.
    raw: Return the decoded JSON payload without tabular extraction.
    fields: Optional field list or comma-separated field string applied after extraction.
    as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
    **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

Returns:
    A pandas ``DataFrame`` by default, Python rows when
    ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
    payloads when multi-page fetching is used with ``raw=True``.
```

<h4 id="api-stock-intraday"><code>stock_intraday</code></h4>

- 接口名称：股票日内分时
- HTTP：`GET`
- Path：`api/v1/market/security/{symbol}/intraday`
- 参数：`symbol`
- 来源文档：`股票日内分时.md`
- 原始接口：`stock_intraday`

```text
股票日内分时.

Endpoint: ``api/v1/market/security/{symbol}/intraday``.
Method: ``GET``.
Documented endpoint: ``stock_intraday``.

Args:
    symbol: 标的代码 (type: SymbolKey; required: Y).
    raw: Return the decoded JSON payload without tabular extraction.
    fields: Optional field list or comma-separated field string applied after extraction.
    as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
    **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

Returns:
    A pandas ``DataFrame`` by default, Python rows when
    ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
    payloads when multi-page fetching is used with ``raw=True``.
```

<h4 id="api-stock-ipos-paginated"><code>stock_ipos_paginated</code></h4>

- 接口名称：股票IPO分页
- HTTP：`GET`
- Path：`api/v1/market/data/stock-ipos`
- 参数：`page`, `page_size`
- 来源文档：`股票IPO分页.md`
- 原始接口：`stock_ipos_paginated`

```text
股票IPO分页.

Endpoint: ``api/v1/market/data/stock-ipos``.
Method: ``GET``.
Documented endpoint: ``stock_ipos_paginated``.

Args:
    page: Page number, starting from 1. If omitted, the server default is used unless ``limit`` or ``all_pages`` is set.
    page_size: Rows per page. The SDK validates this against the endpoint-specific maximum.
    limit: Maximum number of rows to return. The SDK may fetch multiple pages to satisfy this limit.
    all_pages: Fetch and combine pages until the server reports the last page.
    max_pages: Optional safety cap for ``all_pages``.
    raw: Return the decoded JSON payload without tabular extraction.
    fields: Optional field list or comma-separated field string applied after extraction.
    as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
    **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

Returns:
    A pandas ``DataFrame`` by default, Python rows when
    ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
    payloads when multi-page fetching is used with ``raw=True``.
```

<h4 id="api-stock-related"><code>stock_related</code></h4>

- 接口名称：相关股票
- HTTP：`GET`
- Path：`api/v1/market/security/{symbol}/related`
- 参数：`symbol`, `limit`
- 来源文档：`相关股票.md`
- 原始接口：`stock_related`

```text
相关股票.

Endpoint: ``api/v1/market/security/{symbol}/related``.
Method: ``GET``.
Documented endpoint: ``stock_related``.

Args:
    symbol: 标的代码 (type: SymbolKey; required: Y).
    limit: 返回数量上限，服务端默认 3 (type: int; required: N).
    raw: Return the decoded JSON payload without tabular extraction.
    fields: Optional field list or comma-separated field string applied after extraction.
    as_dataframe: Return a pandas ``DataFrame`` by default; set to ``False`` for Python rows.
    **kwargs: Extra request parameters forwarded unchanged. Useful when the service adds parameters before the SDK is regenerated.

Returns:
    A pandas ``DataFrame`` by default, Python rows when
    ``as_dataframe=False``, raw JSON when ``raw=True``, or raw page
    payloads when multi-page fetching is used with ``raw=True``.
```
