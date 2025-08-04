import pandas as pd
import math 

data = pd.read_csv("F:\Machine Learning Lab - 5th sem\Assignment 1\weather.csv")
print(data)

# Count total no of Yes and No present in the dataset
total_yes = len(data[data["Played football"]=="Yes"])
total_no = len(data[data["Played football"]=="No"])
print("Total Yes :",total_yes)
print("Total No :",total_no)
total = total_yes + total_no 
print("Total no of tupils in the dataset : ",total)

# Count Outlook wise Yes/No 

# Sunny
sunny_yes = len(data[(data["Outlook"]=="Sunny") & (data["Played football"]=="Yes")])
print("Sunny Yes :",sunny_yes)
sunny_no = len(data[(data["Outlook"]=="Sunny") & (data["Played football"]=="No")])
sunny_total = sunny_yes + sunny_no
print("Sunny No :",sunny_no)

# Overcast
overcast_yes = len(data[(data["Outlook"]=="Overcast") & (data["Played football"]=="Yes")])
print("Overcast Yes :",overcast_yes)
overcast_no = len(data[(data["Outlook"]=="Overcast") & (data["Played football"]=="No")])
overcast_total = overcast_yes + overcast_no
print("Overcast No :",overcast_no)

# Rain
rain_yes = len(data[(data["Outlook"]=="Rain") & (data["Played football"]=="Yes")])
print("Rain Yes :",rain_yes)
rain_no = len(data[(data["Outlook"]=="Rain") & (data["Played football"]=="No")])
print("Rain No:",rain_no)
rain_total = rain_yes + rain_no 

# define the entropy function 
def cal_entropy(y,n):
    total = y + n 
    p_yes = y/total 
    p_no = n/total 

    if total == 0:
        return 0
    
    entropy = 0
    if(p_yes>0):
        entropy -= p_yes * math.log2(p_yes)
    if(p_no>0):
        entropy -= p_no * math.log2(p_no)

    return entropy 

# Calculate the entropy of the total dataset 
entropy_total = cal_entropy(total_yes,total_no)
print("Entropy of the total dataset : ",entropy_total)

entropy_sunny = cal_entropy(sunny_yes,sunny_no)
entropy_overcast = cal_entropy(overcast_yes,overcast_no)
entropy_rain = cal_entropy(rain_yes,rain_no)

# Compute Information Gain of Attribute : Outlook 
IG_Outlook = entropy_total - ((sunny_total/total) * entropy_sunny
                              +(overcast_total/total) * entropy_overcast
                              +(rain_total/total) * entropy_rain)
print("Information Gain for Outlook : ",IG_Outlook)