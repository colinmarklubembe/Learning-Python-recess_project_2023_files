#running a php script 
print('Running a python script')

print(2 + 2)


#comments

#single line comment 
    
"""
Multiline comments 
"""
    
#indentation

#snake_case
#camelCase
#PascalCase

#variables
f_name = "Colin"
l_name = "Wafula"
age: int  = 21


print("First Name: " + f_name)
print(age)

#printing multiple outputs 
print("First Name: " + f_name , "Last Name: " + l_name)


#data structures
"""
Numeric: 1 - 10
-integer values (int)
-float values like pi = 3.14

Strings(str)
"Colin" , 'Colin' or "23"

boolean(bool) - represents logical values 

sequence types 
-list( [] ) : enclose with square brackets 
-tuple( () ) : enclosed with parantheses
-range : use interaction, loops

Mapping types
dict - dictionary : enclosed with curly braces '{}'
    
Item Dict
    {Apple, Banana, Pear}
    
Set Types
{Apple, Mango, Banana} represent unordered types that are unique

None types: None - represent absence of a value 

name: none 
        
    

"""



#DATATYPES 

#lists
fruits = ["Apple", "Banana", "Pear"]
print(fruits)

#how to access a list
print(fruits[0])
print(fruits[1])
print(fruits[2])

#adding items to the list
fruits.append("Orange")
print(fruits)

#inserting in lists 
fruits.insert(0, "Mango")
print(fruits)

#removing items from the list
fruits.remove("Banana")
print(fruits)

#popping items from the list
fruits.pop()
print(fruits)

#dict
fruits = {
    "Apple" : "red",
    "Banana" : "yellow",
    "Pear" : "green"
}
print(fruits)

#tuples
fruits = ("Apple", "Banana", "Pear")
print(fruits)

#how to access tuples
fruits = ("Apple", "Banana", "Pear")
print(fruits[0])
print(fruits[1])
print(fruits[2])

#looping through a tuple
fruits = ("Apple", "Banana", "Pear")
for fruit in fruits:
    print(fruit)
    

#adding items to a tuple
x = list(fruits)
x.append("Mango")
phones = tuple(x)

print(fruits)

#adding two tuples together 
fruits = ("Apple", "Banana", "Pear")
fruits2 = ("Orange", "Mango", "Grape")

fruits = fruits + fruits2
print(fruits)

#adding to another tuple
fruits = ("Apple", "Banana", "Pear")
fruits2 = ("Orange", "Mango", "Grape")

fruits3 = fruits + fruits2
print(fruits3)

#adding a tuple with one element
fruits = ("Apple", "Banana", "Pear")
fruits2 = ("Orange",)

fruits = fruits + fruits2
print(fruits)


#range
fruits = range(1,10)
print(fruits)

#duplicates in lists
fruits = ["Apple", "Apple", "Banana", "Pear"]
print(fruits)

#duplicates in dict
fruits = {
    "Apple" : "red",
    "Apple" : "yellow",
    "Banana" : "yellow",
    "Pear" : "green"
}
print(fruits)

print(type(fruits))

#modifyting list elements 
fruits = ["Apple", "Banana", "Pear"]
fruits[1] = "Orange"
print(fruits)



#DAY 2

#Control Flow

#Conditional Statements (if, elif, else)

#if
age = 16

if age >= 18:
    print("Your are of age")
else:
    print("Your are not of age")

#elif
age = int(input())

if age < 18:
    print("Your are underage")
elif age >= 18 and age <=65:
    print("Your are an adult")
else:
    print("Your are a senior citizen")
    
    
#LOOPS
#[for , while]

#while (executes while a condition is satisfied)

age = int(input())

while age < 18:
    print("You are underage")
    age = int(input())
    
x = 1

while x <= 5:
    print(x)
    x += 1
    
#for

fruits = ["Apple", "Banana", "Pear"]

for fruit in fruits:
    print(fruit)
    
print("\n\n")

#range for loop
x = range(1,10)

for i in x:
    print(i)
    
    
#dict
fruits = {
    "Apple" : "red",
    "Banana" : "yellow",
    "Pear" : "green"
}

for fruit in fruits: 
    print(fruit)
    
 
#break and continue


fruits = ["Apple", "Banana", "Pear"]

for fruit in fruits:
    if fruit == "Banana":
        break
    print(fruit)
    
x = range(1 , 10)

for i in x:
    if i % 2 == 1:
        continue
    print(i)
    
#try

try:
    x = int(input())
    y = int(input())
    z = x / y
    print(z)

except:
    print("Error")
    
#finally

try:
    x = int(input())
    y = int(input())
    z = x / y
    print(z)
    
except:
    print("Error")
    
finally:
    print("Finally")
    
    
#index error
x = [1, 2, 3, 4]

try:
    print(x[5])

except IndexError as error:
    print(error)
finally:
    print("Finally")
    

#name error
try:
    print(y)
except NameError as error:
    print(error)
finally:
    print("Finally")
    

#example using dict

emotion = {
    "happy" : "I'm glad!",
    "sad" : "Oh, I'm sorry!",
    "angry" : "You can try to calm down!"
} 

user_input = input("How are youmfeeling today?")

