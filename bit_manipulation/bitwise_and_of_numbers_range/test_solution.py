import unittest

class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        pass

class TestRangeBitwiseAnd(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.rangeBitwiseAnd(5, 7), 4)

    def test_example_2(self):
        self.assertEqual(self.solution.rangeBitwiseAnd(0, 0), 0)

    def test_example_3(self):
        self.assertEqual(self.solution.rangeBitwiseAnd(1, 2147483647), 0)

    def test_same_number(self):
        self.assertEqual(self.solution.rangeBitwiseAnd(10, 10), 10)

    def test_power_of_two(self):
        self.assertEqual(self.solution.rangeBitwiseAnd(8, 15), 8)

    def test_large_range(self):
        self.assertEqual(self.solution.rangeBitwiseAnd(1000000, 2000000), 983040)

    def test_zero_to_positive(self):
        self.assertEqual(self.solution.rangeBitwiseAnd(0, 100), 0)

    def test_all_ones(self):
        self.assertEqual(self.solution.rangeBitwiseAnd(255, 255), 255)

if __name__ == '__main__':
    unittest.main()