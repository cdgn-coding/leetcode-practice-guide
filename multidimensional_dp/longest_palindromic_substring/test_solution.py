import unittest

class Solution:
    def longestPalindrome(self, s: str) -> str:
        pass

class TestLongestPalindrome(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertIn(self.solution.longestPalindrome("babad"), ["bab", "aba"])

    def test_example_2(self):
        self.assertEqual(self.solution.longestPalindrome("cbbd"), "bb")

    def test_single_character(self):
        self.assertEqual(self.solution.longestPalindrome("a"), "a")

    def test_all_same_characters(self):
        self.assertEqual(self.solution.longestPalindrome("aaaa"), "aaaa")

    def test_no_palindrome(self):
        self.assertIn(self.solution.longestPalindrome("abcd"), ["a", "b", "c", "d"])

    def test_palindrome_at_start(self):
        self.assertEqual(self.solution.longestPalindrome("abcddcba123"), "abcddcba")

    def test_palindrome_at_end(self):
        self.assertEqual(self.solution.longestPalindrome("123abcddcba"), "abcddcba")

    def test_even_length_palindrome(self):
        self.assertEqual(self.solution.longestPalindrome("1234abccba5678"), "abccba")

    def test_odd_length_palindrome(self):
        self.assertEqual(self.solution.longestPalindrome("1234abcdcba5678"), "abcdcba")

    def test_multiple_palindromes(self):
        self.assertEqual(self.solution.longestPalindrome("abcddcbaeeffeegg"), "abcddcba")

if __name__ == '__main__':
    unittest.main()