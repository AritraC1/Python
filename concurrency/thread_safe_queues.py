# Thread-safe Queues using queue.Queue

'''
- Used to safely share data between threads.
- No need for manual locks (queue is synchronized).
- Useful for producer-consumer pattern.

Key Methods:
- put(): Add item to the queue.
- get(): Remove item from the queue.
- task_done(), join(): For coordination.

Thread-safe because it uses internal locks to prevent race conditions.

Use Cases:
- Data pipelines
- Background tasks
- Safe sharing of work between threads
'''

import threading
import queue
import time

q = queue.Queue()

def producer():
    for i in range(5):
        print(f"[Producer] Producing item {i}")
        q.put(i)
        time.sleep(1)
    q.put(None)  # Sentinel to signal consumer to stop

def consumer():
    while True:
        item = q.get()
        if item is None:
            print("[Consumer] No more items. Exiting.")
            break
        print(f"[Consumer] Consumed item {item}")
        q.task_done()

# Create and start threads
producer_thread = threading.Thread(target=producer)
consumer_thread = threading.Thread(target=consumer)

producer_thread.start()
consumer_thread.start()

producer_thread.join()
consumer_thread.join()