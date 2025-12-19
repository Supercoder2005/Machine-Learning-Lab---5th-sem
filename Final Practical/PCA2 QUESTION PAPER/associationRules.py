import csv 
data = []
with open("F:\\Machine Learning Lab - 5th sem\\Final Practical\\PCA2 QUESTION PAPER\\transactionData.txt","r")as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        data.append(row[1:])
print(data)

min_support = 2 
min_confidence = 0.5

# list down all unique items from the dataset 
itemsets = []
for x in data:
    for product in x:
        if product not in itemsets:
            itemsets.append(product)
print("All unique items from the dataset are : ",itemsets)

# count frequency of each itemset of any combination(single,double or tripple)
def count_freq(itemsets):
    count = 0
    for items in data:
        present = True
        for product in itemsets:
            if product not in items:
                present = False 
                break 
        if present == True :
            count += 1 
    return count

# make all possible combinations of itemsets 
from itertools import combinations 
count_combination_freq = {}
for k in range(1,len(itemsets)+1):
    c = combinations(itemsets,k)
    for x in c:
        if(count_freq(x)>=min_support):
            count_combination_freq[x] = count_freq(x)
print(count_combination_freq)
for comb in count_combination_freq:
    print(comb," were bought ",count_combination_freq[comb]," times.")

# create Association rules 
for items in count_combination_freq:
    if len(items)>= 2:
        for k in range(1,len(items)):
            for left in combinations(items,k):
                right = tuple(sorted(set(items)-set(left)))
                if left in count_combination_freq and right in count_combination_freq:
                    confidence = count_combination_freq[items]/count_combination_freq[left]
                if confidence>=min_confidence:
                    print(left," ---> ",right," : ",confidence)