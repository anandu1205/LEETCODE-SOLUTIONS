class Solution:
    def closedIsland(self, grid: list[list[int]]) -> int:
        rows,cols=len(grid),len(grid[0])
        from collections import deque
        q=deque()
        for r in range(rows):
            for c in range(cols):
                if (r==0 or r==rows-1) or (c==0 or c==cols-1):
                    if grid[r][c]==0:
                        grid[r][c]=1
                        q.append((r,c))
        directions=[(1,0),(-1,0),(0,1),(0,-1)]
        while q:
            r,c=q.popleft()
            for dr,dc in directions:
                nr,nc=r+dr,c+dc
                if 0<=nr<=rows-1 and 0<=nc<=cols-1:
                    if  grid[nr][nc]==0:
                        grid[nr][nc]=1
                        q.append((nr,nc))
        count=0
        def bfs(r,c):
            q=deque()
            q.append((r,c))
            while q:
                r,c=q.popleft()
                for dr,dc in directions:
                    nr,nc=r+dr,c+dc
                    if 0<=nr<rows and 0<=nc<cols:
                        if grid[nr][nc]==0:
                            grid[nr][nc]=1
                            q.append((nr,nc))
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==0:
                    count+=1
                    bfs(r,c)
        return count
        