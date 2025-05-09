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
    while True:
        numbers = yield
        window = []
        total = 0