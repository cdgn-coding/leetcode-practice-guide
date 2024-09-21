import unittest

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        pass

class TestGameOfLife(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
        expected = [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]
        self.solution.gameOfLife(board)
        self.assertEqual(board, expected)

    def test_example2(self):
        board = [[1,1],[1,0]]
        expected = [[1,1],[1,1]]
        self.solution.gameOfLife(board)
        self.assertEqual(board, expected)

    def test_empty_board(self):
        board = []
        expected = []
        self.solution.gameOfLife(board)
        self.assertEqual(board, expected)

    def test_single_cell_alive(self):
        board = [[1]]
        expected = [[0]]
        self.solution.gameOfLife(board)
        self.assertEqual(board, expected)

    def test_single_cell_dead(self):
        board = [[0]]
        expected = [[0]]
        self.solution.gameOfLife(board)
        self.assertEqual(board, expected)

    def test_all_dead(self):
        board = [[0,0,0],[0,0,0],[0,0,0]]
        expected = [[0,0,0],[0,0,0],[0,0,0]]
        self.solution.gameOfLife(board)
        self.assertEqual(board, expected)

    def test_all_alive(self):
        board = [[1,1,1],[1,1,1],[1,1,1]]
        expected = [[1,0,1],[0,0,0],[1,0,1]]
        self.solution.gameOfLife(board)
        self.assertEqual(board, expected)

    def test_oscillator(self):
        board = [[0,0,0],[1,1,1],[0,0,0]]
        expected = [[0,1,0],[0,1,0],[0,1,0]]
        self.solution.gameOfLife(board)
        self.assertEqual(board, expected)

if __name__ == '__main__':
    unittest.main()