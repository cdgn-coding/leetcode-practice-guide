import unittest

class TestSolution(unittest.TestCase):
    def test_convert(self):
        solution = Solution()
        
        s = "PAYPALISHIRING"
        numRows = 3
        self.assertEqual(solution.convert(s, numRows), "PAHNAPLSIIGYIR")
        
        s = "PAYPALISHIRING"
        numRows = 4
        self.assertEqual(solution.convert(s, numRows), "PINALSIGYAHRPI")
        
        s = "A"
        numRows = 1
        self.assertEqual(solution.convert(s, numRows), "A")
        
        s = "ABC"
        numRows = 1
        self.assertEqual(solution.convert(s, numRows), "ABC")
        
        s = "ABC"
        numRows = 2
        self.assertEqual(solution.convert(s, numRows), "ACB")

if __name__ == '__main__':
    unittest.main()