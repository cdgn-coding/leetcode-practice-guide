import unittest
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        pass

class TestMaxDepth(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        root = TreeNode(3)
        root.left = TreeNode(9)
        root.right = TreeNode(20)
        root.right.left = TreeNode(15)
        root.right.right = TreeNode(7)
        self.assertEqual(self.solution.maxDepth(root), 3)

    def test_example_2(self):
        root = TreeNode(1)
        root.right = TreeNode(2)
        self.assertEqual(self.solution.maxDepth(root), 2)

    def test_empty_tree(self):
        self.assertEqual(self.solution.maxDepth(None), 0)

    def test_single_node(self):
        root = TreeNode(1)
        self.assertEqual(self.solution.maxDepth(root), 1)

    def test_left_skewed_tree(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.left.left = TreeNode(3)
        root.left.left.left = TreeNode(4)
        self.assertEqual(self.solution.maxDepth(root), 4)

    def test_right_skewed_tree(self):
        root = TreeNode(1)
        root.right = TreeNode(2)
        root.right.right = TreeNode(3)
        root.right.right.right = TreeNode(4)
        self.assertEqual(self.solution.maxDepth(root), 4)

    def test_balanced_tree(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        root.right.left = TreeNode(6)
        root.right.right = TreeNode(7)
        self.assertEqual(self.solution.maxDepth(root), 3)

if __name__ == '__main__':
    unittest.main()