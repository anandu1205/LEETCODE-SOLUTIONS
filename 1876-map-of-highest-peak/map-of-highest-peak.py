from collections import deque

class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:

        m = len(isWater)
        n = len(isWater[0])

        queue = deque()
        visited = set()

        ans = [[0] * n for _ in range(m)]

        # Start BFS from all water cells
        for i in range(m):
            for j in range(n):

                if isWater[i][j] == 1:
                    queue.append((i, j))
                    visited.add((i, j))

        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        while queue:

            r, c = queue.popleft()

            for dr, dc in directions:

                nr = r + dr
                nc = c + dc

                if (
                    0 <= nr < m and
                    0 <= nc < n and
                    (nr, nc) not in visited
                ):

                    ans[nr][nc] = ans[r][c] + 1

                    visited.add((nr, nc))
                    queue.append((nr, nc))

        return ans
        