
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        dp = [1] * n
        next2 = next3 = next5 = 0

        for i in range(1, n):
            dp[i] = min(
                dp[next2] * 2,
                dp[next3] * 3,
                dp[next5] * 5
            )

            if dp[i] == dp[next2] * 2:
                next2 += 1
            if dp[i] == dp[next3] * 3:
                next3 += 1
            if dp[i] == dp[next5] * 5:
                next5 += 1

        return dp[n - 1]

        