import unittest
from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def create_linked_list(values: List[int]) -> Optional[ListNode]:
    dummy = ListNode(0)
    current = dummy
    for val in values:
        current.next = ListNode(val)
        current = current.next
    return dummy.next

def linked_list_to_list(head: Optional[ListNode]) -> List[int]:
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        pass

class TestRemoveNthFromEnd(unittest.TestCase):
    def test_example_1(self):
        head = create_linked_list([1, 2, 3, 4, 5])
        n = 2
        expected = [1, 2, 3, 5]
        result = Solution().removeNthFromEnd(head, n)
        self.assertEqual(linked_list_to_list(result), expected)

    def test_example_2(self):
        head = create_linked_list([1])
        n = 1
        expected = []
        result = Solution().removeNthFromEnd(head, n)
        self.assertEqual(linked_list_to_list(result), expected)

    def test_example_3(self):
        head = create_linked_list([1, 2])
        n = 1
        expected = [1]
        result = Solution().removeNthFromEnd(head, n)
        self.assertEqual(linked_list_to_list(result), expected)

    def test_remove_first_node(self):
        head = create_linked_list([1, 2, 3, 4, 5])
        n = 5
        expected = [2, 3, 4, 5]
        result = Solution().removeNthFromEnd(head, n)
        self.assertEqual(linked_list_to_list(result), expected)

    def test_remove_last_node(self):
        head = create_linked_list([1, 2, 3, 4, 5])
        n = 1
        expected = [1, 2, 3, 4]
        result = Solution().removeNthFromEnd(head, n)
        self.assertEqual(linked_list_to_list(result), expected)

    def test_single_node(self):
        head = create_linked_list([1])
        n = 1
        expected = []
        result = Solution().removeNthFromEnd(head, n)
        self.assertEqual(linked_list_to_list(result), expected)

    def test_two_nodes_remove_first(self):
        head = create_linked_list([1, 2])
        n = 2
        expected = [2]
        result = Solution().removeNthFromEnd(head, n)
        self.assertEqual(linked_list_to_list(result), expected)

    def test_two_nodes_remove_second(self):
        head = create_linked_list([1, 2])
        n = 1
        expected = [1]
        result = Solution().removeNthFromEnd(head, n)
        self.assertEqual(linked_list_to_list(result), expected)

if __name__ == '__main__':
    unittest.main()