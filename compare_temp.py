import csv
from matplotlib import pyplot as plt
from datetime import datetime

# Чтение дат и максимальных температур из файла
file_name_1 = 'death_valley_2014.csv'
with open(file_name_1) as file_1:
    reader = csv.reader(file_1)
    header_row = next(reader)
    # for index, column_reader in enumerate(header_row):
    #     print(index, column_reader)
    dates, highs, lows = [], [], []
    for row in reader:
        try:
            current_date = datetime.strptime(row[1], '%Y-%m-%d')
            high = int(row[2])
            low = int(row[4])
            l_c = (low - 32) * 5 / 9
            h_c = (high - 32) * 5 / 9
        except ValueError:
            print(current_date, 'missing_data')
        else:
            dates.append(current_date)
            highs.append(round(h_c))
            lows.append(round(l_c))

# Нанесение данных на диаграмму
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, highs, c='green', alpha=0.5)
plt.plot(dates, lows, c='red', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='yellow', alpha=0.1)

# Форматирование диаграммы
plt.title('Температуры по дням за 2014 в Долине Смерти', fontsize=24)
plt.xlabel('', fontsize=12)
fig.autofmt_xdate()
plt.ylabel('Температура (C)', fontsize=12)
plt.tick_params(axis='both', which='major', labelsize=12)

plt.show()
