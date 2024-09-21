import unittest

class Solution:
    def hammingWeight(self, n: int) -> int:
        pass

class TestHammingWeight(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.hammingWeight(11), 3)

    def test_example_2(self):
        self.assertEqual(self.solution.hammingWeight(128), 1)

    def test_example_3(self):
        self.assertEqual(self.solution.hammingWeight(2147483645), 30)

    def test_zero(self):
        self.assertEqual(self.solution.hammingWeight(0), 0)

    def test_one(self):
        self.assertEqual(self.solution.hammingWeight(1), 1)

    def test_all_ones(self):
        self.assertEqual(self.solution.hammingWeight(2**32 - 1), 32)

    def test_power_of_two(self):
        self.assertEqual(self.solution.hammingWeight(2**16), 1)

    def test_alternating_bits(self):
        self.assertEqual(self.solution.hammingWeight(0b10101010101010101010101010101010), 16)

if __name__ == '__main__':
    unittest.main()