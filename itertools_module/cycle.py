# Cycle
# Repeats the elements of an iterable infinitely.

from itertools import cycle

colors = ["red", "green", "blue"]
cycler = cycle(colors)

for _ in range(6):
    print(next(cycler))
