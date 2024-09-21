import unittest

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        pass

class TestLongestConsecutiveSequence(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        nums = [100,4,200,1,3,2]
        self.assertEqual(self.solution.longestConsecutive(nums), 4)

    def test_example_2(self):
        nums = [0,3,7,2,5,8,4,6,0,1]
        self.assertEqual(self.solution.longestConsecutive(nums), 9)

    def test_empty_array(self):
        nums = []
        self.assertEqual(self.solution.longestConsecutive(nums), 0)

    def test_single_element(self):
        nums = [1]
        self.assertEqual(self.solution.longestConsecutive(nums), 1)

    def test_all_same_elements(self):
        nums = [1, 1, 1, 1]
        self.assertEqual(self.solution.longestConsecutive(nums), 1)

    def test_negative_numbers(self):
        nums = [-1, -5, -3, -2, -4]
        self.assertEqual(self.solution.longestConsecutive(nums), 5)

    def test_mixed_positive_negative(self):
        nums = [-1, 0, 1, 2, -3, -2, 5, 6, 7]
        self.assertEqual(self.solution.longestConsecutive(nums), 4)

    def test_large_range(self):
        nums = list(range(-10**9, 10**9, 10**8))
        self.assertEqual(self.solution.longestConsecutive(nums), len(nums))

if __name__ == '__main__':
    unittest.main()