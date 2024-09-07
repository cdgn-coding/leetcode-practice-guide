# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        current = root
        counter = 0
        while current or stack:
            while current:
                stack.append(current)
                current = current.left

            current = stack.pop()
            counter += 1

            if counter == k:
                return current.val

            current = current.right

        raise IndexError()


