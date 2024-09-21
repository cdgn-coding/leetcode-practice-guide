import unittest

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        pass

class TestSearchRange(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        nums = [5,7,7,8,8,10]
        target = 8
        expected = [3,4]
        self.assertEqual(self.solution.searchRange(nums, target), expected)

    def test_example2(self):
        nums = [5,7,7,8,8,10]
        target = 6
        expected = [-1,-1]
        self.assertEqual(self.solution.searchRange(nums, target), expected)

    def test_example3(self):
        nums = []
        target = 0
        expected = [-1,-1]
        self.assertEqual(self.solution.searchRange(nums, target), expected)

    def test_single_element(self):
        nums = [1]
        target = 1
        expected = [0,0]
        self.assertEqual(self.solution.searchRange(nums, target), expected)

    def test_all_same_elements(self):
        nums = [5,5,5,5,5]
        target = 5
        expected = [0,4]
        self.assertEqual(self.solution.searchRange(nums, target), expected)

    def test_target_at_beginning(self):
        nums = [1,2,3,4,5]
        target = 1
        expected = [0,0]
        self.assertEqual(self.solution.searchRange(nums, target), expected)

    def test_target_at_end(self):
        nums = [1,2,3,4,5]
        target = 5
        expected = [4,4]
        self.assertEqual(self.solution.searchRange(nums, target), expected)

    def test_target_not_in_array(self):
        nums = [1,2,3,4,5]
        target = 6
        expected = [-1,-1]
        self.assertEqual(self.solution.searchRange(nums, target), expected)

if __name__ == '__main__':
    unittest.main()