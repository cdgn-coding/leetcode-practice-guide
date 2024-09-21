import unittest
from typing import List

class TestTrie(unittest.TestCase):
    def setUp(self):
        self.trie = Trie()

    def test_example(self):
        self.trie.insert("apple")
        self.assertTrue(self.trie.search("apple"))
        self.assertFalse(self.trie.search("app"))
        self.assertTrue(self.trie.startsWith("app"))
        self.trie.insert("app")
        self.assertTrue(self.trie.search("app"))

    def test_empty_trie(self):
        self.assertFalse(self.trie.search(""))
        self.assertFalse(self.trie.startsWith(""))

    def test_single_character(self):
        self.trie.insert("a")
        self.assertTrue(self.trie.search("a"))
        self.assertTrue(self.trie.startsWith("a"))
        self.assertFalse(self.trie.search("b"))
        self.assertFalse(self.trie.startsWith("b"))

    def test_multiple_words(self):
        words = ["hello", "world", "hi", "hey", "hola"]
        for word in words:
            self.trie.insert(word)
        
        for word in words:
            self.assertTrue(self.trie.search(word))
            self.assertTrue(self.trie.startsWith(word[:len(word)//2]))

    def test_prefix_not_word(self):
        self.trie.insert("hello")
        self.assertTrue(self.trie.startsWith("hel"))
        self.assertFalse(self.trie.search("hel"))

    def test_word_not_prefix(self):
        self.trie.insert("hello")
        self.assertTrue(self.trie.search("hello"))
        self.assertFalse(self.trie.startsWith("helloz"))

    def test_case_sensitivity(self):
        self.trie.insert("hello")
        self.assertTrue(self.trie.search("hello"))
        self.assertFalse(self.trie.search("Hello"))
        self.assertFalse(self.trie.startsWith("He"))

    def test_long_word(self):
        long_word = "a" * 2000
        self.trie.insert(long_word)
        self.assertTrue(self.trie.search(long_word))
        self.assertTrue(self.trie.startsWith("a" * 1000))

    def test_many_inserts(self):
        for i in range(30000):
            self.trie.insert(f"word{i}")
        for i in range(30000):
            self.assertTrue(self.trie.search(f"word{i}"))
            self.assertTrue(self.trie.startsWith(f"word{i}"))

if __name__ == '__main__':
    unittest.main()