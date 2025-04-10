import string
import sys

# Usage: python ex_n.py num1 num2
# In exercise 2 a) two numbers from command line should be provided when starting application

print("\n-- Exercise 1 a) --")
def ex1_a(number):
    if number % 2 == 0:
        print(f"{number} is even")
    else:
        print(f"{number} is odd")

ex1_a(1)
ex1_a(2)

print("\n-- Exercise 1 b) --")
def ex1_b():
    for i in range(2, 11, 1):
        print(f"1/{i} = {1/i:.4f}")

ex1_b()

print("\n-- Exercise 1 c) --")
def ex1_c(number):
    strNumber = str(number)
    strNumber = strNumber[::-1]
    number = int(strNumber)
    print(number)

ex1_c(1230)

print("\n-- Exercise 1 d) --")
def ex1_d(numbers):
    max = 0
    for i in numbers:
        if i > max:
            max = i

    print(max)

ex1_d([1, 2, 435, 4, 5, 4745])

print("\n-- Exercise 1 e) --")
def ex1_e():
    while True:
        number = int(input("Please, enter a number: "))
        for i in range(number, -1, -1):
            print(i)
        decision = input("Would you like to continue? (y/n): ")
        if decision == "n":
            break

ex1_e()

print("\n-- Exercise 2 a) --")
def ex2_a():
    if len(sys.argv) != 3:
        print("Incorrect input. Provide 2 numbers")
        exit()

    print(int(sys.argv[1]) + int(sys.argv[2]))

ex2_a()

print("\n-- Exercise 2 b) --")
def ex2_b():
    a = 5
    b = 3
    print("Arith. Operations")
    print(f"a + b = {a + b}")
    print(f"a - b = {a - b}")
    print(f"a * b = {a * b}")
    print(f"a / b = {a / b}")
    print(f"a // b = {a // b}")
    print(f"a % b = {a % b}")
    print(f"a ** b = {a % b}")
    print("\n")

    print("Comp. operations")
    x = 5
    y = 3
    print(f"x == y: {x == y}")
    print(f"x != y: {x != y}")
    print(f"x > y: {x > y}")
    print(f"x < y: {x < y}")
    print(f"x >= y: {x >= y}")
    print(f"x <= y: {x <= y}")
    print("\n")

    print("logical operations")
    t = True
    f = False
    print(f"t and f = {t and f}")
    print(f"t or f = {t or f}")
    print(f"not t:{not t}")
    print("\n")

    print(f"a & b: {a & b}")
    print(f"a ^ b: {a ^ b}")
    print(f"a | b: {a | b}")
    print(f"a << 1: {a << 1}")
    print(f"a >> 1: {a >> 1}")

ex2_b()

print("\n-- Exercise 2 c) --")
def ex2_c():
    age = int(input("Please, enter your age: "))
    if age >= 18:
        print("You are eligible for voting")
    else:
        print("You are not eligible for voting")

ex2_c()

