import json
from pygal_maps_world.i18n import COUNTRIES
from countries_code import get_country_code
from pygal_maps_world.maps import World

file_name = 'population_data.json'

with open(file_name) as file:
    pop_data = json.load(file)

# Вывод население страны за 2010 год

ww_population = {}
for pop_dict in pop_data:
    if pop_dict['Year'] == '2010':
        country_name = pop_dict['Country Name']
        population = float(pop_dict['Value'])
        code = get_country_code(country_name)
        if code:
            ww_population[code] = population
        # else:
        #     print(f'Error : {str(population)}')
wm = World()
wm.title = 'World Population in 2010, by Country'
wm.add('2010', ww_population)
wm.render_to_file('world_population.svg')

# for country_code in sorted(COUNTRIES.keys()):
#     print(country_code, COUNTRIES[country_code])
