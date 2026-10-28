class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        lmin=prices[0]
        r=0
        for i in range(len(prices)):
            lmin=min(lmin,prices[i])
            r=max(prices[i]-lmin,r)
        return r
