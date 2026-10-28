class Solution(object):
    def maxProductPair(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        mp={}
        for idx,num in enumerate(nums):
            mp[num]=idx
        for idx,num in enumerate(nums):
            num2=target-num
            if num2 in mp:
                return idx,mp[num2] if num>num2 else mp[num2],idx
        return [-1,-1]