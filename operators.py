#DAY 3

#MORNING SESSION

#Basic operators and expressions (Input and output operators)

"""
-Arithmetic operators
    ~addition (+)
    ~subtraction (-)
    ~multiplication (*)
    ~division (/)
    ~modulus (%)
    ~exponentiation (**)
    ~floor division (//)
    
-Comparison operators
    ~equality (==)
    ~inequality (!= or !==)
    ~greater than (>)
    ~less than (<)
    ~greater than or equal to (>=)
    ~less than or equal to (<=)   
    
-Logical operators
    ~and (and)
    ~or (or)
    ~not (not)
    
-Assignment operators
    ~assignment (=)
    ~addition assignment (+=)
    ~subtraction assignment (-=)
    ~multiplication assignment (*=)
    ~division assignment (/=)
    ~modulus assignment (%=)
    ~exponentiation assignment (**=)
    
-Membership operators
    ~In (in): Checks if a value exists in a sequence
    ~Not in (not in): Checks if a value doen't exist in a sequence
    
-Identity operators
    ~is (is): Checks if two values are the same
    ~is not (is not): Checks if two values are not the same

-Bitwise operators
Used to perform operations on individual bits of binary numbers
    ~bitwise AND (&): Performs a bitwise AND operation between the corresponding bits of two integers
    ~bitwise OR (|): Performs a bitwise OR operation between the corresponding bits of two integers
    ~bitwise XOR (^): Performs a bitwise XOR operation between the corresponding bits of two integers
    ~bitwise NOT (~): Performs a bitwise NOT operation on an integer
    ~bitwise left shift (<<): Performs a bitwise left shift operation on an integer
    ~bitwise right shift (>>): Performs a bitwise right shift operation on an integer

"""

#Examples
#Arithmetic operators
#Addition
x = 10 + 5
print(x)
#Subtraction
x = 10 - 5
print(x)
#Multiplication
x = 10 * 5
print(x)
#Division
x = 10 / 5
print(x)
#Modulus
x = 10 % 5
print(x)
#Exponentiation
x = 2 ** 3
print(x)

#Comparison operators
#Equal to
x = 4 == 6
print(x)
#Greater than
x = 4 > 6
print(x)
#Less than
x = 4 < 6
print(x)
#Greater than or equal to
x = 4 >= 6
print(x)
#Less than or equal to
x = 4 <= 6
print(x)
#Not
x = not True
print(x)

#Logical operators
#and: Returns true only when both conditions are met.
a = False
b = True
print(a and b)
#or: Returns true only when at least one condition is met.
a = False
b = True
print(a or b)
#not: Returns the opposite of the condition.
a = False
b = True
print(not a)
print(not b)

#Assignment operators
#Add assignment operator (+=)
x = 10
x += 5
print(x)
#Subtract assignment operator (-=)
x = 10
x -= 5
print(x)
#Multiply assignment operator (*=)
x = 10
x *= 5
print(x)
#Divide assignment operator (/=)
x = 10
x /= 5
print(x)
#Modulus assignment (%=)
x = 10
x %= 5
print(x)
#Exponentiation assignment (**=)
x = 2
x **= 5
print(x)

#Bitwise operators
#bitwise AND
x = 10
y = 5
print(x & y)
#bitwise OR
x = 10
y = 5
print(x | y)
#bitwise XOR
x = 10
y = 5
print(x ^ y)
#bitwise NOT
x = 10
print(~x)
#bitwise left shift (<<)
x = 10
y = 5
print(x << y)
#bitwise right shift (>>)
x = 10
y = 5
print(x >> y)

#Membership operators
#in : Checks if an element exists in list, tuple etc., returns boolean value
cars = ['Jeep', 'Tesla', 'BMW', 'RollsRoyce']

if "Mercedes" in cars:
    print("Found")
else:
    print("Not found")
    
if 'Jeep' in cars:
    print('Jeep is in the list')
    print('Tesla' in cars)
    print('Toyota' in cars)

#not in: Checks if an element exists in list, tuple etc., returns boolean value
cars = ['Jeep', 'Tesla', 'BMW', 'RollsRoyce']

if "Mercedes" not in cars:
    print("Not Found")
else:
    print("Found")
    
#Identity operators
#is: Checks if two values are the same
x = 10
y = 10
print(x is y)
#is not: Checks if two values are not the same
x = 10
y = 20
print(x is not y)

#Example

def calculator(x, y, operator):
    if operator == '+':
        return x + y
    elif operator == '-':
        return x - y
    elif operator == '*':
        return x * y
    elif operator == '/':
        return x / y
    else:
        raise ValueError('Invalid Operator!')
        
try:
    x = int(input('Enter first number: '))
    y = int(input('Enter second number: '))
    operator = input('Enter operator (+, -, *, /): ')
    
    if operator == '+':
        print(calculator(x, y, operator))
    elif operator == '-':
        print(calculator(x, y, operator))
    elif operator == '*':
        print(calculator(x, y, operator))
    elif operator == '/':
        print(calculator(x, y, operator))
    else:
        raise ValueError('Invalid Operator')
except Exception as e:
    print(e)
    