# reverse digits of a number
# Given an Integer n, find the reverse of its digits.

def reversed_number(n):
    rev = 0
    
    while n != 0:
        length = len(str(abs(n)))
        last = n%10
        rev = rev + last*(10 ** (length-1))
        n = n // 10

    return rev

if __name__ == "__main__":
    num = int(input("Enter number = "))

    print("The reverse of the given number is", reversed_number(num))



