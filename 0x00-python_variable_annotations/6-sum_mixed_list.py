#!/usr/bin/env python3
"""Sum a list of int and a float and return a float"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Return the sum of a mixed list"""
    total: float = 0.0
    for ele in mxd_lst:
        total += float(ele)
    return (total)
