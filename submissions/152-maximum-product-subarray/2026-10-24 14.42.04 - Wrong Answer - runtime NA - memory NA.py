class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res=maxp=minp=nums[0]
        for i in nums[1:]:
            if i ==0:
                minp=maxp=0
            maxp=max(maxp*i,minp*i,i)
            minp=min(maxp*i,minp*i,i)
            res=max(res,maxp)
        return res
