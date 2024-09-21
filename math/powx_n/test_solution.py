import unittest

class Solution:
    def myPow(self, x: float, n: int) -> float:
        pass

class TestMyPow(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertAlmostEqual(self.solution.myPow(2.00000, 10), 1024.00000, places=5)

    def test_example_2(self):
        self.assertAlmostEqual(self.solution.myPow(2.10000, 3), 9.26100, places=5)

    def test_example_3(self):
        self.assertAlmostEqual(self.solution.myPow(2.00000, -2), 0.25000, places=5)

    def test_zero_power(self):
        self.assertAlmostEqual(self.solution.myPow(5.0, 0), 1.0, places=5)

    def test_negative_base(self):
        self.assertAlmostEqual(self.solution.myPow(-2.0, 3), -8.0, places=5)

    def test_fractional_base(self):
        self.assertAlmostEqual(self.solution.myPow(0.5, 2), 0.25, places=5)

    def test_large_positive_power(self):
        self.assertAlmostEqual(self.solution.myPow(1.00001, 123456), 3.43804, places=5)

    def test_large_negative_power(self):
        self.assertAlmostEqual(self.solution.myPow(0.99999, -123456), 3.43822, places=5)

    def test_edge_case_min_n(self):
        self.assertAlmostEqual(self.solution.myPow(1.00000, -2**31), 1.0, places=5)

    def test_edge_case_max_n(self):
        self.assertAlmostEqual(self.solution.myPow(1.00000, 2**31 - 1), 1.0, places=5)

if __name__ == '__main__':
    unittest.main()