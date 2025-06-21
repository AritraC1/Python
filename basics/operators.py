# Operators

## Arithmetic Operators - Used to perform mathematical operations
a = 10
b = 3

print("Arithmetic Operators:")
print("Addition: a + b = ", a + b)
print("Subtraction: a - b = ", a - b)
print("Multiplication: a * b = ", a * b)
print("Division: a / b = ", a / b)
print("Floor Division: a // b = ", a // b)
print("Modulus: a % b = ", a % b)
print("Exponentiation: a ** b = ", a ** b) # a**b = a^b
print()

## Comparison (Relational) Operators - Used to compare values; returns True or False
print("Comparison Operators:")
print("Equal to: a == b = ", a == b)
print("Not equal to: a != b = ", a != b)
print("Greater than: a > b = ", a > b)
print("Less than: a < b = ", a < b)
print("Greater than or equal to: a >= b = ", a >= b)
print("Less than or equal to: a <= b = ", a <= b)
print()

## Assignment Operators - Used to assign values to variables
print("Assignment Operators:")
c = 5
print("Initial value: c = ", c)
c += 2  # c = c + 2
print("Add and assign: c += 2 = ", c)
c *= 3  # c = c * 3
print("Multiply and assign: c *= 3 = ", c)
c -= 4  # c = c - 4
print("Subtract and assign: c -= 4 = ", c)
c /= 2  # c = c / 2
print("Divide and assign: c /= 2 = ", c)
print()

## Logical Operators - Used to combine conditional statements
x = True
y = False
print("Logical Operators:")
print("Logical AND: x and y = ", x and y)
print("Logical OR: x or y = ", x or y)
print("Logical NOT: not x = ", not x)
print()

## Bitwise Operators - Operate on bits
p = 5    # 0101 in binary
q = 3    # 0011 in binary
print("Bitwise Operators:")
print("Bitwise AND: p & q = ", p & q)
print("Bitwise OR: p | q = ", p | q)
print("Bitwise XOR: p ^ q = ", p ^ q)
print("Bitwise NOT: ~p = ", ~p)
print("Left Shift: p << 1 = ", p << 1)
print("Right Shift: p >> 1 = ", p >> 1)
print()

## Membership Operators - Check for membership in a sequence (like list, string, tuple
text = "python"
print("Membership Operators:")
print("'y' in text = ", 'y' in text)
print("'z' not in text = ", 'z' not in text)
print()

## Identity Operators - Compare memory locations
m = [1, 2, 3]
n = m
o = [1, 2, 3]
print("Identity Operators:")
print("m is n = ", m is n)
print("m is o = ", m is o)
print("m == o = ", m == o)