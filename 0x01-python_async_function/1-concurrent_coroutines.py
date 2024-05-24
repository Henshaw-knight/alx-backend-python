#!/usr/bin/env python3
"""wait_n async routine module"""
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int):
    """Spawns wait_random `n` times with the specified `max_delay`"""
    delays = []
    for i in range(n):
       delay = await wait_random(max_delay)
       delays.append(delay)

    return sorted(delays)
