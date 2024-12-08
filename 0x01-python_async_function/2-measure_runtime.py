#!/usr/bin/env python3
"""sumary_line

Keyword arguments:
argument -- description
Return: return_description
"""
import time
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def measure_time(n: int, max_delay: int) -> float:
    """sumary_line
    Keyword arguments:
    argument -- description
    Return: return_description
    """
    start_time = time.time()
    asyncio.run(wait_random(max_delay))
    end_time = time.time()

    total_time = end_time - start_time
    return total_time / n
