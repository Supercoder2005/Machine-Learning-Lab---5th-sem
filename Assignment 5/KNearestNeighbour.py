import csv 
training_data = []
labels = []
with open("F:\\Machine Learning Lab - 5th sem\\PCA2 Practice\\labeledData.csv","r") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        training_data.append([float(row[0]),float(row[1])])
        labels.append(int(row[2]))
print("Training dataset :",training_data)
print("Labels of the dataset :",labels)

test_data = [7.0,3.8]
k = 3
print("Test dataset :",test_data)
print("The value of K :",k)

# calculate the distance of test data from each point of training dataset
distances = []
for i in range(len(training_data)):
    d = ((training_data[i][0] - test_data[0])**2 + (training_data[i][1] - test_data[1])**2)**0.5
    distances.append([d,labels[i]])

# now sort the distances list 
for i in range(len(distances)):
    for j in range(i+1,len(distances)):
        if distances[i]>distances[j]:
            distances[i],distances[j] = distances[j],distances[i]
print("Sorted distances :",distances)

# now from the sorted distances pick the first k labels of the points of corresponding distances as neighbours
neighbours = []
for i in range(k):
    neighbours.append(distances[i][1])
print("K nearest Neighbours :",neighbours)

count0 = distances.count(0)
count1 = distances.count(1)

if count0>count1:
    print("Test data belongs to label : 0")
else:
    print("Test data belongs to label : 1")