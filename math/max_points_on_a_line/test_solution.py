import unittest

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        pass

class TestMaxPoints(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        points = [[1,1],[2,2],[3,3]]
        self.assertEqual(self.solution.maxPoints(points), 3)

    def test_example2(self):
        points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
        self.assertEqual(self.solution.maxPoints(points), 4)

    def test_single_point(self):
        points = [[1,1]]
        self.assertEqual(self.solution.maxPoints(points), 1)

    def test_two_points(self):
        points = [[1,1], [2,2]]
        self.assertEqual(self.solution.maxPoints(points), 2)

    def test_vertical_line(self):
        points = [[1,1], [1,2], [1,3], [1,4]]
        self.assertEqual(self.solution.maxPoints(points), 4)

    def test_horizontal_line(self):
        points = [[1,1], [2,1], [3,1], [4,1]]
        self.assertEqual(self.solution.maxPoints(points), 4)

    def test_all_same_point(self):
        points = [[1,1], [1,1], [1,1]]
        self.assertEqual(self.solution.maxPoints(points), 3)

    def test_no_three_points_in_line(self):
        points = [[1,1], [2,2], [3,4], [4,5], [5,6], [7,8]]
        self.assertEqual(self.solution.maxPoints(points), 2)

    def test_negative_coordinates(self):
        points = [[-1,-1], [-2,-2], [-3,-3], [1,1], [2,2], [3,3]]
        self.assertEqual(self.solution.maxPoints(points), 6)

    def test_large_coordinates(self):
        points = [[10000,10000], [20000,20000], [30000,30000]]
        self.assertEqual(self.solution.maxPoints(points), 3)

if __name__ == '__main__':
    unittest.main()