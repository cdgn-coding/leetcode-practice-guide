import unittest

class Solution:
    def twoSum(self, numbers, target):
        pass

class TestTwoSum(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        numbers = [2, 7, 11, 15]
        target = 9
        self.assertEqual(self.solution.twoSum(numbers, target), [1, 2])

    def test_example_2(self):
        numbers = [2, 3, 4]
        target = 6
        self.assertEqual(self.solution.twoSum(numbers, target), [1, 3])

    def test_example_3(self):
        numbers = [-1, 0]
        target = -1
        self.assertEqual(self.solution.twoSum(numbers, target), [1, 2])

    def test_minimum_length(self):
        numbers = [1, 2]
        target = 3
        self.assertEqual(self.solution.twoSum(numbers, target), [1, 2])

    def test_maximum_length(self):
        numbers = list(range(1, 30001))
        target = 59999
        self.assertEqual(self.solution.twoSum(numbers, target), [29999, 30000])

    def test_negative_numbers(self):
        numbers = [-10, -5, 0, 5, 10]
        target = -15
        self.assertEqual(self.solution.twoSum(numbers, target), [1, 2])

    def test_duplicate_numbers(self):
        numbers = [1, 1, 2, 2, 3, 3]
        target = 4
        self.assertEqual(self.solution.twoSum(numbers, target), [2, 5])

    def test_large_numbers(self):
        numbers = [-1000, 0, 1000]
        target = 0
        self.assertEqual(self.solution.twoSum(numbers, target), [1, 3])

if __name__ == '__main__':
    unittest.main()