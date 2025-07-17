# Multiprocessing

'''
Multiprocessing allows you to create multiple processes, each with its own Python interpreter 
and memory space. This bypasses the Global Interpreter Lock (GIL), so CPU-bound tasks 
can run in parallel on multiple CPU cores.

Key points:
- Each process has its own memory space (unlike threads).
- Processes communicate via inter-process communication (IPC) methods like Queues, Pipes, etc.
- Good for CPU-bound tasks needing parallelism.
- Slightly heavier to create and manage compared to threads.
'''

import multiprocessing
import time

def cpu_bound_task(n):
    # CPU-bound task: calculating factorial.
    # This will run truly in parallel on multiple CPU cores using multiprocessing.
    print(f"[Process-{multiprocessing.current_process().name}] Calculating factorial of {n}")
    result = 1
    for i in range(2, n+1):
        result *= i
    print(f"[Process-{multiprocessing.current_process().name}] Factorial of {n} is {result}")

def io_bound_task(name, delay):
    # I/O-bound task simulated with sleep.
    print(f"[Process-{name}] Starting I/O-bound task with {delay}s delay.")
    time.sleep(delay)
    print(f"[Process-{name}] Finished I/O-bound task.")

if __name__ == "__main__":
    # Create processes for I/O-bound tasks
    p1 = multiprocessing.Process(target=io_bound_task, args=("P1", 3))
    p2 = multiprocessing.Process(target=io_bound_task, args=("P2", 2))

    # Create processes for CPU-bound tasks
    p3 = multiprocessing.Process(target=cpu_bound_task, args=(10,))
    p4 = multiprocessing.Process(target=cpu_bound_task, args=(15,))

    # Start all processes
    p1.start()
    p2.start()
    p3.start()
    p4.start()

    # Wait for all to complete
    p1.join()
    p2.join()
    p3.join()
    p4.join()

    print("All processes have completed.")

'''
Output Explanation:

- Multiple processes run simultaneously on different CPU cores.
- CPU-bound tasks (factorials) run truly in parallel.
- I/O-bound tasks also run in separate processes concurrently.
- Each process prints messages with its own process name.

Summary:
- Use multiprocessing.Process to create new processes.
- Use start() and join() as with threads.
- Multiprocessing avoids the GIL, ideal for CPU-bound work.
- Requires more memory and overhead than threading.
'''