# Sum of squares of first n natural numbers

n = int(input("Enter the value of n = "))

sum = 0
for i in range(0, n+1):
    sum = sum + (i**2)
    i = i+1

print("The Sum of squares of first n natural numbers =", sum)