import unittest
from typing import List

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        pass

class TestSnakesAndLadders(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        board = [
            [-1,-1,-1,-1,-1,-1],
            [-1,-1,-1,-1,-1,-1],
            [-1,-1,-1,-1,-1,-1],
            [-1,35,-1,-1,13,-1],
            [-1,-1,-1,-1,-1,-1],
            [-1,15,-1,-1,-1,-1]
        ]
        self.assertEqual(self.solution.snakesAndLadders(board), 4)

    def test_example_2(self):
        board = [[-1,-1],[-1,3]]
        self.assertEqual(self.solution.snakesAndLadders(board), 1)

    def test_no_snakes_or_ladders(self):
        board = [[-1,-1,-1],[-1,-1,-1],[-1,-1,-1]]
        self.assertEqual(self.solution.snakesAndLadders(board), 2)

    def test_impossible_to_reach(self):
        board = [[-1,-1],[-1,-1]]
        self.assertEqual(self.solution.snakesAndLadders(board), -1)

    def test_single_square(self):
        board = [[-1]]
        self.assertEqual(self.solution.snakesAndLadders(board), 0)

    def test_complex_board(self):
        board = [
            [-1,-1,-1,-1],
            [-1,-1,-1,-1],
            [-1,9,8,-1],
            [16,7,-1,15]
        ]
        self.assertEqual(self.solution.snakesAndLadders(board), 2)

if __name__ == '__main__':
    unittest.main()