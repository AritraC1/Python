# Sum of Digits of a Number
# Given a number n, find the sum of its digits.

def sum_of_digits(n):
    sum = 0
    
    while n != 0:
        # Extract the last digit
        last = n % 10

        # Add last digit to sum
        sum += last

        # Remove the last digit
        n //= 10

    return sum

if __name__ == "__main__":
    num = int(input("Enter the number = "))

    print("The sum of digits of", num, "is =", sum_of_digits(num))