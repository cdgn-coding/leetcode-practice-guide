#
# Depth search
from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mappings = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        n = len(digits)
        stack = [(0, "")]
        combinations = []
        while stack:
            i, letters = stack.pop()

            if i == n:
                if len(letters) > 0:
                    combinations.append(letters)
                continue

            digit = digits[i]
            for letter in mappings[digit]:
                stack.append((i + 1, letters + letter))
        combinations.sort()
        return combinations
