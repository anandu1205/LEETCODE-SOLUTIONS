class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        from collections import deque

        m = len(grid)
        n = len(grid[0])

        queue = deque()
        visited = set()

        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        # Add boundary land cells
        for i in range(m):
            if grid[i][0] == 1:
                queue.append((i, 0))
                visited.add((i, 0))

            if grid[i][n - 1] == 1:
                queue.append((i, n - 1))
                visited.add((i, n - 1))

        for j in range(n):
            if grid[0][j] == 1:
                queue.append((0, j))
                visited.add((0, j))

            if grid[m - 1][j] == 1:
                queue.append((m - 1, j))
                visited.add((m - 1, j))

        # BFS from boundary lands
        while queue:
            r, c = queue.popleft()

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if (
                    0 <= nr < m and
                    0 <= nc < n and
                    (nr, nc) not in visited and
                    grid[nr][nc] == 1
                ):
                    visited.add((nr, nc))
                    queue.append((nr, nc))

        # Count enclaves
        count = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (i, j) not in visited:
                    count += 1

        return count


            
        

        
        