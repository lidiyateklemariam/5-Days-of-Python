import math
# for importing mathematics formula. 
# print(dir(math))

print(math.pi)

print(math.sqrt(4))

print(math.sqrt(9))
print(math.sqrt(100))
print(math.sqrt(25))

print(math.sqrt(2))
print(math.floor(9.81))
print(math.ceil(3.14))
print(round(3.1478))
print(round(3.1478, 2))

#or
#print(dir(math))

from math import sqrt, floor, ceil as roof, pi
print(sqrt(2))
print(floor(9.81))
print(roof(3.14))


import random
print(dir(random))
print(random.random()) #0 to 0.999999999
print(random.randint(0, 10))

lottory = []
for i in range(7):
     n = random.randint(0, 10)
     lottory.append(n)
print(lottory)


def get_luck_numbers(n):
    import random
    lottory = []
    for i in range(n):
        n = random.randint(0, 10)
        lottory.append(n) 
        return lottory
print(get_luck_numbers(10))




import countries_list
print(countries_list.countries)

from pprint import pprint
#print(countries_list.countries)
for country in countries_list.countries:
    pass


def get_countries_with_ia():
    new_list = []
    for c in country:
        if'land' in c:
            new_list.append(c)
    return new_list

print(get_countries_with_ia())



def get_countries_with_e():
    new_list = []
    for c in countries_list.countries:
        if c.startswith('E'):
            new_list.append(c)
    return new_list

print(get_countries_with_e())



