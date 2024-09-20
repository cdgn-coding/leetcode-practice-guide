import unittest

class TestMaxProfit(unittest.TestCase):
    def test_example1(self):
        prices = [7, 1, 5, 3, 6, 4]
        self.assertEqual(maxProfit(prices), 5)

    def test_example2(self):
        prices = [7, 6, 4, 3, 1]
        self.assertEqual(maxProfit(prices), 0)

    def test_empty_prices(self):
        prices = []
        self.assertEqual(maxProfit(prices), 0)

    def test_single_price(self):
        prices = [5]
        self.assertEqual(maxProfit(prices), 0)

    def test_decreasing_prices(self):
        prices = [5, 4, 3, 2, 1]
        self.assertEqual(maxProfit(prices), 0)

    def test_increasing_prices(self):
        prices = [1, 2, 3, 4, 5]
        self.assertEqual(maxProfit(prices), 4)

    def test_fluctuating_prices(self):
        prices = [3, 2, 6, 5, 0, 3]
        self.assertEqual(maxProfit(prices), 4)

    def test_large_prices(self):
        prices = [10000, 9000, 8000, 7000, 6000, 5000]
        self.assertEqual(maxProfit(prices), 0)

if __name__ == '__main__':
    unittest.main()