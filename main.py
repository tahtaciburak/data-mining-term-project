
def knn(train_set,test_set,k):
    print("knnn")

def kmeans(train_set,test_set,k):
    print("kmeans")

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

def main():
    operation = input("Choose Your Operation \n\t1.KNN Classification\n\t2.KMeans Clustering\nChoice: ")
    dataset_path = input("Enter dataset path: ")
    test_method = input("Choose test method: \n\t1.kfold Cross Validation\n\t2.Percentage Split\nChoice: ")
    if test_method == '1':
        k = input("Enter k value: ")
    elif test_method == '2':
        percentage = input("Enter percentage: ")
    
    print(read_dataset(dataset_path))

if __name__ == '__main__':
    main()