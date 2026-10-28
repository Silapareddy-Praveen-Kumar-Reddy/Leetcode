class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        s=sum(nums)
        if s%2!=0:
            return False
        target=s//2
        mp=set()
        mp.add(0)
        #subset sum should be half of total
        for i in range(len(nums)-1,-1,-1):
            temp=set()
            for j in mp:
                if (nums[i]+j)not in mp:
                    if (nums[i]+j) ==target:
                        return True
                    temp.add(nums[i]+j)
            
            mp.update(temp)
        return False
                    
