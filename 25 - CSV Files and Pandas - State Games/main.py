# data = []
#
# with open("weather_data.csv") as file:
#     i = 0
#     for line in file.readlines():
#         if i > 0:
#             data.append(line)
#         i += 1
#
# for datum in data:
#     print(datum)

# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#         print(row)
#     print(temperatures)


# import pandas
#
# data = pandas.read_csv("weather_data.csv")
# print(data)
# print(data["temp"])
# print(type(data))
# print(type(data["temp"]))
#
# data_dict = data.to_dict()
# print(data_dict)
#
# #data in Columns
# temp_list = data["temp"].to_list()
#
# print(f"Average temp: {sum(temp_list)/ len(temp_list)}")
# print(data["temp"].mean())
# print(data["temp"].max())
# print(data.condition)


# Data in rows
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])
#
# monday = data[data.day == "Monday"]
# print(monday.condition)
#
# monday = data[data.day == "Monday"]
# monday_temp_c = monday.temp[0]
# monday_temp_f = monday_temp_c * (9/5) + 32
# print(monday_temp_f)


#Create a Dataframe from Scratch
# data_dict = {
#      "students": ["Amy", "James", "Angela"],
#      "scores": [75, 56, 651]
#  }
# data_2 = pandas.DataFrame(data_dict)
# print(data_2)
# data_2.to_csv("new_data.csv")


import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20231123.csv")
colors = data["Primary Fur Color"]
gray = len(data[colors == "Gray"])
red = len(data[colors == "Red"])
black = len(data[colors == "Black"])
data_dict = {
     "Fur Color": ["grey", "red", "black"],
     "Count": [gray, red, black]
}
data_2 = pandas.DataFrame(data_dict)
data_2.to_csv("squirrel_count.csv")