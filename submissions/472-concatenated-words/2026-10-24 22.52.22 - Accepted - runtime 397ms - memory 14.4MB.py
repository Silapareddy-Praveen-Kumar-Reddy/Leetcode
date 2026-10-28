class Solution(object):
    def findAllConcatenatedWordsInADict(self, words):
        res = []
        seen = set()
        for s in sorted(words, key=len):
            l = len(s)
            dp = [False] * (l + 1)
            dp[l] = True
            for i in range(l - 1, -1, -1):
                for j in range(i + 1, l + 1):
                    if dp[j] and s[i:j] in seen:
                        dp[i] = True
                        break
            if dp[0]:
                res.append(s)
            seen.add(s)
        return res