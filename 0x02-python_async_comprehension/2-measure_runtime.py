#!/usr/bin/env python3
"""measure_runtime coroutine module"""
import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Measures and returns the total runtime"""
    start_time = time.time()
    results = await asyncio.gather(*(async_comprehension() for i in range(4)))
    end_time = time.time()

    return (end_time - start_time)
