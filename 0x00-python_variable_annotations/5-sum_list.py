#!/usr/bin/env python3
"""Complex typed annotation"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """Return the sum of a list of flaots"""
    total: float = 0.0
    for num in input_list:
        total += num
    return (total)
