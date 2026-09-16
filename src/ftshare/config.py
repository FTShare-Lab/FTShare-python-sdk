"""Runtime configuration helpers for the ftshare SDK."""

from __future__ import annotations

import os

DEFAULT_BASE_URL = "https://market.ft.tech/gateway/"
"""Default FTShare API base URL."""

DEFAULT_MAX_PAGE_SIZE = 200
"""Default maximum page size used by paginated endpoints."""

_BASE_URL = DEFAULT_BASE_URL


def normalize_base_url(url: str) -> str:
    """Normalize a base URL to the canonical trailing-slash form.

    Args:
        url: API base URL. Both ``https://host/gateway`` and
            ``https://host/gateway/`` are accepted.

    Returns:
        The normalized base URL, always ending with ``/``.

    Raises:
        ValueError: If ``url`` is empty after stripping whitespace.
    """
    value = str(url).strip()
    if not value:
        raise ValueError("base_url must not be empty")
    return value.rstrip("/") + "/"


def get_base_url() -> str:
    """Return the module-level base URL used by new client instances."""
    return _BASE_URL


def set_base_url(url: str) -> str:
    """Set the module-level base URL used by new client instances.

    Args:
        url: API base URL.

    Returns:
        The normalized base URL.
    """
    global _BASE_URL
    _BASE_URL = normalize_base_url(url)
    return _BASE_URL


_env_base_url = os.environ.get("FTSHARE_BASE_URL")
if _env_base_url:
    set_base_url(_env_base_url)
