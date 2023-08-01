# DAY 5
"""Inheritance"""


class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(self.name, "is eating")


class Dog(Animal):

    def bark(self):
        print(self.name, "is barking")


class Cat(Animal):

    def meow(self):
        print(self.name, "is meowing")


# create animal object
animal = Animal("Generic Animal")
dog = Dog("Spot")
cat = Cat("Whiskers")

# invoke methods
animal.eat()
dog.eat()
dog.bark()
cat.eat()
cat.meow()


# EXAMPLE 2
class Vehicle:
    def __init__(self, name, brand, color):
        self.name = name
        self.color = color
        self.brand = brand

    def display_info(self):
        print("Name:", self.name)
        print("Brand:", self.brand)
        print("Color:", self.color)

    def move(self):
        print(self.name, "is moving")


class Car(Vehicle):
    def __init__(self, name, brand, color, year):
        super().__init__(name, brand, color)
        self.year = year

    def display_info(self):
        super().display_info()
        print("Year:", self.year)


# create car object
car = Car("Mustang", "Ford", "Red", 1966)

# access and modify car attributes
car.year = 2018

# invoke car methods
car.display_info()  # notice that the display_info() method is overridden
car.move()  # notice that the move() method is inherited

# create vehicle object
vehicle = Vehicle("Generic Vehicle", "Generic Brand", "Generic Color")
vehicle.display_info()


# Exercise 1
# calculate the area and perimeter of a rectangle using inheritance
# calculate the area and circumference of a circle

class Shape:
    def area(self):
        pass

    def perimeter(self):
        pass


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14 * self.radius


# Example usage
circle = Circle(3)
print("Circle area:", circle.area())
print("Circle circumference:", circle.perimeter())

# Example usage
rectangle = Rectangle(5, 8)
print("Rectangle area:", rectangle.area())
print("Rectangle perimeter:", rectangle.perimeter())

# Alternative by importing math module
import math


class Shape:
    def area(self):
        pass

    def perimeter(self):
        pass


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius


# Example usage
circle = Circle(5)
print("Circle area:", circle.area())
print("Circle circumference:", circle.perimeter())

# Example usage
rectangle = Rectangle(4, 8)
print("Rectangle area:", rectangle.area())
print("Rectangle perimeter:", rectangle.perimeter())


# Multiple Inheritance
class A:
    def method_a(self):
        print("Method A")


class B:
    def method_b(self):
        print("Method B")


class C(A, B):
    def method_c(self):
        print("Method C")


# Example usage
c = C()
c.method_a()  # Output: Method A
c.method_b()  # Output: Method B
c.method_c()  # Output: Method C


# static methods
class A:
    @staticmethod
    def method_a():
        print("Method A")


class B:
    @staticmethod
    def method_b():
        print("Method B")


class C(A, B):
    @staticmethod
    def method_c():
        print("Method C")


# Example usage
C.method_a()  # Output: Method A
C.method_b()  # Output: Method B
C.method_c()  # Output: Method C

"""Method Overriding"""


# Example 1
class Animal:
    def make_sound(self):
        print("Animal making sound")


class Dog(Animal):
    def make_sound(self):
        print("Bark")


class Cat(Animal):
    def make_sound(self):
        print("Meow")


def make_animal_sound(animal):
    animal.make_sound()


# create objects
animal = Animal()
dog = Dog()
cat = Cat()

# invoke methods
animal.make_sound()
dog.make_sound()
cat.make_sound()

# calling make_animal_sound() function will invoke the make_sound() method of the object passed as an argument
make_animal_sound(animal)  # Output: Animal making sound
make_animal_sound(dog)  # Output: Bark
make_animal_sound(cat)  # Output: Meow

"""Polymorphism"""
"""
Method Overloading: Allows a class to have more than one method having the same name, 
if their argument lists are different
"""
"""
Method Overriding: 
Allows a subclass or child class to provide a specific implementation of
a method that is already provided by one of its super-classes or parent classes
 """


# Example 1: Method Overriding
class Shape:
    def calculate_area(self):
        pass


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def calculate_area(self):
        return self.side * self.side


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width


# create objects
square = Square(4)
rectangle = Rectangle(2, 4)

# print the area of the square
print("Area of square: ", square.calculate_area())  # Output: 16

# print the area of the rectangle
print("Area of rectangle: ", rectangle.calculate_area())  # Output: 8


# Example 2: Method Overloading
class Calculator:
    def add(self, a, b, c=None):
        if c is None:
            return a + b
        else:
            return a + b + c


# create object
calculator = Calculator()
print(calculator.add(2, 3, 4))  # Output: 9
print(calculator.add(2, 3))  # Output: 5

"""Abstraction"""
# Allows making relevant information visible and hiding unnecessary details
# Example 1

from abc import ABC, abstractmethod


class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass


class Car(Vehicle):
    def start(self):
        print("Car started")

    def stop(self):
        print("Car stopped")


# create object
car = Car()
car.start()
car.stop()


# Exercise 2
# demonstrate abstraction using calculating the area of a rectangle and a circle
# using inheritance and abstract methods
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14 * self.radius


# create objects
rectangle = Rectangle(5, 6)
circle = Circle(7)

# print the area of the rectangle
print("Area of rectangle:", rectangle.area())  # Output: 30

# print the perimeter of the rectangle
print("Perimeter of rectangle:", rectangle.perimeter())  # Output: 22

# print the area of the circle
print("Area of circle:", circle.area())  # Output: 153.86

# print the circumference of the circle
print("Circumference of circle:", circle.perimeter())  # Output: 43.96

"""Assignment"""
# Create a receipt printing programme with GUI interface. A more advanced detail earns you more points.
