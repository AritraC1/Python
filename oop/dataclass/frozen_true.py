# Immutable Dataclasses with frozen=True
# Makes the dataclass immutable like a tuple. Fields cannot be changed after creation.
# Use case: Hashable, read-only data (e.g., coordinates, config objects)

from dataclasses import dataclass

@dataclass(frozen=True)
class Point:
    x: int
    y: int

p = Point(1, 2)
# p.x = 10  # Error: cannot assign to field