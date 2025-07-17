# Dataclass
# Automatically generates init, repr, eq, and other methods. Reduces boilerplate code for classes used to store data.
# Use case: Simple data containers with type hints.

from dataclasses import dataclass

@dataclass
class Person:
    name: str
    age: int

# Usage
p = Person("Alice", 30)
print(p)             # Person(name='Alice', age=30)
print(p.name)        # Alice
print(p.age)         # 30

# Default Values & Field Ordering
# You can set default values just like normal class attributes. Fields without defaults must come before fields with defaults.
# Use case: Optional parameters without writing your own __init__.

@dataclass
class User:
    username: str
    is_admin: bool = False

u1 = User("john_doe")
print(u1)