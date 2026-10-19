"""Request parameter normalization helpers."""

from __future__ import annotations

from typing import Any


def symbols_to_csv_string(symbols: Any) -> Any:
    """Serialize list/tuple/set symbols into the comma-separated string the realtime kline endpoints document."""
    if isinstance(symbols, (list, tuple, set)):
        return ",".join(str(symbol) for symbol in symbols)
    return symbols
