import unittest

from intervals.summary_ranges.solution import Solution


class SolutionTest(unittest.TestCase):
    def test_contiguous_intervals(self):
        sol = Solution()
        actual = sol.summaryRanges([1,2,3,4,5])
        self.assertEqual(["1->5"], actual)

    def test_non_contiguous_intervals(self):
        sol = Solution()
        actual = sol.summaryRanges([1,3,4])
        self.assertEqual(["1", "3->4"], actual)

    def test_empty(self):
        sol = Solution()
        actual = sol.summaryRanges([])
        self.assertEqual(actual, [])

    def test_mixed_cases(self):
        sol = Solution()
        actual = sol.summaryRanges([0,1,2,4,5,7])
        self.assertEqual(["0->2","4->5","7"], actual)


if __name__ == '__main__':
    unittest.main()
