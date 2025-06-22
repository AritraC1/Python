# File Handling

# THEORY:
# Random Access Memory (RAM) is volatile, all its content are lost once. program teminates in order to persist the data forever, we use files
# File I/O (Input/Output) allows programs to read from and write to files stored on disk.
# Python provides built-in functions to handle file operations using the open() function.

# SYNTAX:
# open(file_path, mode)
# Modes:
# 'r'  -> read (default), error if file doesn't exist
# 'w'  -> write (creates file if not exists, overwrites if exists)
# 'a'  -> append (creates file if not exists, appends if exists)
# 'x'  -> exclusive creation (creates, errors if exists)
# 'b'  -> binary mode
# 't'  -> text mode (default)

import os

# 1. WRITE to a file - Create or overwrite a file and write content
with open("example.txt", "w") as file:
    file.write("Hello World!!\n")
    file.write("This is File I/O in Python.\n")

# 2. READ from a file - Read entire file content
with open("example.txt", "r") as file:
    content = file.read()
    print("File Content (read):\n", content)

# 3. READ line-by-line with a loop
with open("example.txt", "r") as file:
    print("Reading line by line:")
    for line in file:
        print(line.strip())  # .strip() removes newline characters

# 4. APPEND to an existing file
with open("example.txt", "a") as file:
    file.write("Adding a new line via append.\n")

# 5. READLINES and WRITELINES
# Read all lines into a list
with open("example.txt", "r") as file:
    lines = file.readlines()  # returns a list of lines
    print("Lines as list:", lines)

# Write a list of lines to a new file
lines_to_write = ["Line 1\n", "Line 2\n", "Line 3\n"]
with open("new_file.txt", "w") as file:
    file.writelines(lines_to_write)

# 6. FILE EXISTENCE and ERROR HANDLING
filename = "example.txt"

if os.path.exists(filename):
    print(f"{filename} exists!")
else:
    print(f"{filename} does not exist.")

# Exception handling
try:
    with open("non_existing.txt", "r") as file:
        data = file.read()
except FileNotFoundError:
    print("The file does not exist.")

# 7. BINARY MODE (optional)
# Writing binary data (e.g., image or byte stream)
with open("binary_file.bin", "wb") as file:
    file.write(b'\x00\xFF\xA5\xB2')  # writing raw bytes

# Reading binary data
with open("binary_file.bin", "rb") as file:
    binary_data = file.read()
    print("Binary data:", binary_data)