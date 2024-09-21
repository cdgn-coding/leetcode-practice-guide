import unittest
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        pass

class TestSumNumbers(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        self.assertEqual(self.solution.sumNumbers(root), 25)

    def test_example_2(self):
        root = TreeNode(4)
        root.left = TreeNode(9)
        root.right = TreeNode(0)
        root.left.left = TreeNode(5)
        root.left.right = TreeNode(1)
        self.assertEqual(self.solution.sumNumbers(root), 1026)

    def test_single_node(self):
        root = TreeNode(5)
        self.assertEqual(self.solution.sumNumbers(root), 5)

    def test_left_skewed_tree(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.left.left = TreeNode(3)
        self.assertEqual(self.solution.sumNumbers(root), 123)

    def test_right_skewed_tree(self):
        root = TreeNode(1)
        root.right = TreeNode(2)
        root.right.right = TreeNode(3)
        self.assertEqual(self.solution.sumNumbers(root), 123)

    def test_zero_root(self):
        root = TreeNode(0)
        root.left = TreeNode(1)
        root.right = TreeNode(2)
        self.assertEqual(self.solution.sumNumbers(root), 3)

    def test_all_zeros(self):
        root = TreeNode(0)
        root.left = TreeNode(0)
        root.right = TreeNode(0)
        self.assertEqual(self.solution.sumNumbers(root), 0)

if __name__ == '__main__':
    unittest.main()