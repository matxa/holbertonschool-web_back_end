#!/usr/bin/env python3
"""Write a type-annotated function sum_mixed_list
which takes a list mxd_lst of integers and floats
and returns their sum as a float.
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Sum a list of ints and floats

    Parameters
    ----------
    mxd_list : list(int, float)
        list to sum

    Returns
    -------
    float
        sum of mxd_list
    """
    return float(sum(mxd_lst))
