# Enums

# Enum (short for "enumeration") is a class that represents a set of constant values.
# Useful when you have a fixed set of related names (like days, states, statuses, etc.)
# Enums make the code more readable and less error-prone than using plain strings or numbers.

# Enums are defined using the `Enum` class from the `enum` module.
# Each member has a name and a value.

# Enums are immutable and unique by name.
# You can compare them by identity or value.

from enum import Enum, auto

# Defining an enum using explicit values
class Status(Enum):
    PENDING = 1
    IN_PROGRESS = 2
    COMPLETED = 3

# Defining an enum using auto-assigned values
class Direction(Enum):
    NORTH = auto()
    EAST = auto()
    SOUTH = auto()
    WEST = auto()

# Accessing enum members
print("Status.PENDING =", Status.PENDING)
print("Status.PENDING.name =", Status.PENDING.name)
print("Status.PENDING.value =", Status.PENDING.value)

# Comparing enum members
if Status.PENDING == Status(1):
    print("Status.PENDING equals Status(1)")

# Iterating through enum members
print("All directions:")
for d in Direction:
    print(d.name, "=", d.value)

# Enums are type-safe
def move(direction: Direction):
    if direction == Direction.NORTH:
        print("Moving north!")
    elif direction == Direction.SOUTH:
        print("Moving south!")
    else:
        print("Moving in some other direction.")

move(Direction.NORTH)
move(Direction.EAST)

'''
Summary:

Enum is used to define a set of named, constant values
Use the Enum class from the enum module to define them
Access name with .name and value with .value
Use auto() to automatically assign values
Enums can be compared by identity or value
Enums are iterable and type-safe
'''