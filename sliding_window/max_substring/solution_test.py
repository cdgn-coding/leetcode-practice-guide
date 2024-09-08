import unittest

from sliding_window.max_substring.solution import Solution


class MaxSubstringTest(unittest.TestCase):
    def test_max_substring(self):
        sol = Solution()
        self.assertEqual(3, sol.lengthOfLongestSubstring("abcabcbb"))
        self.assertEqual(1, sol.lengthOfLongestSubstring("bbbbb"))
        self.assertEqual(3, sol.lengthOfLongestSubstring("pwwkew"))
        self.assertEqual(1, sol.lengthOfLongestSubstring(" "))