import csv
from pprint import pprint

file_name = 'sitka_weather_07-2014.csv'
with open(file_name) as file:
    reader = csv.reader(file)
    header_row = next(reader)
    for index, column_reader in enumerate(header_row):
        print(index,column_reader)
