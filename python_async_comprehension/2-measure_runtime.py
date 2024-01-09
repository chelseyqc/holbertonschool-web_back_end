#!/usr/bin/env python3
"""a coroutine called measure_runtime"""
import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """executes async_comprehension four times in parallel"""
    start_time = time.time()
    async_coroutines = [async_comprehension() for _ in range(4)]
    await asyncio.gather(*async_coroutines)
    end_time = time.time()
    total_runtime = end_time - start_time
    return total_runtime
