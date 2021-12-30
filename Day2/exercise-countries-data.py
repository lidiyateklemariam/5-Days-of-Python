
from countries_data import countries_data
from pprint import pprint
for c in countries_data:
    print(c['name'],c['capital'], c['population'],len( c['languages']))


# Let us find the 10 most populated countries
# China, India, USA, Pakistan ...

populations = []
for country in countries_data:
    populations.append(country['population'])

# sorted

""" sorted_countries = sorted(populations, reverse=True)
top_ten_countries = sorted_countries[:10]
 """

top_10 = sorted(countries_data, key= lambda c:c['population'], reverse=True)[:10]

# pprint([{'name':c['name'], 'population':c['population']} for c in top_10])
new_list = []
for c in top_10:
    new_list.append({'name': c['name'], 'population': c['population']})

pprint(new_list)

