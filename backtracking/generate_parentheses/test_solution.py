import unittest

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        pass

class TestGenerateParenthesis(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        n = 3
        expected = ["((()))","(()())","(())()","()(())","()()()"]
        result = self.solution.generateParenthesis(n)
        self.assertCountEqual(result, expected)

    def test_example_2(self):
        n = 1
        expected = ["()"]
        result = self.solution.generateParenthesis(n)
        self.assertEqual(result, expected)

    def test_n_equals_2(self):
        n = 2
        expected = ["(())", "()()"]
        result = self.solution.generateParenthesis(n)
        self.assertCountEqual(result, expected)

    def test_n_equals_4(self):
        n = 4
        expected = ["(((())))","((()()))","((())())","((()))()","(()(()))","(()()())","(()())()","(())(())","(())()()","()((()))","()(()())","()(())()","()()(())","()()()()"]
        result = self.solution.generateParenthesis(n)
        self.assertCountEqual(result, expected)

    def test_constraints(self):
        for n in range(1, 9):
            result = self.solution.generateParenthesis(n)
            self.assertTrue(all(self.is_valid_parentheses(s) for s in result))
            self.assertEqual(len(result), self.catalan_number(n))

    def is_valid_parentheses(self, s):
        count = 0
        for char in s:
            if char == '(':
                count += 1
            else:
                count -= 1
            if count < 0:
                return False
        return count == 0

    def catalan_number(self, n):
        if n <= 1:
            return 1
        res = 0
        for i in range(n):
            res += self.catalan_number(i) * self.catalan_number(n - i - 1)
        return res

if __name__ == '__main__':
    unittest.main()