import unittest

class Solution:
    def isPalindrome(self, x: int) -> bool:
        pass

class TestIsPalindrome(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_positive_palindrome(self):
        self.assertTrue(self.solution.isPalindrome(121))
        self.assertTrue(self.solution.isPalindrome(12321))
        self.assertTrue(self.solution.isPalindrome(1))

    def test_negative_number(self):
        self.assertFalse(self.solution.isPalindrome(-121))
        self.assertFalse(self.solution.isPalindrome(-1))

    def test_non_palindrome(self):
        self.assertFalse(self.solution.isPalindrome(10))
        self.assertFalse(self.solution.isPalindrome(123))

    def test_zero(self):
        self.assertTrue(self.solution.isPalindrome(0))

    def test_large_palindrome(self):
        self.assertTrue(self.solution.isPalindrome(1234554321))

    def test_large_non_palindrome(self):
        self.assertFalse(self.solution.isPalindrome(1234567890))

    def test_edge_cases(self):
        self.assertTrue(self.solution.isPalindrome(11))
        self.assertFalse(self.solution.isPalindrome(10))
        self.assertTrue(self.solution.isPalindrome(101))

if __name__ == '__main__':
    unittest.main()