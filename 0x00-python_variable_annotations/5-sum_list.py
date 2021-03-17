#!/usr/bin/env python3
"""Write a type-annotated function sum_list which takes
a list input_list of floats as argument and
returns their sum as a float.
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """Sum a list of floats

    Parameters
    ----------
    input_list : list(float)
        list to sum

    Returns
    -------
    float
        sum of input_list
    """
    return float(sum(input_list))
