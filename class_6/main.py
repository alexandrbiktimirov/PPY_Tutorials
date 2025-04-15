import string
from collections import Counter

print("\n--- Exercise 1 ---")

def reverse_input_string(input_string):
    return input_string[::-1]

input_string = "hello"
print(reverse_input_string(input_string))

print("\n--- Exercise 2 ---")

def vowel_count(input_string):
    return sum(1 for c in input_string if c in "aeiouAEIOU")

print (vowel_count(input_string))

print("\n--- Exercise 3 ---")

def is_palindrome(input_string):
    return input_string == input_string[::-1]

print(is_palindrome("madam"))

print("\n--- Exercise 4 ---")

def every_second_character(input_string):
    return input_string[1::2]

chars = "abcdefg"
print(every_second_character(chars))

print("\n--- Exercise 5 ---")

def first_and_last_character(input_string):
    return input_string[0], input_string[-1]

print(first_and_last_character(chars))

print("\n--- Exercise 6 ---")

def capitalize(input_string):
    return " ".join([c.capitalize() for c in input_string.split(" ")])

input_string = "hello world"
print(capitalize(input_string))

print("\n--- Exercise 7 ---")

def opposite_case(input_string):
    return "".join([c.upper() if c.islower() else c.lower() for c in input_string])

input_string = "PyThOn"
print(opposite_case(input_string))

print("\n--- Exercise 8 ---")

def count_substring(input_string, subinput_string):
    return input_string.count(subinput_string)

input_string = "banana"
print(count_substring(input_string, "an"))

print("\n--- Exercise 9 ---")

def replace_spaces(input_string):
    return input_string.replace(" ", "-")

input_string = "hello world"
print(replace_spaces(input_string))

print("\n--- Exercise 10 ---")

def is_anagram(input_string1, input_string2):
    return sorted(input_string1) == sorted(input_string2)

print(is_anagram("listen", "silent"))

print("\n--- Exercise 11 ---")

def remove_punctuation(input_string):
    return "".join([c for c in input_string if c not in string.punctuation])

input_string = "Some, sentence. with? punctuation!"
print(input_string)
print(remove_punctuation(input_string))

print("\n--- Exercise 12 ---")

def count_frequency(input_string):
    return dict(Counter(remove_punctuation(input_string).split()))

print(count_frequency(input_string))

print("\n--- Exercise 12 ---")

def custom_split(input_string, delimiter):
    result, delim_len = [], len(delimiter)
    idx = 0

    while idx <= len(input_string):
        next_idx = input_string.find(delimiter, idx)

        if next_idx == -1:
            result.append(input_string[idx:])
            break

        result.append(input_string[idx:next_idx])
        idx = next_idx + delim_len

    return result

input_string = "Some, sentence. with? punctuation!"
print(custom_split(input_string, "ds"))

print("\n--- Exercise 14 ---")

# def scan_for_dates(input_string):
#