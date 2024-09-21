import unittest

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        pass

class TestSurroundedRegions(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        board = [
            ["X","X","X","X"],
            ["X","O","O","X"],
            ["X","X","O","X"],
            ["X","O","X","X"]
        ]
        expected = [
            ["X","X","X","X"],
            ["X","X","X","X"],
            ["X","X","X","X"],
            ["X","O","X","X"]
        ]
        self.solution.solve(board)
        self.assertEqual(board, expected)

    def test_example2(self):
        board = [["X"]]
        expected = [["X"]]
        self.solution.solve(board)
        self.assertEqual(board, expected)

    def test_empty_board(self):
        board = []
        expected = []
        self.solution.solve(board)
        self.assertEqual(board, expected)

    def test_all_x(self):
        board = [
            ["X","X","X"],
            ["X","X","X"],
            ["X","X","X"]
        ]
        expected = [
            ["X","X","X"],
            ["X","X","X"],
            ["X","X","X"]
        ]
        self.solution.solve(board)
        self.assertEqual(board, expected)

    def test_all_o(self):
        board = [
            ["O","O","O"],
            ["O","O","O"],
            ["O","O","O"]
        ]
        expected = [
            ["O","O","O"],
            ["O","O","O"],
            ["O","O","O"]
        ]
        self.solution.solve(board)
        self.assertEqual(board, expected)

    def test_o_on_edges(self):
        board = [
            ["X","O","X","X"],
            ["O","X","O","X"],
            ["X","O","X","O"],
            ["X","X","O","X"]
        ]
        expected = [
            ["X","O","X","X"],
            ["O","X","X","X"],
            ["X","O","X","O"],
            ["X","X","O","X"]
        ]
        self.solution.solve(board)
        self.assertEqual(board, expected)

    def test_single_o_surrounded(self):
        board = [
            ["X","X","X"],
            ["X","O","X"],
            ["X","X","X"]
        ]
        expected = [
            ["X","X","X"],
            ["X","X","X"],
            ["X","X","X"]
        ]
        self.solution.solve(board)
        self.assertEqual(board, expected)

if __name__ == '__main__':
    unittest.main()