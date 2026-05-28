from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:

        n = len(grid)

        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return -1

        directions = [
            (0,1), (0,-1),
            (1,0), (-1,0),
            (1,1), (-1,1),
            (1,-1), (-1,-1)
        ]

        queue = deque([(0, 0, 1)])
        visited = set([(0,0)])

        while queue:

            r, c, steps = queue.popleft()

            if r == n-1 and c == n-1:
                return steps

            for dr, dc in directions:

                nr = r + dr
                nc = c + dc

                if (
                    0 <= nr < n and
                    0 <= nc < n and
                    grid[nr][nc] == 0 and
                    (nr, nc) not in visited
                ):

                    visited.add((nr,nc))
                    queue.append((nr, nc, steps + 1))

        return -1
