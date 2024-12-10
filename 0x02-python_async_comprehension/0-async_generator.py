#!/usr/bin/env python3
"""sumary_line

Keyword arguments:
argument -- description
Return: return_description
"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """sumary_line

    Keyword arguments:
    argument -- description
    Return: return_description
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.randint(0, 10)
