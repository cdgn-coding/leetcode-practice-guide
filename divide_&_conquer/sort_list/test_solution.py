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

class TestSortList(unittest.TestCase):
    def test_example_1(self):
        head = create_linked_list([4, 2, 1, 3])
        result = Solution().sortList(head)
        self.assertEqual(linked_list_to_list(result), [1, 2, 3, 4])

    def test_example_2(self):
        head = create_linked_list([-1, 5, 3, 4, 0])
        result = Solution().sortList(head)
        self.assertEqual(linked_list_to_list(result), [-1, 0, 3, 4, 5])

    def test_example_3(self):
        head = create_linked_list([])
        result = Solution().sortList(head)
        self.assertEqual(linked_list_to_list(result), [])

    def test_single_element(self):
        head = create_linked_list([1])
        result = Solution().sortList(head)
        self.assertEqual(linked_list_to_list(result), [1])

    def test_already_sorted(self):
        head = create_linked_list([1, 2, 3, 4, 5])
        result = Solution().sortList(head)
        self.assertEqual(linked_list_to_list(result), [1, 2, 3, 4, 5])

    def test_reverse_sorted(self):
        head = create_linked_list([5, 4, 3, 2, 1])
        result = Solution().sortList(head)
        self.assertEqual(linked_list_to_list(result), [1, 2, 3, 4, 5])

    def test_duplicate_values(self):
        head = create_linked_list([3, 1, 2, 3, 2, 1])
        result = Solution().sortList(head)
        self.assertEqual(linked_list_to_list(result), [1, 1, 2, 2, 3, 3])

    def test_negative_values(self):
        head = create_linked_list([-5, -10, -3, -1, -8])
        result = Solution().sortList(head)
        self.assertEqual(linked_list_to_list(result), [-10, -8, -5, -3, -1])

if __name__ == '__main__':
    unittest.main()