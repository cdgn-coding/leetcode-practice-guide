import unittest

from graph.snakes_ladders.solution import Solution


class SnakesAndLaddersTest(unittest.TestCase):
    def testMovements(self):
        sol = Solution()
        self.assertEqual(4, sol.snakesAndLadders(
            [[-1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1], [-1, 35, -1, -1, 13, -1],
             [-1, -1, -1, -1, -1, -1], [-1, 15, -1, -1, -1, -1]]))
        self.assertEqual(-1, sol.snakesAndLadders([
            [1, 1, -1],
            [1, 1, 1],
            [-1, 1, 1]
        ]))
        self.assertEqual(2, sol.snakesAndLadders(
            [[-1, -1, 30, 14, 15, -1],
             [23, 9, -1, -1, -1, 9],
             [12, 5, 7, 24, -1, 30],
             [10, -1, -1, -1, 25, 17],
             [32, -1, 28, -1, -1, 32],
             [-1, -1, 23, -1, 13, 19]]
        ))
        self.assertEqual(2, sol.snakesAndLadders(
            [[-1, -1, -1, -1, -1, 38, -1],
             [-1, 26, -1, 28, 49, 42, -1],
             [-1, 37, 14, 39, 48, 24, 48],
             [6, -1, 41, 29, 2, -1, 28],
             [-1, -1, -1, 7, -1, -1, 16],
             [21, 19, 21, -1, -1, -1, 48],
             [-1, -1, 2, -1, 35, -1, -1]]
        ))
        self.assertEqual(2, sol.snakesAndLadders(
            [[-1, 14, 62, -1, -1, -1, -1, 53, -1, 22, -1], [19, -1, -1, 36, -1, -1, 39, 60, -1, -1, -1],
             [-1, -1, 50, -1, 27, -1, 38, 54, 1, -1, -1], [-1, -1, -1, -1, -1, -1, 1, -1, -1, -1, -1],
             [-1, -1, 51, 84, -1, -1, 37, -1, -1, 1, -1], [-1, -1, 108, -1, 111, 55, -1, -1, -1, -1, 51],
             [107, -1, -1, -1, -1, -1, -1, -1, 88, 83, 107], [3, -1, -1, -1, -1, 7, -1, -1, 21, -1, -1],
             [-1, 79, 64, -1, 52, 53, -1, 90, -1, -1, -1], [-1, -1, -1, 60, 6, -1, -1, -1, -1, 69, -1],
             [-1, -1, 110, 105, 118, -1, -1, -1, -1, 86, -1]]))

    def testPosition(self):
        sol = Solution()
        self.assertEqual((5, 0), sol.position(6, 1))
        self.assertEqual((0, 0), sol.position(6, 36))
        self.assertEqual((0, 2), sol.position(3, 9))
        self.assertEqual((0, 4), sol.position(6, 32))
        self.assertEqual((1, 1), sol.position(7, 41))
