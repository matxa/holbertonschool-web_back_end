#!/usr/bin/env python3
"""Given the parameters and the return values,
add type annotations to the function

Hint: look into TypeVar

def safely_get_value(dct, key, default = None):
    if key in dct:
        return dct[key]
    else:
        return default
"""
from typing import Mapping, Any, Union, TypeVar


T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any, default: Union[T, None])\
 -> Union[Any, T]:
    """get value in dict given the key

    Parameters
    ----------
    dct : dict
        dictionary to get the value from
    key : Any
        key to get the value of in the dictionary if it exists
    default : Any || None
        what to return if key doesn't exist

    Returns
    -------
    Any || T -> TypeVar
        the value if key is found else return Custom TypeVar
    """
    if key in dct:
        return dct[key]
    else:
        return default
