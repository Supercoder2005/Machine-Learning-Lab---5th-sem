import csv 
data = []
with open("F:\\Machine Learning Lab - 5th sem\\PCA2 Practice\\marketData.csv","r")as file:
    reader = csv.reader(file)
    for row in reader:
        data.append(row[1:])
print(data)

min_support = 2
min_confidence = 0.6 

# find out the unique items from the dataset 
itemsets = []
for x in data:
    for product in x:
        if product not in itemsets:
            itemsets.append(product)
print(itemsets)

# calculate the frequency of each combination of itemsets (single,double or tripplet combinations)
def count_freq(itemsets):
    count = 0
    for x in data:
        for product in itemsets:
            present = True 
            if product not in x:
                present = False 
                break 
        if present == True:
            count += 1
    return count 

# create all possible combinations of itemsets 
from itertools import combinations 
count_combination_freq = {}
for k in range(1,len(itemsets)+1):
    c = (combinations(itemsets,k))
    for x in c :
        print(x," : ",count_freq(x))
        if count_freq(x)>=min_support:
            count_combination_freq[x] = count_freq(x)
print(count_combination_freq)
# print the combination freq which has more than the min_support 
for combination in count_combination_freq:
    print(combination,"were bought ",count_combination_freq[combination]," times.")

# Generate Association rules that follows the min_confidence 
print("\n Association rules -----\n")
for items in count_combination_freq:
    if len(items)>=2:
        for k in range(1,len(items)):
            for left in combinations(items,k):
                right = tuple(sorted(set(items)-set(left)))
                if left in count_combination_freq and right in count_combination_freq:
                    confidence = count_combination_freq[items]/count_combination_freq[left]
                if confidence >= min_confidence :
                    print(left," ---> ",right," : ",confidence)
