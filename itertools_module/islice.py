# islice
# Slices an iterator like a list, but without converting to a list. Efficient for large/infinite iterators.

from itertools import islice, count

# Get items 2 through 6 from an infinite counter
for num in islice(count(10), 2, 7):
    print(num)