import pandas

data = pandas.read_csv("weather_data.csv")
# print(type(data))
# print(data["temp"])

data_dict = data.to_dict()
# print(data_dict)

# List conversion
temp_list = data["temp"].to_list()
# print(temp_list)


# Average using list
# def Average(lst):
#     return sum(lst) / len(lst)


# print(round(Average(temp_list), 2))

# Average using pandas

# print(data["temp"].mean())

# Get the max value
# print(data["temp"].max())

# Get Data in Columns
# print(data["condition"])
# print(data.condition)  # Same as above

# Get Data in Row
# print(data[data.day == "Monday"])

# Get Data in Row with max temp
# print(data[data.temp == data.temp.max()])

monday = data[data.day == "Monday"]
# print(monday.condition)


def f(x):
    # Check if x is a pandas Series and extract the first element if necessary
    if isinstance(x, pandas.Series):
        x = x.iloc[0]
    x = x * 1.8 + 32
    return float(x)


# Print the temperature on Monday in Fahrenheit
# print(f(monday.temp))

# Create a DataFrame from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65],
}

data_studs = pandas.DataFrame(data_dict)
print(data_studs)

# Create a CSV file from scratch
data_studs.to_csv("new_data.csv")
