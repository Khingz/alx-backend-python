#!/usr/bin/env python3
"""Comment"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """Comment"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
