import unittest

from binary_tree.binary_tree_iterator.solution import TreeNode, BSTIteratorLinearMemory, BSTIteratorHeightMemory


class BinaryTreeIteratorTest(unittest.TestCase):
    def test_linear_memory(self):
        root = TreeNode(10)
        root.left = TreeNode(20)
        root.right = TreeNode(30)
        root.left.left = TreeNode(40)
        root.left.right = TreeNode(50)
        root.right.left = TreeNode(60)
        root.right.right = TreeNode(70)

        expected = [40, 20, 50, 10, 60, 30, 70]

        iterator = BSTIteratorLinearMemory(root)
        actual = []
        while iterator.hasNext():
            actual.append(iterator.next())

        self.assertEqual(expected, actual)

    def test_height_memory(self):
        root = TreeNode(10)
        root.left = TreeNode(20)
        root.right = TreeNode(30)
        root.left.left = TreeNode(40)
        root.left.right = TreeNode(50)
        root.right.left = TreeNode(60)
        root.right.right = TreeNode(70)

        expected = [40, 20, 50, 10, 60, 30, 70]

        iterator = BSTIteratorHeightMemory(root)
        actual = []
        while iterator.hasNext():
            actual.append(iterator.next())

        self.assertEqual(expected, actual)