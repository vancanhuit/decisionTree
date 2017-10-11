''' Implement ID3 algorithm '''

import utils


def id3(attributes, targetAttribute, dataset):
    currentAttributes = attributes.copy()
    currentDataSet = dataset.copy()
    targetValues = utils.valuesOf(targetAttribute, currentDataSet)
    default = utils.majorityValue(targetAttribute, currentDataSet)
    currentEntropy = utils.entropy(targetAttribute, currentDataSet)

    # If attributes is empty, return the majority value
    if len(attributes) == 0:
        return default

    # if all examples belong to same class
    if currentEntropy == 0.0:
        [value] = targetValues
        return value

    bestAttribute = utils.selectBestAttribute(
        attributes, targetAttribute, dataset)

    tree = {bestAttribute: {}}
    bestAttributeValues = utils.valuesOf(bestAttribute, currentDataSet)
    currentAttributes.remove(bestAttribute)
    for value in bestAttributeValues:
        subset = utils.subset(bestAttribute, value, currentDataSet)
        subtree = id3(currentAttributes, targetAttribute, subset)

        tree[bestAttribute][value] = subtree

    return tree


def predict(input, tree):
    if not isinstance(tree, dict):
        return tree
    [root] = tree.keys()
    ans = tree[root].get(input[root])
    while ans and isinstance(ans, dict):
        [root] = ans.keys()
        ans = ans[root].get(input[root])

    return ans
