import unittest

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        pass

class TestFindMaximizedCapital(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        k = 2
        w = 0
        profits = [1, 2, 3]
        capital = [0, 1, 1]
        expected = 4
        self.assertEqual(self.solution.findMaximizedCapital(k, w, profits, capital), expected)

    def test_example_2(self):
        k = 3
        w = 0
        profits = [1, 2, 3]
        capital = [0, 1, 2]
        expected = 6
        self.assertEqual(self.solution.findMaximizedCapital(k, w, profits, capital), expected)

    def test_single_project(self):
        k = 1
        w = 0
        profits = [1]
        capital = [0]
        expected = 1
        self.assertEqual(self.solution.findMaximizedCapital(k, w, profits, capital), expected)

    def test_no_projects(self):
        k = 1
        w = 5
        profits = []
        capital = []
        expected = 5
        self.assertEqual(self.solution.findMaximizedCapital(k, w, profits, capital), expected)

    def test_high_initial_capital(self):
        k = 2
        w = 1000000
        profits = [1, 2, 3]
        capital = [0, 1, 2]
        expected = 1000005
        self.assertEqual(self.solution.findMaximizedCapital(k, w, profits, capital), expected)

    def test_insufficient_capital(self):
        k = 3
        w = 0
        profits = [1, 2, 3]
        capital = [1, 2, 3]
        expected = 0
        self.assertEqual(self.solution.findMaximizedCapital(k, w, profits, capital), expected)

    def test_max_constraints(self):
        k = 100000
        w = 1000000000
        profits = [10000] * 100000
        capital = [0] * 100000
        expected = 2000000000
        self.assertEqual(self.solution.findMaximizedCapital(k, w, profits, capital), expected)

if __name__ == '__main__':
    unittest.main()