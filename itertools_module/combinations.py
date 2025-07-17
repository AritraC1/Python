# Combinations
# Generates all possible combinations (without repetition) of a given length.

from itertools import combinations

items = ['A', 'B', 'C']
comb = list(combinations(items, 2))
print("Combinations:", comb)