from die import Die
import pygal

die = Die()

# Моделировние серии бросков
results = []
for roll_number in range(1000):
    result = die.roll()
    results.append(result)
# print(results)

frequencies = []
for value in range(1, die.num_sides + 1):
    frequency = results.count(value)
    frequencies.append(frequency)
# print(frequencies)

hist = pygal.Bar()

hist.title = 'Результаты броска кубика 1000 раз'
hist.x_labels = ['1', '2', '3', '4', '5', '6']
hist.x_title = 'Результат'
hist.y_title = 'Частота результата'
hist.add('Сторона кубика №', frequencies)
hist.render_to_file('die_visual.svg')
