import unittest

class TestSolution(unittest.TestCase):
    def test_strStr(self):
        solution = Solution()
        
        haystack = "sadbutsad"
        needle = "sad"
        self.assertEqual(solution.strStr(haystack, needle), 0)
        
        haystack = "leetcode"
        needle = "leeto"
        self.assertEqual(solution.strStr(haystack, needle), -1)
        
        haystack = ""
        needle = ""
        self.assertEqual(solution.strStr(haystack, needle), 0)
        
        haystack = "a"
        needle = "a"
        self.assertEqual(solution.strStr(haystack, needle), 0)
        
        haystack = "mississippi"
        needle = "issip"
        self.assertEqual(solution.strStr(haystack, needle), 4)

if __name__ == '__main__':
    unittest.main()