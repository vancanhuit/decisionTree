import utils


class TestClass(object):
    ''' Test utility functions '''
    # Initialize dataset for testing
    attributes, dataset = utils.readDataSet('weatherDataSet.csv')

    def testReadDataSet(self):
        assert self.dataset is not None
        assert len(self.dataset) == 14
        assert len(self.attributes) == 5

    def testValuesOf(self):
        values = utils.valuesOf('outlook', self.dataset)
        assert values is not None
        assert len(values) == 3
        assert 'Sunny' in values
        assert 'Overcast' in values
        assert 'Rain' in values

    def testSubset(self):
        s = utils.subset('outlook', 'Sunny', self.dataset)
        assert s is not None
        assert len(s) == 5

    def testCount(self):
        yes = utils.count('playtennis', 'Yes', self.dataset)
        no = utils.count('playtennis', 'No', self.dataset)
        assert yes == 9
        assert no == 5
