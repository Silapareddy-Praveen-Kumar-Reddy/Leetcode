class Solution:
    def rob(self, nums: list[int]) -> int:
        s1=nums[0]
        s2=nums[1]
        even= True
        for i in nums[2:]:
            if even:
                s1+=i
                even=False
            else:
                s2+=i
                even=True
        return max(s1,s2)
