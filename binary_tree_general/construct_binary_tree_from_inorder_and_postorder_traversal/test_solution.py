import unittest
from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        pass  # Placeholder for the actual implementation

class TestBuildTree(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        inorder = [9,3,15,20,7]
        postorder = [9,15,7,20,3]
        root = self.solution.buildTree(inorder, postorder)
        self.assertEqual(root.val, 3)
        self.assertEqual(root.left.val, 9)
        self.assertEqual(root.right.val, 20)
        self.assertIsNone(root.left.left)
        self.assertIsNone(root.left.right)
        self.assertEqual(root.right.left.val, 15)
        self.assertEqual(root.right.right.val, 7)

    def test_example_2(self):
        inorder = [-1]
        postorder = [-1]
        root = self.solution.buildTree(inorder, postorder)
        self.assertEqual(root.val, -1)
        self.assertIsNone(root.left)
        self.assertIsNone(root.right)

    def test_empty_input(self):
        inorder = []
        postorder = []
        root = self.solution.buildTree(inorder, postorder)
        self.assertIsNone(root)

    def test_larger_tree(self):
        inorder = [4,2,5,1,6,3,7]
        postorder = [4,5,2,6,7,3,1]
        root = self.solution.buildTree(inorder, postorder)
        self.assertEqual(root.val, 1)
        self.assertEqual(root.left.val, 2)
        self.assertEqual(root.right.val, 3)
        self.assertEqual(root.left.left.val, 4)
        self.assertEqual(root.left.right.val, 5)
        self.assertEqual(root.right.left.val, 6)
        self.assertEqual(root.right.right.val, 7)

    def test_negative_values(self):
        inorder = [-4,-2,-5,-1,-6,-3,-7]
        postorder = [-4,-5,-2,-6,-7,-3,-1]
        root = self.solution.buildTree(inorder, postorder)
        self.assertEqual(root.val, -1)
        self.assertEqual(root.left.val, -2)
        self.assertEqual(root.right.val, -3)
        self.assertEqual(root.left.left.val, -4)
        self.assertEqual(root.left.right.val, -5)
        self.assertEqual(root.right.left.val, -6)
        self.assertEqual(root.right.right.val, -7)

if __name__ == '__main__':
    unittest.main()