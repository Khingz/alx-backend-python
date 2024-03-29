#!/usr/bin/env python3
"""Complex annotation returning a tuple"""
from typing import Tuple, Union


myTuple = Tuple[str, float]


def to_kv(k: str, v: Union[int, float]) -> myTuple:
    """Return a tuple from args"""
    return (k, float(v * v))
