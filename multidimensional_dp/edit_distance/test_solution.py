import unittest

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        pass

class TestEditDistance(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.minDistance("horse", "ros"), 3)

    def test_example_2(self):
        self.assertEqual(self.solution.minDistance("intention", "execution"), 5)

    def test_empty_strings(self):
        self.assertEqual(self.solution.minDistance("", ""), 0)

    def test_one_empty_string(self):
        self.assertEqual(self.solution.minDistance("abc", ""), 3)
        self.assertEqual(self.solution.minDistance("", "def"), 3)

    def test_same_strings(self):
        self.assertEqual(self.solution.minDistance("hello", "hello"), 0)

    def test_completely_different_strings(self):
        self.assertEqual(self.solution.minDistance("abc", "def"), 3)

    def test_one_character_difference(self):
        self.assertEqual(self.solution.minDistance("cat", "cut"), 1)

    def test_case_sensitivity(self):
        self.assertEqual(self.solution.minDistance("Hello", "hello"), 1)

    def test_long_strings(self):
        self.assertEqual(self.solution.minDistance("a" * 500, "b" * 500), 500)

    def test_substring(self):
        self.assertEqual(self.solution.minDistance("abcde", "abc"), 2)

if __name__ == '__main__':
    unittest.main()