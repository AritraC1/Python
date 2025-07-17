# Context Managers
# A context manager manages setup and cleanup actions, typically used with the `with` statement. The most common example: opening files. It is used to automatically handle resource management (like closing files) and helps in writing cleaner and safer code.

# Built-in context manager for files
with open("sample.txt", "w") as f:
    f.write("This file was written using a context manager.")

# No need to call f.close()

# Creating a Custom Context Manager (Class)
class MyContext:
    def __enter__(self):
        print("Entered the context.")
        return "Resource"
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Exiting the context.")
        if exc_type:
            print(f"An exception occurred: {exc_val}")
        return True  # suppress exceptions

with MyContext() as val:
    print("Using:", val)
    raise ValueError("Oops!")

# Using @contextmanager Decorator
from contextlib import contextmanager

@contextmanager
def open_managed_file(filename, mode):
    f = open(filename, mode)
    try:
        yield f
    finally:
        print("Closing file...")
        f.close()

with open_managed_file("test.txt", "w") as f:
    f.write("Hello from @contextmanager!")