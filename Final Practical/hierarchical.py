import csv 
data = []
with open ("F:\Machine Learning Lab - 5th sem\Final Practical\kmeansData.csv","r")as file:
    reader = csv.reader(file)
    for row in reader:
        data.append([float(row[0]),float(row[1])])
print(data)

def distance(point1,point2):
    total = 0
    for i in range(len(point1)):
        total += (point1[i]-point2[i])**2 
    return total**0.5 

#distance between two clusers --- using single , complete linkage
def single_linkage(c1,c2):
    min_dist = 9999.0
    for point1 in c1:
        for point2 in c2:
            d = distance(point1,point2)
            if d<min_dist:
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
    # initialize each datapoint as its own cluster
    clusters = []
    for point in data :
        clusters.append([point])

    step = 1 # just to keep track of the step of merging of closest clusters 
    
    while(len(clusters)>1):  # we keep merging untill cluster size becomes 1

        min_dist = 9999.0 
        merged_cluster_id = (-1,-1)
        
        for i in range(len(clusters)):
            for j in range(i+1,len(clusters)):
                if linkage == "single":
                    d = single_linkage(clusters[i],clusters[j])
                else:
                    d = complete_linkage(clusters[i],clusters[j])
                if d < min_dist :
                    min_dist = d 
                    merged_cluster_id = (i,j)
        # merge two closest clusters 
        c1,c2 = merged_cluster_id
        merged_cluster = clusters[c1]+clusters[c2]

        # remove old cluster and add the merged one 
        new_clusters = []
        for k in range(len(clusters)):
            if k not in merged_cluster_id:
                new_clusters.append(clusters[k]) # copy the clusters as it is in the new_clusters list which are not merged
        new_clusters.append(merged_cluster)   # add the merged clusters to new_cluster 
        # update the main cluster list 
        clusters = new_clusters 

        print("\nStep",step," Merged clusters : ",merged_cluster_id," at distance = ",min_dist)
        print("\nClusters : ",clusters)

        step += 1

    return clusters[0]
     

print("\n----------SINGLE LINKAGE-----------")
hierarchical_clustering(data,"single")
print("\n-----------COMPLETE LINKAGE----------")
hierarchical_clustering(data,"complete")

