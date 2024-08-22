#!/usr/bin/env python3
"""Measure the total runtime of executing
async_comprehension four times in parallel."""
import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Measure the total runtime of executing
    async_comprehension four times in parallel.
    Returns the total runtime in seconds."""
    start = time.perf_counter()
    await asyncio.gather(async_comprehension(), async_comprehension(),
                         async_comprehension(), async_comprehension())
    end = time.perf_counter()
    return end - start
