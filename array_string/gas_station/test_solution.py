import unittest

class TestGasStation(unittest.TestCase):
    
    def test_example1(self):
        gas = [1,2,3,4,5]
        cost = [3,4,5,1,2]
        self.assertEqual(canCompleteCircuit(gas, cost), 3)
    
    def test_example2(self):
        gas = [2,3,4]
        cost = [3,4,3]
        self.assertEqual(canCompleteCircuit(gas, cost), -1)
    
    def test_single_station_sufficient(self):
        gas = [5]
        cost = [4]
        self.assertEqual(canCompleteCircuit(gas, cost), 0)
    
    def test_single_station_insufficient(self):
        gas = [3]
        cost = [4]
        self.assertEqual(canCompleteCircuit(gas, cost), -1)
    
    def test_multiple_stations_sufficient(self):
        gas = [2,4,3,1,5]
        cost = [3,1,4,5,2]
        self.assertEqual(canCompleteCircuit(gas, cost), 1)
    
    def test_multiple_stations_insufficient(self):
        gas = [1,2,3,4,5]
        cost = [5,4,3,2,1]
        self.assertEqual(canCompleteCircuit(gas, cost), -1)

if __name__ == '__main__':
    unittest.main()