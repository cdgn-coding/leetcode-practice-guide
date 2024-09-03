# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    @staticmethod
    def from_list(nums):
        if len(nums) == 0:
            return None

        head = ListNode(nums[0])
        current = head

        for _, val in enumerate(nums[1:]):
            new_node = ListNode(val)
            current.next = new_node
            current = new_node

        return head, current

    def to_list(self):
        head = self
        arr = []
        while head is not None:
            arr.append(head.val)
            head = head.next
        return arr


class Solution:
    """
        Algorítmo de la liebre y la tortuga
        Memoria O(1)
        Tiempo O(n)
    """
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast = slow = head

        while fast and fast.next:
            if fast.next == slow:
                return True
            slow = slow.next
            fast = fast.next.next

        return False

    """
        Algorítmo con un hash set
        Memoria O(n)
        Tiempo O(n)
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        current = head
        visited = set()
        while current is not None:
            if current in visited:
                return True
            visited.add(current)
            current = current.next
        return False
    """

