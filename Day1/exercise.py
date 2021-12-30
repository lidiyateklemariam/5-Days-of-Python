"""
# The name of the dictionary is person. It will have the follwing keys first name, last name, age, marital status, skills, hobbies, brothers, sisters, parents, country, province, address
, favorite quote

"""
# when creating a dictionary we need a curly bracket. 
# Tuple is for a data or lists which can not be changed. so we use bracket. But list is for a data which can be changed/modified. so we use square bracket.
# the key and the value makes the following data dictionary. 

person = {
'first_name': 'Lidiya',
'last_name': 'Woldesenbet', 
'age': 30, 
'is_married': True, 
'skills': ['HTML', 'CSS', 'Python', 'Git', 'Github'],
'hobbies': ['drawing', 'swiming', 'watching tv', 'learning language', 'coding'],
'brothers': ('Alex', 'Biruk', 'Yibekal'),
'sisters': ('Mekdes', 'Helen'),
'parents': ('Worke', 'Teklemariam'),
'country': 'Finland',
'province': 'Uusimaa',
'favourite_cote': 'practice makes perfect',
'address': {
    'street_name': 'Kirjanpitajankuja 4', 
    'zipcode': '02770',
    'city': 'Espoo',
        }
}
print(person)
