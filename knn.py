
import sys
import math

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

def majority_voting(best_matches):
    benign_count = 0 # 2 benign
    malicant_count = 0 # 4 malicnat
    for classlabel in best_matches:
        if classlabel == "2":
            benign_count += 1
        elif classlabel == "4":
            malicant_count += 1
    if benign_count > malicant_count:
        return "2"
    else:
        return "4"

def main():
    path = sys.argv[1]
    k = int(sys.argv[2])

    dataset = read_dataset(path)
    dataset_size = len(dataset)

    ###
    groups = []
    for i in range(10):
        groups.append(read_dataset("data/"+str(i+1)))

    average_success = 0
    for i in range(10):
        test_ds = groups[i]
        train_ds = []
        for j in range(10):
            if i != j:
                train_ds += groups[j]    

        correctly_classified = 0
        for test_sample in test_ds:
            distances = []
            classes = []
            for train_sample in train_ds:
                distances.append(euclidean_distance(test_sample,train_sample))
                classes.append(train_sample[len(train_sample)-1])
            
            best_matches = []
            for i in range(k):
                min_dist = min(distances)
                best_matches.append(classes[distances.index(min_dist)])
                distances.remove(min_dist)

            actual_class = test_sample[len(test_sample)-1]
            knn_result = majority_voting(best_matches)
            is_correctly_classified = "FALSE"
            if actual_class == knn_result:
                correctly_classified += 1
                is_correctly_classified = "TRUE"
           #print("ID: ",test_sample[0],"Actual Class: ",test_sample[len(test_sample)-1]," KNN Result: ",majority_voting(best_matches)," Correct: ",is_correctly_classified)
        
        success = correctly_classified/len(test_ds)*100
        average_success += success
        print("------------------------------------------------")
        print("Success Rate         : ",success,"%")
        print("Correctly Classified : ",correctly_classified)
        print("False Classified     : ",len(test_ds)-correctly_classified)

    print("------------------------------------------------")
    print("Average Success Rate         : ",average_success/10,"%")
if __name__ == '__main__':
    main()