class Solution(object):
    def findAllConcatenatedWordsInADict(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        res=[]
        for s in words:
            dp=[False]*(len(s)+1)
            dp[len(s)]=True
            for i in range(len(s)-1,-1,-1):
                for word in words:
                    if s==word:
                        continue
                    if (i+len(word))<=len(s) and s[i:i+len(word)]==word:
                        dp[i]=dp[i+len(word)]
                    if dp[i]:
                        break

            if dp[0]:
                res.append(s)
        return res