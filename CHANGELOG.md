# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

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
