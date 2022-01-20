import json
import pprint

#person = {
    #'first_name': 'Пол',
    #'age': 33,
    ##'cities': ['Москва', 'nsk', 'Париж'],
#}

#city1 = person['cities'][0]
#city2 = person['cities'][1]

#for city in person['cities']:
 #   print(city)
#print(city1)
#print(city2)


friends = {'cities': [{'population': 20, 'title': 'ст. Карабудахкент'},
                         {'population': 178116, 'title': 'к. Карачаевск'},
                         {'population': 47068, 'title': 'к. Пятигорск'},
                         {'population': 95254, 'title': 'с. Ржев'},
                         {'population': 61693, 'title': 'г. Сусуман'},
                         {'population': 18, 'title': 'г. Великие Луки'}]}

max_population = 0
big_city = ''   
for city in friend['cities']:
while city['population'] > max_population:
    max_population = city['population']
    big_city = city['title']
