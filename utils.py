""" Utility functions """

import math


def readDataSet(sourceFile, attributes):
    ''' Read dataset from external file '''
    data = {}
    dataset = []
    with open(sourceFile, 'r') as f:
        # Remove any \n character on each line
        lines = [line.rstrip('\n') for line in f]

        for line in lines:
            row = line.split(',')
            for index, attr in enumerate(attributes):
                data[attr] = row[index]

            dataset.append(data.copy())

    return dataset


def valuesOf(attribute, dataset):
    ''' Get all possible values of an attribute in a dataset '''
    values = set()
    for d in dataset:
        values.add(d[attribute])

    return values


def subset(attribute, value, dataset):
    ''' Get subset of dataset in which attribute's value = value '''
    s = []
    for d in dataset:
        if d[attribute] == value:
            s.append(d.copy())

    return s


def count(targetAttribute, targetValue, dataset):
    ''' Count how many target value appear in dataset '''
    sum = 0
    for d in dataset:
        if d[targetAttribute] == targetValue:
            sum += 1

    return sum


def entropy(targetAttribute, dataset):
    ''' Compute entropy of a dataset with a target attribute '''
    # Get all possible values of target attribute
    targetValues = valuesOf(targetAttribute, dataset)

    # Count how many each target value appear in dataset
    valueCounters = [count(targetAttribute, targetValue, dataset)
                     for targetValue in targetValues]

    # Compute entropy
    size = len(dataset)
    e = 0.0
    for p in valueCounters:
        e -= p / size * math.log2(p / size)

    return e


def informationGain(attribute, targetAttribute, dataset):
    ''' Compute gain information of an attribute in a dataset '''
    # Compute entropy of original dataset
    e = entropy(targetAttribute, dataset)
    datasetSize = len(dataset)
    # Initialize information gain
    ig = e

    # Get all possible values of an attribute in dataset
    values = valuesOf(attribute, dataset)
    # Get all subset of dataset in which attribute's value = value
    subsets = [subset(attribute, value, dataset) for value in values]

    for s in subsets:
        # Firstly, compute entropy of subset s
        es = entropy(targetAttribute, s)
        subsetSize = len(s)
        ig -= subsetSize / datasetSize * es

    return ig


def selectBestAttribute(attributes, targetAttribute, dataset):
    igs = [informationGain(attr, targetAttribute, dataset)
           for attr in attributes]

    maxIGIndex = 0
    for index in range(len(igs) - 1):
        if igs[index + 1] > igs[maxIGIndex]:
            maxIGIndex = index + 1

    return attributes[maxIGIndex]
