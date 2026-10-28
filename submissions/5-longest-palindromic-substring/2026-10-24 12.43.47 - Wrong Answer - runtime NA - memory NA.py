class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        left,right=0,0
        for i in range(1,len(s)-1):
            for l,r in [(i,i),(i,i+1)]:
                while l>=0 and r<len(s) and s[l]==s[r]:
                    if r-l >right-left:
                        right=r
                        left=l
                    l-=1
                    r+=1
                    
        return s[left:right+1]