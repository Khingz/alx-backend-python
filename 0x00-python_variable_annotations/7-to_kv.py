#!/usr/bin/env python3
"""Complex annotation returning a tuple"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple:
    """Comment"""
    return (k, v * v)
