import unittest

from backtracking.letter_combinations.solution import Solution


class TestLetterCombinations(unittest.TestCase):
    def test_letterCombinations(self):
        sol = Solution()
        expected = ["ad","ae","af","bd","be","bf","cd","ce","cf"]
        expected.sort()
        self.assertEqual(expected, sol.letterCombinations("23"))