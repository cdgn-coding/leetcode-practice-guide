import unittest

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        pass

class TestLengthOfLastWord(unittest.TestCase):
    def test_example1(self):
        s = "Hello World"
        solution = Solution()
        self.assertEqual(solution.lengthOfLastWord(s), 5)

    def test_example2(self):
        s = "   fly me   to   the moon  "
        solution = Solution()
        self.assertEqual(solution.lengthOfLastWord(s), 4)

    def test_example3(self):
        s = "luffy is still joyboy"
        solution = Solution()
        self.assertEqual(solution.lengthOfLastWord(s), 6)

    def test_single_word(self):
        s = "word"
        solution = Solution()
        self.assertEqual(solution.lengthOfLastWord(s), 4)

    def test_empty_string(self):
        s = ""
        solution = Solution()
        self.assertEqual(solution.lengthOfLastWord(s), 0)

    def test_only_spaces(self):
        s = "   "
        solution = Solution()
        self.assertEqual(solution.lengthOfLastWord(s), 0)

if __name__ == '__main__':
    unittest.main()