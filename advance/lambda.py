# Lambda Functions in Python

# A lambda function is a small, anonymous function defined using the `lambda` keyword.
# It can take any number of arguments but must have only one expression.
# Syntax:
# lambda arguments: expression

# Lambda functions are often used for:
# Short, throwaway functions
# Functions passed as arguments (e.g., to map(), filter(), sorted(), etc.)
# In-place function definitions without naming

# Normal function vs lambda function
def add(x, y):
    return x + y

add_lambda = lambda x, y: x + y

print("Using regular function:", add(3, 4))         # 7
print("Using lambda function:", add_lambda(3, 4))   # 7
print()

# Lambda in map()
numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x ** 2, numbers))
print("Squares using lambda + map():", squares)  # [1, 4, 9, 16, 25]
print()

# Lambda in filter()
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers using lambda + filter():", even_numbers)  # [2, 4]
print()

# Lambda in sorted() with custom key
words = ['apple', 'banana', 'kiwi', 'grape']
sorted_by_length = sorted(words, key=lambda word: len(word))
print("Words sorted by length:", sorted_by_length)  # ['kiwi', 'grape', 'apple', 'banana']
print()

# Lambda with if-else (ternary)
sign = lambda n: "positive" if n > 0 else "zero" if n == 0 else "negative"
print("Sign of -3:", sign(-3))   # negative
print("Sign of 0:", sign(0))     # zero
print("Sign of 5:", sign(5))     # positive