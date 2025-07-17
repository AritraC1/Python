# Cached Property (Python 3.8+)
# Decorator that converts a method into a property that is only computed once. Result is cached and reused on subsequent access. 

from functools import cached_property

class Circle:
    def __init__(self, radius):
        self.radius = radius

    @cached_property
    def area(self):
        print("Calculating area...")
        return 3.1415 * self.radius ** 2


c = Circle(10)
print("Area:", c.area)  # calculates
print("Area again:", c.area)  # uses cached value