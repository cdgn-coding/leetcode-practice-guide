import unittest
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        pass

def create_linked_list(values):
    dummy = ListNode(0)
    current = dummy
    for val in values:
        current.next = ListNode(val)
        current = current.next
    return dummy.next

def linked_list_to_list(head):
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result

class TestReverseKGroup(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        head = create_linked_list([1, 2, 3, 4, 5])
        k = 2
        result = self.solution.reverseKGroup(head, k)
        self.assertEqual(linked_list_to_list(result), [2, 1, 4, 3, 5])

    def test_example_2(self):
        head = create_linked_list([1, 2, 3, 4, 5])
        k = 3
        result = self.solution.reverseKGroup(head, k)
        self.assertEqual(linked_list_to_list(result), [3, 2, 1, 4, 5])

    def test_single_node(self):
        head = create_linked_list([1])
        k = 1
        result = self.solution.reverseKGroup(head, k)
        self.assertEqual(linked_list_to_list(result), [1])

    def test_k_equal_to_length(self):
        head = create_linked_list([1, 2, 3])
        k = 3
        result = self.solution.reverseKGroup(head, k)
        self.assertEqual(linked_list_to_list(result), [3, 2, 1])

    def test_k_greater_than_length(self):
        head = create_linked_list([1, 2, 3])
        k = 4
        result = self.solution.reverseKGroup(head, k)
        self.assertEqual(linked_list_to_list(result), [1, 2, 3])

    def test_empty_list(self):
        head = None
        k = 1
        result = self.solution.reverseKGroup(head, k)
        self.assertEqual(linked_list_to_list(result), [])

if __name__ == '__main__':
    unittest.main()