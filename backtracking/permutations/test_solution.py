import unittest
from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        pass

class TestPermutations(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        nums = [1, 2, 3]
        expected = [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
        result = self.solution.permute(nums)
        self.assertEqual(len(result), len(expected))
        for perm in result:
            self.assertIn(perm, expected)

    def test_example_2(self):
        nums = [0, 1]
        expected = [[0,1],[1,0]]
        result = self.solution.permute(nums)
        self.assertEqual(len(result), len(expected))
        for perm in result:
            self.assertIn(perm, expected)

    def test_example_3(self):
        nums = [1]
        expected = [[1]]
        result = self.solution.permute(nums)
        self.assertEqual(result, expected)

    def test_empty_list(self):
        nums = []
        expected = [[]]
        result = self.solution.permute(nums)
        self.assertEqual(result, expected)

    def test_negative_numbers(self):
        nums = [-1, -2, 3]
        expected = [[-1,-2,3],[-1,3,-2],[-2,-1,3],[-2,3,-1],[3,-1,-2],[3,-2,-1]]
        result = self.solution.permute(nums)
        self.assertEqual(len(result), len(expected))
        for perm in result:
            self.assertIn(perm, expected)

    def test_max_length(self):
        nums = [1, 2, 3, 4, 5, 6]
        result = self.solution.permute(nums)
        self.assertEqual(len(result), 720)  # 6! = 720

    def test_constraints(self):
        nums = [10, -10, 0, 5, -5, 1]
        result = self.solution.permute(nums)
        self.assertTrue(all(len(perm) == 6 for perm in result))
        self.assertTrue(all(-10 <= num <= 10 for perm in result for num in perm))

if __name__ == '__main__':
    unittest.main()