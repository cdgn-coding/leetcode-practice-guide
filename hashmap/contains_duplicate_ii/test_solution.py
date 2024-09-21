import unittest

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        pass

class TestContainsNearbyDuplicate(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        nums = [1,2,3,1]
        k = 3
        self.assertTrue(self.solution.containsNearbyDuplicate(nums, k))

    def test_example_2(self):
        nums = [1,0,1,1]
        k = 1
        self.assertTrue(self.solution.containsNearbyDuplicate(nums, k))

    def test_example_3(self):
        nums = [1,2,3,1,2,3]
        k = 2
        self.assertFalse(self.solution.containsNearbyDuplicate(nums, k))

    def test_empty_array(self):
        nums = []
        k = 0
        self.assertFalse(self.solution.containsNearbyDuplicate(nums, k))

    def test_single_element(self):
        nums = [1]
        k = 0
        self.assertFalse(self.solution.containsNearbyDuplicate(nums, k))

    def test_all_same_elements(self):
        nums = [1,1,1,1,1]
        k = 3
        self.assertTrue(self.solution.containsNearbyDuplicate(nums, k))

    def test_no_duplicates(self):
        nums = [1,2,3,4,5]
        k = 2
        self.assertFalse(self.solution.containsNearbyDuplicate(nums, k))

    def test_duplicates_beyond_k(self):
        nums = [1,2,3,4,1]
        k = 3
        self.assertFalse(self.solution.containsNearbyDuplicate(nums, k))

    def test_large_array(self):
        nums = list(range(100000)) + [0]
        k = 100000
        self.assertTrue(self.solution.containsNearbyDuplicate(nums, k))

    def test_negative_numbers(self):
        nums = [-1,-2,-3,-1]
        k = 3
        self.assertTrue(self.solution.containsNearbyDuplicate(nums, k))

if __name__ == '__main__':
    unittest.main()