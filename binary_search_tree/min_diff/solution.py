from math import inf
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getMinimumDifferenceTraverse(self, root: Optional[TreeNode]) -> int:
        stack = []
        current = root
        prev = None
        diff = inf
        while current or len(stack) > 0:
            while current:
                stack.append(current)
                current = current.left

            current = stack.pop()
            if prev is not None:
                diff = min(diff, abs(current.val - prev.val))
            prev = current

            current = current.right
        return diff


    def getMinimumDifferenceTraverseThenIterate(self, root: Optional[TreeNode]) -> int:
        def inorder(root):
            stack = []
            current = root
            result = []
            while current or len(stack) > 0:
                while current:
                    stack.append(current)
                    current = current.left

                current = stack.pop()
                result.append(current.val)

                current = current.right
            return result

        traversal = inorder(root)
        diff = inf
        for i in range(len(traversal) - 1):
            diff = min(diff, abs(traversal[i] - traversal[i + 1]))
        return diff


