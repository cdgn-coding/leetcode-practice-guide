import unittest

class TestSearchMatrix(unittest.TestCase):
    def test_example_1(self):
        matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
        target = 3
        self.assertTrue(Solution().searchMatrix(matrix, target))

    def test_example_2(self):
        matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
        target = 13
        self.assertFalse(Solution().searchMatrix(matrix, target))

    def test_single_element_matrix(self):
        matrix = [[1]]
        target = 1
        self.assertTrue(Solution().searchMatrix(matrix, target))

    def test_target_not_in_matrix(self):
        matrix = [[1,3,5],[7,9,11]]
        target = 6
        self.assertFalse(Solution().searchMatrix(matrix, target))

    def test_target_greater_than_max(self):
        matrix = [[1,3,5],[7,9,11]]
        target = 12
        self.assertFalse(Solution().searchMatrix(matrix, target))

    def test_target_less_than_min(self):
        matrix = [[1,3,5],[7,9,11]]
        target = 0
        self.assertFalse(Solution().searchMatrix(matrix, target))

    def test_large_matrix(self):
        matrix = [[i*100 + j for j in range(100)] for i in range(100)]
        target = 9999
        self.assertTrue(Solution().searchMatrix(matrix, target))

    def test_negative_numbers(self):
        matrix = [[-10,-8,-6],[-5,-3,-1],[0,2,4]]
        target = -3
        self.assertTrue(Solution().searchMatrix(matrix, target))

if __name__ == '__main__':
    unittest.main()