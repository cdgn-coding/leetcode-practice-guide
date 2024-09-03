# Definition for a binary tree node.
from collections import deque
from dataclasses import dataclass
from typing import List, Optional

@dataclass(eq=False)
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __eq__(self, other: 'TreeNode'):
        return self.val == other.val and self.left == other.left and self.right == other.right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None

        val = preorder.pop(0)
        root = TreeNode(val)

        index = inorder.index(root.val)

        left_hand = inorder[:index]
        right_hand = inorder[index + 1:]

        root.left = self.buildTree(preorder, left_hand)
        root.right = self.buildTree(preorder, right_hand)

        return root

