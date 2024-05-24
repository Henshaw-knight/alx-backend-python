#!/usr/bin/env python3
"""task_wait_n async routine module"""
from typing import List
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Spawns wait_random `n` times with the specified `max_delay`"""
    delays = await asyncio.gather(*(wait_random(max_delay) for i in range(n)))
    return sorted(delays)
