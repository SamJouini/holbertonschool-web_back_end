#!/usr/bin/env python3
"Measure the average execution time of wait_n(n, max_delay)."

import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Measure the average execution time of wait_n(n, max_delay).
    Returns the average execution time per call."""

    start_time = time.time()

    # Run wait_n using asyncio.run
    asyncio.run(wait_n(n, max_delay))

    end_time = time.time()
    total_time = end_time - start_time

    return total_time / n
