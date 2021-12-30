#def means definition.
#Functions: makes code reuseable, maintable, testable.
#Functions are divided in to 2. Built in function and custom function.

def xyz(): 
    print('I am a function')
xyz()


def do_something():
    print('I am doing something')
do_something()


def print_fullname():
    first_name = 'Lidiya'
    last_name = 'Woldesenbet'
    full_name = first_name + ' ' + last_name
    print(full_name)
print_fullname()


""" 
def print_fullname(first_name, last_name):
    full_name = first_name + ' ' + last_name
    print(full_name)
print_fullname('eyob', 'yetayeh')
print_fullname('lidiya', 'woldesenbet')
print_fullname('helen', 'woldesenbet') """



def create_fullname(first_name, last_name):
    full_name = first_name + ' ' + last_name
    return full_name.upper()

print(create_fullname('eyob', 'yetayeh'))
print(create_fullname('lidiya', 'woldesenbet'))
print(create_fullname('helen', 'woldesenbet'))


def add_two_nums(a, b):
    total = a + b
    return total

print(add_two_nums(10, 20))
print(add_two_nums(10, -10))
print(add_two_nums(1, 99))


def add_three_nums(a, b, c):
    total = a + b + c
    return total

print(add_three_nums(10, 20, 30))


#1. The name of the function is calculate_area_rectangle. It takes length and width as a parameter and it returns the area. Formula of area = length * width
#2. Calculate perimeter of a reactangle. It takes lengh and width as parameters and it should return the perimeter of the rectangle. Formula = perimeter = 2 * (length + width)


def calculate_area_rectangle(length, width):
    area = length * width
    return area

print(calculate_area_rectangle(5, 10))



def calculate_area_rectangle(length, width):
    perimeter = 2 * (length + width)
    return perimeter

print(calculate_area_rectangle(5, 10))


def generate_evens(n):
    evens = list(range(0, n + 1, 2))
    return evens
print(generate_evens(50))


def generate_odds(n):
    odds = list(range(1, n + 1, 2))
    return odds
print(generate_odds(50))


def calculate_weight (mass, gravity = 9.81):
    weight = mass * gravity
    return weight
print(calculate_weight)





def add_two_nums(a, b):
    total = a  + b
    return total

def multiply_two_nums(a, b):
    mul = a * b
    return mul

def make_square(n):
    return n ** 2


def calculate_area_rectangle(length, width):
    return length * width

def generate_evens(n):
    evens = list(range(0, n + 1, 2))
    return evens

def calculate_weight (mass, gravity = 9.81):
    weight = mass * gravity
    return weight

def calc_perimeter_rect(length, width):
    perimeter = (length  + width) * 2
    return perimeter


