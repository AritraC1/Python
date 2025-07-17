# Repeat
# Repeats a single value either indefinitely or a specified number of times.

from itertools import repeat

for item in repeat("hello", 3):
    print(item)