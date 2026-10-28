class Solution(object):
    def findSubarrays(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        mp=set()
        for i in range(1,len(nums)):
            s=nums[i-1]+nums[i]
            if s in mp:
                return True
            mp.add(s)
        return False