class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        total=0
        if not grid:
            return 0
        visited=set()
        rows=len(grid)
        coloums=len(grid[0])
        def bfs(r,c):
            q=collections.deque()
            q.append((r,c))
            visited.add((r,c))
            while q:
                row,coloum=q.popleft()
                d=[(0,1),(1,0),(-1,0),(0,-1)]#4 dir
                for i in d:
                    r=row+i[0]
                    c=coloum +i[1]
                    # if row,coloum in range() and grid[i]=="1" and r,c not in in visited
                    if r in range(rows) and c in range(coloums) and grid[r][c]=='1' and (r,c) not in visited:
                        

                        q.append((r,c))
                        visited.add((r,c))

        #go to every element if not visited and =1 call bfs total+1
        #return total
        for i in range(rows):
            for j in range(coloums):
                if grid[i][j] =='1' and (i,j) not in visited:
                    total+=1
                    bfs(i,j)
        return total