#!/usr/bin/env python3
"""sumary_line

Keyword arguments:
argument -- description
Return: return_description
"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def task_wait_random(max_delay: int) -> asyncio.Task:
    """sumary_line
    Keyword arguments:
    argument -- description
    Return: return_description
    """
    return asyncio.create_task(wait_random(max_delay))
