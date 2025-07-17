# @property
# Allows you to access a method like an attribute. Used to compute values on-the-fly, while hiding implementation.

'''
Syntax:

class MyClass:
    @property
    def attribute(self):
        return computed_value

Use case: 

Hide computation logic, make API cleaner.
'''

class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def area(self):
        print("Calculating area...")
        return 3.1415 * self._radius ** 2


c = Circle(5)
print("Area:", c.area)  # No () — looks like an attribute