import unittest

from hashmap.ransom_note.solution import Solution


class TestSolution(unittest.TestCase):
    def test_possible_ransom_note(self):
        sol = Solution()
        actual = sol.canConstruct("aa", "aab")
        self.assertTrue(actual)

    def test_impossible_ransom_note(self):
        sol = Solution()
        actual = sol.canConstruct("aac", "aab")
        self.assertFalse(actual)