import unittest

class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        pass

class TestMinSubArrayLen(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        target = 7
        nums = [2,3,1,2,4,3]
        self.assertEqual(self.solution.minSubArrayLen(target, nums), 2)

    def test_example_2(self):
        target = 4
        nums = [1,4,4]
        self.assertEqual(self.solution.minSubArrayLen(target, nums), 1)

    def test_example_3(self):
        target = 11
        nums = [1,1,1,1,1,1,1,1]
        self.assertEqual(self.solution.minSubArrayLen(target, nums), 0)

    def test_single_element_equal_to_target(self):
        target = 5
        nums = [5]
        self.assertEqual(self.solution.minSubArrayLen(target, nums), 1)

    def test_single_element_less_than_target(self):
        target = 5
        nums = [4]
        self.assertEqual(self.solution.minSubArrayLen(target, nums), 0)

    def test_all_elements_sum_equal_to_target(self):
        target = 15
        nums = [1,2,3,4,5]
        self.assertEqual(self.solution.minSubArrayLen(target, nums), 5)

    def test_subarray_at_beginning(self):
        target = 6
        nums = [3,3,1,1,1,1,1]
        self.assertEqual(self.solution.minSubArrayLen(target, nums), 2)

    def test_subarray_at_end(self):
        target = 6
        nums = [1,1,1,1,1,3,3]
        self.assertEqual(self.solution.minSubArrayLen(target, nums), 2)

    def test_large_numbers(self):
        target = 1000000000
        nums = [1,1,1,1,1,1,1,1,1,1000000000]
        self.assertEqual(self.solution.minSubArrayLen(target, nums), 1)

if __name__ == '__main__':
    unittest.main()