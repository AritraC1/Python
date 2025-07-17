# namedtuple
# Factory function for creating tuple subclasses with named fields. More readable and self-documenting than using plain tuples.

from collections import namedtuple

# Define a Point with x and y fields
Point = namedtuple("Point", ["x", "y"])

# Create an instance
p = Point(10, 20)

# Access like attributes
print(f"Point: {p}, x = {p.x}, y = {p.y}")

# Namedtuples are immutable like regular tuples
# p.x = 30  # Error