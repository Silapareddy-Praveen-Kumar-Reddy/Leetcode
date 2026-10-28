class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        total=0
        if not grid:
            return 0
        visted=set()
        #rows,coloums
        def bfs(r,c):
            q=collections.deque()
            q.append((r,c))
            visited.add((r,c))
            while q:
                row,coloum=q.popleft()
                directions=[]#4 dir
                for i in d:
                    r=row+i[0]
                    # if row,coloum in range() and grid[i]=="1" and r,c not in in visited
                    #q.append(r,c)
                    visited.add()r,c

        #go to every element if not visited and =1 call bfs total+1
        #return total