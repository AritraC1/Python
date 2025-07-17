# Counter
# Dictionary subclass for counting hashable items. Useful for frequency analysis.

from collections import Counter

# Count characters in a string
c = Counter("banana")

print("Counter:", c)  # Counter({'a': 3, 'n': 2, 'b': 1})

# Most common elements
print("Most common:", c.most_common(2))  # [('a', 3), ('n', 2)]