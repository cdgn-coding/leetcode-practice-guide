import unittest

from binary_search_tree.kth_min_element.solution import TreeNode, Solution


class KthMinBSTTest(unittest.TestCase):
    def test(self):
        root = TreeNode(4)

        root.left = TreeNode(2)
        root.right = TreeNode(6)

        root.left.left = TreeNode(1)
        root.left.right = TreeNode(3)

        sol = Solution()
        self.assertEqual(1, sol.kthSmallest(root, 1))
        self.assertEqual(2, sol.kthSmallest(root, 2))
        self.assertEqual(3, sol.kthSmallest(root, 3))
        self.assertEqual(4, sol.kthSmallest(root, 4))
        self.assertEqual(6, sol.kthSmallest(root, 5))
        self.assertRaises(IndexError, sol.kthSmallest, root, 6)