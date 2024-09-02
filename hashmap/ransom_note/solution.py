"""
Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.



Example 1:

Input: ransomNote = "a", magazine = "b"
Output: false
Example 2:

Input: ransomNote = "aa", magazine = "ab"
Output: false
Example 3:

Input: ransomNote = "aa", magazine = "aab"
Output: true


Constraints:

1 <= ransomNote.length, magazine.length <= 105
ransomNote and magazine consist of lowercase English letters.
"""


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazinecount = {}
        for letter in magazine:
            magazinecount[letter] = magazinecount.get(letter, 0) + 1

        for letter in ransomNote:
            if letter in magazinecount:
                magazinecount[letter] -= 1
            else:
                return False

        for count in magazinecount.values():
            if count < 0:
                return False

        return True

