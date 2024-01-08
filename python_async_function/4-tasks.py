#!/usr/bin/env python3
"""Altered wait_n to a new function task_wait_n"""
import asyncio
import random
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int = 10) -> List[float]:
    """
    takes 2 two args n and max_delay and returns the list of all the delays
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    completed = await asyncio.gather(*tasks)
    return sorted(completed)
