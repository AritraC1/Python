# Inter-process Communication (IPC) using multiprocessing.Queue

'''
- Processes don't share memory (unlike threads), so use Queue or Pipe.
- multiprocessing.Queue is a process-safe queue (uses IPC under the hood).
- Good for passing messages or data between processes.

Similar to threading queue, but works between processes.

Use Cases:
- Passing data between CPU-intensive processes
- Logging, data aggregation in parallel systems
'''

import multiprocessing

def process_producer(q):
    for i in range(5):
        print(f"[Producer] Putting {i}")
        q.put(i)
    q.put(None)  # Sentinel

def process_consumer(q):
    while True:
        item = q.get()
        if item is None:
            print("[Consumer] Exiting")
            break
        print(f"[Consumer] Got {item}")

if __name__ == '__main__':
    q = multiprocessing.Queue()

    p1 = multiprocessing.Process(target=process_producer, args=(q,))
    p2 = multiprocessing.Process(target=process_consumer, args=(q,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()