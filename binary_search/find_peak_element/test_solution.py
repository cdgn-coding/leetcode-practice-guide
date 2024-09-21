import unittest

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        pass

class TestFindPeakElement(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        nums = [1,2,3,1]
        self.assertEqual(self.solution.findPeakElement(nums), 2)

    def test_example_2(self):
        nums = [1,2,1,3,5,6,4]
        result = self.solution.findPeakElement(nums)
        self.assertIn(result, [1, 5])

    def test_single_element(self):
        nums = [1]
        self.assertEqual(self.solution.findPeakElement(nums), 0)

    def test_two_elements_ascending(self):
        nums = [1, 2]
        self.assertEqual(self.solution.findPeakElement(nums), 1)

    def test_two_elements_descending(self):
        nums = [2, 1]
        self.assertEqual(self.solution.findPeakElement(nums), 0)

    def test_all_ascending(self):
        nums = [1, 2, 3, 4, 5]
        self.assertEqual(self.solution.findPeakElement(nums), 4)

    def test_all_descending(self):
        nums = [5, 4, 3, 2, 1]
        self.assertEqual(self.solution.findPeakElement(nums), 0)

    def test_peak_in_middle(self):
        nums = [1, 2, 3, 4, 3, 2, 1]
        self.assertEqual(self.solution.findPeakElement(nums), 3)

    def test_multiple_peaks(self):
        nums = [1, 3, 2, 4, 1, 5, 2]
        result = self.solution.findPeakElement(nums)
        self.assertIn(result, [1, 3, 5])

    def test_edge_case_min_max(self):
        nums = [-2**31, 2**31 - 1]
        self.assertEqual(self.solution.findPeakElement(nums), 1)

if __name__ == '__main__':
    unittest.main()