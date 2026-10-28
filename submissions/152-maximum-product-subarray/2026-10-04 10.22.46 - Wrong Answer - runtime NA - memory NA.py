class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        maxproduct=product=nums[0]
        for i in nums[1:]:
            product=product*i
            maxproduct=max(maxproduct,product,i)
        return maxproduct