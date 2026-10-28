class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        n=len(coins)
        if amount==0: return 0
        self.memo={}
        return self._solve(coins,amount)
    def _solve(self,coins,rem):
        if rem < 0:
            return -1
        if rem == 0:
            return 0
        if rem in self.memo:
            return self.memo[rem]
        mincount=float('inf')
        for coin in coins:
            res=self._solve(coins,rem-coin)
            if res!=-1:
                mincount=min(mincount,res+1)
        self.memo[rem]=mincount if mincount!=float('inf') else -1
        return self.memo[rem]

