import unittest

class Solution:
    def trailingZeroes(self, n: int) -> int:
        pass

class TestTrailingZeroes(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.trailingZeroes(3), 0)

    def test_example_2(self):
        self.assertEqual(self.solution.trailingZeroes(5), 1)

    def test_example_3(self):
        self.assertEqual(self.solution.trailingZeroes(0), 0)

    def test_large_number(self):
        self.assertEqual(self.solution.trailingZeroes(25), 6)

    def test_very_large_number(self):
        self.assertEqual(self.solution.trailingZeroes(10000), 2499)

    def test_edge_case_1(self):
        self.assertEqual(self.solution.trailingZeroes(1), 0)

    def test_edge_case_4(self):
        self.assertEqual(self.solution.trailingZeroes(4), 0)

    def test_edge_case_20(self):
        self.assertEqual(self.solution.trailingZeroes(20), 4)

    def test_edge_case_100(self):
        self.assertEqual(self.solution.trailingZeroes(100), 24)

if __name__ == '__main__':
    unittest.main()