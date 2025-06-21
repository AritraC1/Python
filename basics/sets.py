# Sets
# A set is an unordered collection of unique, immutable elements.
# Sets are mutable (you can add or remove elements), but they cannot contain duplicates.

# Creating Sets
print("Creating sets:")
set1 = {1, 2, 3, 4}
set2 = set([3, 4, 5, 6])  # Using set() constructor
print("Set 1:", set1)
print("Set 2:", set2)
print()

# No Duplicates Allowed
print("Demonstrating uniqueness:")
duplicate_set = {1, 2, 2, 3, 3, 3}
print("Set with duplicates removed:", duplicate_set)
print()

# Adding Elements
print("Adding elements:")
my_set = {1, 2}
my_set.add(3)
my_set.add(2)  # Will not be added again
print("After additions:", my_set)
print()

# Removing Elements
print("Removing elements:")
my_set.remove(1)  # Removes 1
# my_set.remove(10)  # Error if not present
my_set.discard(10)  # No error if not present
print("After removals:", my_set)
print()

# Set Operations
print("Set operations:")
a = {1, 2, 3}
b = {3, 4, 5}

print("Set A:", a)
print("Set B:", b)

print("Union (A | B):", a | b)            # or a.union(b)
print("Intersection (A & B):", a & b)     # or a.intersection(b)
print("Difference (A - B):", a - b)       # or a.difference(b)
print("Symmetric Difference (A ^ B):", a ^ b)  # or a.symmetric_difference(b)
print()

# Checking Membership
print("Membership testing:")
print("Is 2 in set A?", 2 in a)
print("Is 5 not in set A?", 5 not in a)
print()

# Set Methods Summary
print("Set methods summary:")
sample_set = {10, 20, 30}
sample_set.update([40, 50])  # Adds multiple items
print("After update:", sample_set)

sample_set.clear()
print("After clear:", sample_set)

copy_set = {1, 2, 3}
copied = copy_set.copy()
print("Original set:", copy_set)
print("Copied set:", copied)
print()

# Frozen Set (Immutable Set)
print("Frozen sets:")
frozen = frozenset([1, 2, 3])
print("Frozen set:", frozen)
# frozen.add(4)  # Will raise an error because it's immutable
print()

# Set Comprehension
print("Set comprehension:")
squared = {x**2 for x in range(6)}
print("Squares set:", squared)
print()

# Practical Example: Removing duplicates from a list
print("Use case: Removing duplicates from a list:")
numbers = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = set(numbers)
print("Original list:", numbers)
print("Unique values:", unique_numbers)
print()