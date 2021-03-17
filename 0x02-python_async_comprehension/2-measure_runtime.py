#!/usr/bin/env python3
""""Measure Runtime"""
import time
import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    -----------------------
    METHOD: measure_runtime
    -----------------------
    """
    start = time.time()
    await asyncio.gather(
        *(async_comprehension() for i in range(4))
    )
    end = time.time()

    return end - start
