#!/usr/bin/env python3
"""sumary_line

Keyword arguments:
argument -- description
Return: return_description
"""
from typing import Mapping, Any, Union, Optional, TypeVar

T = TypeVar('T')


def safely_get_value(
    a: Mapping[Any, Any],
    k: Any,
    default: Optional[T] = None
) -> Union[Any, T]:
    """returns value of a mapping for a key or default if not found"""
    if k in a:
        return a[k]
    else:
        return default
