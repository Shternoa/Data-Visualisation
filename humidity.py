import csv
from pprint import pprint
from matplotlib import pyplot as plt
from datetime import datetime

# Чтение дат и максимальных температур из файла
file_name = 'sitka_weather_2014.csv'
with open(file_name) as file:
    reader = csv.reader(file)
    header_row = next(reader)
    dates, highs, lows = [], [], []
    for row in reader:
        try:
            current_date = datetime.strptime(row[0], '%Y-%m-%d')
            high = int(row[7])
            low = int(row[9])
        except ValueError:
            print(current_date, 'missing_data')
        else:
            dates.append(current_date)
            highs.append(round(high))
            lows.append(round(low))

# Нанесение данных на диаграмму
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, highs, c='green', alpha=0.5)
plt.plot(dates, lows, c='red', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='yellow', alpha=0.1)

# Форматирование диаграммы
plt.title('Влажность Ситки', fontsize=24)
plt.xlabel('', fontsize=12)
fig.autofmt_xdate()
plt.ylabel('Процет флажности', fontsize=12)
plt.tick_params(axis='both', which='major', labelsize=12)

plt.show()
