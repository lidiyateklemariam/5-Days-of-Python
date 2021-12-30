String = 'anything inside a single or double quote is a string.'
letters = 'a-z'

program = 'five days of python'

print(len(program))
print(program.upper())
print(program.lower())
print(program.title())
print(program.split(' '))

sentences = 'I love people. Love is the greates thing. I love python.'
print(sentences.lower().count('love'))
print(sentences.split())
print(sentences.replace('.',''). split(' '))


statement = 'You can not end a sentece with because because because is a conjunction'
print(statement.find('because'))
print(statement.rfind('because'))

starting_pos = statement.find('because')
ending_pos = statement.rfind('because') + len('because')

print(statement[starting_pos:ending_pos])







