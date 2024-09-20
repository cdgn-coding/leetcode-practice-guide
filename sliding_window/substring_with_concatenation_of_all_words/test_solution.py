import unittest

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        pass

class TestFindSubstring(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        s = "barfoothefoobarman"
        words = ["foo", "bar"]
        expected = [0, 9]
        self.assertEqual(self.solution.findSubstring(s, words), expected)

    def test_example_2(self):
        s = "wordgoodgoodgoodbestword"
        words = ["word", "good", "best", "word"]
        expected = []
        self.assertEqual(self.solution.findSubstring(s, words), expected)

    def test_example_3(self):
        s = "barfoofoobarthefoobarman"
        words = ["bar", "foo", "the"]
        expected = [6, 9, 12]
        self.assertEqual(self.solution.findSubstring(s, words), expected)

    def test_empty_string(self):
        s = ""
        words = ["test"]
        expected = []
        self.assertEqual(self.solution.findSubstring(s, words), expected)

    def test_single_word(self):
        s = "abcabc"
        words = ["abc"]
        expected = [0, 3]
        self.assertEqual(self.solution.findSubstring(s, words), expected)

    def test_no_match(self):
        s = "abcdef"
        words = ["xyz"]
        expected = []
        self.assertEqual(self.solution.findSubstring(s, words), expected)

    def test_overlapping_matches(self):
        s = "aaaaaa"
        words = ["aa", "aa"]
        expected = [0, 2]
        self.assertEqual(self.solution.findSubstring(s, words), expected)

    def test_longer_words(self):
        s = "wordgoodgoodgoodbestword"
        words = ["word", "good", "best", "good"]
        expected = [8]
        self.assertEqual(self.solution.findSubstring(s, words), expected)

if __name__ == '__main__':
    unittest.main()