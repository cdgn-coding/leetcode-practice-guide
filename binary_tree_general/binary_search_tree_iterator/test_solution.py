import unittest
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class TestBSTIterator(unittest.TestCase):
    def test_example_case(self):
        root = TreeNode(7)
        root.left = TreeNode(3)
        root.right = TreeNode(15)
        root.right.left = TreeNode(9)
        root.right.right = TreeNode(20)

        bst_iterator = BSTIterator(root)

        self.assertEqual(bst_iterator.next(), 3)
        self.assertEqual(bst_iterator.next(), 7)
        self.assertTrue(bst_iterator.hasNext())
        self.assertEqual(bst_iterator.next(), 9)
        self.assertTrue(bst_iterator.hasNext())
        self.assertEqual(bst_iterator.next(), 15)
        self.assertTrue(bst_iterator.hasNext())
        self.assertEqual(bst_iterator.next(), 20)
        self.assertFalse(bst_iterator.hasNext())

    def test_single_node(self):
        root = TreeNode(1)
        bst_iterator = BSTIterator(root)

        self.assertTrue(bst_iterator.hasNext())
        self.assertEqual(bst_iterator.next(), 1)
        self.assertFalse(bst_iterator.hasNext())

    def test_left_skewed_tree(self):
        root = TreeNode(3)
        root.left = TreeNode(2)
        root.left.left = TreeNode(1)

        bst_iterator = BSTIterator(root)

        self.assertEqual(bst_iterator.next(), 1)
        self.assertEqual(bst_iterator.next(), 2)
        self.assertEqual(bst_iterator.next(), 3)
        self.assertFalse(bst_iterator.hasNext())

    def test_right_skewed_tree(self):
        root = TreeNode(1)
        root.right = TreeNode(2)
        root.right.right = TreeNode(3)

        bst_iterator = BSTIterator(root)

        self.assertEqual(bst_iterator.next(), 1)
        self.assertEqual(bst_iterator.next(), 2)
        self.assertEqual(bst_iterator.next(), 3)
        self.assertFalse(bst_iterator.hasNext())

    def test_complex_tree(self):
        root = TreeNode(8)
        root.left = TreeNode(3)
        root.right = TreeNode(10)
        root.left.left = TreeNode(1)
        root.left.right = TreeNode(6)
        root.left.right.left = TreeNode(4)
        root.left.right.right = TreeNode(7)
        root.right.right = TreeNode(14)
        root.right.right.left = TreeNode(13)

        bst_iterator = BSTIterator(root)

        expected_order = [1, 3, 4, 6, 7, 8, 10, 13, 14]
        for val in expected_order:
            self.assertTrue(bst_iterator.hasNext())
            self.assertEqual(bst_iterator.next(), val)

        self.assertFalse(bst_iterator.hasNext())

if __name__ == '__main__':
    unittest.main()