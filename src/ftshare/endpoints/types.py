"""Endpoint metadata types for FTShare market data."""

from __future__ import annotations

from collections.abc import Mapping
from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class Endpoint:
    """Metadata for a single FTShare API endpoint."""

    name: str
    path: str | None
    method: str = "GET"
    title: str = ""
    doc_file: str | None = None
    original_api: str = ""
    params: tuple[str, ...] = ()
    path_params: tuple[str, ...] = ()
    max_page_size: int = 200


def build_endpoints(specs: Mapping[str, Mapping[str, Any]]) -> dict[str, Endpoint]:
    """Build endpoint objects from compact ftshare-doc topic specs."""
    return {
        name: Endpoint(
            name=name,
            path=spec["path"],
            method=spec.get("method", "GET"),
            title=spec.get("title", ""),
            doc_file=spec.get("doc_file"),
            original_api=spec.get("original_api", ""),
            params=tuple(spec.get("params", ())),
            path_params=tuple(spec.get("path_params", ())),
            max_page_size=spec.get("max_page_size", 200),
        )
        for name, spec in specs.items()
    }
