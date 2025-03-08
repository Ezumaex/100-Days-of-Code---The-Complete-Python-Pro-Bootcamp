# # with open("./weather_data.csv", "r") as data_file:
# #     data = data_file.readlines()
# #     print(data)
# #
# # import csv
# #
# # with open("./weather_data.csv") as data_file:
# #     data = csv.reader(data_file)
# #     temperatures = []
# #     for row in data:
# #         if row[1] != "temp":
# #             temperatures.append(int(row[1]))
# #     print(temperatures)
#
# import pandas
#
# data = pandas.read_csv("weather_data.csv")
# # print(type(data))
# # print(data["temp"])
#
# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data["temp"].to_list()
# print(temp_list)
#
# print(data["temp"].max())
#
# print(data[data.temp == data.temp.max()])
#
# monday = data[data.day == "Monday"]
# monday_temp = monday.temp * 9/5 + 32
# print(monday_temp)
#
# data_dict = {
#     "students": ["Amy"]
# }


import pandas as pd

data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20250301.csv")

squirrel_count = pd.DataFrame({
    "Fur Color": data["Primary Fur Color"].value_counts().index,
    "Count": data["Primary Fur Color"].value_counts().values
})

squirrel_count.to_csv('squirrel_count.csv')