#!/usr/bin/env python3

import asyncio

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def main():
    """summary_line

    Keyword arguments:
    argument -- description
    Return: return_description
    """

    print(await async_comprehension())

asyncio.run(main())
