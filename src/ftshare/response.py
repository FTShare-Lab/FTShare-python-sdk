"""Response parsing helpers for FTShare API envelopes."""

from __future__ import annotations

from typing import Any

from .exceptions import FtshareAPIError


def raise_for_api_error(payload: Any) -> None:
    """Raise ``FtshareAPIError`` when a business response reports failure.

    FTShare responses commonly include ``code`` and ``message`` at the top
    level. Most endpoints use ``0`` for success, while a few legacy-style
    envelopes use HTTP-like ``200``.
    """
    if isinstance(payload, dict) and "code" in payload and payload.get("code") not in (0, "0", 200, "200"):
        message = payload.get("message")
        raise FtshareAPIError(payload.get("code"), str(message) if message is not None else None, payload)


def extract_tabular(payload: Any) -> Any:
    """Extract common row containers from FTShare response shapes.

    Supported envelopes:
        - ``{"data": {"records": [...]}}``
        - ``{"items": [...]}``

    Any unsupported shape is returned unchanged so callers do not lose data.
    """
    if isinstance(payload, dict):
        data = payload.get("data")
        if isinstance(data, dict) and isinstance(data.get("records"), list):
            return data["records"]
        if isinstance(data, dict) and isinstance(data.get("items"), list):
            return data["items"]
        if isinstance(payload.get("items"), list):
            return payload["items"]
    return payload


def total_pages(payload: Any) -> int | None:
    """Return total page count from supported pagination envelopes."""
    if not isinstance(payload, dict):
        return None

    data = payload.get("data")
    if isinstance(data, dict) and data.get("pages") is not None:
        return int(data["pages"])
    if isinstance(data, dict) and data.get("total_pages") is not None:
        return int(data["total_pages"])
    if payload.get("total_pages") is not None:
        return int(payload["total_pages"])
    return None
