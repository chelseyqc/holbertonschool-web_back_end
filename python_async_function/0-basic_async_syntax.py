#!/usr/bin/env python3
"""
An asynchronous coroutine that takes an integer argument
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """takes an integer argument and returns a float"""
    random_delay = random.uniform(0, max_delay)
    await asyncio.sleep(random_delay)
    return random_delay
