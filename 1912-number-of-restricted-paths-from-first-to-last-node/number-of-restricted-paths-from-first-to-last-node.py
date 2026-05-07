class Solution:
    def countRestrictedPaths(self, n: int, edges: List[List[int]]) -> int:

        from collections import defaultdict
        from functools import cache
        import heapq

        MOD = 10**9 + 7

        graph = defaultdict(list)

        for u, v, weight in edges:
            graph[u].append((v, weight))
            graph[v].append((u, weight))

        # Dijkstra from node n
        dist = [float('inf')] * (n + 1)
        dist[n] = 0

        heap = [(0, n)]

        while heap:

            distance, node = heapq.heappop(heap)

            if distance > dist[node]:
                continue

            for nei, weight in graph[node]:

                new_dist = distance + weight

                if new_dist < dist[nei]:

                    dist[nei] = new_dist
                    heapq.heappush(heap, (new_dist, nei))

        # DFS + memoization
        @cache
        def dfs(node):

            if node == n:
                return 1

            ways = 0

            for nei, weight in graph[node]:

                if dist[nei] < dist[node]:

                    ways += dfs(nei)
                    ways %= MOD

            return ways

        return dfs(1)