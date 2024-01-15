#!/usr/bin/env python3
"""Simple Async await"""
import asyncio
import random


async def wait_random(max_delay: int =10) -> float:
    """Simple async function"""
    time = random.uniform(0, max_delay)
    await asyncio.sleep(time)
    return (time)
