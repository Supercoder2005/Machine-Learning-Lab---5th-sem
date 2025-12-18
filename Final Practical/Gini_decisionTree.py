import pandas as pd 
import math 

data = pd.read_csv("F:\\Machine Learning Lab - 5th sem\\PCA1 Practice\\music.csv")
print(data)

def giniIndex_calculation(yes,no):
    total = yes+no
    p_yes = yes/total
    p_no = no/total 
    gini = 1-(p_yes**2 + p_no**2)
    return gini 

yes = len(data[data["Play Music"]=="Yes"])
no = len(data[data["Play Music"]=="No"])
total = yes+no 
total_gini = giniIndex_calculation(yes,no)
print("Total Yes :",yes)
print("Total No :",no)
print("Total no of datasets :",total)
print("Gini Index of the entire dataset :",total_gini)

features = ["Weather","Time","Mood"]
ig_results = {}
for feature in features:
    print("--------Feature:",feature,"--------")
    feature_values = data[feature].unique()
    for value in feature_values:
        subset = data[data[feature]==value]
        yes = len(subset[subset["Play Music"]=="Yes"])
        no = len(subset[subset["Play Music"]=="No"])
        gini_index = giniIndex_calculation(yes,no)
        feature_gini = ((yes+no)/total)*gini_index
        print(f"{value} ---> Yes :{yes}, No :{no}, Gini Index :{gini_index}")
    information_gain = total_gini - feature_gini
    ig_results[feature] = information_gain 
    print("Information Gain :",information_gain)

best_feature = None 
best_ig = -1 
for feature,ig in ig_results.items():
    if ig>best_ig:
        best_ig = ig 
    best_feature = feature 
print("\n The root node of the decision tree : ",best_feature," with IG = ",best_ig)
