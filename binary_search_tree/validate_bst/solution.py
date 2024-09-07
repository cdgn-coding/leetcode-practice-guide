from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        stack = []
        current = root
        prev = None
        while current or stack:
            while current:
                stack.append(current)
                current = current.left

            current = stack.pop()
            if prev is not None and current.val < prev.val:
                return False
            prev = current

            current = current.right

        return True