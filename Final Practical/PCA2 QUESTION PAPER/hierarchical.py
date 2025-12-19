import csv 
data = []
with open("F:\\Machine Learning Lab - 5th sem\\PCA2 Practice\\data.csv","r")as file:
    reader = csv.reader(file)
    for row in reader:
        data.append([float(row[0]),float(row[1])])
print(data)

def distance(point1,point2):
    total = 0
    for i in range(len(point1)):
        total += (point1[i]-point2[i])**2
    return total**0.5 

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

def hierarchical(data,linkage):
    clusters = []
    for point in data:
        clusters.append([point])
    step = 1
    while(len(clusters)>1):
        min_dist = 9999.0
        merged_cluster_id = (-1,-1)
        for i in range(len(clusters)):
            for j in range(i+1,len(clusters)):
                if linkage == "single":
                    d = single_linkage(clusters[i],clusters[j])
                else:
                    d = complete_linkage(clusters[i],clusters[j])
                if d<min_dist:
                    min_dist = d
                    merged_cluster_id = (i,j)
        c1,c2 = merged_cluster_id
        merged_cluster = clusters[c1]+clusters[c2]

        print(f"Step {step} : Merging {clusters[c1]} and {clusters[c2]} at distance : {min_dist}")

        clusters.pop(c2)
        clusters.pop(c1)
        clusters.append(merged_cluster)

        step += 1
    print("Final cluster :",clusters[0])

print("\n------SINGLE LINKAGE-----\n")
hierarchical(data,"single")
print("\n------COMPLETE LINKAGE-----\n")
hierarchical(data,"complete")




