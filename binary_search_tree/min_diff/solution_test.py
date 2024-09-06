import unittest

from binary_search_tree.min_diff.solution import TreeNode, Solution


class MinDiffBSTTest(unittest.TestCase):
    def test(self):
        root = TreeNode(4)

        root.left = TreeNode(2)
        root.right = TreeNode(6)

        root.left.left = TreeNode(1)
        root.left.right = TreeNode(3)

        sol = Solution()
        actual = sol.getMinimumDifference(root)

        self.assertEqual(1, actual)