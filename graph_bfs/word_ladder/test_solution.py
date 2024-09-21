import unittest

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        pass

class TestLadderLength(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        beginWord = "hit"
        endWord = "cog"
        wordList = ["hot","dot","dog","lot","log","cog"]
        expected = 5
        self.assertEqual(self.solution.ladderLength(beginWord, endWord, wordList), expected)

    def test_example_2(self):
        beginWord = "hit"
        endWord = "cog"
        wordList = ["hot","dot","dog","lot","log"]
        expected = 0
        self.assertEqual(self.solution.ladderLength(beginWord, endWord, wordList), expected)

    def test_single_letter_change(self):
        beginWord = "a"
        endWord = "c"
        wordList = ["a","b","c"]
        expected = 3
        self.assertEqual(self.solution.ladderLength(beginWord, endWord, wordList), expected)

    def test_no_transformation_possible(self):
        beginWord = "abc"
        endWord = "def"
        wordList = ["abc","abcd","defg"]
        expected = 0
        self.assertEqual(self.solution.ladderLength(beginWord, endWord, wordList), expected)

    def test_begin_word_not_in_list(self):
        beginWord = "hit"
        endWord = "cog"
        wordList = ["hot","dot","dog","lot","log","cog"]
        expected = 5
        self.assertEqual(self.solution.ladderLength(beginWord, endWord, wordList), expected)

    def test_end_word_not_in_list(self):
        beginWord = "hit"
        endWord = "cog"
        wordList = ["hot","dot","dog","lot","log"]
        expected = 0
        self.assertEqual(self.solution.ladderLength(beginWord, endWord, wordList), expected)

    def test_empty_word_list(self):
        beginWord = "hit"
        endWord = "cog"
        wordList = []
        expected = 0
        self.assertEqual(self.solution.ladderLength(beginWord, endWord, wordList), expected)

    def test_begin_equals_end(self):
        beginWord = "hit"
        endWord = "hit"
        wordList = ["hot","dot","dog","lot","log"]
        expected = 1
        self.assertEqual(self.solution.ladderLength(beginWord, endWord, wordList), expected)

if __name__ == '__main__':
    unittest.main()