print("\n-- Exercise 2 d) --")
def ex2_d(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(f"{year} is a leap year")
    else:
        print(f"{year} is not a leap year")

ex2_d(2000)
ex2_d(2025)

print("\n-- Exercise 3 a) --")
def ex3_a(n):
    naturalNumbers = range(0, n + 1, 1)

    print(naturalNumbers)

ex3_a(223)

print("\n-- Exercise 3 b) --")
def ex3_b(number):
    strNumber = str(number)
    strNumber = strNumber[::-1]
    reverseNumber = int(strNumber)

    print(f"{number} is palindrome? {number == reverseNumber}")

ex3_b(121)
ex3_b(123)

print("\n-- Exercise 3 c) --")
def ex3_c(number):
    factorial = 1
    for i in range(number, 0, -1):
        factorial = factorial * i

    print(f"Factorial of {number} is {factorial}.")

ex3_c(4)

print("\n-- Exercise 3 d) --")
def ex3_d(n):
    if type(n) == type(1.1) or n < 0:
        print("Provide a natural number")
        return

    sum = 0
    naturalNumbers = range(0, n + 1, 1)

    for i in naturalNumbers:
        sum += i

    print(f"Sum of natural number is: {sum}")

ex3_d(1)

print("\n-- Exercise 3 e) --")
def ex3_e(number):
    sum = 0
    strNumber = str(number)

    for i in strNumber:
        sum += int(i)**3

    if sum == number:
        print(f"{number} is an Armstrong number")
    else:
        print(f"{number} is not an Armstrong number")

ex3_e(3)

print("\n-- Exercise 3 f) --")
def ex3_f(n):
    if n <= 1:
        print("No prime numbers")

    primeNumbers = []

    for i in range(2, n + 1):
        isPrime = True

        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                isPrime = False
                break
        if isPrime:
            primeNumbers.append(i)

    print(primeNumbers)

ex3_f(20)

print("\n-- Exercise 4 a) --")
def ex4_a(list):
    sum = 0

    for i in list:
        sum += i

    print(f"Sum is: {sum}")
    print(f"Average is: {int(sum/len(list))}")

numbers = [1, 2, 3, 4, 5, 1234, 1234, 234, 1253, 123, -1]
ex4_a(numbers)

print("\n-- Exercise 4 b) --")
def ex4_b(list):
    print(list[::-1])

ex4_b(numbers)

print("\n-- Exercise 4 c) --")
def ex4_c(list):
    min = list[0]
    max = 0

    for i in list:
        if i > max:
            max = i
        if i < min:
            min = i

    print(f"Maximum is: {max}. Minimum is: {min}")

ex4_c(numbers)

print("\n-- Exercise 5 a) --")
def ex5_a(inputStr):
    print(f"Original string: {inputStr}")
    print(f"Uppercase: {inputStr.upper()}")
    print(f"Lowercase: {inputStr.lower()}")
    print(f"Title Case: {inputStr.title()}")
    print(f"Is the string alphanumeric? {inputStr.replace(' ', '').isalnum()}")
    print(f"After replacing 'Python' with 'Java': {inputStr.replace('Python', 'Java')}")
    print(f"Number of occurrences of 'o': {inputStr.count('o')}")
    print(f"Trimmed string (no leading/trailing whitespace): {inputStr.strip()}")
    print(f"List of words in the string: {inputStr.split()}")
    print("\nString module constants:")
    print(f"ASCII Letters: {string.ascii_letters}")
    print(f"Digits: {string.digits}")
    print(f"Punctuation: {string.punctuation}")

ex5_a("Some string written in Python")

print("\n-- Exercise 5 b) --")
def ex5_b(inputStr):
    if inputStr.lower() == inputStr[::-1].lower():
        print(f"{inputStr} is a palindrome")
    else:
        print(f"{inputStr} is not a palindrome")

ex5_b("Madam")

print("\n-- Exercise 5 c) --")
def ex5_c(text):
    characters = 0
    vowels = 0
    blankSpaces = 0

    for i in text.strip():
        if i == ' ':
            blankSpaces += 1
        elif i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
            vowels += 1

    for i in text.split():
        characters += len(i)
    print(f"In a sentence: '{text}'")
    print(f"Number of characters: {characters}. Number of vowels: {vowels}. Number of blank spaces: {blankSpaces}")

ex5_c("Palindrome is a word, phrase, or sequence that reads the same backwards as forwards, e.g. madam or nurses run.")

print("\n-- Exercise 6 a) --")
def ex6_a(num1, num2, num3):
    numbers = [num1, num2, num3]

    max = 0
    for i in numbers:
        if i > max:
            max = i

    print(f"The largest number is: {max}")

ex6_a(132, 2, 3)

print("\n-- Exercise 6 b) --")
def ex6_b():
    numbers = []

    for i in range(1000, 2000):
        if i % 7 == 0 and i % 5 != 0:
            numbers.append(i)

    print(numbers)

ex6_b()

print("\n-- Exercise 7 a) --")
def ex7_a(n):
    if n <= 0:
        return []
    if n == 1:
        return [0]

    sequence = [0, 1]

    while len(sequence) < n:
        nextNumber = sequence[-1] + sequence[-2]
        sequence.append(nextNumber)

    return sequence

print(ex7_a(10))

print("\n-- Exercise 7 b) --")
def ex7_b(number):
    power = len(str(number))

    def sum_of_digits(num):
        if num == 0:
            return 0

        return (num % 10) ** power + sum_of_digits(num // 10)

    return number == sum_of_digits(number)

print(ex7_b(153))

print("\n-- Exercise 7 c) (call by value)--")
def ex7_c_callByValue(num):
    print(f"Before modification: {num}")
    num += 10

x = 10
ex7_c_callByValue(x)
print(f"After modification: {x}")

print("\n-- Exercise 7 c) (call by reference) --")
def ex7_c_callByReference(list):
    print(f"Before modification: {list}")
    list.append(99)

ls = [1, 2, 3]
ex7_c_callByReference(ls)
print(f"After modification: {ls}")

print("\n-- Exercise 7 d) --")
def ex7_d(n):
    if n == 0:
        return 1

    return n * ex7_d(n-1)

print(ex7_d(4))

print("\n-- Exercise 8 a) --")
def ex8_a():
    numbers = input("Enter comma-separated numbers: ")

    l = numbers.split(',')
    t = tuple(l)

    print(l, t)

ex8_a()

print("\n-- Exercise 8 b) --")
def ex8_b(t):
    t1 = t[:len(t)//2]
    t2 = t[len(t) // 2:]

    print(t1)
    print(t2)

t = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
ex8_b(t)