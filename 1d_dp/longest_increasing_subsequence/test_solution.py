import unittest

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        pass

class TestLengthOfLIS(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        nums = [10,9,2,5,3,7,101,18]
        self.assertEqual(self.solution.lengthOfLIS(nums), 4)

    def test_example2(self):
        nums = [0,1,0,3,2,3]
        self.assertEqual(self.solution.lengthOfLIS(nums), 4)

    def test_example3(self):
        nums = [7,7,7,7,7,7,7]
        self.assertEqual(self.solution.lengthOfLIS(nums), 1)

    def test_empty_array(self):
        nums = []
        self.assertEqual(self.solution.lengthOfLIS(nums), 0)

    def test_single_element(self):
        nums = [5]
        self.assertEqual(self.solution.lengthOfLIS(nums), 1)

    def test_all_increasing(self):
        nums = [1,2,3,4,5]
        self.assertEqual(self.solution.lengthOfLIS(nums), 5)

    def test_all_decreasing(self):
        nums = [5,4,3,2,1]
        self.assertEqual(self.solution.lengthOfLIS(nums), 1)

    def test_random_sequence(self):
        nums = [3,1,4,1,5,9,2,6,5,3,5]
        self.assertEqual(self.solution.lengthOfLIS(nums), 5)

if __name__ == '__main__':
    unittest.main()