# Dictionary Merge and Update in Python

# Two common ways to combine dictionaries:
# 1. Merging (creates a new dictionary)
# 2. Updating (modifies an existing dictionary)

# 🔧 Sample dictionaries
a = {'x': 1, 'y': 2}
b = {'y': 20, 'z': 3}

# MERGE (Non-destructive / New Dictionary)

# Merging combines two dictionaries into a new one.
# The original dictionaries are NOT changed.
# If there are duplicate keys, the right-hand side wins.

# Method 1: Using `|` operator
merged1 = a | b
print("Merged using a | b: ", merged1)
print()

# Method 2: Using unpacking
merged2 = {**a, **b}
print("Merged using {**a, **b}: ", merged2)
print()

# Original dictionaries remain unchanged
print("Original a: ", a)
print("Original b: ", b)
print()

# UPDATE (In-place Modification)

# Updates the original dictionary directly (in-place).
# Keys in the original dict are overwritten by those in the new dict.
# Method: `dict1.update(dict2)`
# Returns None.

# Update a with b
a.update(b)  # modifies 'a'
print("After a.update(b): ", a)
print()

# Dictionary 'a' is now changed
# Dictionary 'b' remains unchanged
print("Updated a: ", a)
print("Unchanged b: ", b)


'''
Summary: 

# MERGE:
# - Use `|` or `{**a, **b}`
# - Returns a new dict
# - Original dicts stay the same

# UPDATE:
# - Use `a.update(b)`
# - Modifies 'a' directly
# - Overwrites keys in 'a' if also in 'b'
'''