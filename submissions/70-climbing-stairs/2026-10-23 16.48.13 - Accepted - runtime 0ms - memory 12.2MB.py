class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        first=1
        sec=1
        for i in range(n-1):
            tem=sec
            sec=first+sec
            first=tem
        return sec