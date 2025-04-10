import string
import time
from collections import Counter

print("\n--- Exercise 1 ---")

def double_even_indeces(numbers):
    for i, num in enumerate(numbers):
        if i % 2 == 0:
            numbers[i] *= 2

    return numbers

nums = [1, 2, 3, 4, 5]
print(f"Initial list: {nums}")
print(f"Final list: {double_even_indeces(nums)}")

print("\n--- Exercise 2 ---")

def sort_by_last_char(strings):
    return sorted(strings, key = lambda string: string[-1])

strs = ["list", "lambda", "append", "exercise", "character"]

print(f"Initial list: {strs}")
print(f"Sorted list: {sort_by_last_char(strs)}")

print("\n--- Exercise 3 ---")

def filter_multiples_of_n(numbers, n):
    return list(filter(lambda num: num % n == 0, numbers))

nums = [10, 20, 14, 899, 67]
print(f"Initial list: {nums}")
print(f"Filtered list: {filter_multiples_of_n(nums, 2)}")

print("\n--- Exercise 4 ---")

def time_execution(func):
    def wrapper():
        start = time.time()
        result = func()
        end = time.time()
        print(f"Execution time: {round(end - start, 2)} seconds")

        return result

    return wrapper

@time_execution
def slow_function():
    time.sleep(2)
    return "Task completed"

print(slow_function())

print("\n--- Exercise 5 ---")

user_authenticated = False

def requires_auth(func):
    def wrapper():
        if user_authenticated is False:
            print("Access Denied")
            return

        return func()

    return wrapper

@requires_auth
def view_profile():
    return """First name: John
Last name: Doe
Age: ??"""

print(view_profile())

user_authenticated = True

print(view_profile())

print("\n--- Exercise 6 ---")

def filter_even_squares(nums):
    return [x*x for x in nums if x % 2 == 0]

nums = [1, 2, 3, 4, 5, 6]
print(f"Initial list: {nums}")
print(f"Filtered list: {filter_even_squares(nums)}")

print("\n--- Exercise 7 ---")

def count_word_frequencies(words):
    return {word: words.count(word) for word in set(words)}

str = ["some", "string", "in", "python", "in", "some", "quotes"]
print(f"Initial strings: {str}")
print(f"Count: {count_word_frequencies(str)}")

print("\n--- Exercise 8 ---")

def fibonacci():
    a, b = 0, 1
    while True:
        yield a

        a, b = b, a + b

print("First 10 fibonacci numbers")
f = fibonacci()
for i in range(10):
    print(next(f))

print("\n--- Exercise 9 ---")

def transpose_matrix(matrix):
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

nums = [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]]
print(f"Initial matrix: {nums}")
print(f"Transposed matrix: {transpose_matrix(nums)}")

print("\n--- Exercise 10 ---")

def time_execution(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Execution time: {end - start} seconds")

        return result

    return wrapper

@time_execution
def filter_and_time_execution(numbers, n):
    return list(filter(lambda num: num % n == 0, numbers))

nums = [10, 20, 14, 899, 67]
print(f"Initial list: {nums}")
print(f"Filtered list: {filter_and_time_execution(nums, 2)}")

print("\n--- Exercise 11 ---")

def generate_even_squares(limits):
    n = 0
    while n <= limits:
        if n % 2 == 0:
            yield n * n

        n += 1

result = (lambda squares: sum(squares))(generate_even_squares(10))
print(f"The sum of the first 10 squares is: {result}")

print("\n--- Exercise 12 ---")

def validate_inputs(func):
    def wrapper(nums, n):
        if len(nums) == 0:
            raise Exception("There are no numbers in the list")
        elif n == 0:
            raise Exception("Division by 0 is not allowed")
        return func(nums, n)

    return wrapper

@validate_inputs
def find_multiples_and_square(nums, n):
    return [num ** 2 for num in nums if num % n == 0]

nums = [1, 2, 3, 4, 5, 6]
print(find_multiples_and_square(nums, 2))

try:
    nums = []
    print(find_multiples_and_square(nums, 2))
except:
    print("List is empty, thus the exception was raised")

nums = [1, 2, 3, 4, 5, 6]
try:
    print(find_multiples_and_square(nums, 0))
except:
    print("Division by zero is not allowed, thus the exception was raised")

print("\n--- Advanced exercise ---")

def remove_punctuation_and_convert_to_lowercase(func):
    def wrapper(text, *args, **kwargs):
        cleaned_text = ''.join(c for c in text if c not in string.punctuation)
        cleaned_text = cleaned_text.lower()
        return func(cleaned_text, *args, **kwargs)

    return wrapper

def word_generator(text):
    for word in text.split():
        if len(word) > 2:
            yield word

@remove_punctuation_and_convert_to_lowercase
def top_n_frequent_words(text, n):
    words = list(word_generator(text))

    word_counter = Counter(words)

    if n > len(word_counter):
        n = len(word_counter)

    return [word for word in word_counter.most_common(n)]

text = "Some words in some string in Python, which uses punctuation, which is then removed."
print(text)
print(top_n_frequent_words(text, 4))