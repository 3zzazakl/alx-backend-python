#!/usr/bin/env python3
"""summary_line

Keyword arguments:
argument -- description
Return: return_description
"""
from typing import Iterable, List, Union


def zoom_array(a: Iterable[int], factor: Union[int, float] = 2) -> List[int]:
    """returns a list of integers zoomed by a factor"""
    zoomed_in: List[int] = [
        item for item in a
        for i in range(int(factor))
    ]
    return zoomed_in

array = [12, 72, 91]
zoom_2x = zoom_array(array)
zoom_3x = zoom_array(array, 3.0)
