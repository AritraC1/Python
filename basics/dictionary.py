# Dictionary
# A dictionary in Python is an unordered, mutable, and indexed collection of key-value pairs. 
# It is one of the built-in data types, alongside lists, tuples, and sets.


# Creating a Dictionary
person = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}
print("Initial dictionary:", person)
print()

# Accessing Values
print("Accessing values:")
print("Name:", person["name"])  # Direct access
print("Country (using get):", person.get("country", "Not specified"))  # Safe access
print()

# Modifying Dictionary
print("Modifying dictionary:")
person["age"] = 26 # Update existing value
person["gender"] = "Female" # Add new key-value pair
print("After modification:", person)
print()

# Removing Items
print("Removing items:")
del person["city"] # Removes 'city'
gender = person.pop("gender") # Removes 'gender' and returns its value
print("After deletions:", person)
print("Removed gender:", gender)
print()

# Dictionary Methods
print("Using dictionary methods:")
print("Keys:", person.keys())
print("Values:", person.values())
print("Items:", person.items())
print()

# Looping Through a Dictionary
print("Looping through dictionary:")
for key, value in person.items():
    print(f"{key} => {value}")
print()

# Dictionary Comprehension
print("Dictionary comprehension:")
squares = {x: x**2 for x in range(5)}
print("Squares:", squares)
print()

# Nested Dictionary
print("Nested dictionaries:")
students = {
    "101": {"name": "Bob", "grade": "A"},
    "102": {"name": "Eve", "grade": "B"},
}
print("Student 101 name:", students["101"]["name"])
print()

# Using dict() constructor
print("Using dict constructor:")
config = dict(server="localhost", port=8080)
print("Config dictionary:", config)
print()

# Clearing and Copying
print("Clearing and copying:")
copy_config = config.copy()
config.clear()
print("Original config after clear():", config)
print("Copied config remains intact:", copy_config)
print()

# Common Use Case: Frequency Counter
print("Use case: Counting character frequencies:")
text = "banana"
freq = {}
for char in text:
    freq[char] = freq.get(char, 0) + 1
print("Character frequencies:", freq)
print()

# Dictionary inside list (e.g., JSON-like structure)
print("List of dictionaries:")
people = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 30}
]
for p in people:
    print(f"{p['name']} is {p['age']} years old")
print()

# Use Cases of Dictionaries:
# Storing data with meaningful labels (e.g., JSON)
# Counting frequencies (e.g., word count)
# Lookup tables
# Caching and memoization