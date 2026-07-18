class Solution:
    def maxConsistentColumns(self, grid: List[List[int]], limit: int) -> int:
        m = len(grid)
        n = len(grid[0])

        dp = [1] * n

        for curr in range(n):
            for prev in range(curr):
                ok = True

                for row in range(m):
                    if abs(grid[row][curr] - grid[row][prev]) > limit:
                        ok = False
                        break

                if ok:
                    dp[curr] = max(dp[curr], dp[prev] + 1)

        return max(dp)