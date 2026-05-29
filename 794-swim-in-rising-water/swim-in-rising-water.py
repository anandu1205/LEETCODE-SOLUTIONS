class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n=len(grid)
        import heapq
        pq=[(grid[0][0],0,0)] # max_time,r,c
        max_time=-1
        directions=[(0,1),(0,-1),(1,0),(-1,0)]
        visited=set()
        while pq:
            time,r,c=heapq.heappop(pq)
            if (r, c) in visited:
               continue
            visited.add((r,c))
            if r==n-1 and c==n-1:
                return time
            for dr,dc in directions:
                nr,nc=r+dr,c+dc
                if nr>=0 and nc>=0 and nr<n and nc<n and (nr,nc) not in visited:

                    new_time = max(time, grid[nr][nc])
                    heapq.heappush(pq, (new_time, nr, nc))
                    
                    
        return time
        