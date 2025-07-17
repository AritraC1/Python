# Asynchronous Programming with Async/Await

'''
- Uses cooperative multitasking instead of threads or processes.
- Best suited for I/O-bound and high-level structured network code.
- Based on the event loop: tasks voluntarily yield control (non-blocking).

Tools:
- asyncio (built-in since Python 3.4+)
- async def, await, asyncio.create_task()

Important:
- Async functions are defined using `async def`.
- `await` is used to pause execution until the awaited task completes.

Use Cases:
- Network requests (APIs, sockets)
- File I/O (with aiofiles)
- Database access (with async DB drivers)
'''

import asyncio

async def async_io_task(name, delay):
    print(f"[{name}] Starting async I/O task with {delay}s delay.")
    await asyncio.sleep(delay)  # Non-blocking sleep
    print(f"[{name}] Finished async I/O task.")

async def main():
    # Schedule multiple async tasks concurrently
    task1 = asyncio.create_task(async_io_task("Task-1", 2))
    task2 = asyncio.create_task(async_io_task("Task-2", 1))
    task3 = asyncio.create_task(async_io_task("Task-3", 3))

    await task1
    await task2
    await task3
    print("All async tasks completed.")

# Run the async main
asyncio.run(main())
