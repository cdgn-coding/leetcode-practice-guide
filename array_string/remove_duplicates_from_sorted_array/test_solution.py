import unittest

class TestSolution(unittest.TestCase):
    def test_removeDuplicates(self):
        solution = Solution()

        nums = [1, 1, 2]
        expectedNums = [1, 2]
        k = solution.removeDuplicates(nums)
        self.assertEqual(k, len(expectedNums))
        for i in range(k):
            self.assertEqual(nums[i], expectedNums[i])

        nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
        expectedNums = [0, 1, 2, 3, 4]
        k = solution.removeDuplicates(nums)
        self.assertEqual(k, len(expectedNums))
        for i in range(k):
            self.assertEqual(nums[i], expectedNums[i])

        nums = [1]
        expectedNums = [1]
        k = solution.removeDuplicates(nums)
        self.assertEqual(k, len(expectedNums))
        for i in range(k):
            self.assertEqual(nums[i], expectedNums[i])

        nums = []
        expectedNums = []
        k = solution.removeDuplicates(nums)
        self.assertEqual(k, len(expectedNums))

if __name__ == '__main__':
    unittest.main()