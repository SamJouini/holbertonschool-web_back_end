#!/usr/bin/env python3
"Asynchronous coroutine that waits for a random delay and returns it."

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Asynchronous coroutine that waits for a random delay and returns it.
    Returns the random delay waited."""

    # Generate a random delay between 0 and max_delay (inclusive)
    delay = random.uniform(0, max_delay)

    # Wait for the random delay
    await asyncio.sleep(delay)

    # Return the delay
    return delay
