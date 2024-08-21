#!/usr/bin/env python3
"""Calculate the start and end indexes for pagination."""


def index_range(page: int, page_size: int) -> tuple:
    """Calculate the start and end indexes for pagination.
    Returns a tuple containing the start index and end index."""
    if page <= 0 or page_size <= 0:
        return (0, 0)

    start_index = (page - 1) * page_size
    end_index = start_index + page_size

    return (start_index, end_index)
