#data types are:
numbers (int, float, complex)
strings
booleans (True or False)
List, set, tuple, dictionary
#Builtin fuction we use to check a type are: type(). e.g. type(10)
print(type(10))
print(type('10')) #it is string.
print(type(9.81)) #it is float. 
print(type(1 + 2j)) #it is complex


print(type(10))
print(type('10'))
print(type(9.81))
print(type(1 + 2j))
#integers are -3,-2,-1,0,1,2,3,.....
#floats: numbers with decimal. e.g. 3.14,1.5,96.7
#complex numbers: 2 + 2j, 1 + 4j
#strings: are texts. As short as a single character or as long as many pages. 

letter = 'a'
word = 'love'

print(letter)
print(len(letter))
print(word)
print(len(word))
print(word[0])
print(word[1])
last_index=len(word) -1
print(word[3])
print(word[last_index])
print(word[4])


#method have to be attached with something. eg. print with uppercase
#function are not attached to anything. eg. print. 

sentence = 'I love python'
print(sentence)
print(sentence.upper())
print(sentence.lower())
print(sentence.count())


dna = '''gtggcgctgcagagtagaactccgttgttagaccagtaatatctgggggcggaagatggc
ctcggagcgaggctgaaggaactcagtatctaaaagttaattgatgagcatttctaccgg
ggagcgccgtagatggcagtgagccgtttaaagctcatcatctcagcaccgcgaagagtc
ctctgtgggggtccgggcacaccccgagtagtatcctgcacccaacacaggcatcccgtc
gagtatagtataaagaaggtctgcggttatttggtcctgttttctctttacgatacaacg
tataaaccgcgggcttgcagaagccatctcaatttaccttaccttcttcggtatattctt
tataggctggtcaacaacaatcaacattgggggtcgcgaaattcgtgacgccttaggccc
ttgcgtacaggacgttgttcttaccataattacaggctgacttgtgcgaaaagtccgatt
tgccacatgacactcctaccgagcagcttgcgttaggacagttcgcaaattccctaacaa
aggtagcgtttcggaagatacccaaagcggcgcaggtcttcccgaagcaaagtgtggccg
tgtggtgtacatggccacatgggaacagtcgagacgacgtctctcataagtagacggata
tgctatacttgcggcaggcaccagggttctattccggtatctttccgtgggggtgcattc
cgtccataggcctcgtcgccggggattaacggcggcttcgcccaccgttccattaagtgc
gcctatcggcatagaaggtcgtttcctagaaccgggtgctccctagttttacggactcca
tggatttgtatgggccacttgctattcgcgtaagggatcacatatggtttagagacccac
cggtgcaccaaaactcggccttcaagagcctgacaatttacatggctcacccttgtgacg
gtctagccgtagggctgaataacctcttttgcctaaacac'''

print(dna)
print(len(dna))

total_count = len(dna)
a = dna.count('a')
c = dna.count('c')
t = dna.count('t')
g = dna.count('g')
print(a, c,t, g)
print('proporation', 'a nucotide:',  round(a / total_count * 100, 2), '%')
print('proporation','c nucotide:',round(c / total_count * 100, 2), '%')
print('proporation', 't nucotide:', round(t/total_count * 100, 2), '%')
print('proporation',  'g nucotide:', round(g/total_count * 100, 2), '%')


# string methods are:
#.upper(), .lower() and .count()

Sentences = 'I love python and I love Javascript. I am looking for a new job. I can not wait to get started.'
Print(sentences.count('I'))
Print(sentences.count('love'))
Print(sentences.count('I love'))

Print(sentences.title())
Print(sentences.swapcase())
Print(sentences.startswith('T'))
Print(sentences.startswith('I love'))
Print(sentences.endswith('t.'))
Print(sentences.rfind('o'))
Print(len(sentences))
print(sentences.split('.'))
print(sentences.split(' '))
words = sentences.split(' ')
print(len(words))
print(sentences.count('love') / len(words))

a = 4
a = 400
print(a)
#the result would be 400
print(2/20)


first_name = 'Lidiya'
last_name = 'Woldesenbet'
full_name = first_name + ' ' + last_name
print(full_name)

#tab....\t 



#string formatting
country ='Ethiopia'
city= 'Addis Ababa'
gravity = 9.81
mass = 74 # mass in kg
weight =  mass * gravity
# This is the old way of formatting strings.
print('%s is in Africa.The capital is %s.' %('country, city'))
print('%.2f is the gravitational constant.' %(gravity))
print('The gravity is %.2f and the mass is %d in kg and the weight is %.2f' in Newton.' %(gravity, mass, weight))

# This is the better formatter
print('THE BETTER WAY')
print('{} is in Africa.The capital is {}.' .format(country, city))
print('{} is the gravitational constant.' .format(gravity))
print('The gravity is {} and the mass is {} in kg and the weight is {}' in Newton.' .format(gravity, mass, weight))

print('BEST WAY')

print(f'{country} is in Africa.The capital is {city}.')
print(f'{gravity} is the gravitational constant.')
print(f'The gravity is {gravity} and the mass is {mass} in kg and the weight is {weight}' in Newton.')

a = 4
b = 3

print(f'The sum of {a} and {b} is {a + b}.')
print(f'The difference of {a} and {b} is {a - b}.')
print(f'The product of {a} and {b} is {a * b}.')

""" I am Lidiya Woldesenbet. I live in Helsinki, Finland. I study Python. My skills are HTML, CSS, git, github and Python. I am 30 years old. """

first_name: 'Lidiya'
last_name: 'Woldesenbet'
age: 30
city: 'Espoo'
country: 'Finland'
skills: 'HTML, CSS, git, github, Python'

print(first_name)
print(last_name)
print(age)
print(city)
print(country)
print(skills)


print(f'I am {first_name} {last_name}. I live in {city} {country}. I am learingin {learning}. My skills are {skills}. I am {age} old.')
I am Dawit Negash. I live in Herndon USA. I am learingin Python. My skills are ['HTML', 'CSS', 'JS', 'Python']. I am 250 old.







