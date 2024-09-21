import unittest
from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        pass

class TestMergeKLists(unittest.TestCase):
    def test_example_1(self):
        lists = [
            self.create_linked_list([1, 4, 5]),
            self.create_linked_list([1, 3, 4]),
            self.create_linked_list([2, 6])
        ]
        expected = [1, 1, 2, 3, 4, 4, 5, 6]
        self.assertEqual(self.linked_list_to_list(Solution().mergeKLists(lists)), expected)

    def test_example_2(self):
        lists = []
        expected = []
        self.assertEqual(self.linked_list_to_list(Solution().mergeKLists(lists)), expected)

    def test_example_3(self):
        lists = [[]]
        expected = []
        self.assertEqual(self.linked_list_to_list(Solution().mergeKLists(lists)), expected)

    def test_single_list(self):
        lists = [self.create_linked_list([1, 2, 3])]
        expected = [1, 2, 3]
        self.assertEqual(self.linked_list_to_list(Solution().mergeKLists(lists)), expected)

    def test_multiple_empty_lists(self):
        lists = [[], [], []]
        expected = []
        self.assertEqual(self.linked_list_to_list(Solution().mergeKLists(lists)), expected)

    def test_lists_with_negative_numbers(self):
        lists = [
            self.create_linked_list([-5, -1, 3]),
            self.create_linked_list([-4, 0, 4]),
            self.create_linked_list([-3, 1, 5])
        ]
        expected = [-5, -4, -3, -1, 0, 1, 3, 4, 5]
        self.assertEqual(self.linked_list_to_list(Solution().mergeKLists(lists)), expected)

    def create_linked_list(self, values):
        dummy = ListNode(0)
        current = dummy
        for val in values:
            current.next = ListNode(val)
            current = current.next
        return dummy.next

    def linked_list_to_list(self, head):
        result = []
        current = head
        while current:
            result.append(current.val)
            current = current.next
        return result

if __name__ == '__main__':
    unittest.main()