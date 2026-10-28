class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        res=0
        for i in range(len(s)):
            for l,r in [(i,i),(i,i+1)]:
                while l>=0 and r<len(s) and s[l]==s[r]:
                    res+=1
                    r+=1
                    l-=1
        return res