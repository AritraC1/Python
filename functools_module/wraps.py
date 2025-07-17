# Wraps
# Used inside decorators to preserve metadata of the original function. Without it, docstrings and function names get lost.

from functools import wraps

def my_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Calling decorated function...")
        return func(*args, **kwargs)
    return wrapper

@my_decorator
def greet():
    """Returns a greeting"""
    print("Hello!")

greet()
print("Function name:", greet.__name__)
print("Docstring:", greet.__doc__)