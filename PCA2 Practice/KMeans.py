import random

data = []
with open("F:\Machine Learning Lab - 5th sem\PCA2 Practice\data.csv","r") as f:
    for line in f:
        point = line.strip().split(",")
        #print(point)
        temp = []
        for x in point:
            temp.append(float(x))
        data.append(temp)
#print(data) : [[1.0, 2.0], [1.5, 1.8], [5.0, 8.0], [8.0, 8.0], [1.0, 0.6], [9.0, 11.0]]

# Function to calculate Euclidean distance between two points
def distance(point1,point2):
    total = 0
    # as point = [x,y]; dimension of each point = 2
    for i in range(len(point1)):
        total += (point1[i]-point2[i])**2
    return total**0.5

# Function to calculate the mean(centroid) of a cluster
def mean(points):
    n = len(points)  # no of points in the cluster 
    dims = len(points[0]) # no of dimensions i.e. 2D or 3D points
    result = []
    for i in range(dims):
        s = 0
        for j in range(n):
            s += points[j][i] # sum values of i-th dimension
        result.append(s/n)
    return result 


k = 3
max_iterations = 100   #The loop will stop after 100 iterations

def kmeans(data,k,max_iterations):
    # randomly selects k points from the dataset to set as centroids 
    centroids = random.sample(data,k)
    #print(centroids)

    # Repeat untill maximum iterations
    for x in range(max_iterations):
        # Create empty clusters 
        clusters = []
        for i in range(k):
            clusters.append([])  # it will generate the structure : [[],[],[]]

        # assign each point to the nearest centrioid
        for point in data: # here point means : [x,y] and data means : [[x,y],[z,p],...]
            distances = []
            for c in centroids:
                d = distance(c,point)
                distances.append(d) # distances array will store distance of each point from 3 centroids
            min_index = distances.index(min(distances)) # index of nearest centroid 
            clusters[min_index].append(point) # assign the point to that nearest centroid's cluster

        # Recalculate centroids of each cluster 
        new_centroids = []
        for cluster in clusters:
            if cluster: # if cluster is not empty
                new_c = mean(cluster)
            else:       # if cluster is empty, pick a random point as centroid
                new_c = random.choice(data)
            new_centroids.append(new_c)

        # when the iteration will stop ? if centroids didn't change
        if new_centroids == centroids :
            break 

        centroids = new_centroids 

    return centroids,clusters

# Step 5: Run K-Means
final_centroids, final_clusters = kmeans(data,3,100)

# Step 6: Print results
print("\nFinal Centroids:")
for i in range(len(final_centroids)):
    print("Centroid ",i+1," :",final_centroids[i])

print("\nFinal Clusters:")
for i in range(len(final_clusters)):
    print("Clusters ",i+1," :",final_clusters[i])

