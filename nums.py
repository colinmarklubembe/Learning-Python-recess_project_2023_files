
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