import unittest

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        pass

class TestIsSubsequence(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertTrue(self.solution.isSubsequence("abc", "ahbgdc"))

    def test_example_2(self):
        self.assertFalse(self.solution.isSubsequence("axc", "ahbgdc"))

    def test_empty_s(self):
        self.assertTrue(self.solution.isSubsequence("", "ahbgdc"))

    def test_empty_t(self):
        self.assertFalse(self.solution.isSubsequence("abc", ""))

    def test_both_empty(self):
        self.assertTrue(self.solution.isSubsequence("", ""))

    def test_s_longer_than_t(self):
        self.assertFalse(self.solution.isSubsequence("abcde", "abc"))

    def test_s_equals_t(self):
        self.assertTrue(self.solution.isSubsequence("abc", "abc"))

    def test_single_character(self):
        self.assertTrue(self.solution.isSubsequence("a", "a"))

    def test_repeated_characters(self):
        self.assertTrue(self.solution.isSubsequence("aaa", "aaaaaa"))

    def test_all_different_characters(self):
        self.assertFalse(self.solution.isSubsequence("xyz", "abc"))

    def test_long_strings(self):
        s = "abcdefghijklmnopqrstuvwxyz"
        t = "a" + "b" * 100 + "c" * 100 + "d" * 100 + s[4:]
        self.assertTrue(self.solution.isSubsequence(s, t))

if __name__ == '__main__':
    unittest.main()