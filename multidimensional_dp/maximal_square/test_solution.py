import unittest

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        pass

class TestMaximalSquare(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
        self.assertEqual(self.solution.maximalSquare(matrix), 4)

    def test_example2(self):
        matrix = [["0","1"],["1","0"]]
        self.assertEqual(self.solution.maximalSquare(matrix), 1)

    def test_example3(self):
        matrix = [["0"]]
        self.assertEqual(self.solution.maximalSquare(matrix), 0)

    def test_empty_matrix(self):
        matrix = []
        self.assertEqual(self.solution.maximalSquare(matrix), 0)

    def test_single_row(self):
        matrix = [["1","1","1","1"]]
        self.assertEqual(self.solution.maximalSquare(matrix), 1)

    def test_single_column(self):
        matrix = [["1"],["1"],["1"],["1"]]
        self.assertEqual(self.solution.maximalSquare(matrix), 1)

    def test_all_zeros(self):
        matrix = [["0","0","0"],["0","0","0"],["0","0","0"]]
        self.assertEqual(self.solution.maximalSquare(matrix), 0)

    def test_all_ones(self):
        matrix = [["1","1","1"],["1","1","1"],["1","1","1"]]
        self.assertEqual(self.solution.maximalSquare(matrix), 9)

    def test_large_matrix(self):
        matrix = [["1" for _ in range(300)] for _ in range(300)]
        self.assertEqual(self.solution.maximalSquare(matrix), 90000)

if __name__ == '__main__':
    unittest.main()