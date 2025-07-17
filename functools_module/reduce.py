# Reduce
# Applies a function cumulatively to the items of an iterable. Used for folding/reducing to a single value.

from functools import reduce

# Sum of numbers
nums = [1, 2, 3, 4]

total = reduce(lambda x, y: x + y, nums)
print("Sum using reduce:", total)