class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        if (len(s1)+len(s2)!=len(s3)):
            return False
        dp={}
        def backtrack(l1,l2):
            if l1==len(s1) and l2==len(s2):
                return True
            if (l1,l2)in dp:
                return dp[(l1,l2)]
            if l1<len(s1) and s3[l1+l2]==s1[l1] and backtrack(l1+1,l2):
                dp[(l1,l2)]=True
            elif l2<len(s2) and s3[l1+l2]==s2[l2] and backtrack(l1,l2+1):
                dp[(l1,l2)]=True
            else:
                dp[(l1,l2)]=False
            return dp[(l1,l2)]
        return backtrack(0,0)
            
