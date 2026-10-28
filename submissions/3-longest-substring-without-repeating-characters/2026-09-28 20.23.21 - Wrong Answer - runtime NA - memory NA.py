class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res=0
        hash_map=set()
        l=0
        for i in range(len(s)):
            if s[i] not in hash_map:
                l+=1
                hash_map.add(s[i])
                res=max(l,res)
            else:
                l=0
                hash_map=set()
        return res
            

