# Generators

'''
A generator is a special type of iterator that yields values one at a time using the `yield` keyword. They are memory-efficient and lazy — meaning values are produced only when needed.

Why Use Generators?
- Efficient looping over large datasets
- Useful for streaming data
- Avoids loading everything into memory at once

yield vs return
- `return` exits the function completely.
- `yield` pauses the function, saving its state for the next call.

'''

# Simple Generator Function
def count_up_to(n):
    # Generator that counts from 1 to n.
    print("\nStarting count:")
    for i in range(1, n+1):
        yield i

# Test
for num in count_up_to(3):
    print("Yielded:", num)

print()

# Generator Expression (like list comp)
squares = (x * x for x in range(5))  # Note: () not []

for val in squares:
    print("Square:", val)

print()

# Using next() to Manually Get Values
gen = count_up_to(2)
print(next(gen))  # 1
print(next(gen))  # 2
# print(next(gen))  # StopIteration