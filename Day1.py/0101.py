

first_name = input('What is your first name? ')
last_name = input('What is your last name? ')
country = input('Where are you from? ')
city = input('What is the capital city? ')
year_born = int(input('When were you born '))
current_year = 2021
gender = input('What is your gender ? ').lower()

pronoun = ''

if gender == 'female':
    pronoun = 'She'
else:
    pronoun = 'He'

age = current_year - year_born
print(age)
  
print(f'{pronoun} is {first_name} {last_name}, Ethiopian. {pronoun} is {age} years old. {pronoun} lives in {city}, {country}.')



