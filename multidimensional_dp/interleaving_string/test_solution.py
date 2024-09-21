import unittest

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        pass

class TestIsInterleave(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertTrue(self.solution.isInterleave("aabcc", "dbbca", "aadbbcbcac"))

    def test_example_2(self):
        self.assertFalse(self.solution.isInterleave("aabcc", "dbbca", "aadbbbaccc"))

    def test_example_3(self):
        self.assertTrue(self.solution.isInterleave("", "", ""))

    def test_empty_s1(self):
        self.assertTrue(self.solution.isInterleave("", "abc", "abc"))

    def test_empty_s2(self):
        self.assertTrue(self.solution.isInterleave("abc", "", "abc"))

    def test_s3_longer(self):
        self.assertFalse(self.solution.isInterleave("abc", "def", "abcdefg"))

    def test_s3_shorter(self):
        self.assertFalse(self.solution.isInterleave("abc", "def", "abcde"))

    def test_interleave_alternating(self):
        self.assertTrue(self.solution.isInterleave("abc", "def", "adbecf"))

    def test_interleave_non_alternating(self):
        self.assertTrue(self.solution.isInterleave("abc", "def", "abcdef"))

    def test_same_letters_different_order(self):
        self.assertFalse(self.solution.isInterleave("aabcc", "dbbca", "aadbbbccac"))

    def test_long_strings(self):
        s1 = "a" * 100
        s2 = "b" * 100
        s3 = "ab" * 100
        self.assertTrue(self.solution.isInterleave(s1, s2, s3))

    def test_non_interleave(self):
        self.assertFalse(self.solution.isInterleave("abc", "def", "abefdc"))

if __name__ == '__main__':
    unittest.main()