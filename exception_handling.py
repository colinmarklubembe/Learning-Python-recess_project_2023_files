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

