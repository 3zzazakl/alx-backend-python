#!/usr/bin/env python3
"""sumary_line

Keyword arguments:
argument -- description
Return: return_description
"""
from typing import Callable


def make_multiplier(a: float) -> Callable[[float], float]:
    """returns a function that multiplies by a"""
    def multiplier(b: float) -> float:
        return a * b
    return multiplier
