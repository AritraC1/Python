# Decorators
# A decorator is a function that takes another function as input, adds some functionality to it, and returns the modified function.
# A decorator is used because -> Code reuse, Separation of concerns (logging, timing, authentication, etc.), Cleaner syntax for wrapping functions

# Basic Decorator
def my_decorator(func):
    def wrapper():
        print("Before the function runs.")
        func()
        print("After the function runs.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

# Test
say_hello()

print()

# Decorator with Arguments
def repeat(n):
    # Decorator that repeats a function n times.
    def decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(n):
                print(f"Execution {i+1}:")
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def greet(name):
    print(f"Hi, {name}!")

# Test
greet("Alice")

print()

# Using functools.wraps
import functools

def log_call(func):
    # Logs the call to the function with its name and docstring.
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling function '{func.__name__}'")
        return func(*args, **kwargs)
    return wrapper

@log_call
def add(x, y):
    """Adds two numbers."""
    return x + y

# Test
print("Result:", add(3, 4))
print("Function name:", add.__name__)        # Should print 'add'
print("Function doc:", add.__doc__)          # Should print docstring

print()

# Multiple Decorators
def upper_case(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()
    return wrapper

def exclaim(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result + "!"
    return wrapper

@exclaim
@upper_case
def welcome():
    return "welcome to python"

# Test
print(welcome())  # Output: WELCOME TO PYTHON!