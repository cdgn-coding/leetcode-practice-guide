import unittest

from binary_tree.max_depth.solution import TreeNode, RecursiveMaxDepthSolution, IterativeBFSMaxDepthSolution, \
    IterativeDFSMaxDepthSolution


class BinaryTreeMaxDepthTest(unittest.TestCase):
    def test_recursive(self):
        root = TreeNode(10)
        root.left = TreeNode(20)
        root.right = TreeNode(30)
        root.left.left = TreeNode(40)
        root.left.right = TreeNode(50)
        root.right.left = TreeNode(60)
        root.right.right = TreeNode(70)

        sol = RecursiveMaxDepthSolution()
        self.assertEqual(3, sol.maxDepth(root))

    def test_iterative_bfs(self):
        root = TreeNode(10)
        root.left = TreeNode(20)
        root.right = TreeNode(30)
        root.left.left = TreeNode(40)
        root.left.right = TreeNode(50)
        root.right.left = TreeNode(60)
        root.right.right = TreeNode(70)

        sol = IterativeBFSMaxDepthSolution()
        self.assertEqual(3, sol.maxDepth(root))

    def test_iterative_dfs(self):
        root = TreeNode(10)
        root.left = TreeNode(20)
        root.right = TreeNode(30)
        root.left.left = TreeNode(40)
        root.left.right = TreeNode(50)
        root.right.left = TreeNode(60)
        root.right.right = TreeNode(70)

        sol = IterativeDFSMaxDepthSolution()
        self.assertEqual(3, sol.maxDepth(root))