class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        row=len(matrix)
        col=len(matrix[0])
        dp={}
        def dfs(i,j,prev):
            if i<0 or j<0 or i==row or j==col or matrix[i][j]<=prev :
                return 0
            if (i,j) in dp:
                return dp[(i,j)]
            dir=[(1,0),(0,1),(-1,0),(0,-1)]
            res=1
            for a,b in dir:
                res=max(res,1+dfs(i+a,j+b,matrix[i][j]))
            dp[(i,j)]=res
            return res
        for r in range(row):
            for c in range(col):
                dfs(r,c,float('-inf'))
        return max(dp.values())