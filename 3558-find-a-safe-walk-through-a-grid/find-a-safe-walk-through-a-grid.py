from typing import List
import heapq

class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        m, n = len(grid), len(grid[0])

        INF = float("inf")
        dist = [[INF] * n for _ in range(m)]

        start_loss = grid[0][0]
        dist[0][0] = start_loss

        pq = [(start_loss, 0, 0)]  # (health lost, row, col)

        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        while pq:
            loss, r, c = heapq.heappop(pq)

            if loss > dist[r][c]:
                continue

            if r == m - 1 and c == n - 1:
                return loss < health

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if 0 <= nr < m and 0 <= nc < n:
                    new_loss = loss + grid[nr][nc]

                    if new_loss < dist[nr][nc]:
                        dist[nr][nc] = new_loss
                        heapq.heappush(pq, (new_loss, nr, nc))

        return False