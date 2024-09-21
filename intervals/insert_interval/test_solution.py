import unittest

class Solution:
    def insert(self, intervals, newInterval):
        pass

class TestInsertInterval(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        intervals = [[1,3],[6,9]]
        newInterval = [2,5]
        expected = [[1,5],[6,9]]
        self.assertEqual(self.solution.insert(intervals, newInterval), expected)

    def test_example_2(self):
        intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
        newInterval = [4,8]
        expected = [[1,2],[3,10],[12,16]]
        self.assertEqual(self.solution.insert(intervals, newInterval), expected)

    def test_empty_intervals(self):
        intervals = []
        newInterval = [5,7]
        expected = [[5,7]]
        self.assertEqual(self.solution.insert(intervals, newInterval), expected)

    def test_non_overlapping_insert_start(self):
        intervals = [[3,5],[6,9]]
        newInterval = [1,2]
        expected = [[1,2],[3,5],[6,9]]
        self.assertEqual(self.solution.insert(intervals, newInterval), expected)

    def test_non_overlapping_insert_end(self):
        intervals = [[1,2],[3,5]]
        newInterval = [6,8]
        expected = [[1,2],[3,5],[6,8]]
        self.assertEqual(self.solution.insert(intervals, newInterval), expected)

    def test_overlapping_multiple_intervals(self):
        intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
        newInterval = [4,9]
        expected = [[1,2],[3,10],[12,16]]
        self.assertEqual(self.solution.insert(intervals, newInterval), expected)

    def test_completely_overlapping_interval(self):
        intervals = [[1,5]]
        newInterval = [2,3]
        expected = [[1,5]]
        self.assertEqual(self.solution.insert(intervals, newInterval), expected)

    def test_large_intervals(self):
        intervals = [[1,2],[3,4],[5,6],[7,8],[9,10]] * 2000
        newInterval = [0,100000]
        expected = [[0,100000]]
        self.assertEqual(self.solution.insert(intervals, newInterval), expected)

if __name__ == '__main__':
    unittest.main()