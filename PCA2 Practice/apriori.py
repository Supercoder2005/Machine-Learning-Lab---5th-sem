import csv 
data = []
with open("F:\Machine Learning Lab - 5th sem\PCA2 Practice\marketData.csv","r")as f:
    reader = csv.reader(f)
    for row in reader:
        data.append(row[1:]) # ignore the first column thats why 1:
print(data)  # [['Milk', 'Bread', 'Butter'], ['Bread', 'Butter'], ['Milk', 'Bread'], ['Milk', 'Butter'], ['Bread'], ['Milk', 'Bread', 'Butter']]


def get_support_count(itemset,data):
    count = 0
    for x in data:
        present = True
        for item in itemset:
            if item not in data:
                present = False 
                break 
        if present:
            count += 1
    return count



def generate_candidates(prev_freq_sets,k):
    # prev_freq_sets = [['Milk','Bread'], ['Milk','Butter'], ['Bread','Butter']]
    # k = 3  , size of the newly generated itemsets from the pre_freq_sets : ['Milk','Bread','Butter'] have set of k=3 items
    candidates = []
    n = len(prev_freq_sets)
    # compare each pair of item sets once 
    for i in range(n):   
        for j in range(i+1,n):   
            L1 = list(prev_freq_sets[i])   #['Milk','Bread']
            L2 = list(prev_freq_sets[j])   #['Milk','Butter']
            L1.sort()
            L2.sort()
            # Check if prefixes match (eligible for joining)
            if (L1[:k-2] == L2[:k-2]):
                new_candidate = list(set(L1) | set(L2)) # join both list using set union | function
                new_candidate.sort()
                # check whether it already exists in the candidate list to prevent duplicates
                exists = False 
                for c in candidates:
                    if c == new_candidate:
                        exists = True 
                        break
                if not exists:
                    candidates.append(new_candidate)
    return candidates



def apriori(data,min_support):

    # at first all unique items that appears in all transactions
    items = []  # ['Milk','Bread','Butter']
    for x in data:  # x = ['Milk', 'Bread', 'Butter']
        for item in data :   # item = 'Milk'
            if [item] not in items: # if the single item (as a list) [item] is not already present in items.
                items.append([item])  # after one iteration items = [['Milk']]
    # print(items) = [['Milk'],['Bread'],['Butter']]


    # calculate support for each item and select only those that are frequent enough
    freq_itemsets = [] # This will store all frequent itemsets of every size
    support_data = {}  # This dictionary keeps track of support values for every itemset
    L1 = []   # This list will store frequent 1-itemsets, i.e., items that meet the minimum support threshold
    for item in items :
        support = get_support_count(item,data)/float(len(data))
        support_data[tuple(item)] = support 
        if (support >= min_support):
            L1.append(item)
    freq_itemsets.append(L1) # list of frequent 1-itemsets

    k = 2 # now want to find frequent 2-itemsets, so we start with k = 2.
    while(len(freq_itemsets[k-2])>0):
        candidates_k = generate_candidates(freq_itemsets[k-1],k)
        
