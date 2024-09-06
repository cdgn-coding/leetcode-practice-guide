import unittest

from binary_search_tree.min_diff.solution import TreeNode, Solution


class MinDiffBSTTest(unittest.TestCase):
    def testTraverseThenIterate(self):
        root = TreeNode(4)

        root.left = TreeNode(2)
        root.right = TreeNode(6)

        root.left.left = TreeNode(1)
        root.left.right = TreeNode(3)

        sol = Solution()
        actual = sol.getMinimumDifferenceTraverseThenIterate(root)

        self.assertEqual(1, actual)
    def testTraverseOnce(self):
        root = TreeNode(4)

        root.left = TreeNode(2)
        root.right = TreeNode(6)

        root.left.left = TreeNode(1)
        root.left.right = TreeNode(3)

        sol = Solution()
        actual = sol.getMinimumDifferenceTraverse(root)

        self.assertEqual(1, actual)