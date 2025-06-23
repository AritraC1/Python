# __name__ and "__main__"

# In every Python file, a special built-in variable called __name__ exists.

# When a file is:
# Run directly:         __name__ == "__main__"
# Imported as a module: __name__ == "<module_name>"

# Why is this useful?
# It lets you write test/demo code in a file that only runs when the file is executed directly — not when it’s imported elsewhere.

# Common pattern:
# if __name__ == "__main__":
#     <run some code>

# This makes a script both:
# Executable as a standalone program
# Importable as a module without running the test code

# 🔁 CODE DEMONSTRATION

def greet(name: str) -> None:
    print(f"Hello, {name}!")

# This will always run when the function is called
# But the block below will ONLY run if this file is the main program
if __name__ == "__main__":
    # This will NOT run if the file is imported as a module
    print("This script is running directly.")
    greet("Alice")
    print(f"__name__ is: {__name__}")
else:
    # This will run if the file is imported elsewhere
    print("This script is being imported.")
    print(f"__name__ is: {__name__}")

'''
Summary:

__name__ is a special variable in every Python module
"__main__" is the value of __name__ when the file is run directly
Use if __name__ == "__main__": to control script vs module behavior
'''