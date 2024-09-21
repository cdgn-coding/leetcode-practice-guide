import unittest
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        pass

class TestSameTree(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        p = TreeNode(1, TreeNode(2), TreeNode(3))
        q = TreeNode(1, TreeNode(2), TreeNode(3))
        self.assertTrue(self.solution.isSameTree(p, q))

    def test_example_2(self):
        p = TreeNode(1, TreeNode(2))
        q = TreeNode(1, None, TreeNode(2))
        self.assertFalse(self.solution.isSameTree(p, q))

    def test_example_3(self):
        p = TreeNode(1, TreeNode(2), TreeNode(1))
        q = TreeNode(1, TreeNode(1), TreeNode(2))
        self.assertFalse(self.solution.isSameTree(p, q))

    def test_empty_trees(self):
        self.assertTrue(self.solution.isSameTree(None, None))

    def test_one_empty_tree(self):
        p = TreeNode(1)
        self.assertFalse(self.solution.isSameTree(p, None))
        self.assertFalse(self.solution.isSameTree(None, p))

    def test_different_values(self):
        p = TreeNode(1, TreeNode(2), TreeNode(3))
        q = TreeNode(1, TreeNode(2), TreeNode(4))
        self.assertFalse(self.solution.isSameTree(p, q))

    def test_different_structures(self):
        p = TreeNode(1, TreeNode(2, TreeNode(3)))
        q = TreeNode(1, None, TreeNode(2, None, TreeNode(3)))
        self.assertFalse(self.solution.isSameTree(p, q))

    def test_single_node(self):
        p = TreeNode(1)
        q = TreeNode(1)
        self.assertTrue(self.solution.isSameTree(p, q))

if __name__ == '__main__':
    unittest.main()