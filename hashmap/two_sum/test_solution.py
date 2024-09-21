import unittest

class TestTwoSum(unittest.TestCase):
    def test_example_1(self):
        nums = [2, 7, 11, 15]
        target = 9
        expected = [0, 1]
        self.assertCountEqual(two_sum(nums, target), expected)

    def test_example_2(self):
        nums = [3, 2, 4]
        target = 6
        expected = [1, 2]
        self.assertCountEqual(two_sum(nums, target), expected)

    def test_example_3(self):
        nums = [3, 3]
        target = 6
        expected = [0, 1]
        self.assertCountEqual(two_sum(nums, target), expected)

    def test_no_solution(self):
        nums = [1, 2, 3, 4]
        target = 10
        with self.assertRaises(ValueError):
            two_sum(nums, target)

    def test_negative_numbers(self):
        nums = [-1, -2, -3, -4, -5]
        target = -8
        expected = [2, 4]
        self.assertCountEqual(two_sum(nums, target), expected)

    def test_large_numbers(self):
        nums = [1000000000, 2000000000, 3000000000]
        target = 5000000000
        expected = [1, 2]
        self.assertCountEqual(two_sum(nums, target), expected)

    def test_minimum_length(self):
        nums = [1, 2]
        target = 3
        expected = [0, 1]
        self.assertCountEqual(two_sum(nums, target), expected)

    def test_maximum_length(self):
        nums = list(range(10000))
        target = 19997
        expected = [9998, 9999]
        self.assertCountEqual(two_sum(nums, target), expected)

if __name__ == '__main__':
    unittest.main()