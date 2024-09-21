import unittest
from typing import List

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        pass  # Placeholder for the actual implementation

class TestWordSearch(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
        words = ["oath","pea","eat","rain"]
        expected = ["eat","oath"]
        self.assertCountEqual(self.solution.findWords(board, words), expected)

    def test_example2(self):
        board = [["a","b"],["c","d"]]
        words = ["abcb"]
        expected = []
        self.assertEqual(self.solution.findWords(board, words), expected)

    def test_empty_board(self):
        board = []
        words = ["word"]
        expected = []
        self.assertEqual(self.solution.findWords(board, words), expected)

    def test_empty_words(self):
        board = [["a","b"],["c","d"]]
        words = []
        expected = []
        self.assertEqual(self.solution.findWords(board, words), expected)

    def test_single_letter_board(self):
        board = [["a"]]
        words = ["a", "b"]
        expected = ["a"]
        self.assertEqual(self.solution.findWords(board, words), expected)

    def test_long_word(self):
        board = [["a","b","c"],["d","e","f"],["g","h","i"]]
        words = ["abcdefghi"]
        expected = ["abcdefghi"]
        self.assertEqual(self.solution.findWords(board, words), expected)

    def test_repeated_letters(self):
        board = [["a","a","a"],["a","a","a"],["a","a","a"]]
        words = ["aaa", "aaaa"]
        expected = ["aaa"]
        self.assertEqual(self.solution.findWords(board, words), expected)

    def test_no_matching_words(self):
        board = [["a","b"],["c","d"]]
        words = ["ef", "gh", "ij"]
        expected = []
        self.assertEqual(self.solution.findWords(board, words), expected)

if __name__ == '__main__':
    unittest.main()