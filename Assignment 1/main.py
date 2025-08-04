import pandas as pd
import math 

data = pd.read_csv("F:\Machine Learning Lab - 5th sem\Assignment 1\weather.csv")
print(data)

# Count total no of Yes and No present in the dataset
total_yes = len(data[data["Played football"]=="Yes"])
total_no = len(data[data["Played football"]=="No"])
print(total_yes,total_no)