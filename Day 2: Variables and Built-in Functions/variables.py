# Day 2: 30 Days of Python programming

# Variables in Python programming

first_name = 'Gregory'
last_name = 'Kipngeno'
full_name = first_name + ' ' + last_name
country = 'Kenya'
city = 'Nairobi'
age = 23
is_married = False
skills = ['JavaScript', 'React', 'Python', 'Node.js', 'SQL']
profession = 'Software Developer'
hobby = 'Cycling😎'
university = 'Zetech University'
year_of_study = 4
person_info = {
    'firstname': first_name,
    'lastname': last_name,
    'country': country,
    'city': city,
    'age': age,
    'skills': skills,
    'profession': profession,
    'university': university
}

# Printing the values stored in the variables

print('Full Name:', full_name)
print('First name length:', len(first_name))
print('Last name length:', len(last_name))
print('Country:', country)
print('City:', city)
print('Age:', age)
print('Married:', is_married)
print('Skills:', skills)
print('Profession:', profession)
print('Hobby:', hobby)
print('University:', university)
print('Person Information:', person_info)

# Declaring multiple variables in one line

first_name, last_name, country, age, is_married = 'Gregory', 'Kipngeno', 'Kenya', 23, False

print(first_name, last_name, country, age, is_married)
print('First name:', first_name)
print('Last name:', last_name)
print('Country:', country)
print('Age:', age)
print('Married:', is_married)
