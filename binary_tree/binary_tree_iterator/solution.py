from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIteratorLinearMemory:
    def __init__(self, root: Optional[TreeNode]):
        stack = []

        def inorder_traversal(root):
            if root:
                if root.left: inorder_traversal(root.left)
                stack.append(root)
                if root.right: inorder_traversal(root.right)

        inorder_traversal(root)
        self.stack = stack

    def next(self) -> int:
        current = self.stack[0]
        self.stack = self.stack[1:]
        return current.val

    def hasNext(self) -> bool:
        return len(self.stack) > 0

class BSTIteratorHeightMemory:
    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        self.left_order_traversal(root)

    def left_order_traversal(self, root):
        if root:
            self.stack.append(root)
            self.left_order_traversal(root.left)

    def next(self) -> int:
        current = self.stack.pop()

        if current.right:
            self.left_order_traversal(current.right)

        return current.val


    def hasNext(self) -> bool:
        return len(self.stack) > 0

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()