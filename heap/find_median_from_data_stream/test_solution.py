import unittest
from typing import List

class TestMedianFinder(unittest.TestCase):
    def setUp(self):
        self.median_finder = MedianFinder()

    def test_example_1(self):
        self.median_finder.addNum(1)
        self.median_finder.addNum(2)
        self.assertAlmostEqual(self.median_finder.findMedian(), 1.5, delta=1e-5)
        self.median_finder.addNum(3)
        self.assertAlmostEqual(self.median_finder.findMedian(), 2.0, delta=1e-5)

    def test_single_element(self):
        self.median_finder.addNum(5)
        self.assertEqual(self.median_finder.findMedian(), 5.0)

    def test_even_number_of_elements(self):
        self.median_finder.addNum(1)
        self.median_finder.addNum(2)
        self.median_finder.addNum(3)
        self.median_finder.addNum(4)
        self.assertAlmostEqual(self.median_finder.findMedian(), 2.5, delta=1e-5)

    def test_odd_number_of_elements(self):
        self.median_finder.addNum(1)
        self.median_finder.addNum(2)
        self.median_finder.addNum(3)
        self.median_finder.addNum(4)
        self.median_finder.addNum(5)
        self.assertEqual(self.median_finder.findMedian(), 3.0)

    def test_negative_numbers(self):
        self.median_finder.addNum(-1)
        self.median_finder.addNum(-2)
        self.median_finder.addNum(-3)
        self.assertAlmostEqual(self.median_finder.findMedian(), -2.0, delta=1e-5)

    def test_mixed_positive_and_negative(self):
        self.median_finder.addNum(-1)
        self.median_finder.addNum(1)
        self.median_finder.addNum(0)
        self.assertEqual(self.median_finder.findMedian(), 0.0)

    def test_large_numbers(self):
        self.median_finder.addNum(100000)
        self.median_finder.addNum(-100000)
        self.assertEqual(self.median_finder.findMedian(), 0.0)

    def test_duplicate_numbers(self):
        self.median_finder.addNum(1)
        self.median_finder.addNum(1)
        self.median_finder.addNum(2)
        self.assertAlmostEqual(self.median_finder.findMedian(), 1.0, delta=1e-5)

if __name__ == '__main__':
    unittest.main()