import unittest

class TestMinArrowShots(unittest.TestCase):
    def test_example_1(self):
        points = [[10,16],[2,8],[1,6],[7,12]]
        self.assertEqual(Solution().findMinArrowShots(points), 2)

    def test_example_2(self):
        points = [[1,2],[3,4],[5,6],[7,8]]
        self.assertEqual(Solution().findMinArrowShots(points), 4)

    def test_example_3(self):
        points = [[1,2],[2,3],[3,4],[4,5]]
        self.assertEqual(Solution().findMinArrowShots(points), 2)

    def test_single_balloon(self):
        points = [[1,5]]
        self.assertEqual(Solution().findMinArrowShots(points), 1)

    def test_overlapping_balloons(self):
        points = [[1,5],[2,4],[3,6]]
        self.assertEqual(Solution().findMinArrowShots(points), 1)

    def test_non_overlapping_balloons(self):
        points = [[1,2],[4,5],[7,8]]
        self.assertEqual(Solution().findMinArrowShots(points), 3)

    def test_large_numbers(self):
        points = [[-2147483648,2147483647]]
        self.assertEqual(Solution().findMinArrowShots(points), 1)

    def test_maximum_balloons(self):
        points = [[i, i+1] for i in range(100000)]
        self.assertEqual(Solution().findMinArrowShots(points), 100000)

if __name__ == '__main__':
    unittest.main()