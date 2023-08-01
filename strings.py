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

