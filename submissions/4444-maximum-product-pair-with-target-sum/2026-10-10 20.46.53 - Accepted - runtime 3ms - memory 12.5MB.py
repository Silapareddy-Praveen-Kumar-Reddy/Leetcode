class Solution(object):
    def maxProductPair(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        mp={}
        max_prod=float('-inf')
        res=[-1,-1]
        for idx,num in enumerate(nums):
            mp[num]=idx
        for idx,num in enumerate(nums):
            num2=target-num
            if num2 in mp and num!=num2:
                p=num*num2
                if max_prod<(p):
                    res= [idx,mp[num2]] if num>num2 else [mp[num2],idx]
                    max_prod=p
        return res