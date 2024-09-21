import unittest

class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        pass

class TestMaxSubarraySumCircular(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        nums = [1,-2,3,-2]
        self.assertEqual(self.solution.maxSubarraySumCircular(nums), 3)

    def test_example_2(self):
        nums = [5,-3,5]
        self.assertEqual(self.solution.maxSubarraySumCircular(nums), 10)

    def test_example_3(self):
        nums = [-3,-2,-3]
        self.assertEqual(self.solution.maxSubarraySumCircular(nums), -2)

    def test_single_element(self):
        nums = [5]
        self.assertEqual(self.solution.maxSubarraySumCircular(nums), 5)

    def test_all_positive(self):
        nums = [1,2,3,4,5]
        self.assertEqual(self.solution.maxSubarraySumCircular(nums), 15)

    def test_all_negative(self):
        nums = [-1,-2,-3,-4,-5]
        self.assertEqual(self.solution.maxSubarraySumCircular(nums), -1)

    def test_circular_sum(self):
        nums = [3,-1,2,-1]
        self.assertEqual(self.solution.maxSubarraySumCircular(nums), 4)

    def test_large_array(self):
        nums = [i % 5 - 2 for i in range(30000)]
        self.assertEqual(self.solution.maxSubarraySumCircular(nums), 90000)

if __name__ == '__main__':
    unittest.main()