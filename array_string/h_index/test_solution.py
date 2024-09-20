import unittest

class TestSolution(unittest.TestCase):
    def test_hIndex(self):
        solution = Solution()
        
        citations1 = [3, 0, 6, 1, 5]
        self.assertEqual(solution.hIndex(citations1), 3)
        
        citations2 = [1, 3, 1]
        self.assertEqual(solution.hIndex(citations2), 1)
        
        citations3 = [0]
        self.assertEqual(solution.hIndex(citations3), 0)
        
        citations4 = [100]
        self.assertEqual(solution.hIndex(citations4), 1)
        
        citations5 = [0, 0, 0]
        self.assertEqual(solution.hIndex(citations5), 0)
        
        citations6 = [1, 1, 1, 1, 1]
        self.assertEqual(solution.hIndex(citations6), 1)
        
        citations7 = [5, 5, 5, 5, 5]
        self.assertEqual(solution.hIndex(citations7), 5)
        
        citations8 = [1, 2, 3, 4, 5]
        self.assertEqual(solution.hIndex(citations8), 3)
        
        citations9 = [5, 4, 3, 2, 1]
        self.assertEqual(solution.hIndex(citations9), 3)
        
        citations10 = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]
        self.assertEqual(solution.hIndex(citations10), 3)

if __name__ == '__main__':
    unittest.main()