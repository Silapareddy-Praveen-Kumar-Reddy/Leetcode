import heapq
class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        temp=[]
        for x,y in (points):
            temp.append([(x**2 )+( y**2),x,y])
        heapq.heapify(temp)
        res=[]
        while k>0:
            dis,x,y=heapq.heappop(temp)
            res.append([x,y])
            k-=1
        return res