import unittest

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        pass

class TestUniquePaths(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
        self.assertEqual(self.solution.uniquePathsWithObstacles(obstacleGrid), 2)

    def test_example_2(self):
        obstacleGrid = [[0,1],[0,0]]
        self.assertEqual(self.solution.uniquePathsWithObstacles(obstacleGrid), 1)

    def test_single_cell_no_obstacle(self):
        obstacleGrid = [[0]]
        self.assertEqual(self.solution.uniquePathsWithObstacles(obstacleGrid), 1)

    def test_single_cell_with_obstacle(self):
        obstacleGrid = [[1]]
        self.assertEqual(self.solution.uniquePathsWithObstacles(obstacleGrid), 0)

    def test_start_cell_blocked(self):
        obstacleGrid = [[1,0,0],[0,0,0],[0,0,0]]
        self.assertEqual(self.solution.uniquePathsWithObstacles(obstacleGrid), 0)

    def test_end_cell_blocked(self):
        obstacleGrid = [[0,0,0],[0,0,0],[0,0,1]]
        self.assertEqual(self.solution.uniquePathsWithObstacles(obstacleGrid), 0)

    def test_all_cells_blocked(self):
        obstacleGrid = [[1,1,1],[1,1,1],[1,1,1]]
        self.assertEqual(self.solution.uniquePathsWithObstacles(obstacleGrid), 0)

    def test_no_obstacles(self):
        obstacleGrid = [[0,0,0],[0,0,0],[0,0,0]]
        self.assertEqual(self.solution.uniquePathsWithObstacles(obstacleGrid), 6)

    def test_large_grid(self):
        obstacleGrid = [[0] * 100 for _ in range(100)]
        self.assertGreater(self.solution.uniquePathsWithObstacles(obstacleGrid), 0)

if __name__ == '__main__':
    unittest.main()