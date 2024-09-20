import unittest

class TestRemoveDuplicates(unittest.TestCase):
    def test_example1(self):
        nums = [1, 1, 1, 2, 2, 3]
        expectedNums = [1, 1, 2, 2, 3]
        k = removeDuplicates(nums)
        self.assertEqual(k, len(expectedNums))
        for i in range(k):
            self.assertEqual(nums[i], expectedNums[i])

    def test_example2(self):
        nums = [0, 0, 1, 1, 1, 1, 2, 3, 3]
        expectedNums = [0, 0, 1, 1, 2, 3, 3]
        k = removeDuplicates(nums)
        self.assertEqual(k, len(expectedNums))
        for i in range(k):
            self.assertEqual(nums[i], expectedNums[i])

    def test_single_element(self):
        nums = [1]
        expectedNums = [1]
        k = removeDuplicates(nums)
        self.assertEqual(k, len(expectedNums))
        for i in range(k):
            self.assertEqual(nums[i], expectedNums[i])

    def test_all_duplicates(self):
        nums = [1, 1, 1, 1, 1]
        expectedNums = [1, 1]
        k = removeDuplicates(nums)
        self.assertEqual(k, len(expectedNums))
        for i in range(k):
            self.assertEqual(nums[i], expectedNums[i])

    def test_no_duplicates(self):
        nums = [1, 2, 3, 4, 5]
        expectedNums = [1, 2, 3, 4, 5]
        k = removeDuplicates(nums)
        self.assertEqual(k, len(expectedNums))
        for i in range(k):
            self.assertEqual(nums[i], expectedNums[i])

if __name__ == '__main__':
    unittest.main()