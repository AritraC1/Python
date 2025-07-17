# Deque
# - Double-ended queue. Faster appends and pops from both ends compared to lists. Great for implementing queues and stacks.

from collections import deque

# Create deque
d = deque([1, 2, 3])

# Append to the right
d.append(4)

# Append to the left
d.appendleft(0)

print("Deque after appends:", d)  # deque([0, 1, 2, 3, 4])

# Pop from both ends
d.pop()
d.popleft()

print("Deque after pops:", d)  # deque([1, 2, 3])