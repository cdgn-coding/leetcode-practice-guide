import unittest
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        pass

class TestHasPathSum(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        root = TreeNode(5)
        root.left = TreeNode(4)
        root.right = TreeNode(8)
        root.left.left = TreeNode(11)
        root.left.left.left = TreeNode(7)
        root.left.left.right = TreeNode(2)
        root.right.left = TreeNode(13)
        root.right.right = TreeNode(4)
        root.right.right.right = TreeNode(1)
        self.assertTrue(self.solution.hasPathSum(root, 22))

    def test_example_2(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        self.assertFalse(self.solution.hasPathSum(root, 5))

    def test_example_3(self):
        self.assertFalse(self.solution.hasPathSum(None, 0))

    def test_single_node_true(self):
        root = TreeNode(1)
        self.assertTrue(self.solution.hasPathSum(root, 1))

    def test_single_node_false(self):
        root = TreeNode(1)
        self.assertFalse(self.solution.hasPathSum(root, 2))

    def test_negative_values(self):
        root = TreeNode(-2)
        root.left = TreeNode(-3)
        self.assertTrue(self.solution.hasPathSum(root, -5))

    def test_zero_sum(self):
        root = TreeNode(1)
        root.left = TreeNode(-1)
        self.assertTrue(self.solution.hasPathSum(root, 0))

    def test_large_tree(self):
        root = TreeNode(1)
        current = root
        for i in range(2, 5001):
            current.right = TreeNode(i)
            current = current.right
        self.assertTrue(self.solution.hasPathSum(root, sum(range(1, 5001))))

if __name__ == '__main__':
    unittest.main()