class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
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
            
        """
        if (len(s1)+len(s2)!=len(s3)):
            return False
        l1=len(s1)
        l2=len(s2)
        dp=[[False]*(l2+1) for _ in range(l1+1)]
        dp[l1][l2]=True
        for i in range(l1, -1, -1):
            for j in range(l2, -1, -1):
                if s1[i] == s3[i+j] and dp[i+1][j]:
                    dp[i][j] = True
                if s2[j] == s3[i+j] and dp[i][j+1]:
                    dp[i][j] = True   
        return dp[0][0]
                