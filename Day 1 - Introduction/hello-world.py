# Day 1 - Introduction to Python 🚀

# ✅ 1. Hello World
print("Hello, Python learners!")

# ✅ 2. Basic Arithmetic Operators
print(3 + 2)    # Addition
print(3 - 2)    # Subtraction
print(3 * 2)    # Multiplication
print(3 / 2)    # Division
print(3 ** 2)   # Exponentiation
print(3 % 2)    # Modulus
print(3 // 2)   # Floor Division

# ✅ 3. Data Types
print(type(10))                    # Integer
print(type(3.14))                  # Float
print(type(1 + 3j))                # Complex
print(type('Gregory'))             # String
print(type([1, 2, 3]))             # List
print(type({'name': 'Gregory'}))   # Dictionary
print(type({9.8, 3.14, 2.7}))      # Set
print(type((9.8, 3.14, 2.7)))      # Tuple
print(type(3 == 3))                # Boolean
print(type(3 >= 3))                # Boolean

# ✅ 4. Variables and Data Types
name = "Gregory"
age = 21
is_coding = True
height = 1.75  # in meters

# Output using f-string
print(f"My name is {name}. I am {age} years old. Coding: {is_coding}")

# ✅ 5. Type Checking
print(type(name))      # str
print(type(age))       # int
print(type(is_coding)) # bool
print(type(height))    # float

# ✅ 6. More Arithmetic: Age & BMI
birth_year = 2025 - age
bmi = 68 / (height ** 2)

print(f"I was born in {birth_year}")
print(f"My estimated BMI is {round(bmi, 2)}")

# ✅ 7. Mini Task - Personal Practice
book_title = "A Doll’s House"
author = "Henrik Ibsen"

print(f"My favorite book is '{book_title}' by {author}.")
