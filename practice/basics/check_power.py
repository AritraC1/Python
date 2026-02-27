# Check Power
# Given two positive numbers x and y, check if y is a power of x or not.

def check_power(x, y):
    for i in range (0, x):
        if x**i == y:
            return True
    
    return False


if __name__ == "__main__":
    x = int(input("Enter number = "))
    y = int(input("Enter number = "))

    print(check_power(x, y))
