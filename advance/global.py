# Global Variables in Python

# A global variable is defined outside of all functions and is accessible
# throughout the entire module (file).
# By default, variables assigned inside a function are **local** to that function.
# If you want to modify a global variable from inside a function,
# you must use the `global` keyword.

# Rules:
# - You can read global variables inside a function without using 'global'
# - To modify a global variable from inside a function, declare it as global first

x = 10  # global variable

def read_global():
    # Reading global variable (allowed)
    print("Inside read_global, x =", x)

def modify_global():
    # Modifying global variable (must declare as global)
    global x
    x = 20
    print("Inside modify_global, x changed to", x)

def create_local():
    # Creates a local variable named x (does NOT affect global x)
    x = 99
    print("Inside create_local, local x =", x)

# Run all functions to see behavior
print("Initially, global x =", x)
read_global()
create_local()
print("After create_local, global x still =", x)
modify_global()
print("After modify_global, global x now =", x)

'''
Summary:

Use global x to modify x inside a function
Without global, assignments create a new local variable
Reading a global variable without changing it requires no special keyword
'''