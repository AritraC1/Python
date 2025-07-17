# __slots__ vs __dict__

'''
__dict__:
Every Python object by default stores attributes in a dynamic dictionary called `__dict__`. This allows flexible, runtime addition/removal of attributes.

__slots__:
`__slots__` is a way to tell Python to pre-allocate a fixed set of attributes. It avoids creating `__dict__`, making instances lighter and faster.
'''

# Default class behavior with __dict__
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p = Person("Alice", 30)

print("[__dict__] p.__dict__:", p.__dict__)

# Dynamically add new attributes
p.country = "India"
print("[__dict__] After adding 'country':", p.__dict__)

print()

# Memory-efficient class using __slots__
class PersonSlots:
    __slots__ = ['name', 'age']

    def __init__(self, name, age):
        self.name = name
        self.age = age

s = PersonSlots("Bob", 25)

# No __dict__ exists
# print(s.__dict__)  # AttributeError

print("[__slots__] s.name:", s.name)

# Cannot add new attributes
# s.country = "India"  # AttributeError: 'PersonSlots' object has no attribute 'country'

print()

# Compare memory usage
import sys

class Regular:
    def __init__(self):
        self.a = 1
        self.b = 2

class Slotted:
    __slots__ = ['a', 'b']
    def __init__(self):
        self.a = 1
        self.b = 2

r = Regular()
s = Slotted()

print("[Memory] Regular instance size:", sys.getsizeof(r))
print("[Memory] Slotted instance size:", sys.getsizeof(s))

# Note: For detailed memory profiling use `memory_profiler` or `pympler` packages.

print()

# Inheritance with __slots__
class Base:
    __slots__ = ['x']

class Child(Base):
    __slots__ = ['y']

c = Child()
c.x = 10
c.y = 20

print("[Inheritance] c.x + c.y =", c.x + c.y)

# c.z = 30  # AttributeError: 'Child' object has no attribute 'z'

'''
Use __slots__ when:
- You're creating **millions of instances** (e.g., nodes in a tree).
- Memory is critical (e.g., embedded systems, data processing).
- You want to prevent dynamic attributes and enforce strict models.

Avoid __slots__ when:
- You need dynamic attributes.
- You plan to use mixins that rely on `__dict__` or expect flexibility.
- You rely on libraries (like some serializers) that expect `__dict__`.
'''