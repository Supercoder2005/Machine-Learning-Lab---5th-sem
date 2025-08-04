import pandas as pd
import math 

data = pd.read_csv("F:\Machine Learning Lab - 5th sem\Assignment 1\weather.csv")
print(data)

# Count total no of Yes and No present in the dataset
total_yes = len(data[data["Played football"]=="Yes"])
total_no = len(data[data["Played football"]=="No"])
print(total_yes)
print(total_no)
total = total_yes + total_no 
print(total)

# Count Outlook wise Yes/No 

# Sunny
sunny_yes = len(data[(data["Outlook"]=="Sunny") & (data["Played football"]=="Yes")])
print(sunny_yes)
sunny_no = len(data[(data["Outlook"]=="Sunny") & (data["Played football"]=="No")])
sunny_total = sunny_yes + sunny_no
print(sunny_no)

# Overcast
overcast_yes = len(data[(data["Outlook"]=="Overcast") & (data["Played football"]=="Yes")])
print(overcast_yes)
overcast_no = len(data[(data["Outlook"]=="Overcast") & (data["Played football"]=="No")])
overcast_total = overcast_yes + overcast_no
print(overcast_no)

# Rain
rain_yes = len(data[(data["Outlook"]=="Rain") & (data["Played football"]=="Yes")])
print(rain_yes)
rain_no = len(data[(data["Outlook"]=="Rain") & (data["Played football"]=="No")])
print(rain_no)
rain_total = rain_yes + rain_no 

# define the entropy function 


