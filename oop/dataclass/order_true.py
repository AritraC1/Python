# Comparison & Ordering with order=True
# Adds comparison methods: <, <=, >, >=
# Use case: Sort lists of objects easily.

from dataclasses import dataclass

@dataclass(order=True)
class Book:
    title: str
    pages: int

b1 = Book("Python", 300)
b2 = Book("C++", 200)

print(b1 > b2)  # True (compares based on order of fields)