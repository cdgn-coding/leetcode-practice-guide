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

class TestMergeTwoLists(unittest.TestCase):
    def test_example_1(self):
        list1 = create_linked_list([1, 2, 4])
        list2 = create_linked_list([1, 3, 4])
        merged = Solution().mergeTwoLists(list1, list2)
        self.assertEqual(linked_list_to_list(merged), [1, 1, 2, 3, 4, 4])

    def test_example_2(self):
        list1 = create_linked_list([])
        list2 = create_linked_list([])
        merged = Solution().mergeTwoLists(list1, list2)
        self.assertEqual(linked_list_to_list(merged), [])

    def test_example_3(self):
        list1 = create_linked_list([])
        list2 = create_linked_list([0])
        merged = Solution().mergeTwoLists(list1, list2)
        self.assertEqual(linked_list_to_list(merged), [0])

    def test_one_empty_list(self):
        list1 = create_linked_list([1, 2, 3])
        list2 = create_linked_list([])
        merged = Solution().mergeTwoLists(list1, list2)
        self.assertEqual(linked_list_to_list(merged), [1, 2, 3])

    def test_different_lengths(self):
        list1 = create_linked_list([1, 3, 5])
        list2 = create_linked_list([2, 4, 6, 8])
        merged = Solution().mergeTwoLists(list1, list2)
        self.assertEqual(linked_list_to_list(merged), [1, 2, 3, 4, 5, 6, 8])

    def test_negative_values(self):
        list1 = create_linked_list([-3, -1, 1])
        list2 = create_linked_list([-2, 0, 2])
        merged = Solution().mergeTwoLists(list1, list2)
        self.assertEqual(linked_list_to_list(merged), [-3, -2, -1, 0, 1, 2])

if __name__ == '__main__':
    unittest.main()