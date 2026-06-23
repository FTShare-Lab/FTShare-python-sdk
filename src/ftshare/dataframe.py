"""pandas conversion helpers."""

from __future__ import annotations

from typing import Any


def to_dataframe(result: Any) -> Any:
    """Convert a row-like result into a pandas ``DataFrame``.

    ``pandas`` is an install dependency of this SDK, but importing it lazily
    keeps module import time low and avoids side effects during metadata reads.
    """
    import pandas as pd

    if isinstance(result, list):
        return pd.DataFrame(result)
    return pd.DataFrame([result])
