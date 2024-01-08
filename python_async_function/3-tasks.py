#!/usr/bin/env python3
"""a function task_wait_random"""
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Takes an int max_delay and returns an asyncio.Task"""
    return asyncio.create_task(wait_random(max_delay))
