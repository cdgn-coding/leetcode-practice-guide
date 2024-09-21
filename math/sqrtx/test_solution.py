import unittest

class Solution:
    def mySqrt(self, x: int) -> int:
        pass

class TestSqrtCalculation(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_sqrt_of_zero(self):
        self.assertEqual(self.solution.mySqrt(0), 0)

    def test_sqrt_of_one(self):
        self.assertEqual(self.solution.mySqrt(1), 1)

    def test_sqrt_of_four(self):
        self.assertEqual(self.solution.mySqrt(4), 2)

    def test_sqrt_of_eight(self):
        self.assertEqual(self.solution.mySqrt(8), 2)

    def test_sqrt_of_nine(self):
        self.assertEqual(self.solution.mySqrt(9), 3)

    def test_sqrt_of_fifteen(self):
        self.assertEqual(self.solution.mySqrt(15), 3)

    def test_sqrt_of_sixteen(self):
        self.assertEqual(self.solution.mySqrt(16), 4)

    def test_sqrt_of_large_number(self):
        self.assertEqual(self.solution.mySqrt(2147395600), 46340)

    def test_sqrt_of_max_input(self):
        self.assertEqual(self.solution.mySqrt(2**31 - 1), 46340)

if __name__ == '__main__':
    unittest.main()