#!/usr/bin/env python3
" Create and return an asyncio.Task for wait_random."

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Create and return an asyncio.Task for wait_random.
    Returns a task object for the wait_random coroutine."""

    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    delays = await asyncio.gather(*tasks)
    return sorted(delays)
