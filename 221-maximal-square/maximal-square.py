class Solution:
    def maximalSquare(self, matrix: list[list[str]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        dp = [[0] * cols for _ in range(rows)]
        max_side = 0

        for r in range(rows - 1, -1, -1):
            for c in range(cols - 1, -1, -1):
                if matrix[r][c] == "1":
                    if r == rows - 1 or c == cols - 1:
                        dp[r][c] = 1
                    else:
                        dp[r][c] = 1 + min(
                            dp[r + 1][c],
                            dp[r][c + 1],
                            dp[r + 1][c + 1]
                        )

                    max_side = max(max_side, dp[r][c])

        return max_side * max_side

        