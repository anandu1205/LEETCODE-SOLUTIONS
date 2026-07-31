from typing import List
import heapq

class Solution:
    def minCost(self, m: int, n: int, penalty: List[List[int]]) -> int:
        directions = [
            (0, 1),   # right
            (1, 0),   # down
            (0, -1),  # left
            (-1, 0),  # up
        ]

        odd_allowed = {(0, 1), (1, 0)}
        even_allowed = {(0, -1), (-1, 0)}

        dist = [[[float("inf")] * 2 for _ in range(n)] for _ in range(m)]

        dist[0][0][1] = 1
        pq = [(1, 0, 0, 1)]  # cost, row, col, parity

        while pq:
            cost, row, col, parity = heapq.heappop(pq)

            if cost > dist[row][col][parity]:
                continue

            if row == m - 1 and col == n - 1:
                return cost

            allowed = odd_allowed if parity == 1 else even_allowed
            next_parity = 1 - parity

            for dr, dc in directions:
                nr = row + dr
                nc = col + dc

                if 0 <= nr < m and 0 <= nc < n:
                    enter_cost = (nr + 1) * (nc + 1)

                    if (dr, dc) in allowed:
                        new_cost = cost + enter_cost
                    else:
                        new_cost = cost + enter_cost + penalty[row][col]

                    if new_cost < dist[nr][nc][next_parity]:
                        dist[nr][nc][next_parity] = new_cost
                        heapq.heappush(pq, (new_cost, nr, nc, next_parity))

            wait_cost = penalty[row][col]
            new_cost = cost + wait_cost

            if new_cost < dist[row][col][next_parity]:
                dist[row][col][next_parity] = new_cost
                heapq.heappush(pq, (new_cost, row, col, next_parity))

        return -1