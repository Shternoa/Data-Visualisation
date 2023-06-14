import json
from pygal_maps_world.i18n import COUNTRIES
from countries_code import get_country_code
from pygal_maps_world.maps import World
from pygal.style import RotateStyle
from pygal.style import LightColorizedStyle as LCS

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
            # Группировка по уровню население
            ww_pop_1, ww_pop_2, ww_pop_3 = {}, {}, {}
            for ww, pop in ww_population.items():
                if pop < 10000000:
                    ww_pop_1[ww] = pop
                elif pop < 1000000000:
                    ww_pop_2[ww] = pop
                else:
                    ww_pop_3[ww] = pop
            # Провеврка кол-ва странн на каждом уровне
            print(len(ww_pop_1), len(ww_pop_2), len(ww_pop_3))
        # else:
        #     print(f'Error : {str(population)}')

wm_style = RotateStyle('#446699',base_style=LCS)
wm = World(style=wm_style)
wm.title = 'World Population in 2010, by Country'
wm.add('0-10m', ww_pop_1)
wm.add('10m-1bn', ww_pop_2)
wm.add('>1bn', ww_pop_3)
# wm.add('2010', ww_population)
wm.render_to_file('world_population_4.svg')

# for country_code in sorted(COUNTRIES.keys()):
#     print(country_code, COUNTRIES[country_code])
