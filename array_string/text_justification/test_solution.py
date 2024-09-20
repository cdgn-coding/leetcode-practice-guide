import unittest

class TestSolution(unittest.TestCase):
    def test_example1(self):
        words = ["This", "is", "an", "example", "of", "text", "justification."]
        maxWidth = 16
        expected = [
            "This    is    an",
            "example  of text",
            "justification.  "
        ]
        self.assertEqual(Solution().fullJustify(words, maxWidth), expected)

    def test_example2(self):
        words = ["What","must","be","acknowledgment","shall","be"]
        maxWidth = 16
        expected = [
            "What   must   be",
            "acknowledgment  ",
            "shall be        "
        ]
        self.assertEqual(Solution().fullJustify(words, maxWidth), expected)

    def test_example3(self):
        words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"]
        maxWidth = 20
        expected = [
            "Science  is  what we",
            "understand      well",
            "enough to explain to",
            "a  computer.  Art is",
            "everything  else  we",
            "do                  "
        ]
        self.assertEqual(Solution().fullJustify(words, maxWidth), expected)

    def test_single_word(self):
        words = ["Hello"]
        maxWidth = 10
        expected = ["Hello     "]
        self.assertEqual(Solution().fullJustify(words, maxWidth), expected)

    def test_single_line(self):
        words = ["This", "is", "a", "single", "line"]
        maxWidth = 20
        expected = ["This is a single line"]
        self.assertEqual(Solution().fullJustify(words, maxWidth), expected)

    def test_empty_input(self):
        words = []
        maxWidth = 10
        expected = []
        self.assertEqual(Solution().fullJustify(words, maxWidth), expected)

if __name__ == '__main__':
    unittest.main()