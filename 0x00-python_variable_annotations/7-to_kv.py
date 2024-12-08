#!/usr/bin/env python3
"""sumary_line

Keyword arguments:
argument -- description
Return: return_description
"""


from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, Union[int, float]]:
    """returns a tuple of a string and a number"""
    return (k, float(v ** 2))
