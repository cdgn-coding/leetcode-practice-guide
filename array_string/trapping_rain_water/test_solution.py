import unittest

class TestSolution(unittest.TestCase):
    def test_example1(self):
        height = [0,1,0,2,1,0,1,3,2,1,2,1]
        expected = 6
        self.assertEqual(Solution().trap(height), expected)
    
    def test_example2(self):
        height = [4,2,0,3,2,5]
        expected = 9
        self.assertEqual(Solution().trap(height), expected)
    
    def test_empty_list(self):
        height = []
        expected = 0
        self.assertEqual(Solution().trap(height), expected)
    
    def test_no_water_trapped(self):
        height = [1,2,3,4,5]
        expected = 0
        self.assertEqual(Solution().trap(height), expected)
    
    def test_all_same_height(self):
        height = [2,2,2,2,2]
        expected = 0
        self.assertEqual(Solution().trap(height), expected)
    
    def test_large_input(self):
        height = [0,1,0,2,1,0,1,3,2,1,2,1] * 1000
        expected = 6000
        self.assertEqual(Solution().trap(height), expected)
    
    def test_single_element(self):
        height = [5]
        expected = 0
        self.assertEqual(Solution().trap(height), expected)

if __name__ == '__main__':
    unittest.main()