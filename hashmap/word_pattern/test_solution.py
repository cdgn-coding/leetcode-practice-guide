import unittest

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        pass

class TestWordPattern(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertTrue(self.solution.wordPattern("abba", "dog cat cat dog"))

    def test_example_2(self):
        self.assertFalse(self.solution.wordPattern("abba", "dog cat cat fish"))

    def test_example_3(self):
        self.assertFalse(self.solution.wordPattern("aaaa", "dog cat cat dog"))

    def test_single_letter_pattern(self):
        self.assertTrue(self.solution.wordPattern("a", "dog"))

    def test_different_length_pattern_and_words(self):
        self.assertFalse(self.solution.wordPattern("abc", "dog cat"))

    def test_same_word_different_letters(self):
        self.assertFalse(self.solution.wordPattern("abba", "dog dog dog dog"))

    def test_different_words_same_letter(self):
        self.assertFalse(self.solution.wordPattern("abba", "dog cat fish dog"))

    def test_empty_pattern_and_string(self):
        self.assertTrue(self.solution.wordPattern("", ""))

    def test_long_pattern_and_string(self):
        pattern = "abcdefghijklmnopqrstuvwxyz" * 11 + "abcd"
        s = " ".join(["word" + str(i) for i in range(300)])
        self.assertTrue(self.solution.wordPattern(pattern, s))

    def test_max_constraint_pattern_and_string(self):
        pattern = "a" * 300
        s = "word " * 299 + "word"
        self.assertTrue(self.solution.wordPattern(pattern, s))

if __name__ == '__main__':
    unittest.main()