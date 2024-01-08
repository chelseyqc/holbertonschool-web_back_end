#!/usr/bin/env python3
"""an async routine called wait_n"""
import asyncio
import random
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int = 10) -> List[float]:
    """
    takes 2 two args n and max_delay and returns the list of all the delays
    """
    tasks = [wait_random(max_delay) for _ in range(n)]
    completed = await asyncio.gather(*tasks)
    return sorted(completed)
