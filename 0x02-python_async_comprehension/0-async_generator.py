#!/usr/bin/env python3
"""sumary_line

Keyword arguments:
argument -- description
Return: return_description
"""
import asyncio
import random


async def async_generator():
    """sumary_line

    Keyword arguments:
    argument -- description
    Return: return_description
    """
    random.seed(0)
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.randint(0, 10)
