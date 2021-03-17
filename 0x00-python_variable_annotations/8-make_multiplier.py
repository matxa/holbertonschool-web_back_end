#!/usr/bin/env python3
"""Write a type-annotated function make_multiplier
that takes a float multiplier as argument and returns
a function that multiplies a float by multiplier.
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Returns a function that multiplies a float by multiplier.

    Parameters
    ----------
    multiplier : float
        number to multiply to

    Returns
    -------
    callback(float) -> float
        function that takes in a float then multiplies float by multiplier
    """
    return lambda x: x * multiplier
