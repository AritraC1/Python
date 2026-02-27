# Check Prime Number

def check_prime(n):
    if n <= 1:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True

if __name__ == "__main__":
    n = int(input("Enter number = "))

    if (check_prime(n) == False):
        print("The given number is not a prime number")
    else: 
        print("The given number is a prime number")
