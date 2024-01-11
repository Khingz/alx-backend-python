#!/usr/bin/env python3
"""Sequence typing"""
from typing import Sequence, Iterable, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Comment"""
    return [(i, len(i)) for i in lst]
