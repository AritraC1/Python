# Strings in Python
# A string is a sequence of characters used to represent text. 
# Strings are an immutable data type, meaning their content cannot be changed after creation.

## 3 ways to write a string in Python
a = 'Tony'
print(a)

b = "Tony"
print(b)

# Multiline string
c = '''Tony
Stark ''' 
print(c)

## String Operations

s = "Hello, Python!"

### Length of the string
print(len(s))  # Output: 13

### Access characters by index (0-based)
print(s[0])   # 'H'
print(s[-1])  # '!' (last character)

### Slicing strings
print(s[0:5])  # 'Hello'
print(s[7:])   # 'Python!'

### String concatenation
greeting = "Hello"
name = "Alice"
message = greeting + ", " + name + "!"
print(message)  # 'Hello, Alice!'

### Repeating strings
print("Hi! " * 3)  # 'Hi! Hi! Hi! '

### Check if substring exists
print("Python" in s)  # True

### Convert to uppercase/lowercase
print(s.upper())  # 'HELLO, PYTHON!'
print(s.lower())  # 'hello, python!'

## String Methods
text = "  Python Programming  "

### Remove leading/trailing whitespace
print(text.strip())

### Replace substring
print(text.replace("Python", "Java"))

### Split by whitespace into a list ['Python', 'Programming']
print(text.split())

print(text.startswith("  Py"))  # True

print(text.endswith("ing  "))    # True

print(text.find("gram"))    # 11 (index of substring)

## Formatting string

### Old-style formatting with %
name = "Alice"
age = 30

### Using % formatting
print("My name is %s and I am %d years old." % (name, age))

### str.format() method
name = "Bob"
score = 95.5

#### Using format method
print("Student {0} scored {1} points.".format(name, score))

#### Using named placeholders
print("Student {student} scored {points} points.".format(student=name, points=score))

pi = 3.14159265
print("Pi rounded to 2 decimals: {:.2f}".format(pi))

### f-strings (Python 3.6+) - This is the most modern and readable way.
name = "Charlie"
height = 1.75

print(f"My name is {name} and I am {height} meters tall.")

value = 123.456789

### Limit decimal places
print(f"Value: {value:.2f}")

### Padding and alignment
print(f"Left aligned: '{value:<10.2f}'")
print(f"Right aligned: '{value:>10.2f}'")
print(f"Center aligned: '{value:^10.2f}'")