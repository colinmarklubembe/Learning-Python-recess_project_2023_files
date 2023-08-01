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


