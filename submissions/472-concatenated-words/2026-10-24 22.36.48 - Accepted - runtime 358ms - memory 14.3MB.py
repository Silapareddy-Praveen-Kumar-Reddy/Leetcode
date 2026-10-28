class Solution(object):
    def findAllConcatenatedWordsInADict(self, words):
        seen = set()
        res = []
        for s in sorted(words, key=len):
            if s and self.can(s, seen):
                res.append(s)
            seen.add(s)
        return res

    def can(self, s, seen):
        if not seen:
            return False
        l = len(s)
        dp = [False] * (l + 1)
        dp[0] = True
        for i in range(1, l + 1):
            for j in range(i):
                if dp[j] and s[j:i] in seen:
                    dp[i] = True
                    break
        return dp[l]