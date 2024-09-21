import unittest

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        pass

class TestEvalRPN(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        tokens = ["2","1","+","3","*"]
        self.assertEqual(self.solution.evalRPN(tokens), 9)

    def test_example_2(self):
        tokens = ["4","13","5","/","+"]
        self.assertEqual(self.solution.evalRPN(tokens), 6)

    def test_example_3(self):
        tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
        self.assertEqual(self.solution.evalRPN(tokens), 22)

    def test_single_number(self):
        tokens = ["42"]
        self.assertEqual(self.solution.evalRPN(tokens), 42)

    def test_negative_numbers(self):
        tokens = ["-3","-4","+"]
        self.assertEqual(self.solution.evalRPN(tokens), -7)

    def test_division_truncation(self):
        tokens = ["7","-3","/"]
        self.assertEqual(self.solution.evalRPN(tokens), -2)

    def test_complex_expression(self):
        tokens = ["3","4","+","2","*","7","/"]
        self.assertEqual(self.solution.evalRPN(tokens), 2)

    def test_large_numbers(self):
        tokens = ["200","10","*","300","+"]
        self.assertEqual(self.solution.evalRPN(tokens), 2300)

if __name__ == '__main__':
    unittest.main()