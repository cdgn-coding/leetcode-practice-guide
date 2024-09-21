import unittest

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        pass

class TestLetterCombinations(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(sorted(self.solution.letterCombinations("23")),
                         sorted(["ad","ae","af","bd","be","bf","cd","ce","cf"]))

    def test_example_2(self):
        self.assertEqual(self.solution.letterCombinations(""), [])

    def test_example_3(self):
        self.assertEqual(sorted(self.solution.letterCombinations("2")),
                         sorted(["a","b","c"]))

    def test_single_digit_4(self):
        self.assertEqual(sorted(self.solution.letterCombinations("4")),
                         sorted(["g","h","i"]))

    def test_two_digits_45(self):
        self.assertEqual(sorted(self.solution.letterCombinations("45")),
                         sorted(["gj","gk","gl","hj","hk","hl","ij","ik","il"]))

    def test_four_digits_2345(self):
        result = self.solution.letterCombinations("2345")
        self.assertEqual(len(result), 81)
        self.assertTrue("adgj" in result)
        self.assertTrue("cfmp" in result)

    def test_invalid_input(self):
        self.assertEqual(self.solution.letterCombinations("1"), [])
        self.assertEqual(self.solution.letterCombinations("0"), [])

if __name__ == '__main__':
    unittest.main()