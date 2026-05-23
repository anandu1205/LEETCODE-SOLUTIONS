import heapq

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m = len(heights)
        n = len(heights[0])

        pq = [(0, 0, 0)]   # effort, row, col

        INF = float('inf')
        efforts = [[INF for _ in range(n)] for _ in range(m)]

        efforts[0][0] = 0

        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        while pq:
            curr_effort, r, c = heapq.heappop(pq)

            if r == m - 1 and c == n - 1:
                return curr_effort

            if curr_effort > efforts[r][c]:
                continue

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                if 0 <= nr < m and 0 <= nc < n:

                    edge_cost = abs(heights[nr][nc] - heights[r][c])

                    new_effort = max(curr_effort, edge_cost)

                    if new_effort < efforts[nr][nc]:
                        efforts[nr][nc] = new_effort
                        heapq.heappush(pq, (new_effort, nr, nc))