if user_input in emotion:
    print(emotion[user_input])
else:
    print("I don't understand")
    
    
#write a program to ask a student about their mental health.

health = {
    "happy" : "I'm glad!",
    "sad" : "Oh, I'm sorry!",
    "depressed" : "You could try talking to your therapist"
}

user_input = input("How do you feel lately?")

if user_input in health :
    print(health[user_input])
else:
    print("I don't understand")
    
    
#prompt students on a scale from 1 to 10 to rate their mental health
health = {
    1: 'Depressed.',
    2: 'Very sad',
    3: 'Sad',
    4: 'A little sad',
    5: 'Neutral',
    6: 'Content',
    7: 'A little happy',
    8: 'Happy',
    9: 'Very happy',
    10: 'Extatic!'
}
rating: int = input("Rate your mental health from 1 to 10")

try:
    rating = int(rating)
except ValueError:
    print("Please enter a number between 1 and 10 inclusive.")
    rating = int(input())
finally:
    print(health[rating])
    

#DAY 2 AFTERNOON

#dicts (used to store data values in key value pairs)
#discts are ordered, changeable and dont allow duplicates 

person: dict = {
    "name": "John",
    "age": 30,
    "city": "Kampala"
}
print(person)

#length if a dict
print(len(person))

#datatype
print(type(person))

#accessing a dictionary using keys
print(person["name"])
print(person["age"])
print(person["city"])

#iterating through items
for key, value in person.items():
    print(f"{key}: {value}")
    
#adding a new key value pair
person: dict = {
    "name": "John",
    "age": 30,
    "city": "Kampala"
}

person["gender"] = "male"
print(person)

#accessing the keys
print(person.keys())

#using the values() method
person: dict = {
    "name": "John",
    "age": 30,
    "city": "Kampala"
}

print(person.values())

#to check if a key exists in the dict
person = {
    "name": "John",
    "age": 30,
    "city": "Kampala"
}

if "name" in person:
    print("The 'name' key exists in the dictionary.")
else:
    print("The 'name' key does not exist in the dictionary.")

#changing items in dicts
person: dict = {
    "name": "John",
    "age": 30,
    "city": "Kampala"
}

person["age"] = 35
print(person)

#removing items
person: dict = {
    "name": "John",
    "age": 30,
    "city": "Kampala"
}

del person["age"]
print(person)

#nested dicts
person: dict = {
    "name": "John",
    "age": 30,
    "city": "Kampala",
    "address": {
    "street": "Nanfubambi",
    "village": "Kikoni"
    }
}
print(person)
print(person["address"])



#NUMBERS
#integers, floats, complex numbers 

#integers
w = 10
print(type(w))

#floats
x = 10.5
print(type(x))

#complex numbers
y = 1j
c = 10 + 6j
print(type(y))
print(type(c))

#TYPE CONVERSION
#conversion of type is possible using the built-in functions:
#int(), float() and complex(). The conversion may be explicit or implicit depending on context

x = 10.5
print(int(x))
print(complex(x))

#conversion from int to float
x = 10
print(float(x))

#conversion from complex to float
x = 10 + 6j
print(float(x.real))

#conversion from float to complex
x = 10.5
print(complex(x))

#conversion from complex to int
x = 10 + 6j
print(int(x.real))

#conversion from int to complex
x = 10
print(complex(x))

#conversion from float to int
x = 10.5
print(int(x))

#CASTING
# converting a value into another data type without changing its original representation in memory

print(int(20))
print(float(2.5))
print(complex("8"))

#STRINGS
#print("Afternoon")
#print('Afternoon')

#assign string to a variable
x = "Afternoon"
print(type(x))

#multi line stings
y = """
    This is a multi-line string
    with multiple lines
"""
print(type(y))

#string as an array
x = "Afternoon"
print(type(x))
print(x[0])
print(x[1])
print(x[2])
print(x[3])

#string concatenation
x = "Afternoon"
y = "Morning"
z = x + " " + y
print(type(z))
print(z)

#using the len() function
x = "Afternoon"
print(len(x))

#looping within a string
x = "Afternoon"
for c in x:
    print(c)
    
#string slicing
x = "Afternoon"
print(x[0:3])
print(x[3:])
print(x[:3])
print(x[:])

#modifying string 
x = "Afternoon"
x = x.replace("o", "O")

print(x)
print(x.lower())
print(x.upper())

#removing white space
x = " Afternoon "
print(x.strip())
print(x.lstrip())
print(x.rstrip())

#string formatting
x = "Afternoon"
y = "Morning"
z = f"{x} {y}"
print(type(z))
print(z)

age = 21
name = "Colin"
greeting = f'Hello, my name is {name}, and I am {age}.'
print(greeting)
print(type(greeting))


#BOOLEANS
#true and false
x = True
print(type(x))

y = False
print(type(y))

#comparison operators
x = 10
y = 20
print(x == y)
print(x != y)
print(x > y)
print(x < y)

print(bool(15))

#conditional statement to show how to use boolean
x = 10
y = 20
if x == y:
    print("True")
else:
    print("False")




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
    
"""
Create a simple calculator program with a GUI interface. 
Make your title of the Calculator programme window with ypur name
"""

#AFTERNOON SESSION

