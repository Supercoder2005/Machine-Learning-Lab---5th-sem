import pandas as pd
import math

# Load the dataset
data = pd.read_csv("F:\\Machine Learning Lab - 5th sem\\Assignment 1\\weather.csv")
print(data)

# Entropy calculation function
def cal_entropy(yes, no):
    total = yes + no
    if total == 0:
        return 0
    p_yes = yes / total
    p_no = no / total
    entropy = 0
    if p_yes > 0:
        entropy -= p_yes * math.log2(p_yes)
    if p_no > 0:
        entropy -= p_no * math.log2(p_no)
    return entropy

# Step 1: Calculate total dataset entropy
total_yes = len(data[data["Played football"] == "Yes"])
total_no = len(data[data["Played football"] == "No"])
total_entropy = cal_entropy(total_yes, total_no)
total = total_yes + total_no
print(f"Total Entropy of dataset: {total_entropy:.4f}")

# Step 2: Calculate Information Gain for each feature
features = ["Outlook", "Temperature", "Humidity", "Wind"]
ig_results = {}

for feature in features:
    feature_values = data[feature].unique()
    feature_entropy = 0
    print(f"\nCalculating Information Gain for feature: {feature}")
    for value in feature_values:
        subset = data[data[feature] == value]
        yes = len(subset[subset["Played football"] == "Yes"])
        no = len(subset[subset["Played football"] == "No"])
        entropy = cal_entropy(yes, no)
        weight = (yes + no) / total
        feature_entropy += weight * entropy
        print(f"  {value} → Yes: {yes}, No: {no}, Entropy: {entropy:.4f}, Weight: {weight:.4f}")
    
    ig = total_entropy - feature_entropy
    ig_results[feature] = ig
    print(f"Information Gain for {feature}: {ig:.4f}")

# Step 3: Find the feature with the highest Information Gain
best_feature = max(ig_results, key=ig_results.get)
print("\n--- Summary ---")
for feature, ig in ig_results.items():
    print(f"{feature} : {ig:.4f}")

print(f"\nRoot node should be: {best_feature} (Highest IG: {ig_results[best_feature]:.4f})")
