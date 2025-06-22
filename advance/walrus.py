# Walrus Operator
# It allows you to assign and return a value in the same expression. 
# This can help reduce redundancy and sometimes improve performance or readability.

# Syntax
# variable := expression

# Example 1: While Loop

# Without the walrus operator:
line = input("Enter something: ")
while line != "quit":
    print(f"You said: {line}")
    line = input("Enter something: ")

# With the walrus operator:
while (line := input("Enter something: ")) != "quit":
    print(f"You said: {line}")


# Example 2: In List Comprehensions
# Create a list of lengths for words longer than 3 letters
words = ["apple", "is", "a", "fruit"]
lengths = [n for word in words if (n := len(word)) > 3]
print(lengths)