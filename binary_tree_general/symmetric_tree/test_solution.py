import unittest
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        pass

class TestSymmetricTree(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_symmetric_tree(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(2)
        root.left.left = TreeNode(3)
        root.left.right = TreeNode(4)
        root.right.left = TreeNode(4)
        root.right.right = TreeNode(3)
        self.assertTrue(self.solution.isSymmetric(root))

    def test_asymmetric_tree(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(2)
        root.left.right = TreeNode(3)
        root.right.right = TreeNode(3)
        self.assertFalse(self.solution.isSymmetric(root))

    def test_single_node_tree(self):
        root = TreeNode(1)
        self.assertTrue(self.solution.isSymmetric(root))

    def test_null_tree(self):
        self.assertTrue(self.solution.isSymmetric(None))

    def test_asymmetric_complex_tree(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(2)
        root.left.left = TreeNode(3)
        root.left.right = TreeNode(4)
        root.right.left = TreeNode(4)
        root.right.right = TreeNode(5)
        self.assertFalse(self.solution.isSymmetric(root))

    def test_symmetric_complex_tree(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(2)
        root.left.left = TreeNode(3)
        root.left.right = TreeNode(4)
        root.right.left = TreeNode(4)
        root.right.right = TreeNode(3)
        root.left.left.left = TreeNode(5)
        root.left.left.right = TreeNode(6)
        root.left.right.left = TreeNode(7)
        root.left.right.right = TreeNode(8)
        root.right.left.left = TreeNode(8)
        root.right.left.right = TreeNode(7)
        root.right.right.left = TreeNode(6)
        root.right.right.right = TreeNode(5)
        self.assertTrue(self.solution.isSymmetric(root))

if __name__ == '__main__':
    unittest.main()