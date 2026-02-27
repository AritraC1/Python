# Find Closest to n and Divisible by m
# Given two integers n and m (m != 0). Find the number closest to n and divisible by m. If there is more than one such number, then output the one having maximum absolute value.

n = int(input("Enter the value of n = "))
m = int(input("Enter the value of m = "))

q = n // m

n1 = m * q
n2 = m * (q + 1)

# Choose the closest
if abs(n - n1) < abs(n - n2):
    result = n1
elif abs(n - n1) > abs(n - n2):
    result = n2
else:
    # If equally close, choose one with greater absolute value
    result = n1 if abs(n1) > abs(n2) else n2

print("Solution:", result)