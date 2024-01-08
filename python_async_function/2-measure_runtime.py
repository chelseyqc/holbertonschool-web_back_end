#!/usr/bin/env python3
"""a measure_time function with integers n and max_delay"""
import asyncio
import random
import time
from typing import List

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    takes integers as arguments and returns a float
    """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()
    total_time = end_time - start_time
    return total_time / n
