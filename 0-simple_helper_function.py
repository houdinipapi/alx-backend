#!/usr/bin/env python3

"""
Simple helper function
"""


def index_range(page, page_size):
    """
    Return a tuple of size two containing the start and
    end index for pagination.

    Args:
    - page (int): The current page number (1-indexd).
    - page_size (int): The number of items per page.

    Returns:
    - tuple: A tuple containing the start and end index.
    """
    if page < 1:
        page = 1  # Ensure that page is at least 1
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)
