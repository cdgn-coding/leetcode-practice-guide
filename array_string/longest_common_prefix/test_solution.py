import unittest

class TestLongestCommonPrefix(unittest.TestCase):
    def test_example1(self):
        strs = ["flower", "flow", "flight"]
        self.assertEqual(longestCommonPrefix(strs), "fl")

    def test_example2(self):
        strs = ["dog", "racecar", "car"]
        self.assertEqual(longestCommonPrefix(strs), "")

    def test_single_string(self):
        strs = ["hello"]
        self.assertEqual(longestCommonPrefix(strs), "hello")

    def test_empty_array(self):
        strs = []
        self.assertEqual(longestCommonPrefix(strs), "")

    def test_no_common_prefix(self):
        strs = ["apple", "banana", "cherry"]
        self.assertEqual(longestCommonPrefix(strs), "")

    def test_all_same_strings(self):
        strs = ["abc", "abc", "abc"]
        self.assertEqual(longestCommonPrefix(strs), "abc")

    def test_different_lengths(self):
        strs = ["a", "ab", "abc"]
        self.assertEqual(longestCommonPrefix(strs), "a")

    def test_empty_string(self):
        strs = ["", "b", "c"]
        self.assertEqual(longestCommonPrefix(strs), "")

if __name__ == '__main__':
    unittest.main()