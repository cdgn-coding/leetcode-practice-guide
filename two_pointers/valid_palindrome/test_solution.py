import unittest

class Solution:
    def isPalindrome(self, s: str) -> bool:
        pass

class TestIsPalindrome(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_valid_palindrome(self):
        self.assertTrue(self.solution.isPalindrome("A man, a plan, a canal: Panama"))

    def test_invalid_palindrome(self):
        self.assertFalse(self.solution.isPalindrome("race a car"))

    def test_empty_string(self):
        self.assertTrue(self.solution.isPalindrome(" "))

    def test_single_character(self):
        self.assertTrue(self.solution.isPalindrome("a"))

    def test_alphanumeric_palindrome(self):
        self.assertTrue(self.solution.isPalindrome("ab1c1ba"))

    def test_case_insensitive(self):
        self.assertTrue(self.solution.isPalindrome("AbBa"))

    def test_special_characters(self):
        self.assertTrue(self.solution.isPalindrome("A,b,B@a"))

    def test_numbers_only(self):
        self.assertTrue(self.solution.isPalindrome("12321"))

    def test_mixed_alphanumeric(self):
        self.assertFalse(self.solution.isPalindrome("0P"))

if __name__ == '__main__':
    unittest.main()