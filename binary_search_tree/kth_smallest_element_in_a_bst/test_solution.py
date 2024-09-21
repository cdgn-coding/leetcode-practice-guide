import unittest
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        pass

class TestKthSmallest(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        root = TreeNode(3)
        root.left = TreeNode(1)
        root.right = TreeNode(4)
        root.left.right = TreeNode(2)
        self.assertEqual(self.solution.kthSmallest(root, 1), 1)

    def test_example2(self):
        root = TreeNode(5)
        root.left = TreeNode(3)
        root.right = TreeNode(6)
        root.left.left = TreeNode(2)
        root.left.right = TreeNode(4)
        root.left.left.left = TreeNode(1)
        self.assertEqual(self.solution.kthSmallest(root, 3), 3)

    def test_single_node(self):
        root = TreeNode(1)
        self.assertEqual(self.solution.kthSmallest(root, 1), 1)

    def test_balanced_tree(self):
        root = TreeNode(4)
        root.left = TreeNode(2)
        root.right = TreeNode(6)
        root.left.left = TreeNode(1)
        root.left.right = TreeNode(3)
        root.right.left = TreeNode(5)
        root.right.right = TreeNode(7)
        self.assertEqual(self.solution.kthSmallest(root, 4), 4)

    def test_unbalanced_tree(self):
        root = TreeNode(5)
        root.left = TreeNode(3)
        root.left.left = TreeNode(2)
        root.left.left.left = TreeNode(1)
        root.right = TreeNode(6)
        self.assertEqual(self.solution.kthSmallest(root, 4), 5)

    def test_k_equals_n(self):
        root = TreeNode(3)
        root.left = TreeNode(1)
        root.right = TreeNode(4)
        root.left.right = TreeNode(2)
        self.assertEqual(self.solution.kthSmallest(root, 4), 4)

if __name__ == '__main__':
    unittest.main()