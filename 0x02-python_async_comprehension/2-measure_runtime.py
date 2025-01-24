#!/usr/bin/env python3
"""summary_line

Keyword arguments:
argument -- description
Return: return_description
"""
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """summary_line

    Keyword arguments:
    argument -- description
    Return: return_description
    """
    start = time.time()
    tasks = [asyncio.create_task(async_comprehension()) for _ in range(4)]
    await asyncio.gather(*tasks)
    end_time = time.time()
    return end_time - start
