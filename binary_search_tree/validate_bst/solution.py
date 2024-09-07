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
        traversal = []
        while current or stack:
            while current:
                stack.append(current)
                current = current.left

            current = stack.pop()
            traversal.append(current.val)

            current = current.right

        for i in range(1, len(traversal)):
            if not traversal[i - 1] < traversal[i]:
                return False

        return True