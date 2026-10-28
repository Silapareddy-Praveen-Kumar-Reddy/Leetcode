class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        s1=s=nums[0]
        for i in range(1,len(nums)):
            s=max(s+nums[i],nums[i])
            
            s1=max(s,s1)
        return s1