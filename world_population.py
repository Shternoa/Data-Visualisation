import json
from pygal_maps_world.i18n import COUNTRIES
from countries_code import get_country_code

file_name = 'population_data.json'

with open(file_name) as file:
    pop_data = json.load(file)

# Вывод население страны за 2010 год

for pop_dict in pop_data:
    if pop_dict['Year'] == '2010':
        country_name = pop_dict['Country Name']
        population = pop_dict['Value']
        code = get_country_code(country_name)
        if code:
            print(f'{country_name} : {population}')
        else:
            print(f'Error : {str(population)}')

# for country_code in sorted(COUNTRIES.keys()):
#     print(country_code, COUNTRIES[country_code])
