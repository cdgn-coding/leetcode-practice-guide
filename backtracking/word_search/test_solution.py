import unittest

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        pass

class TestWordSearch(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
        word = "ABCCED"
        self.assertTrue(self.solution.exist(board, word))

    def test_example2(self):
        board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
        word = "SEE"
        self.assertTrue(self.solution.exist(board, word))

    def test_example3(self):
        board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
        word = "ABCB"
        self.assertFalse(self.solution.exist(board, word))

    def test_single_letter(self):
        board = [["A"]]
        word = "A"
        self.assertTrue(self.solution.exist(board, word))

    def test_word_too_long(self):
        board = [["A","B"],["C","D"]]
        word = "ABCDE"
        self.assertFalse(self.solution.exist(board, word))

    def test_empty_board(self):
        board = []
        word = "A"
        self.assertFalse(self.solution.exist(board, word))

    def test_empty_word(self):
        board = [["A","B"],["C","D"]]
        word = ""
        self.assertTrue(self.solution.exist(board, word))

    def test_word_not_in_board(self):
        board = [["A","B"],["C","D"]]
        word = "E"
        self.assertFalse(self.solution.exist(board, word))

    def test_zigzag_word(self):
        board = [["A","B","C"],["D","E","F"],["G","H","I"]]
        word = "ABEHI"
        self.assertTrue(self.solution.exist(board, word))

    def test_same_letter_not_reused(self):
        board = [["A","A","A"],["A","A","A"],["A","A","A"]]
        word = "AAAAAAAAAA"
        self.assertFalse(self.solution.exist(board, word))

if __name__ == '__main__':
    unittest.main()