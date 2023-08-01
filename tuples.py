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


