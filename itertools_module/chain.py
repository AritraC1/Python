# Chain
# Combines multiple iterables into a single sequence. Useful for flattening (means taking multiple sequences, like lists of numbers and combining them into one single sequence, without any nested structure).

from itertools import chain

a = [1, 2]
b = [3, 4]
c = [5]

combined = list(chain(a, b, c))
print("Chained:", combined)