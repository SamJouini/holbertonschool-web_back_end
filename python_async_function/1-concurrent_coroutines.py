#!/usr/bin/env python3
"Spawn wait_random n times with the specified max_delay."

import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Spawn wait_random n times with the specified max_delay.
    Returns a list of delays in ascending order."""
    # Create a list of coroutines
    tasks = [wait_random(max_delay) for _ in range(n)]

    # Use asyncio.as_completed to get results as they complete
    delays = []

    for future in asyncio.as_completed(tasks):
        delay = await future

        # Insert the delay in the correct position to maintain ascending order
        insertion_index = next((i for i, x in
                                enumerate(delays) if x > delay), len(delays))
        delays.insert(insertion_index, delay)

    return delays
