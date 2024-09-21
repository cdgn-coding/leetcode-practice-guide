import unittest
from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        pass

class TestAverageOfLevels(unittest.TestCase):
    def test_example_1(self):
        root = TreeNode(3)
        root.left = TreeNode(9)
        root.right = TreeNode(20)
        root.right.left = TreeNode(15)
        root.right.right = TreeNode(7)
        
        solution = Solution()
        result = solution.averageOfLevels(root)
        
        expected = [3.00000, 14.50000, 11.00000]
        self.assertEqual(len(result), len(expected))
        for r, e in zip(result, expected):
            self.assertAlmostEqual(r, e, places=5)

    def test_example_2(self):
        root = TreeNode(3)
        root.left = TreeNode(9)
        root.right = TreeNode(20)
        root.left.left = TreeNode(15)
        root.left.right = TreeNode(7)
        
        solution = Solution()
        result = solution.averageOfLevels(root)
        
        expected = [3.00000, 14.50000, 11.00000]
        self.assertEqual(len(result), len(expected))
        for r, e in zip(result, expected):
            self.assertAlmostEqual(r, e, places=5)

    def test_single_node(self):
        root = TreeNode(1)
        
        solution = Solution()
        result = solution.averageOfLevels(root)
        
        expected = [1.00000]
        self.assertEqual(len(result), len(expected))
        for r, e in zip(result, expected):
            self.assertAlmostEqual(r, e, places=5)

    def test_unbalanced_tree(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.left.left = TreeNode(3)
        root.left.left.left = TreeNode(4)
        
        solution = Solution()
        result = solution.averageOfLevels(root)
        
        expected = [1.00000, 2.00000, 3.00000, 4.00000]
        self.assertEqual(len(result), len(expected))
        for r, e in zip(result, expected):
            self.assertAlmostEqual(r, e, places=5)

if __name__ == '__main__':
    unittest.main()