"""Field selection helpers for tabular SDK results."""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from typing import Any


def normalize_fields(fields: Sequence[str] | str | None) -> list[str] | None:
    """Normalize ``fields`` from sequence or comma-separated string."""
    if fields is None:
        return None
    if isinstance(fields, str):
        return [field.strip() for field in fields.split(",") if field.strip()]
    return [str(field) for field in fields]


def select_fields(result: Any, fields: Sequence[str] | str | None) -> Any:
    """Select requested fields from mapping rows while preserving row order.

    Missing fields are represented as ``None`` to match DataFrame-friendly
    tabular behavior and avoid silently changing the requested column layout.
    """
    normalized = normalize_fields(fields)
    if not normalized:
        return result

    def select_one(row: Any) -> Any:
        if isinstance(row, Mapping):
            return {field: row.get(field) for field in normalized}
        return row

    if isinstance(result, list):
        return [select_one(row) for row in result]
    return select_one(result)
