import unittest

class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head):
        pass

class TestCopyRandomList(unittest.TestCase):
    def test_example1(self):
        # Create the original list
        head = Node(7)
        node2 = Node(13)
        node3 = Node(11)
        node4 = Node(10)
        node5 = Node(1)
        head.next = node2
        node2.next = node3
        node3.next = node4
        node4.next = node5
        node2.random = head
        node3.random = node5
        node4.random = node3
        node5.random = head

        solution = Solution()
        copied = solution.copyRandomList(head)

        # Check if the copied list is correct
        self.assertEqual(copied.val, 7)
        self.assertEqual(copied.next.val, 13)
        self.assertEqual(copied.next.next.val, 11)
        self.assertEqual(copied.next.next.next.val, 10)
        self.assertEqual(copied.next.next.next.next.val, 1)
        self.assertIsNone(copied.random)
        self.assertEqual(copied.next.random.val, 7)
        self.assertEqual(copied.next.next.random.val, 1)
        self.assertEqual(copied.next.next.next.random.val, 11)
        self.assertEqual(copied.next.next.next.next.random.val, 7)

        # Check if the copied list is deep (not referencing original nodes)
        self.assertIsNot(copied, head)
        self.assertIsNot(copied.next, node2)
        self.assertIsNot(copied.next.next, node3)
        self.assertIsNot(copied.next.next.next, node4)
        self.assertIsNot(copied.next.next.next.next, node5)

    def test_example2(self):
        head = Node(1)
        node2 = Node(2)
        head.next = node2
        head.random = node2
        node2.random = node2

        solution = Solution()
        copied = solution.copyRandomList(head)

        self.assertEqual(copied.val, 1)
        self.assertEqual(copied.next.val, 2)
        self.assertEqual(copied.random.val, 2)
        self.assertEqual(copied.next.random.val, 2)
        self.assertIsNot(copied, head)
        self.assertIsNot(copied.next, node2)

    def test_example3(self):
        head = Node(3)
        node2 = Node(3)
        node3 = Node(3)
        head.next = node2
        node2.next = node3
        node2.random = head

        solution = Solution()
        copied = solution.copyRandomList(head)

        self.assertEqual(copied.val, 3)
        self.assertEqual(copied.next.val, 3)
        self.assertEqual(copied.next.next.val, 3)
        self.assertIsNone(copied.random)
        self.assertEqual(copied.next.random.val, 3)
        self.assertIsNone(copied.next.next.random)
        self.assertIsNot(copied, head)
        self.assertIsNot(copied.next, node2)
        self.assertIsNot(copied.next.next, node3)

    def test_empty_list(self):
        solution = Solution()
        copied = solution.copyRandomList(None)
        self.assertIsNone(copied)

if __name__ == '__main__':
    unittest.main()