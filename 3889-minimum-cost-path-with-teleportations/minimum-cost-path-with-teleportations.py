class Solution:
    def minCost(self, grid: list[list[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])

        points = sorted(
            [(grid[i][j], i, j) for i in range(m) for j in range(n)]
        )

        cost = [[float("inf")] * n for _ in range(m)]

        for _ in range(k + 1):

            # Teleportation
            best = float("inf")
            start = 0

            for end in range(len(points)):
                best = min(best, cost[points[end][1]][points[end][2]])

                if end + 1 == len(points) or points[end][0] != points[end + 1][0]:
                    for p in range(start, end + 1):
                        i, j = points[p][1], points[p][2]
                        cost[i][j] = best
                    start = end + 1

            # Normal moves
            for i in range(m - 1, -1, -1):
                for j in range(n - 1, -1, -1):

                    if i == m - 1 and j == n - 1:
                        cost[i][j] = 0
                        continue

                    if i + 1 < m:
                        cost[i][j] = min(
                            cost[i][j],
                            cost[i + 1][j] + grid[i + 1][j]
                        )

                    if j + 1 < n:
                        cost[i][j] = min(
                            cost[i][j],
                            cost[i][j + 1] + grid[i][j + 1]
                        )

        return cost[0][0]