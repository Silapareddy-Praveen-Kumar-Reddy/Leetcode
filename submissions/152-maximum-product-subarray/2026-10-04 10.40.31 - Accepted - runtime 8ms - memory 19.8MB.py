class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        res=currmax=currmin=nums[0]

        for i in nums[1:]:
            temp=(i,currmax*i,currmin*i)
            currmax=max(temp)
            currmin=min(temp)
            res=max(res,currmax)
        return res

            
