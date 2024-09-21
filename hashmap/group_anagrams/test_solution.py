import unittest
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        pass

class TestGroupAnagrams(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        strs = ["eat","tea","tan","ate","nat","bat"]
        expected = [["bat"],["nat","tan"],["ate","eat","tea"]]
        result = self.solution.groupAnagrams(strs)
        self.assertEqual(len(result), len(expected))
        for group in result:
            self.assertIn(sorted(group), [sorted(x) for x in expected])

    def test_example_2(self):
        strs = [""]
        expected = [[""]]
        self.assertEqual(self.solution.groupAnagrams(strs), expected)

    def test_example_3(self):
        strs = ["a"]
        expected = [["a"]]
        self.assertEqual(self.solution.groupAnagrams(strs), expected)

    def test_empty_input(self):
        strs = []
        expected = []
        self.assertEqual(self.solution.groupAnagrams(strs), expected)

    def test_all_unique(self):
        strs = ["abc", "def", "ghi"]
        expected = [["abc"], ["def"], ["ghi"]]
        result = self.solution.groupAnagrams(strs)
        self.assertEqual(len(result), len(expected))
        for group in result:
            self.assertIn(group, expected)

    def test_all_anagrams(self):
        strs = ["abc", "bca", "cab"]
        expected = [["abc", "bca", "cab"]]
        result = self.solution.groupAnagrams(strs)
        self.assertEqual(len(result), 1)
        self.assertEqual(sorted(result[0]), sorted(expected[0]))

    def test_mixed_anagrams(self):
        strs = ["abc", "def", "bca", "fed", "cab", "ghi"]
        expected = [["abc", "bca", "cab"], ["def", "fed"], ["ghi"]]
        result = self.solution.groupAnagrams(strs)
        self.assertEqual(len(result), len(expected))
        for group in result:
            self.assertIn(sorted(group), [sorted(x) for x in expected])

if __name__ == '__main__':
    unittest.main()