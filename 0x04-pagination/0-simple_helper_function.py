#!/usr/bin/env python3
"""Write a function named index_range that
takes two integer arguments page and page_size
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple:
    """
    Parameters
    ----------
    page : int
        page number
    page_size : int
        size of page

    Returns
    -------
    tuple
        a tuple of size two containing a start
        index and an end index corresponding to
        the range of indexes to return in a list
        for those particular pagination parameters.
    """
    if page <= 1:
        return (0, page_size)
    else:
        return (page * 10, (page * 10) + page_size)
