#!/usr/bin/env python3
"""annotated function parameters"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    takes an iterable sequence and returns a list of tuples containing
    a sequence and an integer
    """
    return [(i, len(i)) for i in lst]
