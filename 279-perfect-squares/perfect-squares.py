class Solution:
    def numSquares(self, n: int):

        import math

        dp = [float('inf')] * (n + 1)
        dp[0] = 0

        visited = set()

        root = math.isqrt(n)

        for i in range(1, root + 1):
            visited.add(i * i)

        for square in visited:
            for i in range(square, n + 1):
                dp[i] = min(dp[i], 1 + dp[i - square])

        return dp[n]