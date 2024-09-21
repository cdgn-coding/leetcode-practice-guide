import unittest
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        pass

class TestMaxPathSum(unittest.TestCase):
    def test_example_1(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        self.assertEqual(Solution().maxPathSum(root), 6)

    def test_example_2(self):
        root = TreeNode(-10)
        root.left = TreeNode(9)
        root.right = TreeNode(20)
        root.right.left = TreeNode(15)
        root.right.right = TreeNode(7)
        self.assertEqual(Solution().maxPathSum(root), 42)

    def test_single_node(self):
        root = TreeNode(1)
        self.assertEqual(Solution().maxPathSum(root), 1)

    def test_all_negative(self):
        root = TreeNode(-1)
        root.left = TreeNode(-2)
        root.right = TreeNode(-3)
        self.assertEqual(Solution().maxPathSum(root), -1)

    def test_zigzag_path(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.right.right = TreeNode(5)
        self.assertEqual(Solution().maxPathSum(root), 11)

    def test_large_values(self):
        root = TreeNode(1000)
        root.left = TreeNode(-1000)
        root.right = TreeNode(1000)
        self.assertEqual(Solution().maxPathSum(root), 2000)

if __name__ == '__main__':
    unittest.main()