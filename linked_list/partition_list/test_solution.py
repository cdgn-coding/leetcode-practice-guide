import unittest
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

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

class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        pass

class TestPartitionLinkedList(unittest.TestCase):
    def test_example_1(self):
        head = create_linked_list([1,4,3,2,5,2])
        x = 3
        expected = [1,2,2,4,3,5]
        result = linked_list_to_list(Solution().partition(head, x))
        self.assertEqual(result, expected)

    def test_example_2(self):
        head = create_linked_list([2,1])
        x = 2
        expected = [1,2]
        result = linked_list_to_list(Solution().partition(head, x))
        self.assertEqual(result, expected)

    def test_empty_list(self):
        head = None
        x = 0
        expected = []
        result = linked_list_to_list(Solution().partition(head, x))
        self.assertEqual(result, expected)

    def test_single_node(self):
        head = create_linked_list([1])
        x = 2
        expected = [1]
        result = linked_list_to_list(Solution().partition(head, x))
        self.assertEqual(result, expected)

    def test_all_nodes_less_than_x(self):
        head = create_linked_list([1,2,3,4,5])
        x = 6
        expected = [1,2,3,4,5]
        result = linked_list_to_list(Solution().partition(head, x))
        self.assertEqual(result, expected)

    def test_all_nodes_greater_than_or_equal_to_x(self):
        head = create_linked_list([5,4,3,2,1])
        x = 1
        expected = [5,4,3,2,1]
        result = linked_list_to_list(Solution().partition(head, x))
        self.assertEqual(result, expected)

    def test_x_not_in_list(self):
        head = create_linked_list([1,4,3,2,5,2])
        x = 6
        expected = [1,4,3,2,5,2]
        result = linked_list_to_list(Solution().partition(head, x))
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()