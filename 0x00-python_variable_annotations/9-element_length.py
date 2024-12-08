#!/usr/bin/env python3
"""sumary_line

Keyword arguments:
argument -- description
Return: return_description
"""
from typing import List, Tuple, Sequence, Iterable


def element_length(a: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    return [(x, len(x)) for x in a]
