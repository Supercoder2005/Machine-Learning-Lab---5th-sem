import pandas as pd
import math 

data = pd.read_csv("F:\Machine Learning Lab - 5th sem\PCA1 Practice\music.csv")
print(data)

# gini index calculation 
def gini_calculation(yes,no):
    total = yes+no 
    if(total == 0):
        return 0
    p_yes = yes/total 
    p_no = no/total
    gini = 1-(p_yes**2 + p_no**2)
    return gini 

# total gini_index of the dataset 
total_yes = len(data[data["Play Music"]=="Yes"])
total_no = len(data[data["Play Music"]=="No"])
print("Total Yes :",total_yes)
print("Total No :",total_no)
total = total_yes + total_no
print("Total records of the dataset :",total)
total_gini = gini_calculation(total_yes,total_no)
print("Total gini index of the dataset :",total_gini)

# information gain of each feature 
IG_result = {}
features = {"Weather","Time","Mood","Play Music"}
for feature in features:
    feature_values = data[feature].unique()
    #print(feature_values)
    print("\nInformation gain for the feature : ",feature)
    for value in feature_values:
        subset = data[data[feature]==value]
        #print(subset)
        yes = len(subset[subset["Play Music"]=="Yes"])
        no = len(subset[subset["Play Music"]=="no"])
        gini = gini_calculation(yes,no)
        feature_gini = ((yes+no)/total)*gini 
        print(f"{value} ----> Yes : {yes}, No : {no}, Gini : {feature_gini}")
    information_gain = total_gini - feature_gini 
    IG_result[feature] = information_gain
    print("Information Gain :",information_gain)

# find out the root node
best_feature = None 
best_ig = -1 
for feature,ig in IG_result.items():
    if ig>best_ig:
        best_ig = ig 
        best_feature = feature 

print("The root node of the decision tree will be : ",best_feature," , with IG = ",best_ig)
