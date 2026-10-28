class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        length=len(nums)
        res=[]
        for i in range(length-2):
            if i>0 and nums[i]==nums[i-1]:
                continue
            l=i+1
            r=length-1
            while l<r:
                s=nums[l]+nums[i]
                if s+nums[r]>0:
                    r-=1
                elif s+nums[r]<0:
                    l+=1
                else:
                    res.append([nums[i],nums[l],nums[r]])
                    l+=1
                    while l<r and nums[l] ==nums[l+1]:
                        l+=1
        return res

        
                