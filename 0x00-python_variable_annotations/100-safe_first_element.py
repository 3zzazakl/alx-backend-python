#!/usr/bin/env python3
"""sumary_line

Keyword arguments:
argument -- description
Return: return_description
"""
from typing import Sequence, Any, Union


def safe_first_element(a: Sequence[Any]) -> Union[Any, None]:
    """returns first element of a sequence or None if empty"""
    if a:
        return a[0]
    else:
        return None
