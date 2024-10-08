#!/usr/bin/env python3
" Create and return an asyncio.Task for wait_random."

import asyncio
from asyncio import Task

wait_random = __import__("0-basic_async_syntax").wait_random


def task_wait_random(max_delay: int) -> Task:
    """Create and return an asyncio.Task for wait_random.
    Returns a Task object for the wait_random coroutine."""

    # Create and return a Task for wait_random
    return asyncio.create_task(wait_random(max_delay))
