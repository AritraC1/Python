# Lists
# A list is a built-in data structure in Python used to store an ordered collection of items
# Lists can hold items of different types (integers, strings, floats, other lists, etc.)
# Lists are mutable, meaning you can change, add, or remove elements after the list is created.
# Elements in a list are indexed starting from 0.

# Creating Lists - You create a list by placing comma-separated values inside square brackets []
li1 = ["apple", "orange", 1, 3, 5, True, False, 6.45]
print(li1)

li2 = [1, 2, 3, 4, 5]
print(li2)

print()

# Basic List Operations

# Accessing Elements
numbers = [10, 20, 30, 40, 50]
print(numbers[0])   # Output: 10 (first element)
print(numbers[3])   # Output: 40 (fourth element)
print(numbers[-1])  # Output: 50 (last element)

print()

# Modifying Elements
numbers[1] = 25
print(numbers)      # Output: [10, 25, 30, 40, 50]

print()

# Adding Elements
# 1. append() adds an element at the end
# 2. insert() adds an element at a specific index
numbers.append(60)
print(numbers)      # Output: [10, 25, 30, 40, 50, 60]

numbers.insert(2, 28)
print(numbers)      # Output: [10, 25, 28, 30, 40, 50, 60]

print()

# Removing Elements
# 1. remove(): removes the first matching value
# 2. pop(): removes by index and returns the element
# 3. del keyword can also be used
numbers.remove(40)
print(numbers)      # Output: [10, 25, 28, 30, 50, 60]

popped = numbers.pop(3)
print(popped)       # Output: 30
print(numbers)      # Output: [10, 25, 28, 50, 60]

del numbers[0]
print(numbers)      # Output: [25, 28, 50, 60]

print()

# List Slicing - You can get a portion (slice) of a list using the colon : operator
my_list = [1, 2, 3, 4, 5, 6]

print(my_list[1:4])   # Output: [2, 3, 4] (from index 1 to 3)
print(my_list[:3])    # Output: [1, 2, 3] (from start to index 2)
print(my_list[3:])    # Output: [4, 5, 6] (from index 3 to end)
print(my_list[-3:])   # Output: [4, 5, 6] (last 3 elements)

print()

# Other Useful List Methods
nums = [5, 3, 8, 6, 3, 2]

# len(list) — length of the list
print(len(nums))        # Output: 6

# count(x) — number of occurrences of x
print(nums.count(3))    # Output: 2

# index(x) — first index of value x
print(nums.index(8))    # Output: 2

# sort() — sort the list in place
nums.sort()
print(nums)             # Output: [2, 3, 3, 5, 6, 8]

# reverse() — reverse the list in place
nums.reverse()
print(nums)             # Output: [8, 6, 5, 3, 3, 2]

print()

# Notes:
# Lists are built-in, can hold mixed data types, and are flexible but slower for numerical tasks.
# Arrays (from array or NumPy) store same-type data, use less memory, and are faster for math operations.
