import unittest

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        pass

class TestIsIsomorphic(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        self.assertTrue(self.solution.isIsomorphic("egg", "add"))

    def test_example2(self):
        self.assertFalse(self.solution.isIsomorphic("foo", "bar"))

    def test_example3(self):
        self.assertTrue(self.solution.isIsomorphic("paper", "title"))

    def test_empty_strings(self):
        self.assertTrue(self.solution.isIsomorphic("", ""))

    def test_single_character(self):
        self.assertTrue(self.solution.isIsomorphic("a", "b"))

    def test_same_string(self):
        self.assertTrue(self.solution.isIsomorphic("abcde", "abcde"))

    def test_different_lengths(self):
        self.assertFalse(self.solution.isIsomorphic("abc", "abcd"))

    def test_repeated_characters(self):
        self.assertTrue(self.solution.isIsomorphic("aaabbb", "cccddd"))

    def test_different_mappings(self):
        self.assertFalse(self.solution.isIsomorphic("abba", "abab"))

    def test_unicode_characters(self):
        self.assertTrue(self.solution.isIsomorphic("汉字", "ab"))

if __name__ == '__main__':
    unittest.main()