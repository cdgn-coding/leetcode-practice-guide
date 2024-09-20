import unittest

class Solution:
    def intToRoman(self, num: int) -> str:
        pass

class TestIntToRoman(unittest.TestCase):
    def test_example1(self):
        solution = Solution()
        self.assertEqual(solution.intToRoman(3749), "MMMDCCXLIX")

    def test_example2(self):
        solution = Solution()
        self.assertEqual(solution.intToRoman(58), "LVIII")

    def test_example3(self):
        solution = Solution()
        self.assertEqual(solution.intToRoman(1994), "MCMXCIV")

    def test_single_digit(self):
        solution = Solution()
        self.assertEqual(solution.intToRoman(5), "V")

    def test_lower_bound(self):
        solution = Solution()
        self.assertEqual(solution.intToRoman(1), "I")

    def test_upper_bound(self):
        solution = Solution()
        self.assertEqual(solution.intToRoman(3999), "MMMCMXCIX")

    def test_zero(self):
        solution = Solution()
        with self.assertRaises(ValueError):
            solution.intToRoman(0)

    def test_negative(self):
        solution = Solution()
        with self.assertRaises(ValueError):
            solution.intToRoman(-10)

if __name__ == '__main__':
    unittest.main()