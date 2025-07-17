# Product
# Cartesian product of input iterables (like nested loops). Can be used for grid search, all combinations of settings, etc.

from itertools import product

result = list(product([1, 2], ['a', 'b']))
print("Product:", result)