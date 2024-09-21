import unittest

class Solution:
    def rob(self, nums: List[int]) -> int:
        pass

class TestHouseRobber(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        nums = [1,2,3,1]
        self.assertEqual(self.solution.rob(nums), 4)

    def test_example2(self):
        nums = [2,7,9,3,1]
        self.assertEqual(self.solution.rob(nums), 12)

    def test_empty_list(self):
        nums = []
        self.assertEqual(self.solution.rob(nums), 0)

    def test_single_house(self):
        nums = [5]
        self.assertEqual(self.solution.rob(nums), 5)

    def test_two_houses(self):
        nums = [3,1]
        self.assertEqual(self.solution.rob(nums), 3)

    def test_all_same_values(self):
        nums = [2,2,2,2]
        self.assertEqual(self.solution.rob(nums), 4)

    def test_alternating_high_low(self):
        nums = [10,1,10,1,10]
        self.assertEqual(self.solution.rob(nums), 30)

    def test_increasing_sequence(self):
        nums = [1,2,3,4,5]
        self.assertEqual(self.solution.rob(nums), 9)

    def test_decreasing_sequence(self):
        nums = [5,4,3,2,1]
        self.assertEqual(self.solution.rob(nums), 9)

    def test_max_constraint(self):
        nums = [400] * 100
        self.assertEqual(self.solution.rob(nums), 20000)

if __name__ == '__main__':
    unittest.main()