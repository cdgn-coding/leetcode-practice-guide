from math import inf
from typing import List


class Solution:from math import inf
from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        longest = 0
        maxn = float(-inf)
        i = 0
        while i < len(nums):
            if nums[i] < maxn:
                i+= 1
                continue
            new_maxn = nums[i]
            new_longest = 1
            i += 1
            while i < len(nums) and nums[i] == new_maxn:
                new_longest += 1
                i += 1
            if new_maxn == maxn:
                longest = max(longest, new_longest)
            else:
                longest = new_longest
            maxn = new_maxn


        return longest

    def longestSubarray(self, nums: List[int]) -> int:
        longest = 0
        maxn = float(-inf)
        i = 0
        while i < len(nums):
            if nums[i] < maxn:
                i+= 1
                continue
            new_maxn = nums[i]
            new_longest = 1
            i += 1
            while i < len(nums) and nums[i] == new_maxn:
                new_longest += 1
                i += 1
            if new_maxn == maxn:
                longest = max(longest, new_longest)
            else:
                longest = new_longest
            maxn = new_maxn


        return longest
