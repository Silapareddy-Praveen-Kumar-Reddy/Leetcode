class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        """ 
        time and space are O(M*N)
        dp = {}

        def dfs(i, a):
            if a == amount:
                return 1
            if i >= len(coins) or a > amount:
                return 0
            if (i, a) in dp:
                return dp[(i, a)]
            dp[(i, a)] = dfs(i, a + coins[i]) + dfs(i + 1, a)
            return dp[(i, a)]

        return dfs(0, 0)
        """
        # most optimal dp with Space O(N) where n is amount
        dp=[0]*(amount+1)
        dp[0]=1
        for i in range(len(coins)-1,-1,-1):
            temp=[0]*(amount+1)
            temp[0]=1
            for j in range(1,amount+1):
                temp[j]=dp[j]
                if j-coins[i] >=0:
                    temp[j]+=temp[(j-coins[i])]
            dp=temp
        return dp[amount]
