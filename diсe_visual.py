from die import Die
import pygal

die_1 = Die()
die_2 = Die()

# Моделировние серии бросков
results = []
for roll_number in range(1000):
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

hist.title = 'Результаты броска кубиков 1000 раз'
hist.x_labels = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
hist.x_title = 'Результаты'
hist.y_title = 'Частота результатов'
hist.add('Кубик 1 + Кубик 2', frequencies)
hist.render_to_file('diсe_visual.svg')
