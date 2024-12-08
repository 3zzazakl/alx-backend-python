#!/usr/bin/env python3
"""summary_line

Keyword arguments:
argument -- description
Return: return_description
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """returns a function that multiplies by a"""
    def multiply(b: float) -> float:
        return multiplier * b
    return multiply
