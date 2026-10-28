class Solution:
    def trap(self, height: list[int]) -> int:
        if not height:
            return 0
        l, r = 0, len(height) - 1
        left_max, right_max = 0, 0
        total = 0
        while l < r:
            if height[l] < height[r]:
                left_max = max(left_max, height[l])
                total += left_max - height[l]
                l += 1
            else:
                right_max = max(right_max, height[r])
                total += right_max - height[r]
                r -= 1
        return total   