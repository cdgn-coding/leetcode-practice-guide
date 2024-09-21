import unittest
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        pass

class TestLevelOrderTraversal(unittest.TestCase):
    def test_example_1(self):
        root = TreeNode(3)
        root.left = TreeNode(9)
        root.right = TreeNode(20)
        root.right.left = TreeNode(15)
        root.right.right = TreeNode(7)
        
        solution = Solution()
        self.assertEqual(solution.levelOrder(root), [[3],[9,20],[15,7]])
    
    def test_example_2(self):
        root = TreeNode(1)
        
        solution = Solution()
        self.assertEqual(solution.levelOrder(root), [[1]])
    
    def test_example_3(self):
        solution = Solution()
        self.assertEqual(solution.levelOrder(None), [])
    
    def test_single_level(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        
        solution = Solution()
        self.assertEqual(solution.levelOrder(root), [[1],[2,3]])
    
    def test_unbalanced_tree(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.left.left = TreeNode(3)
        root.left.left.left = TreeNode(4)
        
        solution = Solution()
        self.assertEqual(solution.levelOrder(root), [[1],[2],[3],[4]])
    
    def test_full_binary_tree(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        root.right.left = TreeNode(6)
        root.right.right = TreeNode(7)
        
        solution = Solution()
        self.assertEqual(solution.levelOrder(root), [[1],[2,3],[4,5,6,7]])

if __name__ == '__main__':
    unittest.main()