# Args & Kwargs

'''
1. *args:
   - Allows a function to accept any number of positional arguments.
   - Inside the function, args is a tuple.

2. **kwargs:
   - Allows a function to accept any number of keyword (named) arguments.
   - Inside the function, kwargs is a dictionary.

Importance of the * (single star) and ** (double star)
- The * (asterisk) is used to **pack** or **unpack** positional arguments.
    - When used in function parameters: *args collects extra positional arguments into a tuple.
    - When used in function calls: * unpacks a list or tuple into individual positional arguments.

- The ** (double asterisk) is used to **pack** or **unpack** keyword arguments.
    - When used in function parameters: **kwargs collects extra keyword arguments into a dictionary.
    - When used in function calls: ** unpacks a dictionary into individual keyword arguments.

Why use them?
- To write flexible functions that can handle variable numbers of arguments.

'''

# Using *args (Positional)
def add_numbers(*args):
    # Adds any number of numbers passed as positional arguments.
    print("\nPositional args received:", args)
    return sum(args)

print("Sum:", add_numbers(5, 10, 15))

print()

# Using **kwargs (Keyword)
def display_info(**kwargs):
    # Prints all keyword arguments passed.
    print("Keyword args received:", kwargs)
    for key, value in kwargs.items():
        print(f"{key}: {value}")

display_info(name="Alice", age=28, country="USA")

print()

# Using both *args and **kwargs
def full_example(*args, **kwargs):
    print("Args:", args)
    print("Kwargs:", kwargs)

full_example(1, 2, 3, a=10, b=20)

print()

# Argument Unpacking using * and **
def greet(first, middle, last):
    print(f"Hello {first} {middle} {last}!")

# Using * to unpack a tuple
name_tuple = ("John", "F.", "Kennedy")
greet(*name_tuple)

# Using ** to unpack a dictionary
name_dict = {"first": "Elon", "middle": "Reeve", "last": "Musk"}
greet(**name_dict)

print()

# Packing with * and ** in function calls
def show_all(a, b, c):
    print(f"a: {a}, b: {b}, c: {c}")

# Packing a tuple
values = (1, 2, 3)
show_all(*values)  # Equivalent to show_all(1, 2, 3)

# Packing a dictionary
person = {'a': 'Alice', 'b': 'Bob', 'c': 'Charlie'}
show_all(**person)  # Equivalent to show_all(a='Alice', b='Bob', c='Charlie')