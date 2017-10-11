""" Main module """

import pydot
import utils
import id3
import decisiontree

# Read weather dataset
print('Reading weather dataset...')
weatherAttributes, weatherDataSet = utils.readDataSet(
    './datasets/weatherDataSetTrain.csv')
weatherTargetAttribute = weatherAttributes[-1]
weatherAttributes.remove(weatherTargetAttribute)

# Train
print('Training weather dataset...')
weatherTree = id3.id3(
    weatherAttributes, weatherTargetAttribute, weatherDataSet)
print(weatherTree)

print('Plotting weather decision tree...')
weatherGraph = pydot.Dot(graph_type='digraph')
decisiontree.drawTree(weatherGraph, weatherTree)
weatherGraph.write('./images/weather.png', prog=None, format='png')
print('Done.')

# Read car evaluation dataset
print('===========================================')
print('Reading car evaluation training dataset...')
carAttributes, carEvaluationTrainDataSet = utils.readDataSet(
    './datasets/car-evaluation-train.csv')
targetAttribute = carAttributes[-1]
carAttributes.remove(targetAttribute)

# Train
print('>>> Training car evaluation dataset...')
carTree = id3.id3(carAttributes, targetAttribute, carEvaluationTrainDataSet)
print(carTree)

# Test
print('Reading car evaluation test dataset')
_, testDataset = utils.readDataSet('./datasets/car-evaluation-test.csv')
counter = 0
testSize = len(testDataset)

print('>>> Testing...')
for d in testDataset:
    targetValue = id3.predict(d, carTree)
    if targetValue == d[targetAttribute]:
        counter += 1

ratio = counter / testSize * 100
print('Prediction accuracy: {:.2f}%'.format(ratio))
