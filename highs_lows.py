import csv
from pprint import pprint
from matplotlib import pyplot as plt

# Максимальные температуры из файла
file_name = 'sitka_weather_07-2014.csv'
with open(file_name) as file:
    reader = csv.reader(file)
    header_row = next(reader)
    highs = []
    for row in reader:
        high = int(row[1])
        h_c = (high - 32) * 5 / 9
        highs.append(round(h_c))
    print(highs)

# Нанесение данных на диаграмму
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(highs, c='blue')

# Форматирование диаграммы
plt.title('Температура по дням, Июль 2014', fontsize=24)
plt.xlabel('', fontsize=14)
plt.ylabel('Температура (C)', fontsize=14)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
