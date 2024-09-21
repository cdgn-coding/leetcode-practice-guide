import unittest
from typing import List

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        pass

class TestMinPathSum(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        grid = [[1,3,1],[1,5,1],[4,2,1]]
        self.assertEqual(self.solution.minPathSum(grid), 7)

    def test_example_2(self):
        grid = [[1,2,3],[4,5,6]]
        self.assertEqual(self.solution.minPathSum(grid), 12)

    def test_single_cell(self):
        grid = [[5]]
        self.assertEqual(self.solution.minPathSum(grid), 5)

    def test_single_row(self):
        grid = [[1,2,3,4,5]]
        self.assertEqual(self.solution.minPathSum(grid), 15)

    def test_single_column(self):
        grid = [[1],[2],[3],[4],[5]]
        self.assertEqual(self.solution.minPathSum(grid), 15)

    def test_large_grid(self):
        grid = [[i+j for j in range(200)] for i in range(200)]
        self.assertEqual(self.solution.minPathSum(grid), 19701)

    def test_all_zeros(self):
        grid = [[0 for _ in range(10)] for _ in range(10)]
        self.assertEqual(self.solution.minPathSum(grid), 0)

    def test_all_max_values(self):
        grid = [[200 for _ in range(5)] for _ in range(5)]
        self.assertEqual(self.solution.minPathSum(grid), 1800)

if __name__ == '__main__':
    unittest.main()