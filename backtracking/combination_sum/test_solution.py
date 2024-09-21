import unittest

class TestCombinationSum(unittest.TestCase):
    def test_example1(self):
        candidates = [2,3,6,7]
        target = 7
        expected = [[2,2,3],[7]]
        self.assertCountEqual(Solution().combinationSum(candidates, target), expected)

    def test_example2(self):
        candidates = [2,3,5]
        target = 8
        expected = [[2,2,2,2],[2,3,3],[3,5]]
        self.assertCountEqual(Solution().combinationSum(candidates, target), expected)

    def test_example3(self):
        candidates = [2]
        target = 1
        expected = []
        self.assertEqual(Solution().combinationSum(candidates, target), expected)

    def test_empty_candidates(self):
        candidates = []
        target = 5
        expected = []
        self.assertEqual(Solution().combinationSum(candidates, target), expected)

    def test_single_candidate_equal_to_target(self):
        candidates = [5]
        target = 5
        expected = [[5]]
        self.assertEqual(Solution().combinationSum(candidates, target), expected)

    def test_large_numbers(self):
        candidates = [10, 20, 30, 40]
        target = 100
        expected = [[10,10,10,10,10,10,10,10,10,10],[10,10,10,10,10,10,10,10,20],[10,10,10,10,10,10,20,20],[10,10,10,10,20,20,20],[10,10,10,30,40],[10,10,20,20,20,20],[10,10,20,30,30],[10,20,30,40],[20,20,20,20,20],[20,20,20,40],[20,30,30,20],[30,30,40]]
        self.assertCountEqual(Solution().combinationSum(candidates, target), expected)

    def test_no_possible_combinations(self):
        candidates = [5, 10, 15]
        target = 3
        expected = []
        self.assertEqual(Solution().combinationSum(candidates, target), expected)

if __name__ == '__main__':
    unittest.main()