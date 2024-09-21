import unittest

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def create_linked_list(arr):
    dummy = ListNode(0)
    current = dummy
    for val in arr:
        current.next = ListNode(val)
        current = current.next
    return dummy.next

def linked_list_to_array(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

class TestAddTwoNumbers(unittest.TestCase):
    def test_example_1(self):
        l1 = create_linked_list([2, 4, 3])
        l2 = create_linked_list([5, 6, 4])
        result = Solution().addTwoNumbers(l1, l2)
        self.assertEqual(linked_list_to_array(result), [7, 0, 8])

    def test_example_2(self):
        l1 = create_linked_list([0])
        l2 = create_linked_list([0])
        result = Solution().addTwoNumbers(l1, l2)
        self.assertEqual(linked_list_to_array(result), [0])

    def test_example_3(self):
        l1 = create_linked_list([9, 9, 9, 9, 9, 9, 9])
        l2 = create_linked_list([9, 9, 9, 9])
        result = Solution().addTwoNumbers(l1, l2)
        self.assertEqual(linked_list_to_array(result), [8, 9, 9, 9, 0, 0, 0, 1])

    def test_different_lengths(self):
        l1 = create_linked_list([1, 2, 3])
        l2 = create_linked_list([4, 5])
        result = Solution().addTwoNumbers(l1, l2)
        self.assertEqual(linked_list_to_array(result), [5, 7, 3])

    def test_large_carry(self):
        l1 = create_linked_list([9, 9, 9])
        l2 = create_linked_list([1])
        result = Solution().addTwoNumbers(l1, l2)
        self.assertEqual(linked_list_to_array(result), [0, 0, 0, 1])

if __name__ == '__main__':
    unittest.main()