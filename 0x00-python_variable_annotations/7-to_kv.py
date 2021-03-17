#!/usr/bin/env python3
"""Write a type-annotated function to_kv that
takes a string k and an int OR float v as arguments
and returns a tuple. The first element of the tuple
is the string k. The second element is the square of
the int/float v and should be annotated as a float.
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """A tuple - containing k and square of v

    Parameters
    ----------
    k : str
        first of element of returned tuple
    v : int || float
        number to square and second element in a tuple

    Returns
    -------
    tuple(str, float)
        containing k and v**2
    """
    return (k, float(v**2))
