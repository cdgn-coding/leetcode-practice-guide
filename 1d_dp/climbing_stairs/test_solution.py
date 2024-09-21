import unittest

class Solution:
    def climbStairs(self, n: int) -> int:
        pass

class TestClimbStairs(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        self.assertEqual(self.solution.climbStairs(2), 2)

    def test_example2(self):
        self.assertEqual(self.solution.climbStairs(3), 3)

    def test_single_step(self):
        self.assertEqual(self.solution.climbStairs(1), 1)

    def test_four_steps(self):
        self.assertEqual(self.solution.climbStairs(4), 5)

    def test_five_steps(self):
        self.assertEqual(self.solution.climbStairs(5), 8)

    def test_large_input(self):
        self.assertEqual(self.solution.climbStairs(45), 1836311903)

    def test_zero_steps(self):
        with self.assertRaises(ValueError):
            self.solution.climbStairs(0)

    def test_negative_steps(self):
        with self.assertRaises(ValueError):
            self.solution.climbStairs(-1)

if __name__ == '__main__':
    unittest.main()