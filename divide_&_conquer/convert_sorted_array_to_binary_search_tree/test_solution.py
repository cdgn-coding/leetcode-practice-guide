import unittest
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        pass

class TestSortedArrayToBST(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        nums = [-10,-3,0,5,9]
        result = self.solution.sortedArrayToBST(nums)
        self.assertEqual(result.val, 0)
        self.assertEqual(result.left.val, -3)
        self.assertEqual(result.right.val, 9)
        self.assertEqual(result.left.left.val, -10)
        self.assertEqual(result.right.left.val, 5)

    def test_example2(self):
        nums = [1,3]
        result = self.solution.sortedArrayToBST(nums)
        self.assertTrue(result.val in [1, 3])
        if result.val == 1:
            self.assertEqual(result.right.val, 3)
        else:
            self.assertEqual(result.left.val, 1)

    def test_single_element(self):
        nums = [0]
        result = self.solution.sortedArrayToBST(nums)
        self.assertEqual(result.val, 0)
        self.assertIsNone(result.left)
        self.assertIsNone(result.right)

    def test_empty_array(self):
        nums = []
        result = self.solution.sortedArrayToBST(nums)
        self.assertIsNone(result)

    def test_large_array(self):
        nums = list(range(-10000, 10001))
        result = self.solution.sortedArrayToBST(nums)
        self.assertEqual(result.val, 0)
        self.assertTrue(self.is_balanced(result))
        self.assertTrue(self.is_bst(result))

    def is_balanced(self, root):
        if not root:
            return True
        left_height = self.height(root.left)
        right_height = self.height(root.right)
        if abs(left_height - right_height) <= 1 and self.is_balanced(root.left) and self.is_balanced(root.right):
            return True
        return False

    def height(self, root):
        if not root:
            return 0
        return 1 + max(self.height(root.left), self.height(root.right))

    def is_bst(self, root, min_val=float('-inf'), max_val=float('inf')):
        if not root:
            return True
        if root.val <= min_val or root.val >= max_val:
            return False
        return self.is_bst(root.left, min_val, root.val) and self.is_bst(root.right, root.val, max_val)

if __name__ == '__main__':
    unittest.main()