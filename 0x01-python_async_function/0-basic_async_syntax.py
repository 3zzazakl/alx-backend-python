#!/usr/bin/env python3
"""sumary_line

Keyword arguments:
argument -- description
Return: return_description
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """wait_random
    Keyword arguments:
    max_delay -- description
    Return: return_description
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
