# @property.setter
# Allows setting a property value via attribute-style access. Useful when you want to validate or process input.

class Person:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        print("Getting name...")
        return self._name

    @name.setter
    def name(self, value):
        print("Setting name...")
        if not isinstance(value, str):
            raise ValueError("Name must be a string.")
        self._name = value


p = Person("Alice")
print(p.name)       # Get
p.name = "Bob"      # Set with validation
# p.name = 123      # Error: Name must be a string