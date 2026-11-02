class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:

        directions = [
            (1,2), (1,-2),
            (-1,2), (-1,-2),
            (2,1), (2,-1),
            (-2,1), (-2,-1)
        ]

        # Initialize DP
        dp = [[[0.0] * n for _ in range(n)] for _ in range(k+1)]

        # Base case
        dp[0][row][column] = 1.0

        # Calculate probability for each move
        for moves in range(1, k+1):

            for i in range(n):
                for j in range(n):

                    for dr, dc in directions:

                        prev_i = i - dr
                        prev_j = j - dc

                        if 0 <= prev_i < n and 0 <= prev_j < n:

                            dp[moves][i][j] += dp[moves-1][prev_i][prev_j] / 8

        # Calculate total survival probability
        return sum(
            dp[k][i][j]
            for i in range(n)
            for j in range(n)
        )