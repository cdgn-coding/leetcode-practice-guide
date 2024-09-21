import unittest
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        pass

class TestValidBST(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        root = TreeNode(2)
        root.left = TreeNode(1)
        root.right = TreeNode(3)
        self.assertTrue(self.solution.isValidBST(root))

    def test_example_2(self):
        root = TreeNode(5)
        root.left = TreeNode(1)
        root.right = TreeNode(4)
        root.right.left = TreeNode(3)
        root.right.right = TreeNode(6)
        self.assertFalse(self.solution.isValidBST(root))

    def test_single_node(self):
        root = TreeNode(1)
        self.assertTrue(self.solution.isValidBST(root))

    def test_two_nodes_valid(self):
        root = TreeNode(2)
        root.left = TreeNode(1)
        self.assertTrue(self.solution.isValidBST(root))

    def test_two_nodes_invalid(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        self.assertFalse(self.solution.isValidBST(root))

    def test_three_nodes_invalid(self):
        root = TreeNode(2)
        root.left = TreeNode(3)
        root.right = TreeNode(1)
        self.assertFalse(self.solution.isValidBST(root))

    def test_complex_valid_bst(self):
        root = TreeNode(8)
        root.left = TreeNode(3)
        root.right = TreeNode(10)
        root.left.left = TreeNode(1)
        root.left.right = TreeNode(6)
        root.left.right.left = TreeNode(4)
        root.left.right.right = TreeNode(7)
        root.right.right = TreeNode(14)
        root.right.right.left = TreeNode(13)
        self.assertTrue(self.solution.isValidBST(root))

    def test_complex_invalid_bst(self):
        root = TreeNode(8)
        root.left = TreeNode(3)
        root.right = TreeNode(10)
        root.left.left = TreeNode(1)
        root.left.right = TreeNode(6)
        root.left.right.left = TreeNode(4)
        root.left.right.right = TreeNode(7)
        root.right.right = TreeNode(14)
        root.right.right.left = TreeNode(8)  # Invalid: 8 <= 8
        self.assertFalse(self.solution.isValidBST(root))

    def test_minimum_value(self):
        root = TreeNode(-2**31)
        root.right = TreeNode(2**31 - 1)
        self.assertTrue(self.solution.isValidBST(root))

    def test_maximum_value(self):
        root = TreeNode(2**31 - 1)
        root.left = TreeNode(-2**31)
        self.assertTrue(self.solution.isValidBST(root))

if __name__ == '__main__':
    unittest.main()