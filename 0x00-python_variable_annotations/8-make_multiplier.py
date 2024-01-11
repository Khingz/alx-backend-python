#!/usr/bin/env python3
"""Callable"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Comment"""
    def multiplier_function(x: float) -> float:
        return (x * multiplier)
    return (multiplier_function)
