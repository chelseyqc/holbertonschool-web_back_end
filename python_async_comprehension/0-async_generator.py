#!/usr/bin/env python3
"""a coroutine that loops 10 times"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    loops 10 times and each time it will asynchronously wait for 1 sec
    then yield a random number between 0 and 10
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
