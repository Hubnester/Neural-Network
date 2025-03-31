# Imports
import sys
import math
import numpy as np

def loadCsvGzFile(filename, labelIndex = 0, rowsToSkip = 1):
    file = np.loadtxt(filename, delimiter=",", skiprows=rowsToSkip)
    data = []
    for item in file:
        currentData = {}
        # Add the label for the current item
        currentData["label"] = item[labelIndex]
        # Remove the label from the current item since it has already been gotten
        np.delete(item, labelIndex)
        # Add the values for the current item + convert 0 - 255 to 0 - 1 
        currentData["values"] = np.divide(item, 255)
        data.append(currentData)
    return np.array(data)

def main():
    if (len(sys.argv) < 3):
        print("Usage:", sys.argv[0], "<num hidden nodes> <training data filename> <testing data filename>")
        print("E.g.:", sys.argv[0], "500 fashion-mnist_train.csv.gz fashion-mnist_test.csv.gz")
        exit(1)

    hiddenNodes = sys.argv[1]
    trainingData = loadCsvGzFile(sys.argv[2])
    #print(trainingData)
    testingData = loadCsvGzFile(sys.argv[3])
    #print(testingData)
    inputNodes = 0
    outputNodes = 0

if __name__ == "__main__":
    main()