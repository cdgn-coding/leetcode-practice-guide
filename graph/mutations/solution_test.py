import unittest

from graph.mutations.solution import Solution


class MutationSolutionTest(unittest.TestCase):
    def test(self):
        solution = Solution()
        self.assertEqual(4, solution.minMutation("AACCGGTT", "AAACGGTA", ["AACCGATT","AACCGATA","AAACGATA","AAACGGTA"]))
