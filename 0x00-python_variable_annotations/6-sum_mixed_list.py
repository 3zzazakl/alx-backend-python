#!/usr/bin/env python3
"""sumary_line

Keyword arguments:
argument -- description
Return: return_description
"""
from typing import List, Union


def sum_mixed_list(a: List[Union[int, float]]) -> float:
    """returns sum of a list of mixed types"""
    return float(sum(a))
