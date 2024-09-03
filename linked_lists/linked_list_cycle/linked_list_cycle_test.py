import unittest

from linked_lists.linked_list_cycle.linked_list_cycle import ListNode, LinkedListCycle


class LinkedListCycleTest(unittest.TestCase):
    def test_from_list(self):
        self.assertEqual(None, ListNode.from_list([]))

        expected = [1,2,3,4]
        head, _ = ListNode.from_list(expected)
        actual = []
        while head is not None:
            actual.append(head.val)
            head = head.next

        self.assertEqual(expected, actual)

    def test_to_list(self):
        expected = [1,2,3,4]
        head, _ = ListNode.from_list(expected)
        actual = head.to_list()
        self.assertEqual(expected, actual)


    def test_without_cycles(self):
        head, _ = ListNode.from_list([1,2,3,4])
        sol = LinkedListCycle()
        self.assertFalse(sol.hasCycle(head))


    def test_with_cycles(self):
        head, tail = ListNode.from_list([1,2,3,4])
        tail.next = head

        sol = LinkedListCycle()
        self.assertTrue(sol.hasCycle(head))

if __name__ == '__main__':
    unittest.main()
