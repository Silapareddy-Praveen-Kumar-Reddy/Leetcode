class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        start, end = 0, 0
        for i in range(len(s)):
            for a, b in [(i, i), (i, i + 1)]:
                while a >= 0 and b < len(s) and s[a] == s[b]:
                    if b - a > end - start:
                        start, end = a, b
                    a -= 1
                    b += 1
        return s[start:end+1]