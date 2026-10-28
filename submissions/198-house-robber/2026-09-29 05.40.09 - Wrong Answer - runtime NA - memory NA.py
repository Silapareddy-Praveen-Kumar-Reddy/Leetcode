class Solution:
    def rob(self, nums: list[int]) -> int:
        if len(nums)==1:
            return nums[0]
        s1=nums[0]
        s2=nums[1]
        even= True
        if len(nums)>2:
            for i in nums[2:]:
                if even:
                    s1+=i
                    even=False
                else:
                    s2+=i
                    even=True
        return max(s1,s2)
