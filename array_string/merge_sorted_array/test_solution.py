import unittest

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        pass

class TestMerge(unittest.TestCase):
    def test_example1(self):
        nums1 = [1,2,3,0,0,0]
        m = 3
        nums2 = [2,5,6]
        n = 3
        expected = [1,2,2,3,5,6]
        Solution().merge(nums1, m, nums2, n)
        self.assertEqual(nums1, expected)

    def test_example2(self):
        nums1 = [1]
        m = 1
        nums2 = []
        n = 0
        expected = [1]
        Solution().merge(nums1, m, nums2, n)
        self.assertEqual(nums1, expected)

    def test_example3(self):
        nums1 = [0]
        m = 0
        nums2 = [1]
        n = 1
        expected = [1]
        Solution().merge(nums1, m, nums2, n)
        self.assertEqual(nums1, expected)

    def test_empty_nums1(self):
        nums1 = []
        m = 0
        nums2 = [1,2,3]
        n = 3
        expected = [1,2,3]
        Solution().merge(nums1, m, nums2, n)
        self.assertEqual(nums1, expected)

    def test_empty_nums2(self):
        nums1 = [1,2,3]
        m = 3
        nums2 = []
        n = 0
        expected = [1,2,3]
        Solution().merge(nums1, m, nums2, n)
        self.assertEqual(nums1, expected)

if __name__ == '__main__':
    unittest.main()