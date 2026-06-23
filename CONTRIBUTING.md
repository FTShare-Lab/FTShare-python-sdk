# Contributing to ftshare

Thanks for your interest in contributing! This is a short guide to get you started.

## Development setup

Clone the repository and install the package with its test dependencies in editable mode:

```bash
git clone git@github.com:ftshare-lab/ftshare-python-sdk.git
cd ftshare-python-sdk
pip install -e ".[test]"
```

> Replace the repository URL above with your fork once you have one.

## Running tests

The unit test suite uses mocked HTTP and does not require network access:

```bash
python3 -m pytest
```

Real-API integration tests are skipped by default. To run them against a reachable FTShare service:

```bash
FTSHARE_RUN_INTEGRATION=1 python3 -m pytest tests/test_integration_market.py
```

## Making changes

1. Open an issue to discuss significant changes before starting work.
2. Keep the public API surface stable unless an issue calls for a breaking change.
3. Make sure `python3 -m pytest` passes.
4. Submit a pull request with a clear description of the change and motivation.

## Reporting issues

Use the issue tracker for bug reports and feature requests. For security-sensitive reports, see [SECURITY.md](SECURITY.md).
