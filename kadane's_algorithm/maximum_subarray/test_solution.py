import unittest

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        pass

class TestMaxSubArray(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        nums = [-2,1,-3,4,-1,2,1,-5,4]
        self.assertEqual(self.solution.maxSubArray(nums), 6)

    def test_example2(self):
        nums = [1]
        self.assertEqual(self.solution.maxSubArray(nums), 1)

    def test_example3(self):
        nums = [5,4,-1,7,8]
        self.assertEqual(self.solution.maxSubArray(nums), 23)

    def test_all_negative(self):
        nums = [-1,-2,-3,-4,-5]
        self.assertEqual(self.solution.maxSubArray(nums), -1)

    def test_all_positive(self):
        nums = [1,2,3,4,5]
        self.assertEqual(self.solution.maxSubArray(nums), 15)

    def test_alternating(self):
        nums = [1,-1,1,-1,1]
        self.assertEqual(self.solution.maxSubArray(nums), 1)

    def test_large_numbers(self):
        nums = [10000,-9999,10000]
        self.assertEqual(self.solution.maxSubArray(nums), 10001)

    def test_minimum_length(self):
        nums = [5]
        self.assertEqual(self.solution.maxSubArray(nums), 5)

    def test_maximum_length(self):
        nums = [1] * 100000 + [-1] + [1] * 5000
        self.assertEqual(self.solution.maxSubArray(nums), 105000)

if __name__ == '__main__':
    unittest.main()