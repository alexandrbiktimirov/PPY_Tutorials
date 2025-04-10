import cmath

print("\n--- Exercise 1 ---")

def solve_quadratic(a, b, c):
    if a == 0:
        if b == 0:
            if c == 0:
                return "Infinite solutions"
            else:
                return "No solution"
        else:
            return -c / b
    else:
        discriminant = b * b - 4 * a * c
        root_disc = cmath.sqrt(discriminant)

        root1 = (-b + root_disc) / (2 * a)
        root2 = (-b - root_disc) / (2 * a)

        return root1, root2

print(solve_quadratic(0, 0, 0))
print(solve_quadratic(0, 0, 1))
print(solve_quadratic(0, 1, 2))
print(solve_quadratic(1, 24, 3))
print(solve_quadratic(1+2j, 3+4j, 5+6j))

print("\n--- Exercise 2 ---")

def fact_r(n):
    if n == 0:
        return 1

    return n * fact_r(n-1)

def fact_n(n):
    number = n
    result = 1

    while n > 0:
        result *= n
        n -= 1

    print(f"Factorial of {number} is {result}")

fact_n(4)
print(f"Factorial (recursive version) is {fact_r(4)}")

print("\n--- Exercise 3 ---")

def fibo_r(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibo_r(n - 1) + fibo_r(n - 2)

print(fibo_r(7))

def fibo_i(n):
    if n == 0:
        return 0

    a = 0
    b = 1

    for i in range(2, n + 1):
        temp = a + b
        a = b
        b = temp

    return b

print(fibo_r(12))

print("\n--- Exercise 4 ---")

def even_odd_dict(numbers):
    even = []
    odd = []
    result = {"even" : even, "odd" : odd}

    for i in numbers:
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)

    return result

numbers = [1, 2, 3, 4, 5, 6, 7, 8]
print(even_odd_dict(numbers))

print("\n--- Exercise 5 ---")

def word_freq(s):
    result = {}

    words = s.split()

    for i in words:
        if i in result:
            result[i] += 1
        else:
            result[i] = 1

    return result

s = "some text in some string"
print(word_freq(s))

print("\n--- Exercise 6 ---")

def unique_elements(ls):
    newSet = set()

    for i in ls:
        newSet.add(i)

    return newSet

ls = [1, 2, 2, 3, 4, 5, 6, 7, 7, 7, 7]
print(ls)
print(unique_elements(ls))

print("\n--- Exercise 7 ---")

def numbers_average(ls, round_digits = None):
    average = 0

    for i in ls:
        average += i

    if round_digits is None:
        return average / len(ls)
    else:
        return round(average / len(ls), round_digits)

nums = [1, 2, 3, 4, 5, 6, 7, 93]
print(numbers_average(nums))
print(numbers_average(nums, 1))

print("\n--- Exercise 8 ---")

def greet(name, greeting = "Hello"):
    return greeting + ", " + name + "!"

print(greet("John"))
print(greet("John", "Good morning"))

print("\n--- Exercise 9 ---")

def concatenate_strings(*s):
    result = ""

    for i in s:
        result += i + " "

    return result

print(concatenate_strings("Hello", "world", "!"))

print("\n--- Exercise 10 ---")

def calculate_price(price, discount = 0.1):
    return price - price * discount

print(calculate_price(100))
print(calculate_price(100, 0.37))

print("\n--- Exercise 11 ---")

def person_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

person_info(Name="John", Surname="Doe", Age=38)

print("\n--- Exercise 12 ---")

def greet(*args, **kwargs):
    greeting = kwargs.get("greeting", "Hello")
    punctuation = kwargs.get("punctuation", "!")

    for name in args:
        print(f"{greeting}, {name}{punctuation}")

greet("John", "Jane", greeting="Hi", punctuation="?")