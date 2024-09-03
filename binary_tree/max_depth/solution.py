from collections import deque
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class RecursiveMaxDepthSolution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.recursiveMaxDepth(root)

    def recursiveMaxDepth(self, root: Optional[TreeNode], depth = 0):
        if not root:
            return depth

        left_depth = self.recursiveMaxDepth(root.left, depth + 1)
        right_depth = self.recursiveMaxDepth(root.right, depth + 1)

        return max(left_depth, right_depth)

class IterativeBFSMaxDepthSolution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        q = deque()

        if root: q.append(root)

        level = 0

        while q:
            for i in range(len(q)):
                node = q.popleft()

                if node.left: q.append(node.left)
                if node.right: q.append(node.right)

            level += 1

        return level

class IterativeDFSMaxDepthSolution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0

        stack = [(root, 1)]
        max_depth = 0

        while stack:
            node, depth = stack.pop()
            max_depth = max(depth, max_depth)

            if node.left: stack.append((node.left, depth + 1))
            if node.right: stack.append((node.right, depth + 1))

        return max_depth