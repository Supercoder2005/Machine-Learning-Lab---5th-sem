import csv 
data = []
with open("F:\Machine Learning Lab - 5th sem\PCA2 Practice\data.csv","r")as file:
    reader = csv.reader(file)
    for row in reader:
        data.append([float(row[0]),float(row[1])])
print(data) # [[1.0, 2.0], [1.5, 1.8], [5.0, 8.0], [8.0, 8.0], [1.0, 0.6], [9.0, 11.0]]

def distance(p1,p2):
    total = 0
    for i in range(len(p1)):
        total += (p1[i]-p2[i])**2
    return total**0.5

# distance between two clusters 
def single_linkage(c1,c2):
    min_dist = 9999.0
    for point1 in c1:
        for point2 in c2:
            d = distance(point1,point2)
            if d < min_dist:
                min_dist = d 
    return min_dist 

def complete_linkage(c1,c2):
    max_dist = 0
    for point1 in c1:
        for point2 in c2:
            d = distance(point1,point2)
            if d>max_dist:
                max_dist = d 
    return max_dist 

def hierarchical_clustering(data,linkage):
    # converting each point as individual clusters 
    clusters = []
    for point in data:
        clusters.append([point])


    step = 1 # step is just a counter to print the merge steps

    # we keep merging untill only one cluster remains
    while(len(clusters)>1):
        min_dist = 9999
        merged_clusters_id = (-1,-1)

        for i in range(len(clusters)):
            for j in range(i+1,len(clusters)):
                if linkage == "single":
                    d = single_linkage(clusters[i],clusters[j])
                else:
                    d = complete_linkage(clusters[i],clusters[j])
                if d < min_dist:
                    min_dist = d 
                    merged_clusters_id = (i,j)
        # merge the two closest clusters
        c1 , c2 = merged_clusters_id
        
        merged_cluster = clusters[c1] + clusters[c2]

        # remove old cluster and add the merged one
        new_clusters = []
        for k in range(len(clusters)):
            if k not in merged_clusters_id:
                new_clusters.append(clusters[k])
        new_clusters.append(merged_cluster)

        # update the main clusters list 
        clusters = new_clusters

        print(f"\nStep {step}: Merged Cluster {merged_clusters_id} at distance = {min_dist}")
        print(f"\nClusters : {clusters}")

        step += 1
    return clusters[0]

print("\n-----SINGLE LINKAGE------")
hierarchical_clustering(data,"single")
print("\n-----COMPLETE LINKAGE------")
hierarchical_clustering(data,"complete")
