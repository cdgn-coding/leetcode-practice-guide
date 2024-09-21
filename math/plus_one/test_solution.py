import unittest

class Solution:
    def plusOne(self, digits):
        pass

class TestPlusOne(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        self.assertEqual(self.solution.plusOne([1, 2, 3]), [1, 2, 4])

    def test_example2(self):
        self.assertEqual(self.solution.plusOne([4, 3, 2, 1]), [4, 3, 2, 2])

    def test_example3(self):
        self.assertEqual(self.solution.plusOne([9]), [1, 0])

    def test_single_digit(self):
        self.assertEqual(self.solution.plusOne([0]), [1])

    def test_all_nines(self):
        self.assertEqual(self.solution.plusOne([9, 9, 9]), [1, 0, 0, 0])

    def test_no_carry(self):
        self.assertEqual(self.solution.plusOne([1, 2, 3, 4]), [1, 2, 3, 5])

    def test_multiple_carries(self):
        self.assertEqual(self.solution.plusOne([2, 9, 9]), [3, 0, 0])

    def test_large_number(self):
        self.assertEqual(self.solution.plusOne([9, 8, 7, 6, 5, 4, 3, 2, 1, 0]), [9, 8, 7, 6, 5, 4, 3, 2, 1, 1])

if __name__ == '__main__':
    unittest.main()