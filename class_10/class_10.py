import string
from collections import Counter

print("\nStudent grade analysis")
def analyze_grades(student_scores):
    average = sum(student_scores.values())/len(student_scores.values())

    print("Students with above average grade:")
    for item in student_scores.items():
        if item[1] > average:
            print(f"{item[0]} with a grade of {item[1]}")

    print("Top scorer(s):")
    max_score = max(student_scores.values())
    for item in student_scores.items():
        if item[1] == max_score:
            print(f"{item[0]} with a grade of {item[1]}")

scores = {
 'Alice': 85,
 'Bob': 92,
 'Charlie': 78,
 'Diana': 88
}
analyze_grades(scores)

print("\nWord frequency counter")
def word_frequency(text):
    return dict(Counter(text.lower().translate(text.maketrans('', '', string.punctuation)).split()))

text = "The quick brown fox jumps over the lazy dog. The dog was not amused."
print(word_frequency(text))

print("\nCustom range generator")
def custom_range(start, stop, step = 1):
    value = start

    while value < stop:
        yield value
        value += step

for num in custom_range(0.5, 3.0, 0.5):
    print(num)

print("\nFilter and transform even numbers")
def even_squares(numbers):
    return [x * x for x in numbers if x % 2 == 0]

print(even_squares([1, 2, 3, 4, 5, 6]))

print("\nCharacter category counter")
def categorize_characters(text):
    result = {"Letters" : 0, "Digits" : 0, "Spaces" : 0, "Other symbols" : 0}
    for character in text:
        if character.isalpha():
            result["Letters"] += 1
        elif character.isdigit():
            result["Digits"] += 1
        elif character.isspace():
            result["Spaces"] += 1
        else:
            result["Other symbols"] += 1

    return result

print(categorize_characters("Hello, World! 123"))

print("\nShopping cart with discounts")
def calculate_total(cart):
    total = sum(cart.values())
    if total > 100:
        return total * 0.9
    elif total > 50:
        return total * 0.95

    return total

cart = {
 'laptop': 900,
 'mouse': 25,
 'keyboard': 45
}

print(calculate_total(cart))