"""Request parameter normalization helpers."""

from __future__ import annotations

import json
from typing import Any


def symbols_to_json_string(symbols: Any) -> Any:
    """Serialize list/tuple/set symbols into the JSON string realtime kline endpoints require."""
    if isinstance(symbols, (list, tuple, set)):
        return json.dumps(list(symbols))
    return symbols
