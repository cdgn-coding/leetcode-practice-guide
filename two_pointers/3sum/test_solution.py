import unittest

class Solution:
    def threeSum(self, nums):
        pass

class TestThreeSum(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        nums = [-1,0,1,2,-1,-4]
        expected = [[-1,-1,2],[-1,0,1]]
        result = self.solution.threeSum(nums)
        self.assertCountEqual(result, expected)

    def test_example2(self):
        nums = [0,1,1]
        expected = []
        result = self.solution.threeSum(nums)
        self.assertEqual(result, expected)

    def test_example3(self):
        nums = [0,0,0]
        expected = [[0,0,0]]
        result = self.solution.threeSum(nums)
        self.assertEqual(result, expected)

    def test_empty_input(self):
        nums = []
        expected = []
        result = self.solution.threeSum(nums)
        self.assertEqual(result, expected)

    def test_no_solution(self):
        nums = [1,2,3,4,5]
        expected = []
        result = self.solution.threeSum(nums)
        self.assertEqual(result, expected)

    def test_multiple_solutions(self):
        nums = [-1,0,1,2,-1,-4,-2,-3,3,0,4]
        expected = [[-4,0,4],[-4,1,3],[-3,-1,4],[-3,0,3],[-3,1,2],[-2,-1,3],[-2,0,2],[-1,-1,2],[-1,0,1]]
        result = self.solution.threeSum(nums)
        self.assertCountEqual(result, expected)

    def test_duplicate_numbers(self):
        nums = [-2,0,0,2,2]
        expected = [[-2,0,2]]
        result = self.solution.threeSum(nums)
        self.assertCountEqual(result, expected)

    def test_all_negative(self):
        nums = [-1,-2,-3,-4,-5]
        expected = []
        result = self.solution.threeSum(nums)
        self.assertEqual(result, expected)

    def test_all_positive(self):
        nums = [1,2,3,4,5]
        expected = []
        result = self.solution.threeSum(nums)
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()