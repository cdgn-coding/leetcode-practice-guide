import unittest
from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        pass  # Placeholder for the actual implementation

class TestRightSideView(unittest.TestCase):
    def test_example_1(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.right = TreeNode(5)
        root.right.right = TreeNode(4)
        
        solution = Solution()
        self.assertEqual(solution.rightSideView(root), [1, 3, 4])
    
    def test_example_2(self):
        root = TreeNode(1)
        root.right = TreeNode(3)
        
        solution = Solution()
        self.assertEqual(solution.rightSideView(root), [1, 3])
    
    def test_example_3(self):
        solution = Solution()
        self.assertEqual(solution.rightSideView(None), [])
    
    def test_single_node(self):
        root = TreeNode(1)
        
        solution = Solution()
        self.assertEqual(solution.rightSideView(root), [1])
    
    def test_left_side_deeper(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.left.left = TreeNode(3)
        
        solution = Solution()
        self.assertEqual(solution.rightSideView(root), [1, 2, 3])
    
    def test_zigzag(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.right = TreeNode(4)
        root.left.right.left = TreeNode(5)
        
        solution = Solution()
        self.assertEqual(solution.rightSideView(root), [1, 3, 4, 5])

if __name__ == '__main__':
    unittest.main()