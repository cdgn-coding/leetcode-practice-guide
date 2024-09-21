import unittest

class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        pass

class TestQuadTree(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        grid = [[0,1],[1,0]]
        result = self.solution.construct(grid)
        self.assertFalse(result.isLeaf)
        self.assertTrue(result.topLeft.isLeaf and result.topLeft.val == False)
        self.assertTrue(result.topRight.isLeaf and result.topRight.val == True)
        self.assertTrue(result.bottomLeft.isLeaf and result.bottomLeft.val == True)
        self.assertTrue(result.bottomRight.isLeaf and result.bottomRight.val == False)

    def test_example_2(self):
        grid = [[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],
                [1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0]]
        result = self.solution.construct(grid)
        self.assertFalse(result.isLeaf)
        self.assertTrue(result.topLeft.isLeaf and result.topLeft.val == True)
        self.assertFalse(result.topRight.isLeaf)
        self.assertTrue(result.bottomLeft.isLeaf and result.bottomLeft.val == True)
        self.assertTrue(result.bottomRight.isLeaf and result.bottomRight.val == False)

    def test_single_element_grid(self):
        grid = [[1]]
        result = self.solution.construct(grid)
        self.assertTrue(result.isLeaf and result.val == True)

    def test_all_zeros(self):
        grid = [[0,0],[0,0]]
        result = self.solution.construct(grid)
        self.assertTrue(result.isLeaf and result.val == False)

    def test_all_ones(self):
        grid = [[1,1],[1,1]]
        result = self.solution.construct(grid)
        self.assertTrue(result.isLeaf and result.val == True)

    def test_mixed_values(self):
        grid = [[1,1,0,0],[1,1,0,0],[0,0,1,1],[0,0,1,1]]
        result = self.solution.construct(grid)
        self.assertFalse(result.isLeaf)
        self.assertTrue(result.topLeft.isLeaf and result.topLeft.val == True)
        self.assertTrue(result.topRight.isLeaf and result.topRight.val == False)
        self.assertTrue(result.bottomLeft.isLeaf and result.bottomLeft.val == False)
        self.assertTrue(result.bottomRight.isLeaf and result.bottomRight.val == True)

if __name__ == '__main__':
    unittest.main()