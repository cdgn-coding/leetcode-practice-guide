import unittest
from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        pass

class TestCombinations(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        n, k = 4, 2
        expected = [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
        result = self.solution.combine(n, k)
        self.assertEqual(len(result), len(expected))
        for combo in result:
            self.assertIn(combo, expected)

    def test_example_2(self):
        n, k = 1, 1
        expected = [[1]]
        self.assertEqual(self.solution.combine(n, k), expected)

    def test_n_equals_k(self):
        n = k = 3
        expected = [[1,2,3]]
        self.assertEqual(self.solution.combine(n, k), expected)

    def test_k_equals_1(self):
        n, k = 5, 1
        expected = [[1],[2],[3],[4],[5]]
        result = self.solution.combine(n, k)
        self.assertEqual(len(result), len(expected))
        for combo in result:
            self.assertIn(combo, expected)

    def test_n_equals_20_k_equals_3(self):
        n, k = 20, 3
        result = self.solution.combine(n, k)
        self.assertEqual(len(result), 1140)  # 20C3 = 1140
        for combo in result:
            self.assertEqual(len(combo), 3)
            self.assertTrue(all(1 <= num <= 20 for num in combo))

    def test_constraints(self):
        with self.assertRaises(ValueError):
            self.solution.combine(0, 1)
        with self.assertRaises(ValueError):
            self.solution.combine(21, 1)
        with self.assertRaises(ValueError):
            self.solution.combine(5, 0)
        with self.assertRaises(ValueError):
            self.solution.combine(5, 6)

if __name__ == '__main__':
    unittest.main()