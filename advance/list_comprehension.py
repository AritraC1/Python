# List Comprehension

# A list comprehension is a concise way to create lists in a single line.
# It replaces loops and map/filter calls with a more readable syntax.
# It consists of:
#   [ expression for item in iterable if condition ]

# You can:
# - Transform elements
# - Filter elements
# - Create nested structures

# List comprehensions are often faster and more readable than for-loops.

# Basic transformation
squares = [x * x for x in range(5)]
print("Squares:", squares)

# With condition (filtering)
even_squares = [x * x for x in range(10) if x % 2 == 0]
print("Even squares:", even_squares)

# Nested loops
pairs = [(x, y) for x in [1, 2] for y in [3, 4]]
print("All pairs:", pairs)

# From string to list of chars
chars = [ch for ch in "hello"]
print("Characters:", chars) 

# Using list comprehension with functions
def is_prime(n):
    return n > 1 and all(n % i != 0 for i in range(2, int(n**0.5)+1))

primes_under_20 = [x for x in range(20) if is_prime(x)]
print("Primes under 20:", primes_under_20)

# If-else expression in comprehension
labels = ["even" if x % 2 == 0 else "odd" for x in range(5)]
print("Even/Odd labels:", labels)

'''
Summary:

List comprehensions create lists using a clear, compact syntax
Basic form: [expression for item in iterable if condition]
You can use them to transform, filter, and combine elements
They can include nested loops and if-else expressions
More readable and efficient than equivalent for-loops
'''