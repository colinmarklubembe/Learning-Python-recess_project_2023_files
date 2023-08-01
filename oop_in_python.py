# DAY 4

"""
Object oriented programming in pyrhon

1. Class
2. Object
3. Encapsulation
4. Inheritence 
5. Polymorphism
6. Abstraction
    
"""

# CLASSES
# EXample 1: Car


class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def start_engine(self):
        print("Engine Started!")

    def stop_engine(self):
        print("Engine Stopped!")


my_car = Car('Ford', 'Mustang', 2019)
print(my_car.make)
print(my_car.model)
print(my_car.year)
my_car.start_engine()
my_car.stop_engine()


# Example 2: Bank Account

class BankAccount:
    def __init__(self, account_number, balance):
        self.balance = balance
        self.account_number = account_number

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient Balance")

    def print_balance(self):
        print("Account: ", self.account_number)
        print("Balance: ", self.balance)


# create bank account object
bank_acc = BankAccount('758538589', 1000000)

print(bank_acc.balance)
bank_acc.deposit(10000)
bank_acc.withdraw(24500)
bank_acc.print_balance()


# Example 3: Rectangle

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    # Area of rectangle
    @property
    def area(self):
        return self.length * self.width

    # Perimeter of rectangle
    @property
    def perimeter(self):
        return 2 * (self.length + self.width)


my_rectangle = Rectangle(10, 20)
print(my_rectangle.length)
print(my_rectangle.width)
print(my_rectangle.area)
print(my_rectangle.perimeter)


# Example 4: Student

class Student:
    def __init__(self, name, year, course):
        self.name = name
        self.year = year
        self.course = course

    def display_details(self):
        print("Name:", self.name)
        print("Year:", self.year)
        print("Course:", self.course)


student1 = Student("Colin Lubembe", "Third Year",
                   'Bachelor in Software Engineering')
student1.display_details()


# Exercise: Calculate the area and circumference of a circle

class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def area(self):
        return 3.14 * self.radius ** 2

    @property
    def circumference(self):
        return 2 * 3.14 * self.radius


circle = Circle(5)
print('Area:', circle.area)
print('Circumference:', circle.circumference)


# Caclulate and display employee bonuses. The bonus is 15% of salary.{Employee1 salary is 150000 , employee2 salary is 230000}

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    # Getter method
    def getSalary(self):
        return self.salary

    def displaySalary(self):
        print("Name:", self.name)
        print("Salary:", self.getSalary())

    # Getter method
    def getBonus(self):
        return self.salary * 0.15

    def displayBonus(self):
        print("Bonus:", self.getBonus())


emp1 = Employee("Mark", 150000)
emp1.displaySalary()
emp1.displayBonus()

emp2 = Employee("Greg", 230000)
emp2.displaySalary()
emp2.displayBonus()


# ENCAPSULATION
# Main goals of encapsulation:
#    - Data hiding (prevents direct access to data members and methods from outside the class
#    - Information Hiding (hide information about how an object is implemented or what operations it can perform)
#    - Enforces a level of abstraction between classes that use them

# Example with a bank account

class BankAccount:
    def __init__(self, account_number, balance):
        self._balance = balance
        self._account_number = account_number

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        if self._balance >= amount:
            self._balance -= amount
        else:
            print("Insufficient Balance")

    def get_balance(self):
        return self._balance

    def print_balance(self):
        print("Account: ", self._account_number)
        print("Balance: ", self._balance)


my_bank_account = BankAccount('758538589', 1000000)
my_bank_account.deposit(10000)
my_bank_account.withdraw(24500)
my_bank_account.print_balance()
print(my_bank_account._balance)


# Exercise 2: Convert 37.5 degrees from celcius to farenheit

"""Alternative 1"""


class TemperatureConverter:
    def __init__(self):
        self._celsius = None
        self._fahrenheit = None

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        self._celsius = value
        self._fahrenheit = None

    @property
    def fahrenheit(self):
        if self._fahrenheit is None:
            self._fahrenheit = (self._celsius * 9/5) + 32
        return self._fahrenheit


# Create an instance of TemperatureConverter
temp_converter = TemperatureConverter()

# Set the Celsius temperature
temp_converter.celsius = 37.5

# Access the Fahrenheit temperature using the property
fahrenheit_temp = temp_converter.fahrenheit

# Print the result

print(f"The temperature in Fahrenheit is: {fahrenheit_temp}°F")


"""Simplified alternative 2"""


class TemperatureConverter:
    def __init__(self, celsius):
        self.__celsius = celsius

    @property
    def fahrenheit(self):
        return (self.__celsius * 9/5) + 32


# Create an instance of TemperatureConverter
temp_converter = TemperatureConverter(37.5)

# Access the Fahrenheit temperature using the property
fahrenheit_temp = temp_converter.fahrenheit

# Print the result
print(f"The temperature in Fahrenheit is: {fahrenheit_temp}°F")


"""With a default value in case no value is provided"""


class TemperatureConverter:
    def __init__(self, celsius=None):
        self.__celsius = celsius

    @property
    def fahrenheit(self):
        if self.__celsius is not None:
            return (self.__celsius * 9/5) + 32


# Create an instance of TemperatureConverter without specifying the Celsius temperature
temp_converter = TemperatureConverter()

# Access the Fahrenheit temperature using the property
fahrenheit_temp = temp_converter.fahrenheit

# Print the result
if fahrenheit_temp is not None:
    print(f"The temperature in Fahrenheit is: {fahrenheit_temp}°F")
else:
    print("No temperature conversion available.")


"""Assignment 2: Show encapsulation with employee information to give a pay increment"""


class Employee:
    def __init__(self, name, salary):
        self._name = name
        self._salary = salary

    # Getter methods
    def getSalary(self):
        return self._salary

    def getName(self):
        return self._name

    def displaySalary(self):
        print("Name:", self.getName())
        print("Initial Salary:", self.getSalary())

    # Method to calculate and display salary increment
    def displayIncrement(self):
        increment = self.getIncrement()
        print("Salary Increment:", increment)
        self._salary += increment
        print("New Salary:", self.getSalary())

    # Internal method to calculate the increment
    def getIncrement(self):
        return self._salary * 0.25  # 25% salary increase


# Create an instance of Employee
employee = Employee("Claude", 500000)

# Display the initial salary
employee.displaySalary()

# Display the salary increment
employee.displayIncrement()
