#!/usr/bin/env python3
"""Take the code from wait_n and alter it into a new function task_wait_n.
The code is nearly identical to wait_n except task_wait_random is being called.
"""
import asyncio
from typing import List


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Make a list of time in second(s)
    that each task took to complete

    Parameters
    ----------
    n : int
        number of task(s) to execute concurrently
    max_delay : int
        max delaying(sleep) time in second(s)

    Returns
    -------
    list(float)
        a sorted list of seconds each task took to complete
    """
    task_wait_random = __import__('3-tasks').task_wait_random
    delays = [task_wait_random(max_delay) for i in range(n)]
    completed = []

    for task in asyncio.as_completed(delays):
        completed.append(await task)

    return completed
