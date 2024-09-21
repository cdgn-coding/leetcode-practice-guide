import unittest

class Solution:
    def totalNQueens(self, n: int) -> int:
        pass

class TestNQueens(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.totalNQueens(4), 2)

    def test_example_2(self):
        self.assertEqual(self.solution.totalNQueens(1), 1)

    def test_minimum_input(self):
        self.assertEqual(self.solution.totalNQueens(1), 1)

    def test_maximum_input(self):
        self.assertEqual(self.solution.totalNQueens(9), 352)

    def test_no_solution(self):
        self.assertEqual(self.solution.totalNQueens(2), 0)
        self.assertEqual(self.solution.totalNQueens(3), 0)

    def test_medium_cases(self):
        self.assertEqual(self.solution.totalNQueens(5), 10)
        self.assertEqual(self.solution.totalNQueens(6), 4)
        self.assertEqual(self.solution.totalNQueens(7), 40)
        self.assertEqual(self.solution.totalNQueens(8), 92)

if __name__ == '__main__':
    unittest.main()