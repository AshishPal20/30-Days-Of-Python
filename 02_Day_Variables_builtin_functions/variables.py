
# Variables in Python

first_name = 'Ashish Pal'
last_name = 'Pal'
country = 'India'
city = 'New Delhi'
age = 20
is_married = False
skills = ['HTML', 'CSS', 'Scikit Learn', 'SQL', 'Python']
person_info = {
    'firstname': 'Ashish',
    'lastname': 'Pal',
    'country': 'India',
    'city': 'New Delhi'
}

# Printing the values stored in the variables

print('First name:', first_name)
print('First name length:', len(first_name))
print('Last name: ', last_name)
print('Last name length: ', len(last_name))
print('Country: ', country)
print('City: ', city)
print('Age: ', age)
print('Married: ', is_married)
print('Skills: ', skills)
print('Person information: ', person_info)

# Declaring multiple variables in one line

first_name, last_name, country, age, is_married = 'Ashish', 'Pal', 'India', 20, False

print(f"First name: {first_name}")
print(f"Last name: {last_name}")
print(f"Country: {country}")
print(f"Age: {age}")
print(f"Married: {is_married}")
