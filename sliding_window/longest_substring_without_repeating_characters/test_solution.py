import unittest

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        pass

class TestLongestSubstring(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        self.assertEqual(self.solution.lengthOfLongestSubstring("abcabcbb"), 3)

    def test_example2(self):
        self.assertEqual(self.solution.lengthOfLongestSubstring("bbbbb"), 1)

    def test_example3(self):
        self.assertEqual(self.solution.lengthOfLongestSubstring("pwwkew"), 3)

    def test_empty_string(self):
        self.assertEqual(self.solution.lengthOfLongestSubstring(""), 0)

    def test_single_character(self):
        self.assertEqual(self.solution.lengthOfLongestSubstring("a"), 1)

    def test_all_unique_characters(self):
        self.assertEqual(self.solution.lengthOfLongestSubstring("abcdefg"), 7)

    def test_with_spaces(self):
        self.assertEqual(self.solution.lengthOfLongestSubstring("ab c d ef"), 5)

    def test_with_digits(self):
        self.assertEqual(self.solution.lengthOfLongestSubstring("ab1c2d3ef"), 9)

    def test_with_symbols(self):
        self.assertEqual(self.solution.lengthOfLongestSubstring("ab!@#$%^&*()"), 11)

    def test_long_string(self):
        self.assertEqual(self.solution.lengthOfLongestSubstring("a" * 50000 + "b"), 2)

if __name__ == '__main__':
    unittest.main()