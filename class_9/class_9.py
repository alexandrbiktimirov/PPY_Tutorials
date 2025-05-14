import re
import os
import time
import asyncio

print("\n--- Exercise 1 ---")
def count_up_to(n):
    for i in range(1, n + 1):
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

print("This function was not included in the output due to it being infinite")
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

print("\n--- Exercise 12 ---")
def printer():
    try:
        while True:
            value = yield
            print(value)
    except GeneratorExit:
        print("Shutting down...")

p = printer()
next(p)

p.send("Hello cleanup")

p.close()

print("\n--- Exercise 13 ---")
def info_handler():
    try:
        while True:
            event = yield
            print("[INFO]", event)
    except GeneratorExit:
        print("Info handler shutting down...")

def error_handler():
    try:
        while True:
            event = yield
            print("[ERROR]", event)
    except GeneratorExit:
        print("Error handler shutting down...")

def debug_handler():
    try:
        while True:
            event = yield
            print("[DEBUG]", event)
    except GeneratorExit:
        print("Debug handler shutting down...")

def event_dispatcher(handlers):
    try:
        while True:
            event = yield
            for prefix, handler in handlers.items():
                if event.startswith(prefix):
                    handler.send(event)
                    break
    except GeneratorExit:
        for handler in handlers.values():
            handler.close()
        print("Dispatcher shutting down...")

info = info_handler(); next(info)
error = error_handler(); next(error)
debug = debug_handler(); next(debug)

disp = event_dispatcher({
    "info:": info,
    "error:": error,
    "debug:": debug
})

next(disp)

disp.send("info: Application started")
disp.send("debug: Initializing modules")
disp.send("error: Failure encountered")
disp.close()

print("\n--- Exercise 14 ---")
def number_generator(n):
    for i in range(1, n + 1):
        yield i

def multiplier(m):
    try:
        while True:
            value = yield
            result = value * m
            feedback = yield result
            print(f"Multiplier received feedback: {feedback}")
    except GeneratorExit:
        print("Multiplier shutting down...")

def running_average():
    total = count = 0
    avg = None

    try:
        while True:
            value = yield avg
            count += 1
            total += value
            avg = total / count
    except GeneratorExit:
        print("Running average shutting down...")

nums = number_generator(5)

mul = multiplier(2)
next(mul)

avg_calc = running_average()
next(avg_calc)

for num in nums:
    doubled = mul.send(num)
    average = avg_calc.send(doubled)
    print(f"Num: {num}, Doubled: {doubled}, Running Average: {average}")
    mul.send(f"Processed {doubled}")

mul.close()
avg_calc.close()

print("\n--- Exercise 15 ---")
def txt_line_reader(root):
    for dirpath, dirnames, filenames in os.walk(root):
        for fname in filenames:
            if fname.endswith(".txt"):
                filepath = os.path.join(dirpath, fname)
                with open(filepath, encoding="utf-8") as f:
                    for line in f:
                        yield line.rstrip("\n")

os.makedirs("test_dir/sub", exist_ok=True)

with open("test_dir/file1.txt", "w", encoding="utf-8") as f:
    f.write("Line1\nLine2\n")

with open("test_dir/sub/file2.txt", "w", encoding="utf-8") as f:
    f.write("SubLine1\nSubLine2\n")

print(list(txt_line_reader("test_dir")))

print("\n--- Exercise 16 ---")
def rate_limiter(max_per_sec):
    interval = 1.0 / max_per_sec
    last_time = None

    try:
        while True:
            task = yield
            now = time.time()
            if last_time is not None:
                to_wait = interval - (now - last_time)
                if to_wait > 0:
                    time.sleep(to_wait)
            print(f"{time.strftime('%X')} - Processing task: {task}")
            last_time = time.time()
    except GeneratorExit:
        print("Rate limiter shutting down...")

r_l = rate_limiter(2)
next(r_l)

for i in range(5):
    r_l.send(f"task {i + 1}")
r_l.close()

print("\n--- Exercise 17 ---")
async def task(name, delay):
    print(f"{time.strftime('%X')} - Task {name} starting (delay {delay}s)")
    await asyncio.sleep(delay)
    print(f"{time.strftime('%X')} - Task {name} completed")

async def main():
    await asyncio.gather(
        task("A", 1),
        task("B", 1.5),
        task("C", 0.5)
    )

asyncio.run(main())