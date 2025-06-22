# EXCEPTION HANDLING in Python

# THEORY:
# Exceptions are errors detected during execution.
# Python provides a way to handle these errors using try-except blocks
# so that the program doesn't crash and can respond gracefully.

# 1. BASIC STRUCTURE

# Syntax:
# try:
#     # Code that might cause an exception
# except SomeException:
#     # Code to run if that exception occurs
# else:
#     # Code to run if NO exception occurs
# finally:
#     # Code that always runs, regardless of exceptions

# 2. EXAMPLE: Division by Zero
try:
    num = 10
    denom = 0
    result = num / denom
except ZeroDivisionError:
    print("Error: You tried to divide by zero.")
else:
    print("Division successful, result is:", result)
finally:
    print("Finished division operation.")

# Output:
# Error: You tried to divide by zero.
# Finished division operation.

# 3. MULTIPLE EXCEPTIONS
try:
    my_list = [1, 2, 3]
    print(my_list[5])  # IndexError
except IndexError:
    print("Error: Index out of range.")
except ValueError:
    print("Error: Value error.")
finally:
    print("Attempted to access list.")

# 4. CATCHING ANY EXCEPTION
try:
    x = int("abc")  # This will raise ValueError
except Exception as e:
    print("An error occurred:", e)

# 5. CUSTOM EXCEPTION HANDLING - You can raise your own exceptions using `raise`
def check_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative.")
    else:
        print(f"Valid age: {age}")

try:
    check_age(-5)
except ValueError as e:
    print("Custom Exception:", e)

# 6. TRY-EXCEPT with FILE I/O
try:
    with open("nonexistent_file.txt", "r") as file:
        data = file.read()
except FileNotFoundError:
    print("Error: The file does not exist.")
else:
    print("File read successfully.")
finally:
    print("File operation attempt finished.")

# 7. FINALLY BLOCK USE CASE - Ensures resources are cleaned up
try:
    file = open("example.txt", "w")
    file.write("Writing something...")
except IOError:
    print("File write error.")
finally:
    file.close()  # Important for resource management
    print("File closed.")

# 8. NESTED TRY-EXCEPT
try:
    try:
        num = int("abc")
    except ValueError:
        print("Inner: Invalid integer conversion.")
    print("Outer try continues...")
except:
    print("Outer: Some other error.")
