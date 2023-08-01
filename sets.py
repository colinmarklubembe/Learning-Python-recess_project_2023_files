#sets
set_one = {"Rice", "Irish", "Potatoes"}

#how to access a set
print(set_one)

#adding to a set
set_one.add("Tomatoes")
print(set_one)

#removing from a set
set_one.remove("Potatoes")
print(set_one)

#checking if an item is in a set
print("Potatoes" in set_one)

#duplicates in sets
set_two = {"Rice", "Irish", "Potatoes", "Potatoes"}
print(set_two)

#length of a set
set_two = {"Rice", "Irish", "Potatoes"}
print(len(set_two))

#accessing items in a set
set_two = {"Rice", "Irish", "Potatoes"}
set_two_list = list(set_two)
food = set_two_list[1]

#iterating through a set
set_two = {"Rice", "Irish", "Potatoes"}
for item in set_two:
    print(item)
    
#combining two sets
set_one = {"Rice", "Irish", "Potatoes"}
set_two = {"Potatoes", "Tomatoes"}
set_three = set_one.union(set_two)
print(set_three)

#data type of the set
set_two = {"Rice", "Irish", "Potatoes"}
print(type(set_two))
