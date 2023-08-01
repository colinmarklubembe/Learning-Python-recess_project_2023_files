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