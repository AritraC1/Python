# Functions in Python
# Functions are reusable blocks of code that perform a specific task.
# You define a function with the 'def' keyword.
# Functions can take inputs (parameters) and return outputs.

# Defining and calling a simple function
print("Defining and calling a simple function:")
def greet():
    print("Hello, world!")

greet()
print()

# Function with parameters
print("Function with parameters:")
def greet_person(name):
    print(f"Hello, {name}!")

greet_person("Alice")
print()

# Function with return value
print("Function with return value:")
def add(a, b):
    return a + b

result = add(5, 3)
print("5 + 3 =", result)
print()

# Function with default parameters
print("Function with default parameters:")
def power(base, exponent=2):
    return base ** exponent

print("2^3 =", power(2, 3))
print("4^2 (default exponent) =", power(4))
print()

# Functions with multiple return values
print("Functions with multiple return values:")
def min_max(numbers):
    return min(numbers), max(numbers)

minimum, maximum = min_max([4, 7, 2, 9, 1])
print("Min:", minimum, "Max:", maximum)
print()

# Using *args and **kwargs
print("Using *args and **kwargs:")
def demo_args(*args, **kwargs):
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)

demo_args(1, 2, 3, name="Alice", age=30)
print()

# Anonymous functions (lambda)
print("Anonymous function (lambda):")
square = lambda x: x * x
print("Square of 5:", square(5))
print()

'''
Note: If no return is specified, the function returns None by default.
'''

# Recursion (Brief introduction)
# Recursion: a function calling itself
# Example: Factorial calculation

def factorial(n):
    if n == 0:
        return 1  # Base case
    else:
        return n * factorial(n - 1)  # Recursive case

print("Factorial of 5:", factorial(5))
print()

# Explanation:
# Recursion involves two main parts:
# Base case - when the function stops calling itself
# Recursive case - when the function calls itself with a smaller input

'''
Caution: improper recursion can lead to infinite loops or stack overflow.
'''
