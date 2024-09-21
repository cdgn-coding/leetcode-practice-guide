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
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        pass

class TestRotateList(unittest.TestCase):
    def test_example_1(self):
        head = create_linked_list([1, 2, 3, 4, 5])
        k = 2
        solution = Solution()
        result = solution.rotateRight(head, k)
        self.assertEqual(linked_list_to_list(result), [4, 5, 1, 2, 3])

    def test_example_2(self):
        head = create_linked_list([0, 1, 2])
        k = 4
        solution = Solution()
        result = solution.rotateRight(head, k)
        self.assertEqual(linked_list_to_list(result), [2, 0, 1])

    def test_empty_list(self):
        head = None
        k = 3
        solution = Solution()
        result = solution.rotateRight(head, k)
        self.assertIsNone(result)

    def test_single_node(self):
        head = create_linked_list([1])
        k = 5
        solution = Solution()
        result = solution.rotateRight(head, k)
        self.assertEqual(linked_list_to_list(result), [1])

    def test_k_greater_than_length(self):
        head = create_linked_list([1, 2, 3])
        k = 5
        solution = Solution()
        result = solution.rotateRight(head, k)
        self.assertEqual(linked_list_to_list(result), [2, 3, 1])

    def test_k_equal_to_length(self):
        head = create_linked_list([1, 2, 3, 4])
        k = 4
        solution = Solution()
        result = solution.rotateRight(head, k)
        self.assertEqual(linked_list_to_list(result), [1, 2, 3, 4])

    def test_k_zero(self):
        head = create_linked_list([1, 2, 3, 4, 5])
        k = 0
        solution = Solution()
        result = solution.rotateRight(head, k)
        self.assertEqual(linked_list_to_list(result), [1, 2, 3, 4, 5])

if __name__ == '__main__':
    unittest.main()