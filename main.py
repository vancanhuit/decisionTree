""" Main module """

import math
import utils

dataset = utils.readDataSet(
    'weatherDataset.csv', ['outlook', 'temperature', 'humidity', 'wind', 'playtennis'])

print(dataset)
print(utils.informationGain('outlook', 'playtennis', dataset))
print(utils.informationGain('humidity', 'playtennis', dataset))
print(utils.informationGain('wind', 'playtennis', dataset))
print(utils.informationGain('temperature', 'playtennis', dataset))
