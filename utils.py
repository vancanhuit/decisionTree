""" Utility functions """

import math


def readDataSet(sourceFile):
    ''' Read dataset from external file '''
    data = []
    attributes = []
    dataset = []
    with open(sourceFile, 'r') as f:
        data = [line.rstrip('\n').split(',') for line in f]

    attributes = data[0]
    data.remove(attributes)

    for row in data:
        d = {}
        for index, attr in enumerate(attributes):
            d[attr] = row[index]

        dataset.append(d.copy())

    return attributes, dataset


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


def majorityValue(targetAttribute, dataset):
    targetValues = valuesOf(targetAttribute, dataset)
    counter = {}
    for value in targetValues:
        if counter.get(value, None) is None:
            counter[value] = 1
        else:
            counter[value] += 1

    max = 0
    majorValue = ""
    for key in counter.keys():
        if counter[key] > max:
            majorValue = key

    return majorValue


def selectBestAttribute(attributes, targetAttribute, dataset):
    igs = [informationGain(attr, targetAttribute, dataset)
           for attr in attributes]

    maxIGIndex = 0
    for index in range(len(igs) - 1):
        if igs[index + 1] > igs[maxIGIndex]:
            maxIGIndex = index + 1

    return attributes[maxIGIndex]
