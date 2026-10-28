class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        map1=set(nums)
        res=0
        for i in map1:
            if i-1 not in map1:
                temp=1
                while (i+temp)in map1:
                    temp+=1
                res=max(temp,res)
        return result