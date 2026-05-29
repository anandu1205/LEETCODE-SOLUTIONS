class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        n=len(grid)
        has_land=False
        has_water=False
        for r in range(n):
            for c in range(n):
                if grid[r][c]==1:
                    has_land=True
                else:
                    has_water=True
        if not has_land or not has_water:
            return -1
        queue=deque()
        visited=set()
        directions=[(1,0),(-1,0),(0,1),(0,-1)]
        for r in range(n):
            for c in range(n):
                if grid[r][c]==1:
                    queue.append((r,c))
                    visited.add((r,c))
        result=-1
        while queue:
            r,c=queue.popleft()
            visited.add((r,c))
            for dr,dc in directions:
                nr,nc=r+dr,c+dc
                if nr>=0 and nc>=0 and nr<n and nc<n and (nr,nc) not in visited and grid[nr][nc]==0:
                    grid[nr][nc]=grid[r][c]+1
                    queue.append((nr,nc))
                    result=max(result,grid[nr][nc])
        return result-1
        