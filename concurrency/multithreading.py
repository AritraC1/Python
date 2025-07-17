# Concurrency and Multithreading

'''
Concurrency is the ability to run multiple tasks seemingly at the same time.
Multithreading is one way to achieve concurrency by running multiple threads 
within a single process.

Key points:
- Threads share the same memory space, so data sharing is easy.
- Python has a Global Interpreter Lock (GIL) that allows only one thread to 
  execute Python bytecode at a time (limits true parallelism in CPU-bound tasks).
- Multithreading is best for I/O-bound tasks (e.g. file I/O, network operations).
- For CPU-bound tasks, multiprocessing or async might be better.

Modules used:
- threading: for creating and managing threads.
- time: for simulating delays.

Multithreading allows multiple threads to run concurrently within the same process.
- Threads share the same memory space (easier to share data).
- Useful mainly for I/O-bound tasks (networking, file I/O, waiting).
- Due to Python's Global Interpreter Lock (GIL), only one thread executes Python bytecode at a time,
  so multithreading does NOT improve CPU-bound task performance.
- Threads are lighter than processes (less memory and overhead).

Common Methods:
- threading.Thread: create and manage threads.
- start(): begins thread execution.
- join(): wait for thread to complete.
'''

import threading
import time

def io_bound_task(name, delay):
    # Simulates an I/O-bound task by sleeping. This kind of task benefits from multithreading because while one thread waits (sleeps), others can run.
    print(f"[{name}] Starting I/O-bound task with {delay}s delay.")
    time.sleep(delay)
    print(f"[{name}] Finished I/O-bound task.")

def cpu_bound_task(n):
    # Simulates a CPU-bound task by computing factorial. This task does not benefit much from multithreading in CPython because of GIL (threads can't run Python code in parallel).
    print(f"[CPU] Calculating factorial of {n}")
    result = 1
    for i in range(2, n+1):
        result *= i
    print(f"[CPU] Factorial of {n} is {result}")

if __name__ == "__main__":
    # Create threads for I/O-bound tasks
    t1 = threading.Thread(target=io_bound_task, args=("Thread-1", 3))
    t2 = threading.Thread(target=io_bound_task, args=("Thread-2", 2))

    # Create a thread for CPU-bound task
    t3 = threading.Thread(target=cpu_bound_task, args=(10,))

    # Start all threads
    t1.start()
    t2.start()
    t3.start()

    # Wait for all threads to complete
    t1.join()
    t2.join()
    t3.join()

    print("All threads have completed.")