from typing import List
from collections import deque

class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        MOD = 10**9 + 7
        m = len(grid)
        n = len(grid[0])

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        indegree = [[0] * n for _ in range(m)]
        dp = [[1] * n for _ in range(m)]

        for r in range(m):
            for c in range(n):
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    if 0 <= nr < m and 0 <= nc < n:
                        if grid[nr][nc] < grid[r][c]:
                            indegree[r][c] += 1

        q = deque()

        for r in range(m):
            for c in range(n):
                if indegree[r][c] == 0:
                    q.append((r, c))

        while q:
            r, c = q.popleft()

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if 0 <= nr < m and 0 <= nc < n:
                    if grid[nr][nc] > grid[r][c]:
                        dp[nr][nc] = (dp[nr][nc] + dp[r][c]) % MOD
                        indegree[nr][nc] -= 1

                        if indegree[nr][nc] == 0:
                            q.append((nr, nc))

        ans = 0
        for r in range(m):
            for c in range(n):
                ans = (ans + dp[r][c]) % MOD

        return ans