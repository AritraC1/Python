# Password Generator

import random
import string

def generate_password(length=12, use_upper=True, use_digits=True, use_symbols=True):
    chars = string.ascii_lowercase
    
    if use_upper:
        chars += string.ascii_uppercase

    if use_digits:
        chars += string.digits
        
    if use_symbols:
        chars += string.punctuation

    if length < 1:
        return ""

    return ''.join(random.choice(chars) for _ in range(length))


if __name__ == "__main__":
    print("Welcome to the Password Generator!")
    try:
        length = int(input("Enter desired password length (e.g. 6): "))
    except ValueError:
        print("Invalid input. Using default length 12.")
        length = 7
    
    use_upper = input("Include uppercase letters? (y/n): ").lower() == 'y'
    use_digits = input("Include digits? (y/n): ").lower() == 'y'
    use_symbols = input("Include symbols? (y/n): ").lower() == 'y'

    password = generate_password(length, use_upper, use_digits, use_symbols)
    print(f"Generated password: {password}")

