import unittest

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        pass

class TestRotatedSortedArraySearch(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        nums = [4, 5, 6, 7, 0, 1, 2]
        target = 0
        self.assertEqual(self.solution.search(nums, target), 4)

    def test_example_2(self):
        nums = [4, 5, 6, 7, 0, 1, 2]
        target = 3
        self.assertEqual(self.solution.search(nums, target), -1)

    def test_example_3(self):
        nums = [1]
        target = 0
        self.assertEqual(self.solution.search(nums, target), -1)

    def test_target_at_start(self):
        nums = [5, 1, 2, 3, 4]
        target = 5
        self.assertEqual(self.solution.search(nums, target), 0)

    def test_target_at_end(self):
        nums = [3, 4, 5, 1, 2]
        target = 2
        self.assertEqual(self.solution.search(nums, target), 4)

    def test_no_rotation(self):
        nums = [1, 2, 3, 4, 5]
        target = 3
        self.assertEqual(self.solution.search(nums, target), 2)

    def test_full_rotation(self):
        nums = [1, 2, 3, 4, 5]
        target = 1
        self.assertEqual(self.solution.search(nums, target), 0)

    def test_large_array(self):
        nums = list(range(1000, 5000)) + list(range(0, 1000))
        target = 4999
        self.assertEqual(self.solution.search(nums, target), 3999)

    def test_negative_numbers(self):
        nums = [-3, -2, -1, 0, 1, 2]
        target = -2
        self.assertEqual(self.solution.search(nums, target), 1)

    def test_all_negative_numbers(self):
        nums = [-5, -4, -3, -2, -1]
        target = -3
        self.assertEqual(self.solution.search(nums, target), 2)

if __name__ == '__main__':
    unittest.main()