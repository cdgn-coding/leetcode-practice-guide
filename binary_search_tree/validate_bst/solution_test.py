import unittest

from binary_search_tree.validate_bst.solution import TreeNode, Solution


class ValidateBSTTest(unittest.TestCase):
    def testFalse(self):
        root = TreeNode(4)

        root.left = TreeNode(2)
        root.right = TreeNode(6)

        root.left.left = TreeNode(1)
        root.left.right = TreeNode(7)

        sol = Solution()
        self.assertFalse(sol.isValidBST(root))

    def testTrue(self):
        root = TreeNode(2)

        root.left = TreeNode(1)
        root.right = TreeNode(3)
        sol = Solution()
        self.assertTrue(sol.isValidBST(root))