from math import inf
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        nodes = [root]
        diff = float(inf)
        while len(nodes) > 0:
            current = nodes.pop()
            if current.right:
                nodes.append(current.right)
                diff = min(abs(current.right.val - current.val), diff)
            if current.left:
                nodes.append(current.left)
                diff = min(abs(current.left.val - current.val), diff)
        return diff

