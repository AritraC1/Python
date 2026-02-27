# sum of n natural numbers

n = int(input("Enter the number = "))

sum = 0
for i in range(0,n+1):
    sum = sum + i
    i = i+1

print("The sum of n natural numbers = ", sum)