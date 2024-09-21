import unittest

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        pass

class TestAddBinary(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.addBinary("11", "1"), "100")

    def test_example_2(self):
        self.assertEqual(self.solution.addBinary("1010", "1011"), "10101")

    def test_equal_length(self):
        self.assertEqual(self.solution.addBinary("1111", "1111"), "11110")

    def test_different_length(self):
        self.assertEqual(self.solution.addBinary("1", "1111"), "10000")

    def test_one_zero(self):
        self.assertEqual(self.solution.addBinary("0", "1111"), "1111")

    def test_both_zero(self):
        self.assertEqual(self.solution.addBinary("0", "0"), "0")

    def test_large_numbers(self):
        a = "1" * 10000
        b = "1"
        expected = "1" + "0" * 10000
        self.assertEqual(self.solution.addBinary(a, b), expected)

    def test_max_length(self):
        a = "1" * 10000
        b = "1" * 10000
        expected = "1" + "0" * 9999 + "0"
        self.assertEqual(self.solution.addBinary(a, b), expected)

if __name__ == '__main__':
    unittest.main()