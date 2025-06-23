# map(), filter(), and reduce() in Python

# These are built-in functions that allow functional-style programming.
# They take a function and an iterable and apply the function in different ways.

# map(function, iterable):
# Applies the function to each item in the iterable
# Returns a map object (convert to list if needed)

nums = [1, 2, 3, 4]
squares = list(map(lambda x: x ** 2, nums))
print("Squares using map:", squares)

# filter(function, iterable):
# Applies the function as a condition (should return True/False)
# Returns items where the function returns True

even_nums = list(filter(lambda x: x % 2 == 0, nums))
print("Even numbers using filter:", even_nums)

# reduce(function, iterable):
# Applies the function cumulatively to reduce the iterable to a single value
# Comes from the functools module

from functools import reduce

product = reduce(lambda x, y: x * y, nums)
print("Product using reduce:", product) 

# More readable example with a named function
def add(x, y):
    return x + y

total = reduce(add, nums)
print("Sum using reduce and named function:", total)  # 10

# We can also combine them
combined = list(map(lambda x: x * 2, filter(lambda x: x > 2, nums)))
print("Double of numbers > 2:", combined)