import unittest

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        pass

class TestCoinChange(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.coinChange([1,2,5], 11), 3)

    def test_example_2(self):
        self.assertEqual(self.solution.coinChange([2], 3), -1)

    def test_example_3(self):
        self.assertEqual(self.solution.coinChange([1], 0), 0)

    def test_no_solution(self):
        self.assertEqual(self.solution.coinChange([2], 1), -1)

    def test_large_amount(self):
        self.assertEqual(self.solution.coinChange([1,2,5], 100), 20)

    def test_single_coin(self):
        self.assertEqual(self.solution.coinChange([5], 15), 3)

    def test_multiple_solutions(self):
        self.assertEqual(self.solution.coinChange([1,2,5], 5), 1)

    def test_zero_amount(self):
        self.assertEqual(self.solution.coinChange([1,2,5], 0), 0)

    def test_large_coins(self):
        self.assertEqual(self.solution.coinChange([186,419,83,408], 6249), 20)

if __name__ == '__main__':
    unittest.main()