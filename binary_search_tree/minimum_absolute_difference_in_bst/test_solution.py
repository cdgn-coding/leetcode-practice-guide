import unittest
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        pass  # Placeholder for the actual implementation

class TestMinimumAbsoluteDifference(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        root = TreeNode(4)
        root.left = TreeNode(2)
        root.right = TreeNode(6)
        root.left.left = TreeNode(1)
        root.left.right = TreeNode(3)
        self.assertEqual(self.solution.getMinimumDifference(root), 1)

    def test_example_2(self):
        root = TreeNode(1)
        root.left = TreeNode(0)
        root.right = TreeNode(48)
        root.right.left = TreeNode(12)
        root.right.right = TreeNode(49)
        self.assertEqual(self.solution.getMinimumDifference(root), 1)

    def test_minimum_tree(self):
        root = TreeNode(1)
        root.right = TreeNode(2)
        self.assertEqual(self.solution.getMinimumDifference(root), 1)

    def test_balanced_tree(self):
        root = TreeNode(4)
        root.left = TreeNode(2)
        root.right = TreeNode(6)
        root.left.left = TreeNode(1)
        root.left.right = TreeNode(3)
        root.right.left = TreeNode(5)
        root.right.right = TreeNode(7)
        self.assertEqual(self.solution.getMinimumDifference(root), 1)

    def test_unbalanced_tree(self):
        root = TreeNode(10)
        root.left = TreeNode(5)
        root.left.left = TreeNode(2)
        root.left.left.left = TreeNode(1)
        root.left.right = TreeNode(7)
        root.right = TreeNode(15)
        root.right.right = TreeNode(20)
        self.assertEqual(self.solution.getMinimumDifference(root), 1)

    def test_large_difference(self):
        root = TreeNode(0)
        root.right = TreeNode(100000)
        self.assertEqual(self.solution.getMinimumDifference(root), 100000)

if __name__ == '__main__':
    unittest.main()