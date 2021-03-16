#!/usr/bin/env python3
"""Annotate the below function’s parameters and
return values with the appropriate types

def element_length(lst):
    return [(i, len(i)) for i in lst]
"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """iterate the list and creating a list of tuples
    of item and length of each item in lst
    """
    return [(i, len(i)) for i in lst]
