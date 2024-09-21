import unittest
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        pass

class TestFlattenBinaryTree(unittest.TestCase):
    def test_example_1(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(5)
        root.left.left = TreeNode(3)
        root.left.right = TreeNode(4)
        root.right.right = TreeNode(6)
        
        Solution().flatten(root)
        
        expected = [1, None, 2, None, 3, None, 4, None, 5, None, 6]
        self.assertListEqual(self.tree_to_list(root), expected)

    def test_example_2(self):
        root = None
        Solution().flatten(root)
        self.assertIsNone(root)

    def test_example_3(self):
        root = TreeNode(0)
        Solution().flatten(root)
        self.assertListEqual(self.tree_to_list(root), [0])

    def test_single_node(self):
        root = TreeNode(1)
        Solution().flatten(root)
        self.assertListEqual(self.tree_to_list(root), [1])

    def test_left_skewed_tree(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.left.left = TreeNode(3)
        Solution().flatten(root)
        self.assertListEqual(self.tree_to_list(root), [1, None, 2, None, 3])

    def test_right_skewed_tree(self):
        root = TreeNode(1)
        root.right = TreeNode(2)
        root.right.right = TreeNode(3)
        Solution().flatten(root)
        self.assertListEqual(self.tree_to_list(root), [1, None, 2, None, 3])

    def test_balanced_tree(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        root.right.left = TreeNode(6)
        root.right.right = TreeNode(7)
        Solution().flatten(root)
        self.assertListEqual(self.tree_to_list(root), [1, None, 2, None, 4, None, 5, None, 3, None, 6, None, 7])

    def tree_to_list(self, root):
        result = []
        while root:
            result.append(root.val)
            result.append(None)
            root = root.right
        return result[:-1]  # Remove the last None

if __name__ == '__main__':
    unittest.main()