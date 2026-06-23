"""Pagination validation helpers."""

from __future__ import annotations


def validate_pagination(
    page: int,
    page_size: int | None,
    max_pages: int | None,
    max_page_size: int,
    *,
    limit: int | None = None,
) -> None:
    """Validate client-side pagination controls before sending a request.

    Args:
        page: Page number, starting from 1.
        page_size: Requested rows per page.
        max_pages: Optional maximum number of pages to fetch.
        max_page_size: Endpoint-specific maximum page size.
        limit: Optional maximum number of rows to return.

    Raises:
        ValueError: If any pagination control is outside the supported range.
    """
    if page < 1:
        raise ValueError(f"page must be >= 1; got {page}")
    if page_size is not None and not 1 <= page_size <= max_page_size:
        raise ValueError(f"page_size must be between 1 and {max_page_size}; got {page_size}")
    if limit is not None and limit < 1:
        raise ValueError(f"limit must be >= 1; got {limit}")
    if max_pages is not None and max_pages < 1:
        raise ValueError(f"max_pages must be >= 1; got {max_pages}")
