import pandas as pd
import math 

# dataset loading
data = pd.read_csv("F:\Machine Learning Lab - 5th sem\PCA1 Practice\music.csv")
print(data)

# Entropy calculation function
def entropy_calculation(yes,no):
    total = yes+no 
    p_yes = yes/total 
    p_no = no/total
    entropy = 0
    if total == 0:
        return 0
    else:
        if(p_yes>0):
            entropy -= p_yes * math.log2(p_yes)
        if(p_no>0):
            entropy -= p_no * math.log2(p_no)
    return entropy

# count total entropy of the dataset
yes = len(data[data["Play Music"]=="Yes"])
no = len(data[data["Play Music"]=="No"])
total = yes+no 
print("Total Yes :",yes)
print("Total_no :",no)
print("Total no of records in the dataset :",total)
total_entropy = entropy_calculation(yes,no)
print("Total entropy :",total_entropy)

# Calculate information gain (IG) for each feature 
features = {"Weather","Time","Mood"}
IG_result = {} # dictionary to store the information gain of each feature 

for feature in features:
    feature_values = data[feature].unique()      # for attribute Time , it will be = {morning,evening}
    feature_entropy = 0
    print("\nCalculating the IG for feature",feature,"---")
    for value in feature_values:
        subset = data[data[feature]==value]    # used to make small datasets of each features with their corresponding values
        yes = len(subset[subset["Play Music"]=="Yes"])
        no = len(subset[subset["Play Music"]=="No"])
        # calulate entropy of each value ex: morning of attribute Time
        entropy = entropy_calculation(yes,no)
        # calculate the feature entropy ex: Time
        feature_entropy = ((yes+no)/total) * entropy 
        print(f"{value} ---> Yes : {yes}, No : {no}, Entropy : {entropy}")

    information_gain = total_entropy - feature_entropy
    IG_result[feature] = information_gain 
    print("\nInformation gain for feature:",feature," = ",information_gain)

best_feature = None 
best_ig = -1
for feature,ig in IG_result.items():
    if ig > best_ig:
        best_ig = ig 
    best_feature = feature 

print("Root node of the decision tree : ",best_feature, " ,with information gain :",ig)

        
    