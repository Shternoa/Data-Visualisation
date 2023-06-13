import csv
from pprint import pprint
from matplotlib import pyplot as plt
from datetime import datetime

# Чтение дат и максимальных температур из файла
file_name = 'sitka_weather_07-2014.csv'
with open(file_name) as file:
    reader = csv.reader(file)
    header_row = next(reader)
    dates, highs = [], []
    for row in reader:
        current_date = datetime.strptime(row[0], '%Y-%m-%d')
        dates.append(current_date)
        high = int(row[1])
        h_c = (high - 32) * 5 / 9
        highs.append(round(h_c))
    print(highs)
# first_date = datetime.strptime('2014-7-1', '%Y-%m-%d')
# print(first_date)

# Нанесение данных на диаграмму
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, highs, c='blue')

# Форматирование диаграммы
plt.title('Температура по дням, Июль 2014', fontsize=24)
plt.xlabel('', fontsize=14)
fig.autofmt_xdate()
plt.ylabel('Температура (C)', fontsize=14)
plt.tick_params(axis='both', which='major', labelsize=14)

plt.show()
