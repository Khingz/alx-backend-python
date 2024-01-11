#!/usr/bin/env python3
"""Comment"""
from typing import Mapping, Any, TypeVar, Union

T = TypeVar('T')
U1 = Union[T, None]
U2 = Union[Any, T]
M = Mapping


def safely_get_value(dct: M, key: Any, default: U1) -> U2:
    """Comment"""
    if key in dct:
        return dct[key]
    else:
        return default
