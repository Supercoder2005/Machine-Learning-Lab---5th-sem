import csv 

training_data = []
labels = []

with open("F:\Machine Learning Lab - 5th sem\PCA2 Practice\labeledData.csv","r") as file:
    data = csv.reader(file)
    next(data)  # skip the header row
    for row in data:
        training_data.append([float(row[0]),float(row[1])])
        labels.append(int(row[2]))
    
#print(training_data) = [[1.0, 2.0], [2.0, 3.0], [3.0, 1.0], [6.0, 5.0], [7.0, 7.0], [8.0, 6.0]]
#print(labels) =  [0, 0, 0, 1, 1, 1]

test_data = [5,5]
k = 3

# compute distances between test data point and each training data point
distances = []
for i in range(len(training_data)):
    d = ((training_data[i][0]-test_data[0])**2 + (training_data[i][1]-test_data[1])**2)**0.5
    # distances list will store --- [[distance1,label1],[distance2,label2],....]
    distances.append([d,labels[i]])

# sort by distance (bubble sort)
for i in range(len(distances)):
    for j in range(i+1,len(distances)):
        if (distances[i] > distances[j]):
            distances[i],distances[j] = distances[j],distances[i]

# from the sorted distances list pick the first k nearest distances and their corressponding labels
neighbours = []
for i in range(k):
    neighbours.append([distances[i][1]]) # store only the labels

# now from the neighbours count the no of different values of labels 
count0 = neighbours.count(0)
count1 = neighbours.count(1)

if(count0>count1):
    print("\n Predicted Class : 0")
else:
    print("\n Predicted Class : 1")





