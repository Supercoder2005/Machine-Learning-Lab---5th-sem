import random 
import csv 

with open ("F:\Machine Learning Lab - 5th sem\Final Practical\kmeansData.csv","r") as file:
    reader = csv.reader(file)
    data = []
    for row in reader:
        data.append([float(row[0]),float(row[1])])
    print(data)

# function to calculate the distance between two points 
def distance(point1,point2):
    toatl = 0
    for i in range(len(point1)):
        total += (point1[i]-point2[i])**2
    return total**0.5 

# function to calculate the mean of the points inside of a cluster 
def mean(points):
    n = len(points) # total no of points in the cluster
    dims = len(points[0]) # dimension of the points - 2D or 3D 
    for i in range(dims):
        s = 0
        for j in range(n):
            s += points[j][i] 
    return s/n 

# def kmeans(data,k,max_iterations):
#     # randomly selects k points from the dataset as k initial centroids 
#     centroids = random.sample(data,k)

#     for x in range(max_iterations):
#         # initialize structure of clusters list 
#         clusters = []
#         for i in range(k):
#             clusters.append([])
#         # find out the distance between each point and cluster centroid
#         distances = []
#         for point in data:
#             for c in centroids:
#                 d = distance(c,point)
#                 distances.append(d)
#             min_index = distances.index(min(distances))
#             clusters[min_index].append(d)
#         # calculate the updated mean/centroid of each cluster 
#         new_centroids = []
#         for cluster in clusters:
#             if cluster:
#                 new_c = mean(cluster)
#             else:
#                 new_c = random.choice(data)
#             new_centroids.append(new_c)


            
def kmeans(data,k,max_iterations):
    # randomly initialize k points as initial cluster centroids 
    centroids = random.sample(data,k) # this will denerate a list of lists 

    # final loop
    for x in range(max_iterations):
        clusters = []
        for i in range(k):
            clusters.append([]) # clusters = [[],[],[]]
        # calculate distance between each datapoint and centroid of cluster 
        for point in data:
            distances = []
            for c in centroids:
                d = distance(c,point)
                distances.append(d)
            min_index = distances.index(min(distances))
            clusters[min_index].append(point)
        
        # calculate the updated centroid 
        new_centroids = []
        for c in clusters:
            if c:
                new_c = mean(c)
            else:
                new_c = random.choice(data)
            new_centroids.append(new_c)
        
        # convergence 
        if new_centroids == centroids:
            break 

        centroids = new_centroids 
    return clusters,centroids

# run the kmeans algorithm 
final_clusters,final_centroids = kmeans(data,3,100)
print("Clusters :\n")

for i in range(len(final_clusters)):
    print("Cluster ",i+1,": ",final_clusters[i])

for i in range(len(final_centroids)):
    print("Centroids ",i+1,": ",final_centroids[i])
    




        
