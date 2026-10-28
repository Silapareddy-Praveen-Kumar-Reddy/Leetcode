class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        maxproduct=product=nums[0]
        for i in nums[1:]:
            product=max(product*i,i)
            maxproduct=max(maxproduct,product)
        return maxproduct