import unittest

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        pass

class TestMaxProfit(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        k = 2
        prices = [2,4,1]
        self.assertEqual(self.solution.maxProfit(k, prices), 2)

    def test_example2(self):
        k = 2
        prices = [3,2,6,5,0,3]
        self.assertEqual(self.solution.maxProfit(k, prices), 7)

    def test_single_transaction(self):
        k = 1
        prices = [1,2,3,4,5]
        self.assertEqual(self.solution.maxProfit(k, prices), 4)

    def test_no_profit(self):
        k = 3
        prices = [5,4,3,2,1]
        self.assertEqual(self.solution.maxProfit(k, prices), 0)

    def test_max_transactions(self):
        k = 100
        prices = [1,2,3,4,5,1,2,3,4,5]
        self.assertEqual(self.solution.maxProfit(k, prices), 8)

    def test_single_price(self):
        k = 1
        prices = [1000]
        self.assertEqual(self.solution.maxProfit(k, prices), 0)

    def test_identical_prices(self):
        k = 5
        prices = [100, 100, 100, 100, 100]
        self.assertEqual(self.solution.maxProfit(k, prices), 0)

    def test_alternating_prices(self):
        k = 3
        prices = [1,5,1,5,1,5]
        self.assertEqual(self.solution.maxProfit(k, prices), 12)

if __name__ == '__main__':
    unittest.main()