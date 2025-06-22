# Object oriented Programming (OOP)

# THEORY:
# OOP is a programming paradigm based on the concept of "objects",
# which contain data (attributes) and behavior (methods).

# Key Concepts:
# 1. Class        - Blueprint for creating objects.
# 2. Object       - Instance of a class.
# 3. Encapsulation - Binding data and functions together.
# 4. Inheritance  - One class can inherit properties from another.
# 5. Polymorphism - Methods behave differently based on the object.
# 6. Abstraction  - Hiding internal implementation from the user.

# Other Concepts:
# 1. Self
# Self is a reference to the current instance of the class. 
# It is used to access instance variables and methods inside the class.
# To differentiate instance variables from local variables and it binds the data (attributes) to the object.
# In Python, you must explicitly include self in method definitions and calls, in Java or C++, this is implicitly available.

# 2. __init__ Method
# It’s a constructor in Python.
# Automatically called when a new object is created.
# Used to initialize the object’s state (set attributes).

#3. Dunder Methods (Double Underscore Methods)
# "Dunder" = Double UNDERscores → __method__
# Special methods in Python used to customize class behavior.
# They enable Python's operator overloading and built-in behavior.


# 1. DEFINING A CLASS
class Person:
    # Constructor (__init__) - called when an object is created
    def __init__(self, name, age):
        self.name = name  # instance variable
        self.age = age

    # Method
    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

# Creating an object (instance) of Person
person1 = Person("Alice", 30)
person1.greet()

# 2. ENCAPSULATION (Use underscore (_) for protected and double underscore (__) for private attributes)
class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance  # private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient funds.")

    def get_balance(self):
        return self.__balance

acc = Account("Bob", 1000)
acc.deposit(500)
acc.withdraw(200)
print("Balance:", acc.get_balance())

# 3. INHERITANCE
class Animal:
    def speak(self):
        print("The animal makes a sound.")

# Dog inherits from Animal
class Dog(Animal):
    def speak(self):
        print("The dog barks.")

# Cat inherits from Animal
class Cat(Animal):
    def speak(self):
        print("The cat meows.")

dog = Dog()
cat = Cat()
dog.speak()
cat.speak()

# 4. POLYMORPHISM - Same method name, different behavior
def animal_sound(animal):
    animal.speak()

animal_sound(dog)  # barks
animal_sound(cat)  # meows

# 5. ABSTRACTION (with ABC module)
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

rect = Rectangle(4, 5)
print("Rectangle area:", rect.area())

# 6. CLASS VS INSTANCE VARIABLES
class Car:
    wheels = 4  # class variable (shared across all instances)

    def __init__(self, brand):
        self.brand = brand  # instance variable (unique to object)

car1 = Car("Toyota")
car2 = Car("Ford")
print("Car1:", car1.brand, "| Wheels:", car1.wheels)
print("Car2:", car2.brand, "| Wheels:", car2.wheels)


# 7. STATIC & CLASS METHODS
class MathUtils:
    @staticmethod
    def add(x, y):
        return x + y

    @classmethod
    def info(cls):
        print("This is a Math utility class.")

print("Add:", MathUtils.add(10, 5))
MathUtils.info()

# 8. DUNDER (MAGIC) METHODS
class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    def __str__(self):
        return f"{self.title} - {self.pages} pages"

    def __len__(self):
        return self.pages

book = Book("Python OOP", 350)
print(book) # calls __str__()
print("Pages:", len(book)) # calls __len__()