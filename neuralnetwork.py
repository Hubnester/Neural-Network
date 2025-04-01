# Imports
import sys
import numpy as np
import timeit

class NeuralNetwork:
    def __init__(self, numInputNodes, numHiddenNodes, numOutputNodes):
        self.numInputNodes = int(numInputNodes)
        self.numHiddenNodes = int(numHiddenNodes)
        self.numOutputNodes = int(numOutputNodes)

        # Initialise the weights using random values
        self.inputToHiddenWeights = np.random.randn(self.numInputNodes, self.numHiddenNodes)
        self.hiddenToOutputWeights = np.random.randn(self.numHiddenNodes, self.numOutputNodes)

        self.hiddenBiasWeights = np.zeros(self.numHiddenNodes)
        self.outputBiasWeights = np.zeros(self.numOutputNodes)

        


def loadCsvGzFile(filename, data, labelIndex = 0, rowsToSkip = 1):
    file = np.loadtxt(filename, delimiter=",", skiprows=rowsToSkip)
    for item in file:
        currentData = {}
        # Add the label for the current item
        currentData["label"] = item[labelIndex]
        # Remove the label from the current item since it has already been gotten
        np.delete(item, labelIndex)
        # Add the values for the current item + convert 0 - 255 to 0 - 1 
        currentData["values"] = np.divide(item, 255)
        data.append(currentData)
        # Temp to make testing faster
        if (len(data) >= 100):
            break
    data = np.array(data)
    return

def getNumInputOutputNodes(data):
    numInputNodes = len(data[0]["values"])
    # Get the number of unique labels in the data
    labels = set()
    for item in data:
        labels.add(item["label"])
    numOutputNodes = len(labels)
    return numInputNodes, numOutputNodes

def main():
    if (len(sys.argv) < 3):
        print("Usage:", sys.argv[0], "<num hidden nodes> <training data filename> <testing data filename>")
        print("E.g.:", sys.argv[0], "500 fashion-mnist_train.csv.gz fashion-mnist_test.csv.gz")
        exit(1)

    # Get the start time to be able to calculate how long the program took to run
    startTime = timeit.default_timer()
    # Get the data to initialise the neural network
    numHiddenNodes = sys.argv[1]
    trainingData = []
    loadCsvGzFile(sys.argv[2], trainingData)
    print("Training data size:", len(trainingData))
    #print(trainingData)
    testingData = []
    loadCsvGzFile(sys.argv[3], testingData)
    print("Testing data size:", len(testingData))
    #print(testingData)
    numInputNodes, numOutputNodes = getNumInputOutputNodes(trainingData)

    # Create the neural network
    nn = NeuralNetwork(numInputNodes, numHiddenNodes, numOutputNodes)


    print("Time taken:", timeit.default_timer() - startTime)

if __name__ == "__main__":
    main()