#!/usr/bin/env python3
"""
type-annotated function make_multiplier that takes a float multiplier
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    takes a float as argument and returns a function that multiplies a float
    """
    def multiplier_function(value: float) -> float:
        return value * multiplier
    return multiplier_function
