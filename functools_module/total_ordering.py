# Total Ordering
# Adds missing comparison methods to a class based on one or two. You define __eq__ and one of (__lt__, __le__, __gt__, __ge__), and it fills in the rest.

from functools import total_ordering

@total_ordering
class Person:
    def __init__(self, age):
        self.age = age

    def __eq__(self, other):
        return self.age == other.age

    def __lt__(self, other):
        return self.age < other.age


p1 = Person(25)
p2 = Person(30)

print(p1 < p2)   # True
print(p1 <= p2)  # True
print(p1 == p2)  # False
print(p1 >= p2)  # False