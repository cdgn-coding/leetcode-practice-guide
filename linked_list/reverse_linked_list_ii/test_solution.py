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
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        pass

class TestReverseBetween(unittest.TestCase):
    def test_example_1(self):
        head = create_linked_list([1, 2, 3, 4, 5])
        solution = Solution()
        result = solution.reverseBetween(head, 2, 4)
        self.assertEqual(linked_list_to_list(result), [1, 4, 3, 2, 5])

    def test_example_2(self):
        head = create_linked_list([5])
        solution = Solution()
        result = solution.reverseBetween(head, 1, 1)
        self.assertEqual(linked_list_to_list(result), [5])

    def test_empty_list(self):
        solution = Solution()
        result = solution.reverseBetween(None, 1, 1)
        self.assertIsNone(result)

    def test_reverse_entire_list(self):
        head = create_linked_list([1, 2, 3, 4, 5])
        solution = Solution()
        result = solution.reverseBetween(head, 1, 5)
        self.assertEqual(linked_list_to_list(result), [5, 4, 3, 2, 1])

    def test_reverse_single_node(self):
        head = create_linked_list([1, 2, 3, 4, 5])
        solution = Solution()
        result = solution.reverseBetween(head, 3, 3)
        self.assertEqual(linked_list_to_list(result), [1, 2, 3, 4, 5])

    def test_reverse_first_two_nodes(self):
        head = create_linked_list([1, 2, 3, 4, 5])
        solution = Solution()
        result = solution.reverseBetween(head, 1, 2)
        self.assertEqual(linked_list_to_list(result), [2, 1, 3, 4, 5])

    def test_reverse_last_two_nodes(self):
        head = create_linked_list([1, 2, 3, 4, 5])
        solution = Solution()
        result = solution.reverseBetween(head, 4, 5)
        self.assertEqual(linked_list_to_list(result), [1, 2, 3, 5, 4])

if __name__ == '__main__':
    unittest.main()