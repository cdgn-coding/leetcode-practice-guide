import unittest
from typing import Optional

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        pass

class TestLowestCommonAncestor(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def create_tree(self, values):
        if not values:
            return None
        root = TreeNode(values[0])
        queue = [root]
        i = 1
        while queue and i < len(values):
            node = queue.pop(0)
            if i < len(values) and values[i] is not None:
                node.left = TreeNode(values[i])
                queue.append(node.left)
            i += 1
            if i < len(values) and values[i] is not None:
                node.right = TreeNode(values[i])
                queue.append(node.right)
            i += 1
        return root

    def test_example1(self):
        root = self.create_tree([3,5,1,6,2,0,8,None,None,7,4])
        p = root.left  # Node with value 5
        q = root.right  # Node with value 1
        result = self.solution.lowestCommonAncestor(root, p, q)
        self.assertEqual(result.val, 3)

    def test_example2(self):
        root = self.create_tree([3,5,1,6,2,0,8,None,None,7,4])
        p = root.left  # Node with value 5
        q = root.left.right.right  # Node with value 4
        result = self.solution.lowestCommonAncestor(root, p, q)
        self.assertEqual(result.val, 5)

    def test_example3(self):
        root = self.create_tree([1,2])
        p = root  # Node with value 1
        q = root.left  # Node with value 2
        result = self.solution.lowestCommonAncestor(root, p, q)
        self.assertEqual(result.val, 1)

    def test_single_node(self):
        root = TreeNode(1)
        result = self.solution.lowestCommonAncestor(root, root, root)
        self.assertEqual(result.val, 1)

    def test_deep_tree(self):
        root = self.create_tree([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
        p = root.left.left.left  # Node with value 8
        q = root.left.right.right  # Node with value 11
        result = self.solution.lowestCommonAncestor(root, p, q)
        self.assertEqual(result.val, 2)

if __name__ == '__main__':
    unittest.main()