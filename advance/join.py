# Join

# The join() method is used to combine elements of a sequence (like a list or tuple)
# into a single string, with a specified separator between each element.

# Syntax:
# 'separator'.join(iterable)

# - The iterable must contain only strings (not integers or other types).
# - The separator is placed **between** each pair of elements.
# - join() does not modify the original list — it returns a new string.

# Joining a list of strings
words = ['Python', 'is', 'awesome']
result = ' '.join(words)
print("Joined with space:", result)  # Python is awesome

# Joining with commas
items = ['apple', 'banana', 'cherry']
csv = ','.join(items)
print("Joined with commas:", csv)  # apple,banana,cherry

# Joining characters of a string
chars = list("join")
joined = '-'.join(chars)
print("Joined characters:", joined)  # j-o-i-n

# Joining with no separator
nums = ['1', '2', '3']
joined_nums = ''.join(nums)
print("Joined with no separator:", joined_nums)  # 123

# Attempting to join non-string values will raise an error
# Example (will raise TypeError):
# invalid = '-'.join([1, 2, 3])  ❌

# Fix by converting to strings first
mixed = [1, 2, 3]
fixed = '-'.join(str(n) for n in mixed)
print("Joined numbers after conversion:", fixed)