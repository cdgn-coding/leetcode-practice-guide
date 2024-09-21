import unittest

class Solution:
    def calculate(self, s: str) -> int:
        pass

class TestBasicCalculator(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_simple_addition(self):
        self.assertEqual(self.solution.calculate("1 + 1"), 2)

    def test_simple_subtraction(self):
        self.assertEqual(self.solution.calculate(" 2-1 + 2 "), 3)

    def test_complex_expression(self):
        self.assertEqual(self.solution.calculate("(1+(4+5+2)-3)+(6+8)"), 23)

    def test_single_number(self):
        self.assertEqual(self.solution.calculate("42"), 42)

    def test_negative_number(self):
        self.assertEqual(self.solution.calculate("-10"), -10)

    def test_multiple_operators(self):
        self.assertEqual(self.solution.calculate("5 + 3 - 2 + 1"), 7)

    def test_nested_parentheses(self):
        self.assertEqual(self.solution.calculate("((1 + 2) * 3) - 4"), 5)

    def test_spaces(self):
        self.assertEqual(self.solution.calculate("  3  +  2  "), 5)

    def test_large_numbers(self):
        self.assertEqual(self.solution.calculate("1000000 + 1000000"), 2000000)

    def test_unary_minus(self):
        self.assertEqual(self.solution.calculate("5 + (-3)"), 2)

if __name__ == '__main__':
    unittest.main()