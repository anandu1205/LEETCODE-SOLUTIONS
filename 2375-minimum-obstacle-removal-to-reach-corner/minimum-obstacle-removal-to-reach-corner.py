from typing import List
import heapq

class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        
        pq = [(grid[0][0], 0, 0)]   # start cost
        costs = [[float('inf')] * n for _ in range(m)]
        costs[0][0] = grid[0][0]
        
        visited = set()
        
        while pq:
            cost, row, col = heapq.heappop(pq)
            
            if (row, col) in visited:
                continue
            visited.add((row, col))
            
            if row == m - 1 and col == n - 1:
                return cost
            
            for dr, dc in directions:
                new_r, new_c = row + dr, col + dc
                
                if new_r < 0 or new_c < 0 or new_r >= m or new_c >= n:
                    continue
                
                # compute new cost safely
                new_cost = cost + grid[new_r][new_c]
                
                if new_cost < costs[new_r][new_c]:
                    costs[new_r][new_c] = new_cost
                    heapq.heappush(pq, (new_cost, new_r, new_c))
        
        return -1


        