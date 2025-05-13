import re
from os.path import split

print("\n--- Exercise 1 ---")
def count_up_to(n):
    for i in range(1, n - 1):
        yield i

for i in count_up_to(5):
    print(i, end=", ")

print("\n--- Exercise 2 ---")
def fibonacci(limit):
    a, b = 0, 1
    while a < limit:
        yield a

        a, b = b, a + b

for i in fibonacci(10):
    print(i, end=", ")

print("\n--- Exercise 3 ---")
def even_numbers(lst):
    for i in lst:
        if i % 2 == 0:
            yield i

for i in even_numbers([1, 2, 3, 4]):
    print(i, end=", ")

print("\n--- Exercise 4 ---")
def lazy_generator(file):
    with open(file) as f:
        for line in f:
            yield line

for word in lazy_generator("sometext"):
    print(word, end=", ")

print("\n--- Exercise 5 ---")
def chunker(seq, size):
    for i in range(0, len(seq), size):
        yield seq[i:i + size]

for chunk in chunker([1, 2, 3, 4, 5], 3):
    print(chunk)

print("\n--- Exercise 6 ---")
def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def generate_primes():
    number = 0
    while True:
        if is_prime(number):
            yield number

        number += 1

# for i in generate_primes():
#     print(i)

print("\n--- Exercise 7 ---")
def printer():
    while True:
        value = yield
        print(value)

p = printer()
next(p)
p.send("Hello, ")
p.send("world!")

print("\n--- Exercise 8 ---")
def running_average():
    total = 0.0
    count = 0
    average = None

    while True:
        value = yield average
        total += value
        count += 1
        average = total / count

r_a = running_average()
next(r_a)

print(r_a.send(10))
print(r_a.send(50))
print(r_a.send(100))

print("\n--- Exercise 9 ---")
def keyword_filter(keyword):
    print(f"Filtering messages with keyword: '{keyword}'")

    while True:
        message = (yield)
        if keyword in message:
            print(message)

k_f = keyword_filter("python")
next(k_f)

k_f.send("Hello, Python")
k_f.send("This message will not be printed")
k_f.send("But this message will be printed, because of Python")

k_f.close()

print("\n--- Exercise 10 ---")
def produce_numbers(n):
    for i in range(n):
        yield i

def double_numbers(target):
    while True:
        number = (yield)
        target.send(number * 2)

def print_results():
    while True:
        result = (yield)
        print("Result:", result)

printer = print_results()
next(printer)

d_n = double_numbers(printer)
next(d_n)

for number in produce_numbers(10):
    d_n.send(number)

d_n.close()

print("\n--- Exercise 11 ---")
def regex_matcher(pattern):
    print(f"Filtering messages with pattern: '{pattern}'")

    while True:
        message = yield
        for line in message.split('\n'):
            if re.findall(pattern, line):
                print(line)

r_m = regex_matcher("")

matcher = regex_matcher(r"\berror\b")
next(matcher)

matcher.send("This line is not printed\n(but this is printed) critical error occurred\nthis is a note")
matcher.send("warning only\nno issue\nerror on line 3")

matcher.close()