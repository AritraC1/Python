# Recursion

'''
Recursion is a programming technique where a function calls itself to solve smaller instances of a problem.

A recursive function must have:
1. Base Case - the condition at which the function stops calling itself.
2. Recursive Case - the part where the function calls itself with modified arguments.
'''

# Print numbers
def print_numbers(lower, upper):
    # Base case
    if lower > upper:
        return # exits code
    
    print(lower)
    print_numbers(lower+1, upper)
    # print(lower)


print_numbers(1, 5)