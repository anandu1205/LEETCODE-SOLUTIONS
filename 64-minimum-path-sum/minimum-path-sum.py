from typing import List
import heapq

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        INF = float('inf')
        least_sum = [[INF] * n for _ in range(m)]
        least_sum[0][0] = grid[0][0]

        pq = []
        heapq.heappush(pq, (grid[0][0], 0, 0))

        directions = [(1, 0), (0, 1)]

        while pq:
            sum1, r, c = heapq.heappop(pq)

            if sum1 > least_sum[r][c]:
                continue

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if 0 <= nr < m and 0 <= nc < n:
                    new_sum = sum1 + grid[nr][nc]

                    if new_sum < least_sum[nr][nc]:
                        least_sum[nr][nc] = new_sum
                        heapq.heappush(pq, (new_sum, nr, nc))

        return least_sum[m - 1][n - 1]