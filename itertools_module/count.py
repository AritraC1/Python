# Count
# Creates an infinite iterator that returns evenly spaced values. Like an endless version of range().

from itertools import count

for i in count(start=5, step=2):
    print(i)
    if i > 10:
        break