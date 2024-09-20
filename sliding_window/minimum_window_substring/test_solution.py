import unittest

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        pass

class TestMinWindowSubstring(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        s = "ADOBECODEBANC"
        t = "ABC"
        self.assertEqual(self.solution.minWindow(s, t), "BANC")

    def test_example_2(self):
        s = "a"
        t = "a"
        self.assertEqual(self.solution.minWindow(s, t), "a")

    def test_example_3(self):
        s = "a"
        t = "aa"
        self.assertEqual(self.solution.minWindow(s, t), "")

    def test_empty_strings(self):
        s = ""
        t = ""
        self.assertEqual(self.solution.minWindow(s, t), "")

    def test_no_match(self):
        s = "ABCDEF"
        t = "XYZ"
        self.assertEqual(self.solution.minWindow(s, t), "")

    def test_full_string_match(self):
        s = "ABCDE"
        t = "ABCDE"
        self.assertEqual(self.solution.minWindow(s, t), "ABCDE")

    def test_repeated_characters(self):
        s = "ADOBECODEBANC"
        t = "AABC"
        self.assertEqual(self.solution.minWindow(s, t), "BANC")

    def test_case_sensitivity(self):
        s = "aaAAAaa"
        t = "AaA"
        self.assertEqual(self.solution.minWindow(s, t), "AAAa")

    def test_long_strings(self):
        s = "A" * 100000 + "B" + "A" * 100000
        t = "AB"
        self.assertEqual(self.solution.minWindow(s, t), "AB")

if __name__ == '__main__':
    unittest.main()