""" Main module """

import utils
import id3

# Prepare dataset
attributes, dataset = utils.readDataSet('weatherDataSet.csv')
targetAttribute = attributes[-1]
attributes.remove(targetAttribute)

tree = id3.id3(attributes, targetAttribute, dataset)
print(tree)
