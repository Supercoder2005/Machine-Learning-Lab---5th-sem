import csv 
data = []
with open("F:\\Machine Learning Lab - 5th sem\\PCA2 Practice\\transactions.csv","r")as file:
    reader = csv.reader(file)
    for row in reader:
        data.append(row[1:]) # for skipping the first column we use [1:]
print(data) # [['Milk', 'Bread', 'Butter'], ['Bread', 'Butter'], ['Milk', 'Bread'], ['Milk', 'Butter'], ['Bread'], ['Milk', 'Bread', 'Butter']]

# given min_support & min_confidence
min_support = 2
min_confidence = 0.6

# get a liat of all unique products from the marketdataset
items = []
for x in data:   # x = ['Milk', 'Bread', 'Butter']
    for product in x:   # product = 'Milk'
        if product not in items:
            items.append(product)
print("\nAll the unique items present in the dataset :",items)

# count frequency of any item combinations 
def count_frequency(itemsets):
    count = 0
    for x in data:    # x = ['Milk', 'Bread', 'Butter']
        for product in itemsets:  # itemsets = ['Bread', 'Butter'] , product = 'Bread'
            present = True 
            if product not in x: 
                present = False 
                break 
        if present == True:
            count += 1
    return count


# Now we will build a dictionary of all the possible combination(single/double/triple/four...etc)
# but it should also maintain the minimum support 
from itertools import combinations 
count_combination_freq = {}
for k in range(1,len(items)+1):
    c = (combinations(items,k)) # combination() is a inbuilt function , where items = ['Milk','Butter','Bread'], k = 1,2,3 in each iteration
    #output = ('Milk',)('Bread',)('Butter',)('Milk','Bread')('Milk','Butter')('Bread','Butter')('Milk','Bread','Butter')
    for x in c:
        print(x," :",count_frequency(x)) # all the possible combinations we can generate using k no of unique items along with their frequencies
        if count_frequency(x) >= min_support: # checking whether the frequency can exceed or equal to the min_support
            count_combination_freq[x] = count_frequency(x)

print(count_combination_freq)
for comb in count_combination_freq:
    if(count_combination_freq[comb]==1):
        print(f"{comb} was bought {count_combination_freq[comb]} times.")
    else:
        print(f"{comb} were bought together {count_combination_freq[comb]} times.")


# Generate all possible Association Rules 
print("\n Shopping pattern rules / association rules------")
for items in count_combination_freq:
    # we only form rules if there are at least 2 products in the combination list
    if len(items) >= 2:
        # split the combination list into left and right parts
        # we want to generate the form : {Milk} --> {Bread,Butter}
        for k in range(1,len(items)):  # outer loop controls the size of LHS
            for left in combinations(items,k):  # generates all possible combinations for LHS
                right = tuple(sorted(set(items) - set(left)))  # RHS = remaining items that are not in the left-hand side

                # Check that LHS and RHS both exits in our count_combination_freq dictionary or not
                if left in count_combination_freq and right in count_combination_freq:
                    # calculation of confidence 
                    # confidence(LHS --> RHS) = support(LHS U RHS)/support(LHS)
                    confidence = count_combination_freq[items]/count_combination_freq[left]
                    
                    if confidence >= min_confidence:
                        print(left," ---> ",right," : ",confidence)