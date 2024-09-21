import unittest
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        pass

class TestZigzagLevelOrder(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        root = TreeNode(3)
        root.left = TreeNode(9)
        root.right = TreeNode(20)
        root.right.left = TreeNode(15)
        root.right.right = TreeNode(7)
        self.assertEqual(self.solution.zigzagLevelOrder(root), [[3],[20,9],[15,7]])

    def test_example_2(self):
        root = TreeNode(1)
        self.assertEqual(self.solution.zigzagLevelOrder(root), [[1]])

    def test_example_3(self):
        self.assertEqual(self.solution.zigzagLevelOrder(None), [])

    def test_single_level(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        self.assertEqual(self.solution.zigzagLevelOrder(root), [[1],[3,2]])

    def test_multiple_levels(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.right.right = TreeNode(5)
        self.assertEqual(self.solution.zigzagLevelOrder(root), [[1],[3,2],[4,5]])

    def test_large_tree(self):
        root = TreeNode(1)
        for i in range(2, 2001):
            new_node = TreeNode(i)
            current = root
            while True:
                if i % 2 == 0:
                    if current.left is None:
                        current.left = new_node
                        break
                    current = current.left
                else:
                    if current.right is None:
                        current.right = new_node
                        break
                    current = current.right
        result = self.solution.zigzagLevelOrder(root)
        self.assertGreater(len(result), 0)
        self.assertLess(len(result), 2000)

if __name__ == '__main__':
    unittest.main()