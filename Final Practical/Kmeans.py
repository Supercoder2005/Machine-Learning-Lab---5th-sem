import random 
import csv 

data = []
with open("F:\\Machine Learning Lab - 5th sem\\Final Practical\\kmeansData.csv","r") as file:
    reader = csv.reader(file)
    for row in reader:
        data.append([float(row[0]),float(row[1])])
print(data)

def distance(point1,point2):
    total = 0
    for i in range(len(point1)):
        total += (point1[i]-point2[i])**2
    return total**0.5

def mean(points):
    n = len(points)
    dims = len(points[0])
    results = []
    for i in range(dims):
        s = 0
        for j in range(n):
            s += points[j][i]
        results.append(s/n)
    return results 

def kmeans(data,k,max_iterations):
    centroids = random.sample(data,k)
    for x in range(max_iterations):
        clusters = []
        for i in range(k):
            clusters.append([])
        for point in data:
            distances = []
            for c in centroids:
                d = distance(point,c)
                distances.append(d)
            min_index = distances.index(min(distances))
            clusters[min_index].append(point)
        new_centroids = []
        for cluster in clusters:
            if cluster:
                new_c = mean(cluster)
            else:
                new_c = random.choice(data)
            new_centroids.append(new_c)
    
        if centroids == new_centroids:
            break
        
        centroids = new_centroids
    return clusters,centroids 

final_clusters,final_centroids = kmeans(data,3,100)
print("\nClusters -----")
for i in range(len(final_clusters)):
    print("\n Cluster",i+1," : ",final_clusters[i])
print("\nCentroids -----")
for i in range(len(final_centroids)):
    print("\n Centroid",i+1," : ",final_centroids[i])



