class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n=len(nums)
        l,r=0,n-1
        while l<=r:
            mid=l+(r-l)//2
            if target==nums[mid]:
                return mid
            elif nums[l]<=nums[mid]:
                if nums[l]>target or target>nums[mid]:
                    l=mid+1
                else:
                    r=mid-1
            
            else:
                if target<nums[mid] or target>nums[r]:
                    r=mid-1
                else:
                    l=mid+1
        return -1