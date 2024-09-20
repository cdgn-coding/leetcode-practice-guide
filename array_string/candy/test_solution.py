import unittest

class TestSolution(unittest.TestCase):
    def test_example1(self):
        ratings = [1, 0, 2]
        expected_output = 5
        self.assertEqual(Solution().candy(ratings), expected_output)

    def test_example2(self):
        ratings = [1, 2, 2]
        expected_output = 4
        self.assertEqual(Solution().candy(ratings), expected_output)

    def test_all_equal_ratings(self):
        ratings = [1, 1, 1, 1, 1]
        expected_output = 5
        self.assertEqual(Solution().candy(ratings), expected_output)

    def test_descending_ratings(self):
        ratings = [5, 4, 3, 2, 1]
        expected_output = 15
        self.assertEqual(Solution().candy(ratings), expected_output)

    def test_ascending_ratings(self):
        ratings = [1, 2, 3, 4, 5]
        expected_output = 15
        self.assertEqual(Solution().candy(ratings), expected_output)

    def test_single_child(self):
        ratings = [1]
        expected_output = 1
        self.assertEqual(Solution().candy(ratings), expected_output)

if __name__ == '__main__':
    unittest.main()