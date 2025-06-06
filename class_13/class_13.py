print("Part 1: Instance and static fields")
print("\n--- Exercise 1 ---")
class Dog:
    times_created = 0
    names = list()

    def __init__(self, name):
        self.name = name
        Dog.times_created += 1
        Dog.names.append(name)

    @staticmethod
    def print_all_names():
        print(Dog.names)

dog1 = Dog("Dog1")
print(dog1.name)
dog2 = Dog("Dog2")
print(dog2.name)
dog3 = Dog("Dog3")
print(dog3.name)
print(f"Total number of dogs: {Dog.times_created}")
Dog.print_all_names()

print("\n--- Exercise 2 ---")

class Car:
    number_of_wheels = 4

    def __init__(self, color):
        self.color = color

car1 = Car("blue")
car2 = Car("red")
car1.number_of_wheels = 6
print(f"Car 1. Color: {car1.color}, Number of wheels: {car1.number_of_wheels}")
print(f"Car 2. Color: {car2.color}, Number of wheels: {car2.number_of_wheels}")
Car.number_of_wheels = 8
print(f"Car 1. Color: {car1.color}, Number of wheels: {car1.number_of_wheels}")
print(f"Car 2. Color: {car2.color}, Number of wheels: {car2.number_of_wheels}")

print("\n--- Exercise 3 ---")
class Employee:
    total_number_of_employees = 0
    departments = dict()

    def __init__(self, name, department):
        self.name = name
        self.department = department
        Employee.total_number_of_employees += 1
        Employee.departments[department] = Employee.departments.get(department, 0) + 1

emp1 = Employee("John", "HR")
emp2 = Employee("Jane", "HR")
emp3 = Employee("Doe", "IT")

print(Employee.departments)
print(Employee.total_number_of_employees)

print("\nPart 2: Instance, Static, and Class Methods")

print("\n--- Exercise 1 ---")
class Calculator:
    def __init__(self, a):
        self.a = a

    def square(self):
        self.print_result(self.a ** 2)

    @classmethod
    def print_result(cls, result):
        print(f"Result is equal to: {result}")

    @staticmethod
    def add_two_numbers(a, b):
        Calculator.print_result(a + b)

c1 = Calculator(5)
c1.square()
Calculator.add_two_numbers(1, 2)

print("\n--- Exercise 2 ---")
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    @classmethod
    def from_string(cls, string):
        title, author = string.split(";")
        return cls(title, author)

b1 = Book.from_string("1984;George Orwell")
print(f"Title: {b1.title}, Author: {b1.author}")

print("\n--- Exercise 3 ---")

class Temperature:
    def __init__(self, temperature):
        self.temperature = temperature

    def convert_celsius_to_fahrenheit(self):
        self.temperature = round(self.temperature * 9 / 5 + 32, 1)

    def convert_fahrenheit_to_celsius(self):
        self.temperature = round((self.temperature - 32) * 5 / 9, 1)

    @staticmethod
    def convert_kelvin_to_celsius(temperature):
        return round(temperature - 273.15, 1)

    @classmethod
    def from_fahrenheit(cls, temperature):
        return Temperature(temperature)

    def __eq__(self, other):
        return self.temperature == other.temperature

    def __lt__(self, other):
        return self.temperature < other.temperature

t1 = Temperature.from_fahrenheit(98.6)
print(f"Temperature in Fahrenheit: {t1.temperature}F")
t1.convert_fahrenheit_to_celsius()
print(f"Temperature in Celsius: {t1.temperature}C")
print(f"Temperature in Kelvin: {Temperature.convert_kelvin_to_celsius(300)}")
t2 = Temperature(-30)
print(f"Is {t1.temperature}C greater than {t2.temperature}C: {t1 > t2}")
t2.temperature = t1.temperature
print(f"Is {t1.temperature}C the same as {t2.temperature}C: {t1 == t2}")

print("\nPart 3: Encapsulation and properties")

print("\n--- Exercise 1 ---")
class Person:
    def __init__(self, name, age):
        self.name = name # Public
        self._age = age # Protected
        self.__ssn = "123-45-6789" # Private

p1 = Person("John", 40)
print(p1.name)
print(p1._age)

try:
    print(p1.__ssn)
except Exception as e:
    print(e)

print(p1._Person__ssn)

print("\n--- Exercise 2 ---")
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance

    @property
    def status(self):
        if self.__balance == 0:
            return "Empty"
        elif self.__balance < 100 :
            return "Low"
        else:
            return "Healthy"

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, amount):
        if amount < 0:
            print("Balance cannot be negative.")
        else:
            self.__balance = amount

b1 = BankAccount(owner="John", balance=100)
print(f"Current balance: {b1.balance}")
print(f"Current status: {b1.status}")
b1.balance = -100
b1.balance = 0
print(f"Current balance: {b1.balance}")
print(f"Current status: {b1.status}")

print("\n--- Exercise 3 ---")
class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def area(self):
        return self._width * self._height

r1 = Rectangle(100, 100)
print(f"Area is equal to: {r1.area}")

try:
    r1.area = 20
except Exception as e:
    print(e)

r1._width = 20
r1._height = 20
print(f"Area is equal to: {r1.area}")

print("\nPart 4: Magic Methods and Operator Overloading")
print("\n--- Exercise 1 ---")

class Movie:
    def __init__(self, title, year):
        self.title = title
        self.year = year

    def __str__(self):
        return f"Title: {self.title}, Year: {self.year}"

    def __repr__(self):
        return f"Debug. Title: {self.title}, Year: {self.year}"

m1 = Movie("Inception", 2010)
print(m1)
print(repr(m1))

print("\n--- Exercise 2 ---")
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __mul__(self, number):
        return Point(self.x * number, self.y * number)

    def __rmul__(self, number):
        return Point(number * self.x, number * self.y)

p1 = Point(1, 2)
p2 = Point(3, 4)
print(f"Are point 1 and point 2 equal? {p1 == p2}")
p3 = p1 + p2
print(f"Result of adding two points: {p3.x}, {p3.y}")
result1 = p1 * 3
print(f"Result of scalar multiplication is: {result1.x}, {result1.y}")
result2 = 3 * p1
print(f"Result of rear scalar multiplication is: {result2.x}, {result2.y}")

print("\n--- Exercise 3 ---")
class Box:
    def __init__(self, volume):
        self.volume = volume

    def __gt__(self, other):
        return self.volume > other.volume

    def __lt__(self, other):
        return self.volume < other.volume

    def __le__(self, other):
        return self.volume <= other.volume

b1 = Box(100)
b2 = Box(200)
b3 = Box(300)

print(f"Is b1 smaller than b2: {b1 < b2}")
print(f"Is b2 greater than b3: {b2 > b3}")
print(f"Is b2 smaller or equals b3: {b2 <= b3}")