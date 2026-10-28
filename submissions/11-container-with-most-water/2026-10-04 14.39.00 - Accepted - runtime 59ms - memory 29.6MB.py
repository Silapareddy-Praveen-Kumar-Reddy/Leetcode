class Solution:
    def maxArea(self, height: list[int]) -> int:
        left,right=0,len(height)-1

        area=0
        while left<right:
            larea=min(height[left],height[right])*(right-left)
            area=max(area,larea)
            if height[left]> height[right]:
                right-=1
            else:
                left+=1

        return area

        



            

