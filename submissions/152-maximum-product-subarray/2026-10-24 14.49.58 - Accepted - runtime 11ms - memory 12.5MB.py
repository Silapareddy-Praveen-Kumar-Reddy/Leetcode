class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res=maxp=minp=nums[0]
        for i in nums[1:]:
            if i ==0:
                minp=maxp=1
            temp=(maxp*i,minp*i,i)
            maxp=max(temp)
            minp=min(temp)
            res=max(res,maxp)
        return res
