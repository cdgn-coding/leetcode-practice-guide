import unittest

class Solution:
    def reverseBits(self, n: int) -> int:
        pass

class TestReverseBits(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.reverseBits(43261596), 964176192)

    def test_example_2(self):
        self.assertEqual(self.solution.reverseBits(4294967293), 3221225471)

    def test_zero(self):
        self.assertEqual(self.solution.reverseBits(0), 0)

    def test_all_ones(self):
        self.assertEqual(self.solution.reverseBits(4294967295), 4294967295)

    def test_alternating_bits(self):
        self.assertEqual(self.solution.reverseBits(2863311530), 1431655765)

    def test_single_one(self):
        self.assertEqual(self.solution.reverseBits(1), 2147483648)

    def test_single_one_at_end(self):
        self.assertEqual(self.solution.reverseBits(2147483648), 1)

if __name__ == '__main__':
    unittest.main()