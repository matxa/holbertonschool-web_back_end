#!/usr/bin/env python3
"""Use mypy to validate the following piece of code and
apply any necessary changes.

def zoom_array(lst: Tuple, factor: int = 2) -> Tuple:
    zoomed_in: Tuple = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = [12, 72, 91]

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3.0)
"""
from typing import Tuple, Any, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """Zoom array - by repeating each number x amount of factors

    Parameters
    ----------
    lst : tuple
        tuple to zoom
    factor : int = 2
        amount of times to repeat each number in the tuple

    Returns
    -------
    list
        zoomed list
    """
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
