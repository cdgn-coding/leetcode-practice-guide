import unittest

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        pass

class TestMinimumTotal(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
        self.assertEqual(self.solution.minimumTotal(triangle), 11)

    def test_example_2(self):
        triangle = [[-10]]
        self.assertEqual(self.solution.minimumTotal(triangle), -10)

    def test_single_row(self):
        triangle = [[1]]
        self.assertEqual(self.solution.minimumTotal(triangle), 1)

    def test_two_rows(self):
        triangle = [[1],[2,3]]
        self.assertEqual(self.solution.minimumTotal(triangle), 3)

    def test_negative_values(self):
        triangle = [[1],[-5,-2],[3,6,1],[-1,2,4,-3]]
        self.assertEqual(self.solution.minimumTotal(triangle), -6)

    def test_large_triangle(self):
        triangle = [[1]] + [[i]*i for i in range(2, 201)]
        self.assertEqual(self.solution.minimumTotal(triangle), 200)

    def test_max_constraint(self):
        triangle = [[10000]] + [[10000]*i for i in range(2, 201)]
        self.assertEqual(self.solution.minimumTotal(triangle), 2000000)

    def test_min_constraint(self):
        triangle = [[-10000]] + [[-10000]*i for i in range(2, 201)]
        self.assertEqual(self.solution.minimumTotal(triangle), -2000000)

if __name__ == '__main__':
    unittest.main()