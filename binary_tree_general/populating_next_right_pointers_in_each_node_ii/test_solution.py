import unittest

class Node:
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        pass  # Placeholder for the actual implementation

class TestConnectRightPointers(unittest.TestCase):
    def test_empty_tree(self):
        solution = Solution()
        self.assertIsNone(solution.connect(None))

    def test_single_node(self):
        root = Node(1)
        solution = Solution()
        result = solution.connect(root)
        self.assertIsNone(result.next)

    def test_complete_binary_tree(self):
        root = Node(1)
        root.left = Node(2)
        root.right = Node(3)
        root.left.left = Node(4)
        root.left.right = Node(5)
        root.right.left = Node(6)
        root.right.right = Node(7)

        solution = Solution()
        result = solution.connect(root)

        self.assertIsNone(result.next)
        self.assertEqual(result.left.next, result.right)
        self.assertIsNone(result.right.next)
        self.assertEqual(result.left.left.next, result.left.right)
        self.assertEqual(result.left.right.next, result.right.left)
        self.assertEqual(result.right.left.next, result.right.right)
        self.assertIsNone(result.right.right.next)

    def test_incomplete_binary_tree(self):
        root = Node(1)
        root.left = Node(2)
        root.right = Node(3)
        root.left.left = Node(4)
        root.left.right = Node(5)
        root.right.right = Node(7)

        solution = Solution()
        result = solution.connect(root)

        self.assertIsNone(result.next)
        self.assertEqual(result.left.next, result.right)
        self.assertIsNone(result.right.next)
        self.assertEqual(result.left.left.next, result.left.right)
        self.assertEqual(result.left.right.next, result.right.right)
        self.assertIsNone(result.right.right.next)

    def test_large_tree(self):
        root = Node(1)
        current = root
        for i in range(2, 6001):
            current.left = Node(i)
            current = current.left

        solution = Solution()
        result = solution.connect(root)

        current = result
        while current.left:
            self.assertIsNone(current.next)
            current = current.left

    def test_edge_values(self):
        root = Node(-100)
        root.left = Node(0)
        root.right = Node(100)

        solution = Solution()
        result = solution.connect(root)

        self.assertIsNone(result.next)
        self.assertEqual(result.left.next, result.right)
        self.assertIsNone(result.right.next)

if __name__ == '__main__':
    unittest.main()