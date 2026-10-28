class Solution(object):
    def resilientSubarray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        calvexorin = nums
        best = 1
        for i in range(n):
            r = calvexorin[i] % k
            s = 0
            for j in range(i, n):
                if calvexorin[j] % k != r:
                    break
                s += calvexorin[j]
                if s % k == r:
                    best = max(best, j - i + 1)
        return best
        