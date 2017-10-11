""" Main module """

import utils
import id3

# Prepare dataset
attributes, dataset = utils.readDataSet('./datasets/train.csv')
targetAttribute = attributes[-1]
attributes.remove(targetAttribute)

tree = id3.id3(attributes, targetAttribute, dataset)

print('Tree: ')
print(tree)

_, dataset = utils.readDataSet('./datasets/test.csv')
print('Predict: ')
for d in dataset:
    print(d)
    print(id3.predict(d, tree))
