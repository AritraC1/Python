# Conditionals
# Conditionals let your program make decisions.
# They run different blocks of code based on conditions (True or False).
# The main keywords are: if, elif, and else.

# Basic if statement
print("Basic if statement:")
age = 18
if age >= 18:
    print("You are an adult.")
print()

# if-else statement
print("if-else statement:")
age = 16
if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")
print()

# if-elif-else ladder
print("if-elif-else ladder:")
score = 75
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")
print()

# Nested conditionals
print("Nested conditionals:")
num = 10
if num > 0:
    print("Positive number")
    if num % 2 == 0:
        print("It is also even.")
    else:
        print("It is also odd.")
else:
    print("Non-positive number")
print()

# Using logical operators (and, or, not)
print("Logical operators in conditionals:")
temperature = 25
is_sunny = True
if temperature > 20 and is_sunny:
    print("It's a nice sunny day.")
elif temperature > 20 and not is_sunny:
    print("Warm but not sunny.")
else:
    print("Not warm.")
print()

# Conditional expressions (ternary operator)
print("Conditional expressions (ternary operator):")
age = 17
status = "Adult" if age >= 18 else "Minor"
print("Status:", status)
print()

# Multiple conditions with membership operator
print("Using membership operators in conditionals:")
fruit = "apple"
if fruit in ["apple", "banana", "cherry"]:
    print(f"{fruit} is a common fruit.")
else:
    print(f"{fruit} is not in the list.")
print()

# Truthy and Falsy values in conditionals
print("Truthy and Falsy values:")
value = []
if value:
    print("Value is True")
else:
    print("Value is False (empty or zero)")
print()

# Comparing variables
print("Comparing variables:")
a = 5
b = 10
if a == b:
    print("a equals b")
elif a > b:
    print("a is greater than b")
else:
    print("a is less than b")
print()

# Using 'pass' in conditionals (placeholder)
print("Using pass statement:")
x = 10
if x > 0:
    pass  # Do nothing for now
else:
    print("x is not positive")
print()