import unittest

from binary_tree.construct_by_preorder_inorder.solution import TreeNode, Solution


class ConstructPreorderInorderTest(unittest.TestCase):
    def test_linear_memory(self):
        root = TreeNode(3)
        root.left = TreeNode(9)
        root.right = TreeNode(20)
        root.right.right = TreeNode(15)
        root.left.left = TreeNode(7)

        sol = Solution()
        actual = sol.buildTree([3,9,20,15,7], [9,3,15,20,7])
        self.assertEqual(root.__repr__(), actual.__repr__())

