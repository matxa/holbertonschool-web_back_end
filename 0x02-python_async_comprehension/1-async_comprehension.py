#!/usr/bin/env python3
"""Import async_generator from the previous task and then write
a coroutine called async_comprehension that takes no arguments.

The coroutine will collect 10 random numbers using an async
comprehensing over async_generator, then return the 10 random numbers.
"""
from typing import List


async def async_comprehension() -> List[float]:
    """async comprehension"""
    list_nums = []
    async_generator = __import__('0-async_generator').async_generator
    async for gen in async_generator():
        list_nums.append(gen)

    return list_nums
