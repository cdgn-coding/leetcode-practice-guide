import unittest

class Solution:
    def merge(self, intervals):
        pass

class TestMergeIntervals(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        intervals = [[1,3],[2,6],[8,10],[15,18]]
        expected = [[1,6],[8,10],[15,18]]
        self.assertEqual(self.solution.merge(intervals), expected)

    def test_example_2(self):
        intervals = [[1,4],[4,5]]
        expected = [[1,5]]
        self.assertEqual(self.solution.merge(intervals), expected)

    def test_no_overlap(self):
        intervals = [[1,2],[3,4],[5,6]]
        expected = [[1,2],[3,4],[5,6]]
        self.assertEqual(self.solution.merge(intervals), expected)

    def test_complete_overlap(self):
        intervals = [[1,4],[2,3]]
        expected = [[1,4]]
        self.assertEqual(self.solution.merge(intervals), expected)

    def test_single_interval(self):
        intervals = [[1,2]]
        expected = [[1,2]]
        self.assertEqual(self.solution.merge(intervals), expected)

    def test_multiple_overlaps(self):
        intervals = [[1,4],[0,2],[3,5]]
        expected = [[0,5]]
        self.assertEqual(self.solution.merge(intervals), expected)

    def test_unsorted_intervals(self):
        intervals = [[2,6],[1,3],[8,10],[15,18]]
        expected = [[1,6],[8,10],[15,18]]
        self.assertEqual(self.solution.merge(intervals), expected)

if __name__ == '__main__':
    unittest.main()