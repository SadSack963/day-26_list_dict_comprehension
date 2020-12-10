# List comprehension
# ==================

# new_list = [new_item for item in list]

numbers = [1, 2, 3, 4, 5]
new_numbers = [n + 1 for n in numbers]
print(new_numbers)

nato_phonetic_alphabet = ["Alpha", "Bravo", "Charlie", "Delta", "Echo", "Foxtrot", "Golf", "Hotel", "India", "Juliet",
                          "Kilo", "Lima", "Mike", "November", "Oscar", "Papa", "Quebec", "Romeo", "Sierra", "Tango",
                          "Uniform", "Victor", "Whisky", "X-ray", "Yankee", "Zulu"]

name = "John Patmore"
letters_list = [letter.upper() for letter in name]
print(letters_list)

double = [n * 2 for n in range(1, 5)]
print(double)


# Conditional list comprehension
# ==============================

# new_list = [new_item for item in list if test]

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
short_name = [name for name in names if len(name) < 5]
print(short_name)
caps_names = [name.upper() for name in names if len(name) > 5]
print(caps_names)


# Tests
# =====

numbers = [1, 1]
for i in range(2, 10):
    numbers.append(numbers[i-2] + numbers[i-1])
print(numbers)

squared_numbers = [n**2 for n in numbers]  # ** = exponent operator
print(squared_numbers)

result = [n for n in numbers if n % 2 == 0]
print(result)

# Create a list called result which contains the numbers
# that are common in both files file1.txt and file2.txt.
# The result should be a list that contains Integers, not Strings.

with open("file1.txt") as file:
    file1 = [int(n.strip()) for n in file.readlines()]  # .readlines() returns a list!
print(file1)

with open("file2.txt") as file:
    file2 = [int(n.strip()) for n in file.readlines()]  # .readlines() returns a list!
print(file2)

result = [n for n in file1 if n in file2]
print(result)

# Dictionary Comprehension
# ========================

# new_dict = {new_key:newvalue for item in list}
# new_dict = {new_key:newvalue for item in list if test}
# new_dict = {new_key:newvalue for (key,value) in dict.items()}
# new_dict = {new_key:newvalue for (key,value) in dict.items() if test}

import random

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
student_scores = {name: random.randint(0,100) for name in names}
print(student_scores)

for item in student_scores.items():
    print(item)
# passed_students = {item[0]: item[1] for item in student_scores.items() if item[1] >= 60}
passed_students = {student: score for (student, score) in student_scores.items() if score >= 60}
print(passed_students)


# Tests
# =====

# Create a dictionary called result that takes each word in the given sentence
# and calculates the number of letters in each word
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# Break sentence into words list
result = {word: len(word) for word in sentence.strip("?").split()}
print(result)

# Create a dictionary called weather_f that takes each temperature in degrees Celcius
# and converts it into degrees Fahrenheit.
weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}
weather_f = {day: (C * 9 / 5 + 32) for (day, C) in weather_c.items()}
print(weather_f)

# Iterate over a Pandas DataFrame
student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98],
}
# Looping through dictionaries:
for (key, value) in student_dict.items():
    print(key, value)

import pandas


