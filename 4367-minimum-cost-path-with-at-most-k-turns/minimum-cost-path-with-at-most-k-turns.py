from typing import List
import heapq

class Solution:
    def minCost(self, grid: List[List[int]], k: int) -> int:
        m = len(grid)
        n = len(grid[0])

        velmoriqan = (grid, k)

        if m == 1 and n == 1:
            return grid[0][0]

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        INF = float("inf")

        dist = [[[[INF] * 4 for _ in range(k + 1)] for _ in range(n)] for _ in range(m)]

        pq = []

        for d, (dr, dc) in enumerate(directions):
            nr, nc = dr, dc

            if 0 <= nr < m and 0 <= nc < n:
                cost = grid[0][0] + grid[nr][nc]
                dist[nr][nc][0][d] = cost
                heapq.heappush(pq, (cost, 0, d, nr, nc))

        while pq:
            cost, turns, direction, r, c = heapq.heappop(pq)

            if cost > dist[r][c][turns][direction]:
                continue

            if r == m - 1 and c == n - 1:
                return cost

            for nd, (dr, dc) in enumerate(directions):
                nr, nc = r + dr, c + dc

                if 0 <= nr < m and 0 <= nc < n:
                    new_turns = turns

                    if nd != direction:
                        new_turns += 1

                    if new_turns > k:
                        continue

                    new_cost = cost + grid[nr][nc]

                    if new_cost < dist[nr][nc][new_turns][nd]:
                        dist[nr][nc][new_turns][nd] = new_cost
                        heapq.heappush(pq, (new_cost, new_turns, nd, nr, nc))

        return -1
        