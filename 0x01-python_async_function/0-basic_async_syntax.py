#!/usr/bin/env python3
"""Simple Async await"""
import asyncio
import random


async def wait_random(max_delay=10):
    """Simple async function"""
    time = random.random * max_delay
    await asyncio.sleep(time)
    return (time)
