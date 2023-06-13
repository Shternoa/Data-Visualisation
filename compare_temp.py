import csv
from matplotlib import pyplot as plt
from datetime import datetime

# Чтение дат и максимальных температур из файла
file_name_1 = 'death_valley_2014.csv'
file_name_2 = 'sitka_weather_2014.csv'
with open(file_name_1) as file_1:
    reader = csv.reader(file_1)
    header_row = next(reader)
    # for index, column_reader in enumerate(header_row):
    #     print(index, column_reader)
    dates_1, highs_1, lows_1 = [], [], []
    for row in reader:
        try:
            current_date = datetime.strptime(row[0], '%Y-%m-%d')
            high = int(row[1])
            low = int(row[2])
            l_c = (low - 32) * 5 / 9
            h_c = (high - 32) * 5 / 9
        except ValueError:
            print(current_date, 'missing_data')
        else:
            dates_1.append(current_date)
            highs_1.append(round(h_c))
            lows_1.append(round(l_c))
with open(file_name_2) as file_2:
    reader = csv.reader(file_2)
    header_row = next(reader)
    dates_2, highs_2, lows_2 = [], [], []
    for row in reader:
        try:
            current_date = datetime.strptime(row[0], '%Y-%m-%d')
            high = int(row[1])
            low = int(row[2])
            l_c = (low - 32) * 5 / 9
            h_c = (high - 32) * 5 / 9
        except ValueError:
            print(current_date, 'missing_data')
        else:
            dates_2.append(current_date)
            highs_2.append(round(h_c))
            lows_2.append(round(l_c))

# Нанесение данных на диаграмму
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates_1, highs_1, c='green', alpha=0.5)
plt.plot(dates_2, highs_2, c='blue', alpha=0.5)
plt.plot(dates_1, lows_1, c='red', alpha=0.5)
plt.plot(dates_2, lows_2, c='purple', alpha=0.5)
plt.fill_between(dates_1, highs_1, lows_1, facecolor='yellow', alpha=0.1)
plt.fill_between(dates_2, highs_2, lows_2, facecolor='yellow', alpha=0.1)
plt.fill_between(dates_1, highs_1, highs_2, where=(highs_1 > highs_2), facecolor='yellow', alpha=0.1)
plt.fill_between(dates_1, lows_1, lows_2, where=(lows_1 < lows_2), facecolor='yellow', alpha=0.1)

# Форматирование диаграммы
plt.title('Cравнение температур', fontsize=24)
plt.xlabel('', fontsize=12)
fig.autofmt_xdate()
plt.ylabel('Температура (C)', fontsize=12)
plt.tick_params(axis='both', which='major', labelsize=12)

plt.show()
