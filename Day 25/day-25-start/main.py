import pandas as pd

data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

# print(data.columns)
furs = pd.DataFrame(data["Primary Fur Color"].value_counts())
furs.to_csv("new_data.csv")
