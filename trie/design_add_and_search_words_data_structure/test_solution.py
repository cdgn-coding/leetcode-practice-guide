import unittest
from typing import List

class TestWordDictionary(unittest.TestCase):
    def setUp(self):
        self.word_dict = WordDictionary()

    def test_example(self):
        self.word_dict.addWord("bad")
        self.word_dict.addWord("dad")
        self.word_dict.addWord("mad")
        self.assertFalse(self.word_dict.search("pad"))
        self.assertTrue(self.word_dict.search("bad"))
        self.assertTrue(self.word_dict.search(".ad"))
        self.assertTrue(self.word_dict.search("b.."))

    def test_empty_word(self):
        self.word_dict.addWord("")
        self.assertTrue(self.word_dict.search(""))
        self.assertFalse(self.word_dict.search("."))

    def test_single_letter(self):
        self.word_dict.addWord("a")
        self.assertTrue(self.word_dict.search("a"))
        self.assertTrue(self.word_dict.search("."))
        self.assertFalse(self.word_dict.search("b"))

    def test_multiple_dots(self):
        self.word_dict.addWord("hello")
        self.assertTrue(self.word_dict.search("h.ll."))
        self.assertTrue(self.word_dict.search("....."))
        self.assertFalse(self.word_dict.search(".."))

    def test_no_match(self):
        self.word_dict.addWord("hello")
        self.assertFalse(self.word_dict.search("world"))
        self.assertFalse(self.word_dict.search("hell"))
        self.assertFalse(self.word_dict.search("helloo"))

    def test_multiple_words(self):
        words = ["apple", "app", "apply", "apricot", "banana"]
        for word in words:
            self.word_dict.addWord(word)
        self.assertTrue(self.word_dict.search("app.."))
        self.assertTrue(self.word_dict.search("appl."))
        self.assertFalse(self.word_dict.search("appp"))
        self.assertTrue(self.word_dict.search("banana"))

    def test_case_sensitivity(self):
        self.word_dict.addWord("hello")
        self.assertTrue(self.word_dict.search("hello"))
        self.assertFalse(self.word_dict.search("Hello"))
        self.assertFalse(self.word_dict.search("HELLO"))

    def test_long_word(self):
        long_word = "abcdefghijklmnopqrstuvwxy"
        self.word_dict.addWord(long_word)
        self.assertTrue(self.word_dict.search(long_word))
        self.assertTrue(self.word_dict.search("a.c.e.g.i.k.m.o.q.s.u.w.y"))
        self.assertFalse(self.word_dict.search(long_word + "z"))

if __name__ == '__main__':
    unittest.main()