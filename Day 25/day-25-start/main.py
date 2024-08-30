# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

# import csv  # import csv module

# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     next(data)  # Skip the header row
#     temps = []
#     for row in data:
#         temps.append(int(row[1]))  # Assuming the temperature is in the second column
#     print(temps)

import pandas  # import pandas module

# pandas.read_csv("weather_data.csv")  # read csv file
data = pandas.read_csv("weather_data.csv")  # read csv file
# print(data)
print(data["temp"])  # print the temp column
