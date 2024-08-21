#!/usr/bin/env python3
"""Collect 10 random numbers using an
async comprehension over async_generator."""

from typing import List
import asyncio

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """ Collect 10 random numbers using an
    async comprehension over async_generator.
    Returns a list of 10 random float numbers."""
    return [number async for number in async_generator()]
