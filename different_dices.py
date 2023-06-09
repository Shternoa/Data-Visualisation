from die import Die

import pygal

die_1 = Die()
die_2 = Die(10)

# Моделировние серии бросков
results = []
for roll_number in range(5000):
    result = die_1.roll() + die_2.roll()
    results.append(result)
# print(results)

frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result + 1):
    frequency = results.count(value)
    frequencies.append(frequency)
# print(frequencies)

hist = pygal.Bar()

hist.title = 'Кубик 6 + Кубик 10'
hist.x_labels = list(range(2, 17))
hist.x_title = 'Результаты'
hist.y_title = 'Частота результатов'
hist.add('Кубик 6 + Кубик 10', frequencies)
hist.render_to_file('different_visual.svg')
