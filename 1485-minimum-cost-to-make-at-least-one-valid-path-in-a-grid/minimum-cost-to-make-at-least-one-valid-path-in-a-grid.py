import heapq
from typing import List

class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        
        # corrected directions
        directions = {
            1: (0, 1),    # right
            2: (0, -1),   # left
            3: (1, 0),    # down
            4: (-1, 0)    # up
        }
        
        m, n = len(grid), len(grid[0])
        
        pq = [(0, 0, 0)]   # (cost, row, col)
        visited = set()
        
        # distance matrix (important for Dijkstra)
        dist = [[float('inf')] * n for _ in range(m)]
        dist[0][0] = 0
        
        while pq:
            cost, row, col = heapq.heappop(pq)
            
            if (row, col) in visited:
                continue
            visited.add((row, col))
            
            if row == m - 1 and col == n - 1:
                return cost
            
            # iterate all 4 directions (your idea of "remaining directions")
            for d in directions:
                dr, dc = directions[d]
                nr, nc = row + dr, col + dc
                
                # correct boundary check
                if nr < 0 or nc < 0 or nr >= m or nc >= n:
                    continue
                
                # cost logic (core idea preserved)
                new_cost = cost if d == grid[row][col] else cost + 1
                
                # relaxation step
                if new_cost < dist[nr][nc]:
                    dist[nr][nc] = new_cost
                    heapq.heappush(pq, (new_cost, nr, nc))
        
        return -1
