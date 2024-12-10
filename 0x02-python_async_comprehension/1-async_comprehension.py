#!/usr/bin/env python3
"""sumary_line

Keyword arguments:
argument -- description
Return: return_description
"""
async_generator = __import__('0-async_generator').async_generator

async def async_comprehension():
    """sumary_line

    Keyword arguments:
    argument -- description
    Return: return_description
    """
    return [num async for num in async_generator()]
