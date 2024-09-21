import unittest

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        pass

class TestNumIslands(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        grid = [
            ["1","1","1","1","0"],
            ["1","1","0","1","0"],
            ["1","1","0","0","0"],
            ["0","0","0","0","0"]
        ]
        self.assertEqual(self.solution.numIslands(grid), 1)

    def test_example_2(self):
        grid = [
            ["1","1","0","0","0"],
            ["1","1","0","0","0"],
            ["0","0","1","0","0"],
            ["0","0","0","1","1"]
        ]
        self.assertEqual(self.solution.numIslands(grid), 3)

    def test_single_island(self):
        grid = [["1"]]
        self.assertEqual(self.solution.numIslands(grid), 1)

    def test_no_island(self):
        grid = [["0"]]
        self.assertEqual(self.solution.numIslands(grid), 0)

    def test_all_islands(self):
        grid = [
            ["1","1","1"],
            ["1","1","1"],
            ["1","1","1"]
        ]
        self.assertEqual(self.solution.numIslands(grid), 1)

    def test_multiple_small_islands(self):
        grid = [
            ["1","0","1","0","1"],
            ["0","1","0","1","0"],
            ["1","0","1","0","1"]
        ]
        self.assertEqual(self.solution.numIslands(grid), 9)

    def test_large_grid(self):
        grid = [["0" if (i + j) % 2 == 0 else "1" for j in range(300)] for i in range(300)]
        self.assertEqual(self.solution.numIslands(grid), 45000)

if __name__ == '__main__':
    unittest.main()