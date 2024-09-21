import unittest

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        pass

class TestAnagram(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        self.assertTrue(self.solution.isAnagram("anagram", "nagaram"))

    def test_example2(self):
        self.assertFalse(self.solution.isAnagram("rat", "car"))

    def test_empty_strings(self):
        self.assertTrue(self.solution.isAnagram("", ""))

    def test_single_character(self):
        self.assertTrue(self.solution.isAnagram("a", "a"))

    def test_different_lengths(self):
        self.assertFalse(self.solution.isAnagram("hello", "world"))

    def test_same_characters_different_counts(self):
        self.assertFalse(self.solution.isAnagram("aab", "aba"))

    def test_unicode_characters(self):
        self.assertTrue(self.solution.isAnagram("こんにちは", "はちにんこ"))

    def test_long_strings(self):
        s = "a" * 50000
        t = "a" * 50000
        self.assertTrue(self.solution.isAnagram(s, t))

    def test_max_length(self):
        s = "a" * 50000
        t = "b" * 50000
        self.assertFalse(self.solution.isAnagram(s, t))

if __name__ == '__main__':
    unittest.main()