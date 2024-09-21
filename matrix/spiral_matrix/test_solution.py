import unittest
from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        pass

class TestSpiralOrder(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        matrix = [[1,2,3],[4,5,6],[7,8,9]]
        expected = [1,2,3,6,9,8,7,4,5]
        self.assertEqual(self.solution.spiralOrder(matrix), expected)

    def test_example2(self):
        matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
        expected = [1,2,3,4,8,12,11,10,9,5,6,7]
        self.assertEqual(self.solution.spiralOrder(matrix), expected)

    def test_single_row(self):
        matrix = [[1,2,3,4]]
        expected = [1,2,3,4]
        self.assertEqual(self.solution.spiralOrder(matrix), expected)

    def test_single_column(self):
        matrix = [[1],[2],[3],[4]]
        expected = [1,2,3,4]
        self.assertEqual(self.solution.spiralOrder(matrix), expected)

    def test_single_element(self):
        matrix = [[1]]
        expected = [1]
        self.assertEqual(self.solution.spiralOrder(matrix), expected)

    def test_empty_matrix(self):
        matrix = []
        expected = []
        self.assertEqual(self.solution.spiralOrder(matrix), expected)

    def test_large_matrix(self):
        matrix = [
            [1, 2, 3, 4, 5],
            [6, 7, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 17, 18, 19, 20],
            [21, 22, 23, 24, 25]
        ]
        expected = [1,2,3,4,5,10,15,20,25,24,23,22,21,16,11,6,7,8,9,14,19,18,17,12,13]
        self.assertEqual(self.solution.spiralOrder(matrix), expected)

    def test_negative_numbers(self):
        matrix = [[-1,-2,-3],[-4,-5,-6],[-7,-8,-9]]
        expected = [-1,-2,-3,-6,-9,-8,-7,-4,-5]
        self.assertEqual(self.solution.spiralOrder(matrix), expected)

if __name__ == '__main__':
    unittest.main()