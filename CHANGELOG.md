# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Fixed
- 24 paginated endpoints exposed only `page`/`page_size`; they now also accept `limit`, `all_pages`, and `max_pages`.
- `bse_mapping` endpoint metadata now records its `page`/`page_size` parameters and documented 500-row page cap.
- Documented per-endpoint `page_size` caps (up to 4000) are now validated client-side.
- `tdx_board_daily`/`tdx_board_index`/`tdx_board_members` exposed the dead parameters `idx_name`/`idx_type`/`idx_type_code`; they are now `board_name`/`board_type`/`board_type_code`, which the service actually honors. The three endpoints also document their full parameter set and enforce the documented 1000-row page cap.
- `limit_event_timeline_3s` exposed only `symbol`/`trade_date`; it now records its documented `page`/`page_size` parameters and accepts `limit`, `all_pages`, and `max_pages`, with the documented 200-row page cap.
- `etf_pcf_infos` referenced the non-existent doc `ETF-PCF信息.md`; corrected to `ETF申赎清单.md`.
- `ashare_rating_factor_snapshot` referenced the non-existent doc `A股相关性Top-K.md`; corrected to `A股相关性 Top-K.md`.
- `goodwill_industry` declared `page`/`page_size` although the service ignores both and returns every industry in one response, which made `all_pages=True` re-fetch the same rows forever. The endpoint now exposes only its documented `date` parameter.

## [0.1.1] - 2026-06-29

### Changed
- Default `base_url` changed from `https://market.ft.tech/data/` to `https://market.ft.tech/gateway/`.
- Endpoint and API mixin registries are now split by `ftshare-doc/api-doc` topic.
- SDK coverage updated to 179 market-data endpoints.

## [0.1.0] - 2026-06-23

### Added
- First public release of the `ftshare` Python SDK.
- Synchronous client (`ftshare.market_api`) returning pandas `DataFrame` by default.
- 176 market-data endpoints generated from the API documentation.
- Field selection (`fields`), pagination (`page`/`page_size`/`limit`/`all_pages`), and `raw`/`as_dataframe` return controls.
- MIT license and open-source project scaffolding (`.gitignore`, `CHANGELOG.md`, `CONTRIBUTING.md`, `SECURITY.md`, CI workflow).
