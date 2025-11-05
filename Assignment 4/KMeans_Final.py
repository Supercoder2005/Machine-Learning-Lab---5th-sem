import csv 
import random 

data = []
with open("F:\\Machine Learning Lab - 5th sem\\PCA2 Practice\\data.csv","r")as file:
    reader = csv.reader(file)
    for row in reader:
        data.append([float(row[0]),float(row[1])])

# function to calculate distance btn two points
def distance(point1,point2):
    total = 0
    for i in range(len(point1)):
        total += (point1[i] - point2[i])**2 
    return total**0.5

# function to calculate mean of a cluster
def mean(points):
    n = len(points)
    dims = len(points[0])
    res = []
    for i in range(dims):
        s = 0
        for j in range(n):
            s += points[j][i]
        res.append(s/n)
    return res 


# main KMeans algorithm function 
def kmeans(data,k,max_iterations):
    # the loop will run till it reach the given max iteration numbers as parameter
    for x in range(max_iterations):
        # randomly generate k centroid values
        centroids = [] 
        for i in range(k):
            centroids = random.sample(data,k)

        # create empty clusters list structure : [[],[],[]]
        clusters = []
        for i in range(k):
            clusters.append([])

        # assign points to their nearest centroid's cluster 
        for point in data:
            distances = [] # will store all distances from a point to k no of centroids
            for c in centroids:
                d = distance(c,point)
                distances.append(d)
            min_index = distances.index(min(distances))
            # assign the point to the cluster corresponding to the nearest centroid whoose index is stored in the min_index
            clusters[min_index].append(point)
            
        # recalculating the centroids of a cluster 
        new_centroids = []
        for points in clusters:
            # if the cluster have some points
            if points: 
                new_centroids.append(mean(points))
            # if the cluster has no point yet
            else:
                new_centroids.append(random.choice(data))
        
        # when the loop will stop ?
        if new_centroids == centroids :
            break
        # assigning the new values of centroid
        centroids = new_centroids
    
    return centroids,clusters


# running the algorithm 
final_centroids,final_clusters = kmeans(data,3,100)

print("\n Final Centroids :")
for i in range(len(final_centroids)):
    print(f"Centroid {i+1} : {final_centroids[i]}")

print("\n Final Clusters :")
for i in range(len(final_clusters)):
    print(f"Clusters {i+1} : {final_clusters[i]}")




