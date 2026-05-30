from typing import List
import heapq

class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        dist = [[float('inf')] * n for _ in range(m)]
        dist[0][0] = 0

        pq = [(0, 0, 0)]  # obstacles_removed, row, col

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while pq:
            obstacles, r, c = heapq.heappop(pq)

            if obstacles > dist[r][c]:
                continue

            if r == m - 1 and c == n - 1:
                return obstacles

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if 0 <= nr < m and 0 <= nc < n:
                    new_obstacles = obstacles + grid[nr][nc]

                    if new_obstacles < dist[nr][nc]:
                        dist[nr][nc] = new_obstacles
                        heapq.heappush(pq, (new_obstacles, nr, nc))

        return -1





        