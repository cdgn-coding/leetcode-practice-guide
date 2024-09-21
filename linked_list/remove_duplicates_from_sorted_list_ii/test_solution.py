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
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pass

class TestDeleteDuplicates(unittest.TestCase):
    def test_example_1(self):
        head = create_linked_list([1,2,3,3,4,4,5])
        solution = Solution()
        result = solution.deleteDuplicates(head)
        self.assertEqual(linked_list_to_list(result), [1,2,5])

    def test_example_2(self):
        head = create_linked_list([1,1,1,2,3])
        solution = Solution()
        result = solution.deleteDuplicates(head)
        self.assertEqual(linked_list_to_list(result), [2,3])

    def test_empty_list(self):
        head = None
        solution = Solution()
        result = solution.deleteDuplicates(head)
        self.assertEqual(linked_list_to_list(result), [])

    def test_single_element(self):
        head = create_linked_list([1])
        solution = Solution()
        result = solution.deleteDuplicates(head)
        self.assertEqual(linked_list_to_list(result), [1])

    def test_all_duplicates(self):
        head = create_linked_list([1,1,1,1,1])
        solution = Solution()
        result = solution.deleteDuplicates(head)
        self.assertEqual(linked_list_to_list(result), [])

    def test_no_duplicates(self):
        head = create_linked_list([1,2,3,4,5])
        solution = Solution()
        result = solution.deleteDuplicates(head)
        self.assertEqual(linked_list_to_list(result), [1,2,3,4,5])

    def test_duplicates_at_beginning(self):
        head = create_linked_list([1,1,2,3,4,5])
        solution = Solution()
        result = solution.deleteDuplicates(head)
        self.assertEqual(linked_list_to_list(result), [2,3,4,5])

    def test_duplicates_at_end(self):
        head = create_linked_list([1,2,3,4,5,5])
        solution = Solution()
        result = solution.deleteDuplicates(head)
        self.assertEqual(linked_list_to_list(result), [1,2,3,4])

if __name__ == '__main__':
    unittest.main()