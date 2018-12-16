
import sys
import math
import random 

def read_dataset(dataset_path):
    dataset = []
    with open(dataset_path,"r") as f:
        lines = f.readlines()
        for line in lines:
            line = line.replace("\n","")
            sample = line.split(",")
            if len(sample) > 0:
                dataset.append(sample)
    return dataset

def euclidean_distance(sample1,sample2):
    sample1_size = len(sample1)
    sample2_size = len(sample2)
    distance = 0

    if sample1_size == sample2_size:
        for i in range(1,sample1_size-1):
            if sample1[i]=="?":
                sample1[i] = 0
            if sample2[i]=="?":
                sample2[i] = 0
            distance += (int(sample1[i])-int(sample2[i])) * (int(sample1[i])-int(sample2[i]))

    return math.sqrt(distance)

def calculate_cluster_mean(cluster):
    avg = [format(float(sum(col))/len(col),".2f") for col in zip(*cluster)]
    return avg

def count_actual_classes(dataset):
    classes = [0,0]
    for sample in dataset:
        if sample[len(sample)-1] == "2":
            classes[1] += 1
        elif sample[len(sample)-1] == "4" :
            classes[0] += 1
    return classes

def main():
    path = sys.argv[1]
    k = int(sys.argv[2])

    dataset = read_dataset(path)

    attrs_size = len(dataset[0])
    centroids = []
    for i in range(k):
        temp = []
        for j in range(attrs_size):
            temp.append(random.randint(1,12))
        centroids.append(temp)

    print(centroids)
    cluster0 = []
    cluster1 = []
    while(True):

    
        for sample in dataset:
            dist_cntr0 = euclidean_distance(sample,centroids[0])
            dist_cntr1 = euclidean_distance(sample,centroids[1])

            vec_sample = []
            for i in range(1,len(sample)-1): # 1den basliyor cunku idyi alma.
                vec_sample.append(int(sample[i]))

            if dist_cntr1 > dist_cntr0:
                cluster0.append(vec_sample)
            elif dist_cntr0 > dist_cntr1:
                cluster1.append(vec_sample)

        old_centroids = []
        for elem in centroids:
            old_centroids.append(elem)

        centroids[0] = calculate_cluster_mean(cluster0)
        centroids[1] = calculate_cluster_mean(cluster1)
        print("Centroid for cluster #0: ",centroids[0])
        print("Centroid for cluster #1: ",centroids[1])
        if old_centroids == centroids:
            break

    print("---------------------------------------")
    print("Centroid for cluster #0     : ",centroids[0])
    print("Centroid for cluster #1     : ",centroids[1])
    print("Total members of cluster #0 : ",len(cluster0))
    print("Total members of cluster #1 : ",len(cluster1))
    print("Acutal Members of Class #0  : ",count_actual_classes(dataset)[0])
    print("Acutal Members of Class #1  : ",count_actual_classes(dataset)[1])

if __name__ == '__main__':
    main()