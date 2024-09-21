import unittest

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        pass

class TestSingleNumber(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        nums = [2,2,1]
        self.assertEqual(self.solution.singleNumber(nums), 1)

    def test_example_2(self):
        nums = [4,1,2,1,2]
        self.assertEqual(self.solution.singleNumber(nums), 4)

    def test_example_3(self):
        nums = [1]
        self.assertEqual(self.solution.singleNumber(nums), 1)

    def test_single_negative_number(self):
        nums = [-1]
        self.assertEqual(self.solution.singleNumber(nums), -1)

    def test_multiple_numbers(self):
        nums = [1,1,2,2,3,3,4,4,5]
        self.assertEqual(self.solution.singleNumber(nums), 5)

    def test_large_range(self):
        nums = [i for i in range(-30000, 30001) for _ in range(2)]
        nums.append(30001)
        self.assertEqual(self.solution.singleNumber(nums), 30001)

    def test_all_negative_numbers(self):
        nums = [-1,-1,-2,-2,-3]
        self.assertEqual(self.solution.singleNumber(nums), -3)

if __name__ == '__main__':
    unittest.main()