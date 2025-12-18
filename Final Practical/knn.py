import csv 
training_set = []
labels = []
with open("F:\\Machine Learning Lab - 5th sem\\PCA2 Practice\\labeledData.csv","r")as file:
    reader = csv.reader(file)
    next(reader) # skip the header of the dataset 
    for row in reader:
        training_set.append([float(row[0]),float(row[1])])
        labels.append(row[2])

test_data = [1,6]
k = 3
print("\n The training dataset :",training_set)
print("\n The labels :",labels)
print('\n The test data :',test_data)

# compute distance between test data and each training data point 
distances = []
for i in range(len(training_set)):
    d = ((training_set[i][0]-test_data[0])**2 + (training_set[i][1]-test_data[1])**2)**0.5
    distances.append([d,labels[i]])
print(distances)

# sort the distances list using bubble sort 
for i in range(len(distances)):
    for j in range(i+1,len(distances)):
        if distances[i]>distances[j]:
            distances[i],distances[j] = distances[j],distances[i]
print("The sorted distances list : ",distances)

# pick the first k no of distances from the sorted distances list as the k nearest neighbours of the test data
neighbours = [] #list to store the labels of the k nearest neighbours
for i in range(k):
    neighbours.append(distances[i][1])
print("\n The labels of the k nearest neighbours : ",neighbours)
label0 = neighbours.count('0')
label1 = neighbours.count('1')

# decision criteria 
if label0>label1:
    print("\n Test data belongs to class : 0")
else:
    print("\n Test data belongs to class : 1")
