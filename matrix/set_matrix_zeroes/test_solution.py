import unittest

class Solution:
    def setZeroes(self, matrix):
        pass

class TestSetZeroes(unittest.TestCase):
    def test_example_1(self):
        solution = Solution()
        matrix = [[1,1,1],[1,0,1],[1,1,1]]
        solution.setZeroes(matrix)
        self.assertEqual(matrix, [[1,0,1],[0,0,0],[1,0,1]])

    def test_example_2(self):
        solution = Solution()
        matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
        solution.setZeroes(matrix)
        self.assertEqual(matrix, [[0,0,0,0],[0,4,5,0],[0,3,1,0]])

    def test_single_element(self):
        solution = Solution()
        matrix = [[0]]
        solution.setZeroes(matrix)
        self.assertEqual(matrix, [[0]])

    def test_no_zeros(self):
        solution = Solution()
        matrix = [[1,2,3],[4,5,6],[7,8,9]]
        solution.setZeroes(matrix)
        self.assertEqual(matrix, [[1,2,3],[4,5,6],[7,8,9]])

    def test_all_zeros(self):
        solution = Solution()
        matrix = [[0,0,0],[0,0,0],[0,0,0]]
        solution.setZeroes(matrix)
        self.assertEqual(matrix, [[0,0,0],[0,0,0],[0,0,0]])

    def test_rectangular_matrix(self):
        solution = Solution()
        matrix = [[1,2,3,4],[5,0,7,8],[9,10,11,12],[13,14,15,0]]
        solution.setZeroes(matrix)
        self.assertEqual(matrix, [[1,0,3,0],[0,0,0,0],[9,0,11,0],[0,0,0,0]])

if __name__ == '__main__':
    unittest.main()