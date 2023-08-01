# input and output in python

# input
# is a function that takes input from the user.  It can be used to take any kind of data as an argument, but it is most commonly used with strings or numbers (integers).

# Example
# name = input("Enter a name: ")
# print(f"The inserted name is {name}")
#
# Example 2
# number = int(input("Enter a number: "))
# product = number*5
#
# print(product)
#
# multiple inputs in python
# x, y, z = map(int, input("Enter three numbers:").split())
# print("The values are:", end=" ")
# print(x, y, z)

# how to capture input from a tuple
w = (2, 4, 6, 8, 10)
print("Current tuple")
print(w)
print(type(w))

e = list(w)
e.append(int(input("Enter new value:")))
w = tuple(e)
print("Updated tuple")
print(w)

# how to capture input from a set
s = {2, 4, 6, 8, 10}
print("Current set")
print(s)
print(type(s))

s.add(int(input("Enter next value: ")))
print("Updated set")
print(s)

mySet = set(map(int, input("Enter set values:").split()))
print(mySet)

