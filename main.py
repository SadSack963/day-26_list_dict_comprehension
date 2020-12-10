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

