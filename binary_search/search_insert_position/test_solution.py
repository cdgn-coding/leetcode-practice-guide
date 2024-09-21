import unittest

class Solution:
    def searchInsert(self, nums, target):
        pass

class TestSearchInsert(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        nums = [1, 3, 5, 6]
        target = 5
        self.assertEqual(self.solution.searchInsert(nums, target), 2)

    def test_example_2(self):
        nums = [1, 3, 5, 6]
        target = 2
        self.assertEqual(self.solution.searchInsert(nums, target), 1)

    def test_example_3(self):
        nums = [1, 3, 5, 6]
        target = 7
        self.assertEqual(self.solution.searchInsert(nums, target), 4)

    def test_target_at_beginning(self):
        nums = [1, 3, 5, 6]
        target = 0
        self.assertEqual(self.solution.searchInsert(nums, target), 0)

    def test_target_at_end(self):
        nums = [1, 3, 5, 6]
        target = 8
        self.assertEqual(self.solution.searchInsert(nums, target), 4)

    def test_single_element_array(self):
        nums = [1]
        target = 1
        self.assertEqual(self.solution.searchInsert(nums, target), 0)

    def test_single_element_array_insert(self):
        nums = [1]
        target = 2
        self.assertEqual(self.solution.searchInsert(nums, target), 1)

    def test_large_array(self):
        nums = list(range(0, 10000, 2))
        target = 9999
        self.assertEqual(self.solution.searchInsert(nums, target), 5000)

    def test_negative_numbers(self):
        nums = [-3, -1, 0, 2, 4]
        target = -2
        self.assertEqual(self.solution.searchInsert(nums, target), 1)

if __name__ == '__main__':
    unittest.main()