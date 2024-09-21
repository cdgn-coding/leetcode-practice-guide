import unittest

class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        pass

class TestMinMutation(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.minMutation("AACCGGTT", "AACCGGTA", ["AACCGGTA"]), 1)

    def test_example_2(self):
        self.assertEqual(self.solution.minMutation("AACCGGTT", "AAACGGTA", ["AACCGGTA","AACCGCTA","AAACGGTA"]), 2)

    def test_no_mutation(self):
        self.assertEqual(self.solution.minMutation("AACCGGTT", "AACCGGTT", ["AACCGGTA"]), 0)

    def test_impossible_mutation(self):
        self.assertEqual(self.solution.minMutation("AAAAACCC", "AACCCCCC", ["AAAACCCC"]), -1)

    def test_empty_bank(self):
        self.assertEqual(self.solution.minMutation("AACCGGTT", "AACCGGTA", []), -1)

    def test_multiple_steps(self):
        self.assertEqual(self.solution.minMutation("AACCGGTT", "AAACGGTA", ["AACCGGTA","AACCGCTA","AAACGGTA","AACCGGTT"]), 2)

    def test_all_mutations_in_bank(self):
        self.assertEqual(self.solution.minMutation("AAAAAAAA", "CCCCCCCC", ["AAAAAAAA","AAAAAAAC","AAAAAACA","AAAAACAA","AAAACCAA","AAACCCAA","AACCCCAA","ACCCCCCAA","CCCCCCCA","CCCCCCCC"]), 8)

if __name__ == '__main__':
    unittest.main()