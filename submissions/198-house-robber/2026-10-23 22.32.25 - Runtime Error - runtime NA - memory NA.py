class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp=[0]*len(nums)
        dp[0]=nums[0]
        dp[1]=max(nums[1],nums[0])
        for i in range(2,len(nums)):
            dp[i]=max(dp[i-2]+nums[i],dp[i-1])
        return dp[-1]