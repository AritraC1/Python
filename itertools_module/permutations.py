# Permutations
# Generates all possible orderings (permutations) of a given length.

from itertools import permutations

items = ['A', 'B']
perm = list(permutations(items))
print("Permutations:", perm)