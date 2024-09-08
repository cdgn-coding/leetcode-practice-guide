class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        maxfound = 0
        for right in range(0, len(s)):
            if right == 0:
                maxfound += 1

            for subindex in range(left, right):
                if s[subindex] == s[right]:
                    left = subindex + 1
                    break

            maxfound = max(right - left + 1, maxfound)

        return maxfound



