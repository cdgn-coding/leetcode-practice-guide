import unittest

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root):
        pass

class TestInvertBinaryTree(unittest.TestCase):
    def test_example_1(self):
        root = TreeNode(4)
        root.left = TreeNode(2)
        root.right = TreeNode(7)
        root.left.left = TreeNode(1)
        root.left.right = TreeNode(3)
        root.right.left = TreeNode(6)
        root.right.right = TreeNode(9)
        
        solution = Solution()
        inverted = solution.invertTree(root)
        
        self.assertEqual(inverted.val, 4)
        self.assertEqual(inverted.left.val, 7)
        self.assertEqual(inverted.right.val, 2)
        self.assertEqual(inverted.left.left.val, 9)
        self.assertEqual(inverted.left.right.val, 6)
        self.assertEqual(inverted.right.left.val, 3)
        self.assertEqual(inverted.right.right.val, 1)

    def test_example_2(self):
        root = TreeNode(2)
        root.left = TreeNode(1)
        root.right = TreeNode(3)
        
        solution = Solution()
        inverted = solution.invertTree(root)
        
        self.assertEqual(inverted.val, 2)
        self.assertEqual(inverted.left.val, 3)
        self.assertEqual(inverted.right.val, 1)

    def test_example_3(self):
        root = None
        
        solution = Solution()
        inverted = solution.invertTree(root)
        
        self.assertIsNone(inverted)

    def test_single_node(self):
        root = TreeNode(1)
        
        solution = Solution()
        inverted = solution.invertTree(root)
        
        self.assertEqual(inverted.val, 1)
        self.assertIsNone(inverted.left)
        self.assertIsNone(inverted.right)

    def test_deep_tree(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        root.right.left = TreeNode(6)
        root.right.right = TreeNode(7)
        root.left.left.left = TreeNode(8)
        
        solution = Solution()
        inverted = solution.invertTree(root)
        
        self.assertEqual(inverted.val, 1)
        self.assertEqual(inverted.left.val, 3)
        self.assertEqual(inverted.right.val, 2)
        self.assertEqual(inverted.left.left.val, 7)
        self.assertEqual(inverted.left.right.val, 6)
        self.assertEqual(inverted.right.left.val, 5)
        self.assertEqual(inverted.right.right.val, 4)
        self.assertEqual(inverted.right.right.right.val, 8)

if __name__ == '__main__':
    unittest.main()