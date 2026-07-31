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

        start_cost = 1

        # state = (row, col, next_action_parity)
        # parity: 1 means next action is odd, 0 means next action is even
        dist = {(0, 0, 1): start_cost}
        pq = [(start_cost, 0, 0, 1)]  # cost, row, col, parity

        while pq:
            cost, row, col, parity = heapq.heappop(pq)

            if (row, col) == (m - 1, n - 1):
                return cost

            if cost > dist.get((row, col, parity), float("inf")):
                continue

            allowed = odd_allowed if parity == 1 else even_allowed
            next_parity = 1 - parity

            # Try moving to adjacent cells
            for dr, dc in directions:
                nr = row + dr
                nc = col + dc

                if 0 <= nr < m and 0 <= nc < n:
                    enter_cost = (nr + 1) * (nc + 1)

                    if (dr, dc) in allowed:
                        new_cost = cost + enter_cost
                    else:
                        new_cost = cost + enter_cost + penalty[row][col]

                    state = (nr, nc, next_parity)

                    if new_cost < dist.get(state, float("inf")):
                        dist[state] = new_cost
                        heapq.heappush(pq, (new_cost, nr, nc, next_parity))

            # Try waiting
            new_cost = cost + penalty[row][col]
            state = (row, col, next_parity)

            if new_cost < dist.get(state, float("inf")):
                dist[state] = new_cost
                heapq.heappush(pq, (new_cost, row, col, next_parity))

        return -1
        