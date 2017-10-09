""" Main module """

import math
import utils

dataset = utils.readWeatherDataSet('dataset.csv')

# e = utils.entropy('playtennis', dataset)
# datasetSize = len(dataset)
# ig = e
# print(e)
# print(datasetSize)
# values = utils.valuesOf('outlook', dataset)
# subsets = [utils.subset('outlook', value, dataset) for value in values]

# for s in subsets:
#     es = utils.entropy('playtennis', s)
#     subsetSize = len(s)
#     ig -= subsetSize / datasetSize * es

# print(ig)

print(utils.informationGain('outlook', 'playtennis', dataset))
print(utils.informationGain('humidity', 'playtennis', dataset))
print(utils.informationGain('wind', 'playtennis', dataset))
print(utils.informationGain('temperature', 'playtennis', dataset))
