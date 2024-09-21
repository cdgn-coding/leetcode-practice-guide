import unittest
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        pass

class TestCountNodes(unittest.TestCase):
    def test_empty_tree(self):
        solution = Solution()
        self.assertEqual(solution.countNodes(None), 0)

    def test_single_node(self):
        solution = Solution()
        root = TreeNode(1)
        self.assertEqual(solution.countNodes(root), 1)

    def test_complete_tree(self):
        solution = Solution()
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        root.right.left = TreeNode(6)
        self.assertEqual(solution.countNodes(root), 6)

    def test_full_tree(self):
        solution = Solution()
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        root.right.left = TreeNode(6)
        root.right.right = TreeNode(7)
        self.assertEqual(solution.countNodes(root), 7)

    def test_large_tree(self):
        solution = Solution()
        root = TreeNode(1)
        current = root
        for i in range(2, 50001):
            if i % 2 == 0:
                current.left = TreeNode(i)
                current = current.left
            else:
                current.right = TreeNode(i)
                current = current.right
        self.assertEqual(solution.countNodes(root), 50000)

if __name__ == '__main__':
    unittest.main()