import unittest

from graph.number_of_islands.solution import Solution


class NumberOfIslandsTest(unittest.TestCase):
    def testOneIsland(self):
        sol = Solution()
        actual = sol.numIslands([
            ["1", "1", "1", "1", "0"],
            ["1", "1", "0", "1", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "0", "0", "0"]
        ])
        self.assertEqual(1, actual)

    def testMultipleIsland(self):
        sol = Solution()
        actual = sol.numIslands([
            ["1", "1", "0", "0", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "1", "0", "0"],
            ["0", "0", "0", "1", "1"]
        ])
        self.assertEqual(3, actual)
