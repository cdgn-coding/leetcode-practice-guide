import unittest

class Solution:
    def romanToInt(self, s: str) -> int:
        pass

class TestSolution(unittest.TestCase):
    def test_example1(self):
        s = Solution()
        self.assertEqual(s.romanToInt("III"), 3)

    def test_example2(self):
        s = Solution()
        self.assertEqual(s.romanToInt("LVIII"), 58)

    def test_example3(self):
        s = Solution()
        self.assertEqual(s.romanToInt("MCMXCIV"), 1994)

    def test_single_symbol(self):
        s = Solution()
        self.assertEqual(s.romanToInt("I"), 1)
        self.assertEqual(s.romanToInt("V"), 5)
        self.assertEqual(s.romanToInt("X"), 10)
        self.assertEqual(s.romanToInt("L"), 50)
        self.assertEqual(s.romanToInt("C"), 100)
        self.assertEqual(s.romanToInt("D"), 500)
        self.assertEqual(s.romanToInt("M"), 1000)

    def test_subtractive_notation(self):
        s = Solution()
        self.assertEqual(s.romanToInt("IV"), 4)
        self.assertEqual(s.romanToInt("IX"), 9)
        self.assertEqual(s.romanToInt("XL"), 40)
        self.assertEqual(s.romanToInt("XC"), 90)
        self.assertEqual(s.romanToInt("CD"), 400)
        self.assertEqual(s.romanToInt("CM"), 900)

    def test_boundary_values(self):
        s = Solution()
        self.assertEqual(s.romanToInt("I"), 1)
        self.assertEqual(s.romanToInt("MMMCMXCIX"), 3999)

if __name__ == '__main__':
    unittest.main()