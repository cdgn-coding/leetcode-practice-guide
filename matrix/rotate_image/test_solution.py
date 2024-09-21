import unittest

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        pass

class TestRotateImage(unittest.TestCase):
    def test_example_1(self):
        matrix = [[1,2,3],[4,5,6],[7,8,9]]
        expected = [[7,4,1],[8,5,2],[9,6,3]]
        Solution().rotate(matrix)
        self.assertEqual(matrix, expected)

    def test_example_2(self):
        matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
        expected = [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
        Solution().rotate(matrix)
        self.assertEqual(matrix, expected)

    def test_single_element(self):
        matrix = [[1]]
        expected = [[1]]
        Solution().rotate(matrix)
        self.assertEqual(matrix, expected)

    def test_2x2_matrix(self):
        matrix = [[1,2],[3,4]]
        expected = [[3,1],[4,2]]
        Solution().rotate(matrix)
        self.assertEqual(matrix, expected)

    def test_large_matrix(self):
        matrix = [[i+j*20 for i in range(20)] for j in range(20)]
        expected = [list(reversed([matrix[i][j] for i in range(20)])) for j in range(20)]
        Solution().rotate(matrix)
        self.assertEqual(matrix, expected)

    def test_negative_values(self):
        matrix = [[-1,-2,-3],[-4,-5,-6],[-7,-8,-9]]
        expected = [[-7,-4,-1],[-8,-5,-2],[-9,-6,-3]]
        Solution().rotate(matrix)
        self.assertEqual(matrix, expected)

if __name__ == '__main__':
    unittest.main()