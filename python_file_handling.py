"""
File handling in Python involves working with files on the filesystem, such as reading from or
writing to files. Python provides built-in functions and methods that make file handling convenient
and straightforward.

Opening a File:
To interact with a file, you need to open it using the open() function.
The open() function takes two parameters: the file name (including the path if necessary)
and the mode in which the file should be opened. The mode can be "r" for reading, "w" for
writing (overwriting the existing file), "a" for appending (adding content at the end of
the file), or "x" for creating a new file. If no mode is specified, the file is opened in
read-only mode ("r").
            file = open("example.txt", "r")  # Open file for reading

Performing File Operations:
Once the file is opened, you can perform various operations on it, depending on the mode in
which it was opened.
Reading from a File:
    -Use the read() method to read the entire content of the file as a string.
    -Use the readline() method to read a single line from the file.
    -Use the readlines() method to read all lines of the file and return them as a list.

            file = open("example.txt", "r")
            content = file.read()  # Read entire file content as a string
            print(content)
            file.close()  # Close the file after reading

Writing to a File:
Use the write() method to write a string to the file.
Use the writelines() method to write a list of strings to the file.
            file = open("example.txt", "w")
            file.write("Hello, world!\n")
            file.write("This is a sample file.")
            file.close()  # Close the file after writing

Closing the File:
After you have finished working with a file, it's important to close it using the close() method.
Closing the file releases system resources and ensures that any pending data is written to the file.

            file = open("example.txt", "r")
            # Perform file operations...
            file.close()  # Close the file

"""

# Example: Writing to a file

# Open the file in write mode
file = open("input.txt", "w")

# Write content to the file
file.write("Hello, world!\n")
file.write("This is a sample file.")

# append to a file
file = open("input.txt", "a")
file.write("\nThis is a new line.")

# Close the file
file.close()

# Inform the user about the successful write operation
print("Content written to the file 'input.txt'.")

# Example: Reading from a file and writing to another file

# Open the input file for reading
input_file = open("input.txt", "r")

# Read the content of the input file
content = input_file.read()

# Close the input file
input_file.close()

# Manipulate the content (in this case, convert it to uppercase)
content = content.upper()

# Open the output file for writing
output_file = open("output.txt", "w")

# Write the modified content to the output file
output_file.write(content)

# Close the output file
output_file.close()

# Inform the user about the successful operation
print("File handling completed. Output written to 'output.txt'.")


# Example that includes exception handling
def write_to_file(file_name, content):
    try:
        # Open the file in write mode
        file = open(file_name, "w")

        # Write content to the file
        file.write(content)

        # Close the file
        file.close()

        # Inform the user about the successful write operation
        print(f"Content written to the file '{file_name}'.")
    except IOError:
        print(f"Error: Failed to write to the file '{file_name}'.")


def read_write_files():
    try:
        # Get user input for file names
        input_file = input("Enter the input file name: ")
        output_file = input("Enter the output file name: ")

        # Open the input file for reading
        with open(input_file, "r") as input_file:
            # Read the content of the input file
            content = input_file.read()

        # Manipulate the content (in this case, convert it to uppercase)
        content = content.upper()

        # Write the modified content to the output file
        write_to_file(output_file, content)

        # Inform the user about the successful operation
        print("File handling completed. Output written to 'output.txt'.")
    except IOError:
        print("Error: Failed to read from or write to files.")


# Example usage
read_write_files()
print("--------------------------------------------------------")

"""Exception Handling"""
"""
Exception handling is a mechanism for stopping "normal" program flow and continuing at some surrounding context or
 block of code. It is a way of handling both expected and unexpected errors.
 """
# Example 1
try:
    x = 10
    y = 0
    result = x / y  # This will raise a ZeroDivisionError
    print("Result:", result)  # This line will not be executed
except ZeroDivisionError:
    print("Error: Division by zero")
else:
    print("No error occurred")
finally:
    print("Cleanup operations")

# Example 2: With user input
try:
    x = int(input("Enter a number: "))
    y = int(input("Enter another number: "))
    result = x / y  # This will raise a ZeroDivisionError
    print("Result:", result)  # This line will not be executed
except ZeroDivisionError:
    print("Error: Division by zero")
else:
    print("No error occurred")
finally:
    print("Cleanup operations")

# Other exceptions
# - NameError
# - SyntaxError
# - TypeError
# - ValueError
# - IndexError
# - KeyError
# - AttributeError
# - IOError e.t.c

# Example 3: Handling multiple exceptions
try:
    x = int(input("Enter a number: "))
    y = int(input("Enter another number: "))
    result = x / y  # This will raise a ZeroDivisionError
    print("Result:", result)  # This line will not be executed
except (ZeroDivisionError, ValueError):
    print("Error: Invalid input")
else:
    print("No error occurred")
finally:
    print("Cleanup operations")

# Example 4: Raising exceptions
try:
    x = int(input("Enter a number: "))
    if x < 0:
        raise ValueError("Negative numbers are not allowed")
except ValueError as e:
    print(e)
else:
    print("No error occurred")
finally:
    print("Cleanup operations")


# Example 5: Creating custom exceptions
class NegativeNumberError(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message


try:
    x = int(input("Enter a number: "))
    if x < 0:
        raise NegativeNumberError("Negative numbers are not allowed")

except NegativeNumberError as e:
    print(e)
else:
    print("No error occurred")
finally:
    print("Cleanup operations")

# Example 6: Using the assert statement
try:
    x = int(input("Enter a number: "))
    assert x >= 0, "Negative numbers are not allowed"
except AssertionError as e:
    print(e)
else:
    print("No error occurred")
finally:
    print("Cleanup operations")
