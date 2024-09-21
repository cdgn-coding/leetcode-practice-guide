import unittest

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        pass

class TestSingleNumber(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        nums = [2,2,3,2]
        self.assertEqual(self.solution.singleNumber(nums), 3)

    def test_example_2(self):
        nums = [0,1,0,1,0,1,99]
        self.assertEqual(self.solution.singleNumber(nums), 99)

    def test_single_element(self):
        nums = [1]
        self.assertEqual(self.solution.singleNumber(nums), 1)

    def test_negative_numbers(self):
        nums = [-2,-2,1,1,4,1,-2]
        self.assertEqual(self.solution.singleNumber(nums), 4)

    def test_large_numbers(self):
        nums = [2147483647, 2147483647, 2147483647, 0]
        self.assertEqual(self.solution.singleNumber(nums), 0)

    def test_all_same_except_one(self):
        nums = [5,5,5,5,5,5,5,5,5,3]
        self.assertEqual(self.solution.singleNumber(nums), 3)

if __name__ == '__main__':
    unittest.main()