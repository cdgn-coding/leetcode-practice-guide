import unittest

class Solution:
    def maxArea(self, height: List[int]) -> int:
        pass

class TestMaxArea(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        height = [1,8,6,2,5,4,8,3,7]
        self.assertEqual(self.solution.maxArea(height), 49)

    def test_example_2(self):
        height = [1,1]
        self.assertEqual(self.solution.maxArea(height), 1)

    def test_minimum_length(self):
        height = [1,2]
        self.assertEqual(self.solution.maxArea(height), 1)

    def test_maximum_length(self):
        height = [i for i in range(100000)]
        self.assertGreater(self.solution.maxArea(height), 0)

    def test_all_zeros(self):
        height = [0] * 10000
        self.assertEqual(self.solution.maxArea(height), 0)

    def test_ascending_order(self):
        height = [1,2,3,4,5,6,7,8,9,10]
        self.assertEqual(self.solution.maxArea(height), 25)

    def test_descending_order(self):
        height = [10,9,8,7,6,5,4,3,2,1]
        self.assertEqual(self.solution.maxArea(height), 25)

    def test_same_height(self):
        height = [5] * 10000
        self.assertEqual(self.solution.maxArea(height), 49995)

    def test_one_tall_line(self):
        height = [1,1,1,1,10000,1,1,1,1]
        self.assertEqual(self.solution.maxArea(height), 8)

if __name__ == '__main__':
    unittest.main()