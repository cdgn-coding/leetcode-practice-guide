import unittest

class Solution:
    def summaryRanges(self, nums):
        pass

class TestSummaryRanges(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        nums = [0, 1, 2, 4, 5, 7]
        expected = ["0->2", "4->5", "7"]
        self.assertEqual(self.solution.summaryRanges(nums), expected)

    def test_example2(self):
        nums = [0, 2, 3, 4, 6, 8, 9]
        expected = ["0", "2->4", "6", "8->9"]
        self.assertEqual(self.solution.summaryRanges(nums), expected)

    def test_empty_array(self):
        nums = []
        expected = []
        self.assertEqual(self.solution.summaryRanges(nums), expected)

    def test_single_element(self):
        nums = [1]
        expected = ["1"]
        self.assertEqual(self.solution.summaryRanges(nums), expected)

    def test_all_consecutive(self):
        nums = [1, 2, 3, 4, 5]
        expected = ["1->5"]
        self.assertEqual(self.solution.summaryRanges(nums), expected)

    def test_no_ranges(self):
        nums = [1, 3, 5, 7, 9]
        expected = ["1", "3", "5", "7", "9"]
        self.assertEqual(self.solution.summaryRanges(nums), expected)

    def test_negative_numbers(self):
        nums = [-5, -4, -3, -1, 0, 2, 4, 6, 8, 9]
        expected = ["-5->-3", "-1->0", "2", "4", "6", "8->9"]
        self.assertEqual(self.solution.summaryRanges(nums), expected)

    def test_large_numbers(self):
        nums = [100, 101, 102, 150, 200, 201, 202, 203, 300]
        expected = ["100->102", "150", "200->203", "300"]
        self.assertEqual(self.solution.summaryRanges(nums), expected)

if __name__ == '__main__':
    unittest.main()