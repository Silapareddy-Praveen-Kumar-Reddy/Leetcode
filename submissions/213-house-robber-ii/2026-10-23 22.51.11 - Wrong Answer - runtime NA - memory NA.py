class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return max(self.helper(nums[1:]),self.helper(nums[:-1]))
    def helper(self,nums):
        a,b=0,0
        for i in nums:
            t=max(a+i,b)
            a=b
            b=t

        return b
        