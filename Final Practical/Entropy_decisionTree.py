import pandas as pd 
import math 
#load the dataset
data = pd.read_csv("F:\\Machine Learning Lab - 5th sem\\PCA1 Practice\\music.csv")
print(data)
# function to calculate the entropy 
def entropy_calculation(yes,no):
    entropy = 0
    total = yes+no
    p_yes = yes/total
    p_no = no/total
    if total == 0:
        return 0 
    else:
        if p_yes>0:
            entropy -= p_yes*math.log2(p_yes)
        if p_no>0:
            entropy -= p_no*math.log2(p_no)
    return entropy 
# calculate the entropy of the total dataset 
yes = len(data[data["Play Music"]=="Yes"])
no = len(data[data["Play Music"]=="No"])
total = yes+no 
total_entropy = entropy_calculation(yes,no)
print("Total yes :",yes)
print("Total no :",no)
print("Total no of datasets :",total)
print("The entropy of the total dataset :",total_entropy)

# calculate the information gain of each feature 
features = ["Weather","Time","Mood"]
IG_results = {}
for feature in features:
    print("\n Information Gain of feature : ",feature)
    feature_values = data[feature].unique()
    for value in feature_values:
        subset = data[data[feature]==value]
        yes = len(subset[subset["Play Music"]=="Yes"])
        no = len(subset[subset["Play Music"]=="No"])
        entropy = entropy_calculation(yes,no)
        feature_entropy = ((yes+no)/total)*entropy
        print(f"{value} ---> Yes :{yes}, No :{no}, Entropy :{entropy}")
    information_gain = total_entropy - feature_entropy
    IG_results[feature] = information_gain
    print("Information gain = ",information_gain)
    
best_feature = None 
best_ig = -1 
for feature,ig in IG_results.items():
    if ig > best_ig:
        best_ig = ig 
    best_feature = feature 
print("\n The root node will be ----",best_feature)
