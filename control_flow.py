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