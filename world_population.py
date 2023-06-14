import json

file_name = 'population_data.json'

with open(file_name) as file:
    pop_data = json.load(file)

# Вывод население страны за 2010 год

for pop_dict in pop_data:
    if pop_dict['Year'] == '2010':
        country_name = pop_dict['Country Name']
        population = pop_dict['Value']
        print(f'{country_name} : {population}')
