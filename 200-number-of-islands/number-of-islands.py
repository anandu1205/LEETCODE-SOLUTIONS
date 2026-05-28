class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        from collections import deque
        m=len(grid)
        n=len(grid[0])
        visited=set()
        directions=[(1,0),(-1,0),(0,1),(0,-1)]
        islands=0
        def bfs(r,c):
            queue=deque([(r,c)])
            visited.add((r,c))
            while queue:
                r,c=queue.popleft()
                for dr,dc in directions:
                    nr,nc=r+dr,c+dc
                    if nr>=0 and nc>=0 and nr<m and nc<n and (nr,nc) not in visited and grid[nr][nc]=="1":
                        visited.add((nr,nc))
                        queue.append((nr,nc))
        for i in range(m):
            for j in range(n):
                if grid[i][j]=="1" and (i,j) not in visited:
                    bfs(i,j)
                    islands+=1
        return islands

        