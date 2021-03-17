#!/usr/bin/env python3
"""Write a type-annotated function concat
that takes a string str1 and a string str2
as arguments and returns a concatenated string
"""


def concat(str1: str, str2: str) -> str:
    """Concatenate two strings

    Parameters
    ----------
    str1 : str
        first string
    str2 : str
        second string

    Returns
    -------
    str
        concatenated string = str1 + str2
    """
    return str1 + str2
