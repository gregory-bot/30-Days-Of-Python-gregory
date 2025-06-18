🟩 Single Line Comment and String Basics
python
Copy
Edit
# Single line comment
letter = 'P'  # A string can be a single character or more
print(letter)               # Output: P
print(len(letter))          # Output: 1

greeting = 'Hello, World!'  # Strings can use single or double quotes
print(greeting)             # Output: Hello, World!
print(len(greeting))        # Output: 13

sentence = "I hope you are enjoying 30 days of Python challenge"
print(sentence)
🟩 Multiline Strings
python
Copy
Edit
multiline_string = '''I am Gregory and enjoy teaching.
I didn't find anything as rewarding as empowering people.
That is why I created 30 days of Python.'''
print(multiline_string)

# Another way
multiline_string = """I am Gregory and enjoy teaching.
I didn't find anything as rewarding as empowering people.
That is why I created 30 days of Python."""
print(multiline_string)
🟩 String Concatenation and Length Check
python
Copy
Edit
first_name = 'Gregory'
last_name = 'Kipngeno'
space = ' '
full_name = first_name + space + last_name
print(full_name)  # Output: Gregory Kipngeno

# Check length
print(len(first_name))         # Output: 7
print(len(last_name))          # Output: 8
print(len(first_name) > len(last_name))  # Output: False
print(len(full_name))          # Output: 16
🟩 Unpacking Characters
python
Copy
Edit
language = 'Python'
a, b, c, d, e, f = language
print(a)  # Output: P
print(b)  # Output: y
print(c)  # Output: t
print(d)  # Output: h
print(e)  # Output: o
print(f)  # Output: n
🟩 Indexing and Negative Indexing
python
Copy
Edit
language = 'Python'
print(language[0])     # P
print(language[1])     # y
print(language[-1])    # n
print(language[-2])    # o
🟩 Slicing and Skipping
python
Copy
Edit
language = 'Python'
print(language[0:3])   # Pyt
print(language[3:6])   # hon
print(language[-3:])   # hon
print(language[3:])    # hon
print(language[0:6:2]) # Pto
🟩 Escape Sequences
python
Copy
Edit
print('Enjoying Python?\nLet\'s level up!\tStart now.')
print('Days\tTopics\tExercises')
print('Day 1\t3\t5')
print('Day 2\t3\t5')
print('Day 3\t3\t5')
print('This is a backslash: \\')
print("In every programming course, we begin with \"Hello, World!\"")
🟩 String Methods Overview
python
Copy
Edit
challenge = 'thirty days of python'
print(challenge.capitalize())        # 'Thirty days of python'
print(challenge.count('y'))          # 3
print(challenge.endswith('on'))      # True
print(challenge.expandtabs(10))      # Replaces \t with spaces
print(challenge.find('y'))           # Index of 'y'
🟩 String Formatting
python
Copy
Edit
first_name = 'Gregory'
last_name = 'Kipngeno'
job = 'developer'
country = 'Kenya'
sentence = 'I am {} {}. I am a {}. I live in {}.'.format(first_name, last_name, job, country)
print(sentence)  # I am Gregory Kipngeno. I am a developer. I live in Kenya.

radius = 10
pi = 3.14
area = pi * radius ** 2
print('The area of a circle with radius {} is {}'.format(radius, area))
🟩 String Validation Methods
python
Copy
Edit
challenge = 'ThirtyDaysPython'
print(challenge.isalnum())     # True

print('123'.isdigit())         # True
print('ten'.isnumeric())       # False

challenge = 'thirty_days_of_python'
print(challenge.isidentifier())  # True

print('python'.islower())      # True
print('PYTHON'.isupper())      # True
🟩 More Useful Methods
python
Copy
Edit
web_tech = ['HTML', 'CSS', 'JavaScript']
joined = '# '.join(web_tech)
print(joined)  # 'HTML# CSS# JavaScript'

challenge = ' thirty days of python '
print(challenge.strip())        # 'thirty days of python'

print(challenge.replace('python', 'coding'))  # 'thirty days of coding'
print(challenge.split())        # ['thirty', 'days', 'of', 'python']
print(challenge.title())        # Thirty Days Of Python
print(challenge.swapcase())     # THIRTY DAYS OF PYTHON
print(challenge.startswith('thirty'))  # True
