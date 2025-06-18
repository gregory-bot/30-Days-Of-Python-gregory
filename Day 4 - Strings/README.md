Strings
Strings in Python represent text. They are created using single ('...'), double ("..."), or triple ('''...''' or """...""") quotes. Python includes many built-in methods to manipulate and format strings.

Creating Strings
You can create a string using quotes and determine its length using the len() function.

python
Copy
Edit
letter = 'P'
print(letter)               # Output: P
print(len(letter))          # Output: 1

greeting = "Hello, World!"
print(greeting)             # Output: Hello, World!
print(len(greeting))        # Output: 13

sentence = "Enjoy learning Python every day!"
print(sentence)             # Output: Enjoy learning Python every day!
Multiline Strings
Use triple quotes (''' or """) to create strings that span multiple lines.

python
Copy
Edit
multiline = '''Python is fun.
It’s simple yet powerful.'''
print(multiline)
String Concatenation
Use the + operator to join strings.

python
Copy
Edit
first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name
print(full_name)  # Output: John Doe
Escape Sequences
Special characters can be inserted using escape sequences:

\n → New line

\t → Tab

\\ → Backslash

\' → Single quote

\" → Double quote

Example:

python
Copy
Edit
print("Python\nis\tawesome!")
String Formatting
Old Style Formatting (% operator)
python
Copy
Edit
name = "Alice"
age = 25
print("My name is %s, and I am %d years old." % (name, age))
str.format() Method
python
Copy
Edit
print("My name is {}, and I am {} years old.".format(name, age))
f-Strings (Python 3.6+)
python
Copy
Edit
print(f"My name is {name}, and I am {age} years old.")
Slicing and Indexing
Strings can be accessed like arrays using index values.

python
Copy
Edit
language = "Python"
print(language[0])    # Output: P
print(language[-1])   # Output: n
print(language[:3])   # Output: Pyt
Reversing Strings
Use slicing to reverse strings:

python
Copy
Edit
print(language[::-1])  # Output: nohtyP
String Methods
Python provides many methods to work with strings.

Method	Description
capitalize()	Capitalizes the first letter
count(x)	Returns number of occurrences of substring x
endswith(x)	Checks if the string ends with x
find(x)	Returns the index of first occurrence of x
join(list)	Joins elements of a list into a string
replace(a, b)	Replaces a with b
split()	Splits string into list
strip(chars)	Removes leading/trailing characters

Example:

python
Copy
Edit
text = "  Python is amazing!  "
print(text.strip())  # Output: Python is amazing!
Advanced String Checks
These methods return boolean values:

python
Copy
Edit
print("Python".isalpha())         # True
print("123".isdigit())            # True
print("Python123".isalnum())      # True
print("python".islower())         # True
print("PYTHON".isupper())         # True
print("python".startswith("py"))  # True
