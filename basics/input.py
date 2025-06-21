num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))

sum = num1 + num2

print(f"Sum of {num1} + {num2} is {sum}") # This 'f' is called an f-string (short for "formatted string literal"). It lets you easily embed variables or expressions inside a string using {}.

# Input is a string by default, so we need to convert it using int() or float() to accept numbers (integers or decimals) as input. Or, input() always returns a string. To perform numeric operations, you must convert the input using int() for integers or float() for decimal numbers.