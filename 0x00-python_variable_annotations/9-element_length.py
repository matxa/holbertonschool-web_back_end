#!/usr/bin/env python3
"""Annotate the below function’s parameters and
return values with the appropriate types

def element_length(lst):
    return [(i, len(i)) for i in lst]
"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Iterate the list and creating a list of tuples
    of item and length of each item in lst

    Parameters
    ----------
    lst: Iterable[Sequence]
        list to iterate

    Returns
    -------
    list(tuple(Sequence, int))
        list of tuples
    """
    return [(i, len(i)) for i in lst]
