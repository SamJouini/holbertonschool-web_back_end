#!/usr/bin/env python3
"""A coroutine that yields 10 random numbers between 0 and 10,
with a 1-second delay between each yield."""

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """A coroutine that yields 10 random numbers between 0 and 10,
    with a 1-second delay between each yield.
    Return a random number between 0 and 10."""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
