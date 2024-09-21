import unittest

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        pass

class TestHasCycle(unittest.TestCase):
    def test_cycle_example1(self):
        head = ListNode(3)
        head.next = ListNode(2)
        head.next.next = ListNode(0)
        head.next.next.next = ListNode(-4)
        head.next.next.next.next = head.next
        self.assertTrue(Solution().hasCycle(head))

    def test_cycle_example2(self):
        head = ListNode(1)
        head.next = ListNode(2)
        head.next.next = head
        self.assertTrue(Solution().hasCycle(head))

    def test_no_cycle_example3(self):
        head = ListNode(1)
        self.assertFalse(Solution().hasCycle(head))

    def test_empty_list(self):
        self.assertFalse(Solution().hasCycle(None))

    def test_single_node_no_cycle(self):
        head = ListNode(1)
        self.assertFalse(Solution().hasCycle(head))

    def test_two_nodes_no_cycle(self):
        head = ListNode(1)
        head.next = ListNode(2)
        self.assertFalse(Solution().hasCycle(head))

    def test_large_cycle(self):
        head = ListNode(1)
        current = head
        for i in range(2, 10001):
            current.next = ListNode(i)
            current = current.next
        current.next = head
        self.assertTrue(Solution().hasCycle(head))

    def test_large_no_cycle(self):
        head = ListNode(1)
        current = head
        for i in range(2, 10001):
            current.next = ListNode(i)
            current = current.next
        self.assertFalse(Solution().hasCycle(head))

if __name__ == '__main__':
    unittest.main()