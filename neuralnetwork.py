# Imports
import sys
import math
import numpy as np

def loadCsvGzFile(filename):
    "placeholder"

def main():
    if (len(sys.argv) < 6):
        print("Usage:", sys.argv[0], "<num input nodes> <num hidden nodes> <num output nodes> <training data filename> <testing data filename>")
        print("E.g.:", sys.argv[0], "784 500 10 fashion-mnist_train.csv.gz fashion-mnist_test.csv.gz")
        exit(1)
    print(sys.argv)

if __name__ == "__main__":
    main()