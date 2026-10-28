class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        dp={}
        def dfs(i,buy):
            if i>=len(prices):
                return 0
            if (i,buy) in dp:
                return dp[(i,buy)]
            if buy:
                dp[(i,buy)]=max(dfs(i+1,not buy)-prices[i],dfs(i+1,buy))
            else:
                dp[(i,buy)]=max(dfs(i+2,not buy)+prices[i],dfs(i+1,buy))
            
            return dp[(i,buy)]
        return dfs(0,True)