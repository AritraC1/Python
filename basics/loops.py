# Loops
# Loops let you repeat a block of code multiple times.
# The two main types are: for loops and while loops.

# For loop over a list
print("For loop over a list:")
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
print()

# For loop using range()
print("For loop using range():")
for i in range(5):
    print(i)
print()

# For loop with start, stop, step in range()
print("For loop with start, stop, step:")
for i in range(2, 10, 2):  # From 2 to 9 stepping by 2
    print(i)
print()

# Loop with else clause
print("For loop with else clause:")
for i in range(3):
    print(i)
else:
    print("Loop finished without break")
print()

# While loop
print("While loop:")
count = 0
while count < 5:
    print(count)
    count += 1
print()

# While loop with else
print("While loop with else clause:")
count = 0
while count < 3:
    print(count)
    count += 1
else:
    print("While loop completed normally")
print()

# Breaking out of a loop
print("Breaking out of a loop:")
for i in range(10):
    if i == 5:
        print("Breaking at", i)
        break
    print(i)
print()

# Continue to skip an iteration
print("Using continue to skip an iteration:")
for i in range(6):
    if i % 2 == 0:
        continue  # Skip even numbers
    print(i)
print()

# Nested loops
print("Nested loops:")
for i in range(1, 4):
    for j in range(1, 3):
        print(f"i = {i}, j = {j}")
print()

# Looping over a dictionary
print("Looping over a dictionary:")
person = {"name": "Alice", "age": 25}
for key, value in person.items():
    print(f"{key}: {value}")
print()

# Using pass as a placeholder inside a loop
print("Using pass in a loop:")
for i in range(3):
    pass  # Placeholder, no operation
print("Loop executed but did nothing")
print()