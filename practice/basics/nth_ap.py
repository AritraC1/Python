# Nth term of AP from First Two Terms
# Given two integers a1 and a2, the first and second terms of an Arithmetic Series respectively, the problem is to find the nth term of the series. 

a1 = int(input("Enter 1st number: "))
a2 = int(input("Enter second number: "))
n = int(input("Enter nth number: "))

d = a2 - a1
nth_term = a1 + (n - 1) * d

print("The", n, "th term is:", nth_term)

