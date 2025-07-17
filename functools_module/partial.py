# partial
# Freezes some portion of a function's arguments and/or keywords. Returns a new function with fewer arguments.

from functools import partial

def multiply(x, y):
    return x * y

# Create a function that always multiplies by 2
double = partial(multiply, 2)

print("Double of 5:", double(5))