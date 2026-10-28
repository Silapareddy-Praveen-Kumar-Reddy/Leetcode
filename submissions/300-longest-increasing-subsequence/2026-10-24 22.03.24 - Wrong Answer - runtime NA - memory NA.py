class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp=[1]*(len(nums)+1)
        localmin=nums[-1]
        for i in range(len(nums)-2,-1,-1):
            if nums[i]<nums[i+1]:
                if nums[i]<localmin: 
                    dp[i]=dp[i+1]+1
                    localmin=nums[i]
                else:
                    dp[i]= dp[i+1]
            else:
                dp[i]=dp[i+1]
        return dp[0]
            
