import unittest

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        pass

class TestMedianSortedArrays(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        nums1 = [1, 3]
        nums2 = [2]
        self.assertAlmostEqual(self.solution.findMedianSortedArrays(nums1, nums2), 2.00000, places=5)

    def test_example2(self):
        nums1 = [1, 2]
        nums2 = [3, 4]
        self.assertAlmostEqual(self.solution.findMedianSortedArrays(nums1, nums2), 2.50000, places=5)

    def test_empty_arrays(self):
        nums1 = []
        nums2 = [1]
        self.assertAlmostEqual(self.solution.findMedianSortedArrays(nums1, nums2), 1.00000, places=5)

    def test_single_element_arrays(self):
        nums1 = [1]
        nums2 = [2]
        self.assertAlmostEqual(self.solution.findMedianSortedArrays(nums1, nums2), 1.50000, places=5)

    def test_different_length_arrays(self):
        nums1 = [1, 2, 3, 4, 5]
        nums2 = [6, 7, 8]
        self.assertAlmostEqual(self.solution.findMedianSortedArrays(nums1, nums2), 4.50000, places=5)

    def test_negative_numbers(self):
        nums1 = [-5, -3, -1]
        nums2 = [-2, 0, 2]
        self.assertAlmostEqual(self.solution.findMedianSortedArrays(nums1, nums2), -1.50000, places=5)

    def test_large_numbers(self):
        nums1 = [100000, 200000]
        nums2 = [300000, 400000]
        self.assertAlmostEqual(self.solution.findMedianSortedArrays(nums1, nums2), 250000.00000, places=5)

    def test_same_numbers(self):
        nums1 = [1, 1, 1]
        nums2 = [1, 1, 1]
        self.assertAlmostEqual(self.solution.findMedianSortedArrays(nums1, nums2), 1.00000, places=5)

if __name__ == '__main__':
    unittest.main()