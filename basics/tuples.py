#  Tuples
# A tuple is a collection of ordered, immutable (unchangeable) elements in Python. 
# Tuples are similar to lists, but unlike lists, tuples cannot be changed after creation.

# Creating Tuples
my_tuple = (1, 2, 3)
mixed_tuple = (1, "hello", 3.14)
single_tuple = (5,)  # Must include comma for single element
packed_tuple = 1, 2, 3  # Tuple packing

print("my_tuple:", my_tuple)
print("mixed_tuple:", mixed_tuple)
print("single_tuple:", single_tuple)
print("packed_tuple:", packed_tuple)

# Accessing Elements
print("First element:", my_tuple[0])
print("Last element (negative index):", my_tuple[-1])

# Tuple Operations
t1 = (1, 2, 3)
t2 = (4, 5)

print("Concatenation:", t1 + t2)
print("Repetition:", t1 * 2)
print("Check if 2 in t1:", 2 in t1)
print("Length of t1:", len(t1))

# Tuple Methods
t = (1, 2, 2, 3, 4)
print("Count of 2:", t.count(2))
print("Index of 3:", t.index(3))

# Using Tuple in a Function
def min_max(numbers):
    return (min(numbers), max(numbers))

result = min_max([4, 1, 7, 0])
print("Min and Max:", result)

# Tuple Unpacking
person = ("Alice", 25, "Engineer")
name, age, job = person

print("Name:", name)
print("Age:", age)
print("Job:", job)

# Why Use Tuples?
# - Tuples are immutable
# - Can be used as dictionary keys
location = (37.7749, -122.4194)  # Tuple used for coordinates
locations_dict = {
    location: "San Francisco"
}
print("Location Dictionary:", locations_dict)
