class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLength = 0
        for i in range(len(s)):
            sub = ""
            for j in range(i, len(s)):
                if s[j] in sub:
                    break
                else:
                    sub = sub + s[j]
                length = j - i + 1
                maxLength = length if length > maxLength else maxLength
        return maxLength
        