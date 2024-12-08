#!/usr/bin/env python3
"""sumary_line

Keyword arguments:
argument -- description
Return: return_description
"""
from asyncio import Task, create_task
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> Task:
    """summary_line
    Keyword arguments:
    argument -- description
    Return: return_description
    """
    return create_task(wait_random(max_delay))
