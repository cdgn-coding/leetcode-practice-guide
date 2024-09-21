import unittest

class Solution:
    def calcEquation(self, equations, values, queries):
        pass

class TestCalcEquation(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        equations = [["a","b"],["b","c"]]
        values = [2.0, 3.0]
        queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
        expected = [6.00000, 0.50000, -1.00000, 1.00000, -1.00000]
        result = self.solution.calcEquation(equations, values, queries)
        self.assertEqual(len(result), len(expected))
        for r, e in zip(result, expected):
            self.assertAlmostEqual(r, e, places=5)

    def test_example_2(self):
        equations = [["a","b"],["b","c"],["bc","cd"]]
        values = [1.5, 2.5, 5.0]
        queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
        expected = [3.75000, 0.40000, 5.00000, 0.20000]
        result = self.solution.calcEquation(equations, values, queries)
        self.assertEqual(len(result), len(expected))
        for r, e in zip(result, expected):
            self.assertAlmostEqual(r, e, places=5)

    def test_example_3(self):
        equations = [["a","b"]]
        values = [0.5]
        queries = [["a","b"],["b","a"],["a","c"],["x","y"]]
        expected = [0.50000, 2.00000, -1.00000, -1.00000]
        result = self.solution.calcEquation(equations, values, queries)
        self.assertEqual(len(result), len(expected))
        for r, e in zip(result, expected):
            self.assertAlmostEqual(r, e, places=5)

    def test_single_equation(self):
        equations = [["x","y"]]
        values = [2.0]
        queries = [["x","y"],["y","x"],["x","x"],["y","y"]]
        expected = [2.00000, 0.50000, 1.00000, 1.00000]
        result = self.solution.calcEquation(equations, values, queries)
        self.assertEqual(len(result), len(expected))
        for r, e in zip(result, expected):
            self.assertAlmostEqual(r, e, places=5)

    def test_multiple_equations(self):
        equations = [["a","b"],["b","c"],["c","d"],["d","e"]]
        values = [2.0, 3.0, 4.0, 5.0]
        queries = [["a","e"],["e","a"],["b","d"],["a","a"],["x","x"]]
        expected = [120.00000, 1/120.00000, 12.00000, 1.00000, -1.00000]
        result = self.solution.calcEquation(equations, values, queries)
        self.assertEqual(len(result), len(expected))
        for r, e in zip(result, expected):
            self.assertAlmostEqual(r, e, places=5)

    def test_circular_equations(self):
        equations = [["a","b"],["b","c"],["c","a"]]
        values = [2.0, 3.0, 1/6.0]
        queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
        expected = [3.00000, 0.50000, -1.00000, 1.00000, -1.00000]
        result = self.