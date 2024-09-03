import unittest

from stacks.valid_parentheses.solution import Solution


class SolutionTestCase(unittest.TestCase):
    def test_valid_parentheses(self):
        sol = Solution()
        self.assertEqual(True, sol.isValid("()"))
        self.assertEqual(True, sol.isValid("(){}[]"))
        self.assertEqual(True, sol.isValid("([])"))

    def test_invalid_parentheses(self):
        sol = Solution()
        self.assertEqual(False, sol.isValid("(()"))
        self.assertEqual(False, sol.isValid("[(){}[]"))

    def test_invalid_close(self):
        sol = Solution()
        self.assertEqual(False, sol.isValid("]"))


if __name__ == '__main__':
    unittest.main()
