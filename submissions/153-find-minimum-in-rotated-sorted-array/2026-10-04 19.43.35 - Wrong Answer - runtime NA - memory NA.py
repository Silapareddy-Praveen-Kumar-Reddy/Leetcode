class Solution:
    def findMin(self, nums: list[int]) -> int:
        l,r=0,len(nums)-1
        least=nums[0]
        while l<r:
            mid=(l+r)//2
            least=min(least,nums[mid])
            if nums[l]>nums[mid] or nums[mid]>nums[r]:
                l=mid+1
            else:
                r=mid
        return least
