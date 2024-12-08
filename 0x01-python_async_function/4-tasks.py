#!/usr/bin/env python3
"""sumary_line

Keyword arguments:
argument -- description
Return: return_description
"""
import asyncio
from typing import List
from random import uniform


async def task_wait_random(max_delay: int) -> float:
    """sumary_line

    Keyword arguments:
    argument -- description
    Return: return_description
    """
    return uniform(0, max_delay)


async def task_wait_n(n: int, max_delay: int = 10) -> List[float]:
    """sumary_line

    Keyword arguments:
    argument -- description
    Return: return_description
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)
    return sorted(delays)
