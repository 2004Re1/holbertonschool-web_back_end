#!/usr/bin/env python3
"""
This module contains an asynchronous generator that yields random
floating-point numbers between 0 and 10 with a one-second delay.
"""

import random
import asyncio
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """
    Asynchronously generates 10 random float numbers between 0 and 10,
    with a delay of 1 second between each number.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
