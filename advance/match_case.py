# Match Case in Python ((Pattern Matching))

# match-case is similar to switch-case but far more powerful.
# It allows structural pattern matching — matching patterns like:
# - literals (e.g. 200, "hello")
# - tuples/lists
# - dictionaries
# - classes / dataclasses
# - nested structures
# - and more, with optional conditions ("guards")

# Basic syntax:
# match <expression>:
#     case <pattern_1>:
#         <block>
#     case <pattern_2>:
#         <block>
#     case _: # The underscore (_) is a wildcard that matches anything (like "else").
#         <default block>

# Matching Integer Literals
def http_status(code: int) -> str:
    match code:
        case 200:
            return "OK"
        case 404:
            return "Not Found"
        case 500:
            return "Server Error"
        case _:
            return "Unknown status code"

print(http_status(200))
print(http_status(404))
print(http_status(123))

# Matching Tuples and Destructuring
def point_location(point: tuple[int, int]) -> str:
    match point:
        case (0, 0):
            return "Origin"
        case (0, y):
            return f"On Y-axis at y = {y}"
        case (x, 0):
            return f"On X-axis at x = {x}"
        case (x, y):
            return f"Point at ({x}, {y})"

print(point_location((0, 0)))
print(point_location((0, 5)))
print(point_location((4, 0)))
print(point_location((3, 7)))

# Matching Dictionaries
def describe_user(user: dict) -> str:
    match user:
        case {"role": "admin", "active": True}:
            return "Active admin user"
        case {"role": "admin"}:
            return "Inactive admin user"
        case {"role": "guest"}:
            return "Guest user"
        case _:
            return "Unknown user"

print(describe_user({"role": "admin", "active": True}))
print(describe_user({"role": "admin", "active": False}))
print(describe_user({"role": "guest"}))
print(describe_user({"role": "other"}))

# Matching with Classes and Dataclasses
from dataclasses import dataclass

@dataclass
class Animal:
    name: str

@dataclass
class Dog(Animal):
    breed: str

@dataclass
class Cat(Animal):
    color: str

def identify_pet(pet: Animal) -> str:
    match pet:
        case Dog(name=name, breed=breed):
            return f"A dog named {name}, breed {breed}"
        case Cat(name=name, color=color):
            return f"A cat named {name}, color {color}"
        case Animal(name=name):
            return f"Some other animal named {name}"
        case _:
            return "Not an animal"

print(identify_pet(Dog(name="Rex", breed="Husky")))
print(identify_pet(Cat(name="Luna", color="Gray")))
print(identify_pet(Animal(name="Unknown")))

# Match with Guards (if conditions)

# In Python's pattern matching (`match-case`), a "guard" is an **if condition**
# that adds extra constraints to a pattern.
# Even if a pattern matches structurally, the guard must also evaluate to True.

# Syntax:
# case <pattern> if <condition>:
#     <block>

# This is useful when multiple patterns could match the structure,
# but you want to apply additional logic to choose the correct one.

def check_number(num: int) -> str:
    match num:
        case x if x < 0:  # This is a guard (extra condition: x must be < 0)
            return "Negative number"
        case x if x == 0:  # This is a guard (x must be exactly 0)
            return "Zero"
        case x if x > 0: # This is a guard (x must be > 0)
            return "Positive number"
        case _: # No guard; matches anything (wildcard)
            return "Not a number"

print(check_number(-5))
print(check_number(0))
print(check_number(8))
