print("\n--- Exercise 1 ---")

class Car:
    make: str
    model: str
    year : int

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(self.make, self.model, self.year)

car1 = Car('Ford', 'Mustang', 1999)
car2 = Car('BMW', 'M5', 2000)
car1.display_info()
car2.display_info()

print("\n--- Exercise 2 ---")

class Temperature:
    temperature_in_celsius : float

    def __init__(self, temperature_in_celsius):
        self.temperature_in_celsius = temperature_in_celsius

    def convert_to_fahrenheit(self):
         print(f"Temperature in Fahrenheit: {self.temperature_in_celsius * 9/5 + 32}")

    def convert_to_kelvin(self):
        print(f"Temperature in Kelvins: {self.temperature_in_celsius + 273.15}")

temperature = Temperature(32)
print(f"Temperature in Celsius: {temperature.temperature_in_celsius}")
temperature.convert_to_kelvin()
temperature.convert_to_fahrenheit()

print("\n--- Exercise 3 ---")
class Animal:
    def sound(self):
        ...

class Lion(Animal):
    def sound(self):
        print("Lion roars")

class Elephant(Animal):
    def sound(self):
        print("Elephant wooos")

lion = Lion()
lion.sound()
elephant = Elephant()
elephant.sound()

print("\n--- Exercise 4 ---")

class Shape:
    def area(self):
        ...

class Rectangle(Shape):
    def __init__(self, width, height):
        if width == 0 or height == 0:
            raise ValueError("Rectangle must have at least two non-zero integers")

        self.width = width
        self.height = height

    def area(self):
        print(f"Rectangle area is : {self.width * self.height}")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        if radius == 0:
            raise ValueError("Circle must have a non-zero radius")

    def area(self):
        print(f"Circle area is : {3.14159 * self.radius**2}")

Rectangle = Rectangle(100, 200)
Rectangle.area()
Circle = Circle(100)
Circle.area()

print("\n--- Exercise 5 ---")

class Employee:
    def get_role(self):
        ...

class Developer(Employee):
    def get_role(self):
        print("Developer")

class Manager(Employee):
    def get_role(self):
        print("Manager")

Developer = Developer()
Developer.get_role()
Manager = Manager()
Manager.get_role()

print("\n--- Exercise 6 ---")

class Person:
    def describe(self):
        print("Person's name")

class Student(Person):
    student_id : str

    def describe(self):
        print("Student's name")

    def add_student_id(self, student_id):
        self.student_id = student_id
        print(f"Id added to student: {self.student_id}")

student = Student()
student.describe()
student.add_student_id("s12345")

print("\n--- Exercise 7 ---")

class Dog:
    number_of_dogs_created = 0

    def __init__(self):
        Dog.number_of_dogs_created += 1

    @staticmethod
    def get_number_of_dogs_created():
        print(f"Number of dogs created: {Dog.number_of_dogs_created}")


dog1 = Dog()
dog2 = Dog()
dog3 = Dog()
dog4 = Dog()

Dog.get_number_of_dogs_created()

print("\n--- Exercise 8 ---")
class NegativeNumberError(Exception):
    def __init__(self, number):
        self.number = number
        super().__init__(f"Negative number not allowed: {number}")

    @staticmethod
    def raise_error(number):
        if number < 0:
            raise NegativeNumberError(number)

NegativeNumberError.raise_error(2)
try:
    NegativeNumberError.raise_error(-2)
except NegativeNumberError as e:
    print(e)

print("\n--- Exercise 9 ---")

class InvalidPriceError(Exception):
    def __init__(self, price):
        self.price = price
        super().__init__(f"Invalid price: {price}")


class Product:
    name : str
    price : int

    def __init__(self, name, price):
        if price < 0:
            raise InvalidPriceError(price)
        self.name = name
        self.price = price

try:
    product1 = Product("Bread", -100)
except InvalidPriceError as e:
    print(e)

print("\n--- Exercise 10 ---")

class Divider:
    @staticmethod
    def divide(a, b):
        try:
            return a / b
        except ZeroDivisionError as e:
            print(e)
            return None

Divider.divide(1, 2)
Divider.divide(1, 0)

print("\n--- Exercise 11 ---")

class FileReader:
    def __init__(self, filename):
        self.filename = filename

    def open_file(self):
        try:
            with open(self.filename) as file:
                return file.read()
        except FileNotFoundError as e:
            print(e)
            return None

file = FileReader("test.txt")
file.open_file()

print("\n--- Exercise 12 ---")

class BankAccount:
    owner : str
    balance : int

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def withdraw(self, amount):
        if (self.balance - amount) < 0:
            raise InsufficientFundsError
        self.balance -= amount


    def deposit(self, amount):
        self.balance += amount

class InsufficientFundsError(Exception):
    def __init__(self):
        super().__init__(f"Insufficient funds")

b1 = BankAccount(owner="Bob", balance=100)

try:
    b1.withdraw(amount=120)
except InsufficientFundsError as e:
    print(e)

print("\n--- Exercise 13 ---")

class UserInputValidator:
    @staticmethod
    def get_age(age):
        if type(age) != int:
            raise ValueError(1.5)

try:
    UserInputValidator.get_age(1.5)
except ValueError as e:
    print(f"ValueError: {e}")

print("\n--- Exercise 14 ---")

class InvalidOperationError(Exception):
    def __init__(self, operation):
        self.operation = operation
        super().__init__(f"Operation is unsupported: {self.operation}")

class Calculator:
    operation : str
    a : float
    b : float

    def __init__(self, operation, a, b):
        self.operation = operation
        self.a = a
        self.b = b
        self.calculate(operation)

    def calculate(self, operation):
        match operation:
            case "+":
                self.add(self.a, self.b)
            case "-":
                self.subtract(self.a, self.b)
            case "*":
                self.multiply(self.a, self.b)
            case "/":
                self.divide(self.a, self.b)
            case _:
                raise InvalidOperationError(operation)

    def add(self, a, b):
        print(a + b)

    def subtract(self, a, b):
        print(a - b)

    def multiply(self, a, b):
        print(a * b)

    def divide(self, a, b):
        try:
            print(a / b)
        except ZeroDivisionError as e:
            print(e)

c1 = Calculator(operation="*", a=5, b=10)

try:
    c2 = Calculator(operation="%", a=5, b=10)
except InvalidOperationError as e:
    print(e)

try:
    c3 = Calculator(operation="/", a=5, b=0)
except ZeroDivisionError as e:
    print(e)

print("\n--- Exercise 15 ---")

class GradeTooLowError(Exception):
    def __init__(self, grade):
        self.grade = grade
        super().__init__(f"Grade too low: {grade} < 40")

class Student:
    @staticmethod
    def check_grade(grade):
        if grade < 40:
            raise GradeTooLowError(grade)

Student.check_grade(41)
try:
    Student.check_grade(39)
except GradeTooLowError as e:
    print(e)