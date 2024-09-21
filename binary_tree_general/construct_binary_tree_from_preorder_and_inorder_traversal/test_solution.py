import unittest
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        pass

class TestBuildTree(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        preorder = [3,9,20,15,7]
        inorder = [9,3,15,20,7]
        result = self.solution.buildTree(preorder, inorder)
        self.assertEqual(result.val, 3)
        self.assertEqual(result.left.val, 9)
        self.assertEqual(result.right.val, 20)
        self.assertEqual(result.right.left.val, 15)
        self.assertEqual(result.right.right.val, 7)

    def test_example_2(self):
        preorder = [-1]
        inorder = [-1]
        result = self.solution.buildTree(preorder, inorder)
        self.assertEqual(result.val, -1)
        self.assertIsNone(result.left)
        self.assertIsNone(result.right)

    def test_empty_input(self):
        preorder = []
        inorder = []
        result = self.solution.buildTree(preorder, inorder)
        self.assertIsNone(result)

    def test_single_node(self):
        preorder = [1]
        inorder = [1]
        result = self.solution.buildTree(preorder, inorder)
        self.assertEqual(result.val, 1)
        self.assertIsNone(result.left)
        self.assertIsNone(result.right)

    def test_left_skewed_tree(self):
        preorder = [3,2,1]
        inorder = [1,2,3]
        result = self.solution.buildTree(preorder, inorder)
        self.assertEqual(result.val, 3)
        self.assertEqual(result.left.val, 2)
        self.assertEqual(result.left.left.val, 1)
        self.assertIsNone(result.right)

    def test_right_skewed_tree(self):
        preorder = [1,2,3]
        inorder = [1,2,3]
        result = self.solution.buildTree(preorder, inorder)
        self.assertEqual(result.val, 1)
        self.assertEqual(result.right.val, 2)
        self.assertEqual(result.right.right.val, 3)
        self.assertIsNone(result.left)

    def test_complex_tree(self):
        preorder = [3,9,20,15,7]
        inorder = [9,3,15,20,7]
        result = self.solution.buildTree(preorder, inorder)
        self.assertEqual(result.val, 3)
        self.assertEqual(result.left.val, 9)
        self.assertEqual(result.right.val, 20)
        self.assertEqual(result.right.left.val, 15)
        self.assertEqual(result.right.right.val, 7)

if __name__ == '__main__':
    unittest.main()