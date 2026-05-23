from collections import deque
import heapq

class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n = len(grid)

        # Step 1: Multi-source BFS
        dist = [[-1] * n for _ in range(n)]
        q = deque()

        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    dist[r][c] = 0
                    q.append((r, c))

        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        while q:
            r, c = q.popleft()

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if 0 <= nr < n and 0 <= nc < n and dist[nr][nc] == -1:
                    dist[nr][nc] = dist[r][c] + 1
                    q.append((nr, nc))

        # Step 2: Max-heap Dijkstra
        maxHeap = [(-dist[0][0], 0, 0)]
        visited = set()

        while maxHeap:
            safeness, r, c = heapq.heappop(maxHeap)

            safeness = -safeness

            if (r, c) == (n-1, n-1):
                return safeness

            if (r, c) in visited:
                continue

            visited.add((r, c))

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if 0 <= nr < n and 0 <= nc < n and (nr, nc) not in visited:

                    newSafeness = min(safeness, dist[nr][nc])

                    heapq.heappush(maxHeap, (-newSafeness, nr, nc))
        