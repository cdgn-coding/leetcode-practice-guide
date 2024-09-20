import unittest

class TestSolution(unittest.TestCase):
    def test_reverse_words(self):
        solution = Solution()
        
        s1 = "the sky is blue"
        output1 = "blue is sky the"
        self.assertEqual(solution.reverseWords(s1), output1)
        
        s2 = "  hello world  "
        output2 = "world hello"
        self.assertEqual(solution.reverseWords(s2), output2)
        
        s3 = "a good   example"
        output3 = "example good a"
        self.assertEqual(solution.reverseWords(s3), output3)
        
        s4 = "  Bob    Loves  Alice   "
        output4 = "Alice Loves Bob"
        self.assertEqual(solution.reverseWords(s4), output4)
        
        s5 = "Alice does not even like bob"
        output5 = "bob like even not does Alice"
        self.assertEqual(solution.reverseWords(s5), output5)

if __name__ == '__main__':
    unittest.main()